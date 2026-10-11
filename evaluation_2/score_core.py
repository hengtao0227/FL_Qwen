#!/usr/bin/env python3
"""Evaluate all supplied cases, including candidates with no positive label."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

TOPS = (1, 3, 5)


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def verify_evidence(directory, truth):
    meta = load(directory / 'case.json')
    hashes = meta['files_sha256']
    fingerprint = hashlib.sha256(json.dumps(hashes, sort_keys=True,
                                separators=(',', ':')).encode()).hexdigest()
    if (fingerprint != truth['input_sha256'] or meta['case_id'] != truth['case_id']
            or meta['input_sha256'] != fingerprint):
        raise ValueError('Run evidence manifest mismatch')
    for name, expected in hashes.items():
        if name != Path(name).name or '/' in name or '\\' in name:
            raise ValueError('Unsafe evidence path')
        if hashlib.sha256((directory / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Run evidence changed: {name}')


def references(truth):
    return {row['candidate_id'] for row in truth['reference_methods']}


def score_prediction(truth, prediction):
    if not isinstance(prediction, dict) or set(prediction) != {'case_id','input_sha256','ranking'}:
        raise ValueError('Prediction schema mismatch')
    if prediction.get('case_id') != truth['case_id']:
        raise ValueError('case_id mismatch')
    if prediction.get('input_sha256') != truth['input_sha256']:
        raise ValueError('input_sha256 missing or mismatched')
    ranking = prediction.get('ranking')
    if not isinstance(ranking, list) or len(ranking) > 5:
        raise ValueError('ranking must be a list of at most 5 items')
    allowed, seen, predictions = set(truth['candidate_ids']), set(), []
    for i, item in enumerate(ranking, 1):
        if (not isinstance(item, dict) or set(item) != {'rank','candidate_id','reason'}
                or type(item.get('rank')) is not int or item['rank'] != i):
            raise ValueError('rank must equal its 1-based array position')
        mid = item.get('candidate_id')
        if not isinstance(mid, str) or mid not in allowed:
            raise ValueError(f'Unknown candidate: {mid}')
        if mid in seen:
            raise ValueError(f'Duplicate candidate: {mid}')
        if not isinstance(item.get('reason'), str) or not item['reason'].strip():
            raise ValueError('Each candidate requires a nonempty reason')
        seen.add(mid)
        predictions.append(mid)
    refs = references(truth)
    return {
        'status': 'ok' if ranking else 'empty_prediction',
        'predictions': predictions, 'reference_candidate_ids': sorted(refs),
        'hits': {f'top{k}': bool(set(predictions[:k]) & refs) for k in TOPS},
        'reference_recall': {f'top{k}': len(set(predictions[:k]) & refs) / len(refs)
                             if refs else None for k in TOPS},
        'reciprocal_rank_at5': next((1 / i for i, mid in enumerate(predictions, 1)
                                    if mid in refs), 0.0),
    }


def aggregate(results):
    n = len(results)
    recall_results = [r for r in results if r['reference_status'] == 'positive_reference_available']
    nr = len(recall_results)
    hits = {f'top{k}': sum(r['hits'][f'top{k}'] for r in results) for k in TOPS}
    return {
        'denominator': n,
        'statuses': dict(collections.Counter(r['status'] for r in results)),
        'reference_statuses': dict(collections.Counter(r['reference_status'] for r in results)),
        'hit_counts': hits,
        'hit_rates': {key: value / n if n else None for key, value in hits.items()},
        'mrr_at5': sum(r['reciprocal_rank_at5'] for r in results) / n if n else None,
        'reference_recall_denominator': nr,
        'macro_reference_recall': {f'top{k}': sum(r['reference_recall'][f'top{k}']
            for r in recall_results) / nr if nr else None for k in TOPS},
    }


def evaluate(truths, prediction_dir, cases):
    if not cases or len(set(cases)) != len(cases) or any(c not in truths for c in cases):
        raise ValueError('Cases must be nonempty, unique, and present in ground truth')
    results = []
    for bug in cases:
        truth = truths[bug]
        refs = references(truth)
        if not refs <= set(truth['candidate_ids']):
            raise ValueError(f'{bug}: reference ID outside candidate set')
        reference_status = ('positive_reference_available' if refs
                            else 'no_positive_reference_in_candidates')
        direct = prediction_dir / f'{bug}.json'
        nested = prediction_dir / bug / 'prediction.json'
        paths = [p for p in (direct, nested) if p.is_file()]
        status, error = 'missing_prediction', None
        integrity = 'not_checked_flat_or_missing_result'
        try:
            if len(paths) > 1:
                status = 'invalid_prediction'
                raise ValueError('Both flat and nested result exist; keep one to avoid ambiguity')
            if not paths:
                raise FileNotFoundError('No prediction file')
            status = 'invalid_prediction'
            if paths[0] == nested:
                verify_evidence(nested.parent, truth)
                integrity = 'verified'
            result = score_prediction(truth, load(paths[0]))
        except (ValueError, TypeError, AttributeError, KeyError, OSError) as exc:
            error = str(exc)
            result = {
                'status': status, 'predictions': [], 'reference_candidate_ids': sorted(refs),
                'hits': {f'top{k}': False for k in TOPS},
                'reference_recall': {f'top{k}': 0.0 if refs else None for k in TOPS},
                'reciprocal_rank_at5': 0.0,
            }
        results.append(dict(case_id=bug, error=error, evidence_integrity=integrity,
                            reference_status=reference_status, **result))
    summary = aggregate(results)
    with_refs = [r for r in results if r['reference_status'] == 'positive_reference_available']
    summary['positive_reference_subset'] = aggregate(with_refs)
    summary['candidate_positive_label_coverage'] = len(with_refs) / len(results)
    summary['scoring_policy'] = (
        'All selected cases remain in the Hit@k/MRR@5 denominator. No-positive-label '
        'cases have zero observed-label hits/MRR, undefined reference recall, and a '
        'separate reference status. This does not prove the true faulty method is absent '
        'or a prediction is semantically incorrect. Recall uses only cases with references.')
    return {'summary': summary, 'results': results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--truth', type=Path, default=Path(__file__).with_name('ground_truth.json'))
    parser.add_argument('--predictions', type=Path, required=True)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--cases', nargs='+')
    group.add_argument('--cases-file', type=Path)
    parser.add_argument('--out', type=Path, default=Path('scores.json'))
    args = parser.parse_args()
    truths = load(args.truth)['cases']
    cases = (args.cases_file.read_text(encoding='utf-8-sig').split() if args.cases_file
             else args.cases if args.cases else sorted(truths))
    try:
        result = evaluate(truths, args.predictions, cases)
    except ValueError as exc:
        parser.error(str(exc))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    s = result['summary']
    print(json.dumps(s, ensure_ascii=False, indent=2))
    md = ['# Method localization scores', '', f'Fixed denominator: {s["denominator"]}', '',
          '| Metric | Hits | Rate |', '|---|---:|---:|']
    for k in TOPS:
        key = f'top{k}'
        md.append(f'| Hit@{k} | {s["hit_counts"][key]} | {s["hit_rates"][key]:.2%} |')
    md.extend(['', f'MRR@5: {s["mrr_at5"]:.6f}', '',
               f'Positive-reference subset denominator: {s["positive_reference_subset"]["denominator"]}',
               f'Reference-recall denominator: {s["reference_recall_denominator"]}', '',
               s['scoring_policy'], '',
               'Missing, invalid and empty predictions score zero; they are not dropped.',
               'Detailed subset metrics, reference status and integrity checks are in JSON.', ''])
    args.out.with_suffix('.md').write_text('\n'.join(md), encoding='utf-8')


if __name__ == '__main__':
    main()
