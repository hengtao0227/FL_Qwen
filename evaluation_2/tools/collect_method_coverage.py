"""Collect method-entry coverage for reconstructed cases using isolated JUnit runs.

This portable Java 8 harness compiles unchanged buggy production sources and
trigger tests, then instruments every compiled production class (not fix classes).
It is not a Defects4J checkout/build. Every trigger must reproduce its recorded
exception type/message before coverage can be used to rebuild the release.
No patch positions or reference labels are read by candidate selection.
"""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import zipfile

from build_input import identity
from case_io import digest, encode, require


def read(path): return json.loads(path.read_bytes())


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encode(data))


def run(command, cwd, log, timeout=240):
    env = dict(os.environ, TZ='America/Los_Angeles')
    with log.open('wb') as out:
        result = subprocess.run(list(map(str, command)), cwd=cwd, stdout=out,
                                stderr=subprocess.STDOUT, env=env, timeout=timeout)
    require(result.returncode == 0, f'Command failed ({result.returncode}); see {log}')


def javac(jdk, sources, destination, cp, sourcepath, work, label):
    destination.mkdir(parents=True, exist_ok=True)
    args = ['-g', '-encoding', 'UTF-8', '-source', '7', '-target', '7',
            '-Xmaxerrs', '30', '-d', str(destination), '-cp', os.pathsep.join(map(str, cp))]
    if sourcepath: args += ['-sourcepath', os.pathsep.join(map(str, sourcepath))]
    args += list(map(str, sources))
    argfile = work/(label+'.args')
    argfile.write_text('\n'.join('"'+a.replace('\\','/')+'"' for a in args), encoding='utf-8')
    run([jdk/'bin/javac.exe', '-J-Duser.language=en', '@'+str(argfile)], work, work/(label+'.log'))


def setup_agent(jdk, d4j, runtime):
    asm = d4j/'framework/projects/Mockito/lib/asm-all-5.0.4.jar'
    junit = d4j/'framework/lib/formatter/lib/junit-4.11.jar'
    src = Path(__file__).with_name('coverage_java')
    classes = runtime/'agent_classes'
    javac(jdk, list(src.glob('*.java')), classes, [asm,junit], [], runtime, 'agent_compile')
    agent = runtime/'method-entry-agent.jar'
    def put(z,name,data):
        info=zipfile.ZipInfo(name,(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,data)
    with zipfile.ZipFile(agent, 'w', zipfile.ZIP_DEFLATED) as z:
        put(z,'META-INF/MANIFEST.MF', 'Manifest-Version: 1.0\nPremain-Class: MethodEntryAgent\n\n')
        for file in sorted(classes.rglob('*.class')): put(z,file.relative_to(classes).as_posix(),file.read_bytes())
        with zipfile.ZipFile(asm) as dep:
            for name in dep.namelist():
                if name.startswith('org/objectweb/asm/') and name.endswith('.class'):
                    put(z,name,dep.read(name))
    with zipfile.ZipFile(runtime/'coverage-recorder.jar','w',zipfile.ZIP_DEFLATED) as z:
        put(z,'CoverageRecorder.class',(classes/'CoverageRecorder.class').read_bytes())
    return agent,junit


def materialize(cid, cache, work):
    root = work/'source'
    audit = read(cache/'source_audit'/f'{cid}.json')
    archive = cache/'archives'/f"{cid.split('_')[0]}-{audit['revision_fixed']}.zip"
    require(digest(archive.read_bytes()) == audit['archive_sha256'], 'Archive hash mismatch')
    if not root.exists():
        root.mkdir()
        with zipfile.ZipFile(archive) as z:
            for entry in z.infolist():
                parts = entry.filename.split('/')[1:]
                if cid.startswith('Time_') and parts and parts[0]=='JodaTime': parts=parts[1:]
                if entry.is_dir() or not parts or parts[0] in ('javadoc','docs','.git'): continue
                target = root.joinpath(*parts)
                require(target.resolve().is_relative_to(root.resolve()), 'Unsafe archive path')
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(z.read(entry))
        for path in (cache/'buggy_sources'/cid).rglob('*.java'):
            target = root/path.relative_to(cache/'buggy_sources'/cid)
            target.parent.mkdir(parents=True, exist_ok=True)
            data = path.read_bytes()
            try: text = data.decode('utf-8-sig')
            except UnicodeDecodeError: text = data.decode('latin-1')
            target.write_text(text, encoding='utf-8', newline='')
    return root,audit


def dependencies(project, root, d4j):
    jars = []
    if project == 'Mockito':
        for sub in ('lib/compile','lib/run','lib/repackaged','lib/test'):
            jars.extend(sorted((root/sub).glob('*.jar')))
        fallback=d4j/'framework/projects/Mockito/lib'
        # Mockito's historical Matcher implementation requires Hamcrest 1.1.
        jars += [fallback/'hamcrest-core-1.1.jar', fallback/'objenesis-2.1.jar',
                 fallback/'cglib-and-asm-1.0.jar',fallback/'asm-all-5.0.4.jar',
                 fallback/'fest-assert-1.3.jar',fallback/'fest-util-1.1.4.jar',
                 fallback/'powermock-reflect-1.2.5.jar',fallback/'assertj-core-2.1.0.jar']
        gradle = '\n'.join(p.read_text(encoding='utf-8',errors='replace') for p in root.glob('*.gradle'))
        version = re.search(r'byte-buddy[:\'"]+([\d.]+)', gradle)
        if version:
            jars.append(d4j/'framework/projects/Mockito/byte-buddy'/('byte-buddy-'+version[1]+'.jar'))
    else:
        jars.extend(sorted((root/'lib').rglob('*.jar')))
        jars.extend(sorted((d4j/f'framework/projects/{project}/lib').rglob('*.jar')))
    resolved=[]
    for p in jars:
        if p.name.endswith(('-sources.jar','-javadoc.jar')): continue
        if not zipfile.is_zipfile(p):
            replacement=Path(__file__).resolve().parents[1]/'coverage_dependencies'/p.name
            require(zipfile.is_zipfile(replacement),'Invalid dependency archive: '+str(p))
            p=replacement
        resolved.append(p)
    return resolved


def expected_tests(report):
    records=[]
    for block in re.split(r'^---\s+', report, flags=re.M)[1:]:
        lines=block.splitlines()
        message=[]
        for line in lines[1:]:
            if re.match(r'\s+at ',line): break
            message.append(line)
        records.append((lines[0].strip(),'\n'.join(message).strip()))
    require(records, 'No triggering tests')
    return records


def normalize_failure(value):
    value=re.sub(r'\$\$EnhancerByMockitoWithCGLIB\$\$[0-9a-f]+',
                 '$$EnhancerByMockitoWithCGLIB$$HASH',value)
    value=re.sub(r'^(junit\.framework\.(?:AssertionFailedError|ComparisonFailure)|org\.junit\.(?:ComparisonFailure|internal.ArrayComparisonFailure)|java\.lang\.AssertionError|org\.mockito\.exceptions\.verification\.[A-Za-z]+)',
                 'AssertionError',value)
    value=re.sub(r'@[0-9a-fA-F]+\b','@OBJECT',value)
    value=re.sub(r'(\.java):\d+',r'\1:LINE',value)
    value=value.replace(': null expected:', ': expected:')
    return ' '.join(value.split())


def failure_key(value, requested):
    value=normalize_failure(value)
    if requested=='org.apache.commons.math3.distribution.HypergeometricDistributionTest::testMath1021':
        match=re.fullmatch(r'AssertionError: sample=(-[0-9]+)',value)
        require(match and -50<=int(match[1])<0,'Unexpected hypergeometric sample failure')
        return 'AssertionError: negative hypergeometric sample in [-50,-1]'
    if requested in ('org.apache.commons.lang3.RandomStringUtilsTest::testExceptions','org.apache.commons.lang3.RandomStringUtilsTest::testLANG805'):
        require(re.fullmatch(r'java.lang.ArrayIndexOutOfBoundsException: [0-9]+',value),'Unexpected random-index failure')
        return 'java.lang.ArrayIndexOutOfBoundsException: RANDOM_INDEX'
    if requested in ('org.apache.commons.lang3.time.FastDateFormat_PrinterTest::testCalendarTimezoneRespected','org.apache.commons.lang3.time.FastDatePrinterTest::testCalendarTimezoneRespected'):
        match=re.fullmatch(r'AssertionError: expected:<(.+) \[IC\]T> but was:<(.+) \[PS\]T>',value)
        require(match and match[1]==match[2],'Unexpected timezone-format failure')
        return 'AssertionError: expected:<CLOCK [IC]T> but was:<CLOCK [PS]T>'
    if requested=='org.apache.commons.math3.distribution.MultivariateNormalDistributionTest::testUnivariateDistribution':
        match=re.fullmatch(r'AssertionError: expected:<([^>]+)> but was:<([^>]+)>',value)
        require(match is not None,'Unexpected distribution failure')
        x,y=map(float,match.groups())
        require(x>0 and abs(y/x-2.506628274631)<1e-8,'Unexpected normal-density ratio')
        return 'AssertionError: normal density differs by sqrt(2*pi)'
    if requested=='org.apache.commons.math3.optimization.direct.CMAESOptimizerTest::testFitAccuracyDependsOnBoundary':
        match=re.fullmatch(r'AssertionError: expected:<([^>]+)> but was:<8.0>',value)
        require(match and abs(float(match[1])-11.1)<1e-5,'Unexpected boundary optimum')
        return 'AssertionError: expected:<11.1 within 1e-5> but was:<8.0>'
    if requested=='org.apache.commons.math3.optimization.direct.CMAESOptimizerTest::testMath864':
        match=re.fullmatch(r'AssertionError: Out of bounds \(([^ ]+) > 0.5\)',value)
        require(match and 0.5<float(match[1])<1,'Unexpected optimization bound failure')
        return 'AssertionError: Out of bounds (value between 0.5 and 1 > 0.5)'
    return value


def verify_failure(expected, actual, archived_block, fresh_log):
    requested=archived_block.split('\n',1)[0].strip()
    require(normalize_failure(expected.split(':',1)[0])==normalize_failure(actual.split(':',1)[0]), 'Failure exception type mismatch: '+actual)
    expected_message=expected.partition(':')[2].strip()
    if expected_message:
        require(failure_key(expected,requested)==failure_key(actual,requested),'Failure message mismatch: expected '+expected+' got '+actual)
    # Require a matching first application stack frame, even if archived message is empty.
    frames=re.findall(r'^\s+at ((?:org\.mockito|org\.mockitousage|org\.apache\.commons|org\.joda|org\.jfree|com\.google)[^\r\n]+)',archived_block,re.M)
    if not frames:
        require('Expected exception:' in expected and
                'org.junit.internal.runners.statements.ExpectException.evaluate(' in archived_block and
                'org.junit.internal.runners.statements.ExpectException.evaluate(' in fresh_log,
                'No application frame or matching JUnit expected-exception frame')
        return
    if expected.startswith('java.lang.StackOverflowError'):
        require(any(frame.split('(')[0]+'(' in fresh_log for frame in frames),'Recursion failure methods not reproduced')
    else:
        require(normalize_failure(frames[0]) in normalize_failure(fresh_log), 'Archived application failure frame not reproduced: '+frames[0])


def map_hits(hit_lines, methods):
    by_source = defaultdict(list)
    for row in methods: by_source[row['src_path']].append(row)
    selected={};unmapped=[]
    for hit in hit_lines:
        binary,source,name,descriptor,numbers=hit.split('\t')
        package=binary.rsplit('/',1)[0]+'/' if '/' in binary else ''
        paths=[p for p in by_source if p.endswith('/'+package+source) or p==package+source]
        if not paths and package=='org/apache/commons/lang/oldenum/':
            original_package='org/apache/commons/lang/enum/'
            paths=[p for p in by_source if p.endswith('/'+original_package+source)]
        if not paths and name in ('<init>','values','valueOf'):
            unmapped.append(hit)
            continue
        require(len(paths)==1, 'Ambiguous/missing production source for '+hit)
        lines={int(n) for n in numbers.split(',') if n}
        candidates=[]
        for row in by_source[paths[0]]:
            short=row['signature'].split('(')[0].rsplit('.',1)[-1]
            if name=='<init>':
                if short != row['class_name'].rsplit('.',1)[-1]: continue
            elif short!=name: continue
            overlap=sum(row['begin_line']<=n<=row['end_line'] for n in lines)
            if overlap: candidates.append((overlap,row))
        if candidates:
            best=max(score for score,row in candidates)
            choices=[row for score,row in candidates if score==best]
            # A nested anonymous method can share its name with the enclosing
            # method. Bytecode lines belong to the smallest containing declaration.
            size=min(row['end_line']-row['begin_line'] for row in choices)
            choices=[row for row in choices if row['end_line']-row['begin_line']==size]
            require(len(choices)==1, 'Ambiguous source method for '+hit)
            row=choices[0]; selected[identity(row)]=row
        else:
            # Implicit constructors/enum compiler methods have no declared source candidate.
            require(name=='<init>' or name in ('values','valueOf'), 'Unmapped declared method: '+hit)
            unmapped.append(hit)
    return list(selected.values()),unmapped


def result_failure(path, requested):
    # splitlines also splits vertical tabs that legitimately occur in Java messages.
    rows=path.read_text(encoding='utf-8').split('\n')
    require(rows[0]=='counts\t1\t1\t0','Trigger did not fail exactly once: '+requested)
    failures=[line.split('\t',4) for line in rows[1:] if line.startswith('failure\t')]
    require(len(failures)==1,'Unexpected failures')
    _,cls,method,exception,message=failures[0]
    require(cls+'::'+method==requested,'Failure is not in requested test: '+str(failures))
    return exception+(': '+message if message else '')


def collect(cid, cache, d4j, jdk, jdk7, runtime, runs, inputs, agent, junit):
    work=(runs/cid).resolve();work.mkdir(parents=True, exist_ok=True)
    raw=cache/'raw_extracted'/cid
    methods=read(raw/'snippet.json')
    expected=expected_tests((raw/'failing_tests').read_text(encoding='utf-8-sig'))
    root,sourceaudit=materialize(cid,cache,work)
    extraction=read(cache/'source_audit'/f'{cid}.extraction.json')
    prod=root/extraction['production_root']
    test_classes=work/'test_classes'
    jars=dependencies(cid.split('_')[0],root,d4j)+[junit]
    if cid.startswith('Chart_'):
        jars.insert(0,junit)
    if cid.startswith('Lang_') and cid not in ('Lang_32','Lang_34'):
        jars.insert(0,d4j/'framework/projects/Lang/lib/junit/junit/4.7/junit-4.7.jar')
    elif cid.startswith('Lang_'): jars.insert(0,junit)
    support=work/'support_classes'
    if cid.startswith('Closure_'):
        support.mkdir(exist_ok=True)
        if (root/'lib/rhino').exists() and not (root/'build/lib/rhino.jar').exists():
            run([jdk/'bin/java.exe','-cp',os.pathsep.join(map(str,[root/'lib/ant.jar',root/'lib/ant-launcher.jar',jdk/'lib/tools.jar'])),
                 'org.apache.tools.ant.Main','rhino-jarjar'],root,work/'rhino_build.log')
        if (root/'build/lib/rhino.jar').exists(): jars.append(root/'build/lib/rhino.jar')
        generated=sorted((root/'gen').rglob('*.java'))
        if generated: javac(jdk,generated,support,jars,[],work,'generated_compile')
        jars.insert(0,support)
    sources=sorted(prod.rglob('*.java'))
    adaptations=[]
    source_hashes={p.relative_to(root).as_posix():digest(p.read_bytes()) for p in sources}
    source_lines={p.relative_to(root).as_posix():p.read_text(encoding='utf-8').splitlines() for p in sources}
    for row in methods:
        require(source_lines[row['src_path']][row['begin_line']-1:row['end_line']]==row['snippet'].splitlines(),
                'Production source changed: '+row['signature'])
    dependency_hashes={str(p):digest(p.read_bytes()) if p.is_file() else
        digest(encode({c.relative_to(p).as_posix():digest(c.read_bytes()) for c in sorted(p.rglob('*.class'))})) for p in jars}
    build_key=digest(encode(dict(sources=source_hashes,dependencies=dependency_hashes,
                                compiler=digest((jdk/'bin/javac.exe').read_bytes()),target='7')))
    prod_classes=work/('production_classes_'+build_key[:16])
    compile_sources=[]
    for path in sources:
        if cid.startswith('Lang_') and '/org/apache/commons/lang/enum/' in path.as_posix():
            target=work/'compat_src'/path.relative_to(prod)
            target=Path(str(target).replace('/enum/','/oldenum/').replace('\\enum\\','\\oldenum\\'))
            target.parent.mkdir(parents=True,exist_ok=True)
            compatible=path.read_text(encoding='utf-8').replace('.enum;','.oldenum;')
            compatible=re.sub(r'\benum\b','enumValue',compatible)
            target.write_text(compatible,encoding='utf-8')
            compile_sources.append(target)
            adaptations.append({'file':path.relative_to(root).as_posix(),'compiled_as':str(target),
                'reason':'Official Lang.pm enum-to-oldenum package compatibility transformation; rename pre-Java-5 local identifier enum; source candidate universe retained.',
                'compiled_sha256':digest(target.read_bytes())})
        elif cid in ('Lang_44','Lang_45','Lang_46','Lang_47') and path.name=='EqualsBuilder.java':
            original=path.read_text(encoding='utf-8')
            before='((java.math.BigDecimal)lhs).compareTo(rhs)'
            require(original.count(before)==1,'Unexpected pre-generics BigDecimal call')
            target=work/'compat_src'/path.relative_to(prod);target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(original.replace(before,'((java.math.BigDecimal)lhs).compareTo((java.math.BigDecimal)rhs)'),encoding='utf-8')
            compile_sources.append(target)
            adaptations.append({'file':path.relative_to(root).as_posix(),'compiled_as':str(target),
                'reason':'Explicit cast matching the pre-Java-5 BigDecimal.compareTo(Object) runtime cast; retain branch and behavior.',
                'compiled_sha256':digest(target.read_bytes())})
        else: compile_sources.append(path)
    if not (work/(build_key+'.ok')).exists():
        javac(jdk,compile_sources,prod_classes,jars,[prod],work,'production_compile')
        (work/(build_key+'.ok')).write_text('compiled')
    if cid.startswith('Time_') and not (prod_classes/'org/joda/time/tz/data/ZoneInfoMap').exists():
        zone_source=prod/'org/joda/time/tz/src';zone_dest=prod_classes/'org/joda/time/tz/data'
        zone_dest.mkdir(parents=True,exist_ok=True)
        run([jdk/'bin/java.exe','-Dorg.joda.time.DateTimeZone.Provider=org.joda.time.tz.UTCProvider',
             '-cp',os.pathsep.join(map(str,[prod_classes]+jars)), 'org.joda.time.tz.ZoneInfoCompiler',
             '-src',zone_source,'-dst',zone_dest,'africa','antarctica','asia','australasia','europe',
             'northamerica','southamerica','pacificnew','etcetera','backward','systemv'],root,work/'timezone_build.log')
    if cid.startswith('Closure_'):
        messages=prod_classes/'rhino_ast/java/com/google/javascript/rhino/Messages.properties'
        messages.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(prod/'com/google/javascript/rhino/Messages.properties',messages)
    extra_prod=root/'mockmaker/bytebuddy/main/java'
    if extra_prod.is_dir():
        javac(jdk,sorted(extra_prod.rglob('*.java')),support,[prod_classes]+jars,[extra_prod],work,'mockmaker_compile')
        jars.insert(0,support)
    test_roots=[root/p for p in ('test','tests','src/test/java','src/test') if (root/p).is_dir()]
    if cid=='Mockito_5' and os.name=='nt':
        helper=root/'test/org/mockitoutil/ClassLoaders.java'
        original=(cache/'buggy_sources'/cid/'test/org/mockitoutil/ClassLoaders.java').read_text(encoding='utf-8')
        before=".substring(root.getAbsolutePath().length() + 1).replace('/', '.')"
        after=".substring(root.getAbsolutePath().length() + 1).replace(File.separatorChar, '.')"
        require(original.count(before)==1,'Unexpected classloader helper')
        helper.write_text(original.replace(before,after),encoding='utf-8',newline='')
        adaptations.append(dict(file='test/org/mockitoutil/ClassLoaders.java',
            before=before,after=after,reason='Normalize native path separators on Windows exactly as slash paths work on Linux; no production or triggering test method changes.'))
    test_sources=[]
    for requested,_ in expected:
        cls=requested.split('::')[0]
        found=[p/(cls.replace('.','/')+'.java') for p in test_roots if (p/(cls.replace('.','/')+'.java')).exists()]
        require(found,'Missing requested test class '+cls)
        test_sources.append(found[0])
    javac(jdk7 if cid=='Lang_15' else jdk,sorted(set(test_sources)),test_classes,[prod_classes]+jars,test_roots,work,'test_compile')
    whitelist=work/'production_classes.txt'
    compiled=sorted(p.relative_to(prod_classes).with_suffix('').as_posix() for p in prod_classes.rglob('*.class'))
    whitelist.write_text('\n'.join(compiled)+'\n',encoding='utf-8')
    resource_roots=[root,prod]+test_roots+[p for p in (root/'src/main/resources',root/'src/test/resources',root/'test-resources') if p.exists()]
    cp=os.pathsep.join(map(str,[prod_classes,test_classes,agent]+jars+resource_roots))
    runner='TriggerRunner'
    if cid=='Closure_26':
        compat=work/'compat_runner'
        compat_source=Path(__file__).with_name('compat_java')/'PosixSourcePathRunner.java'
        javac(jdk,[compat_source],compat,[agent],[],work,'compat_runner_compile')
        cp=str(compat)+os.pathsep+cp
        runner='PosixSourcePathRunner'
        adaptations.append({'reason':'POSIX File.separator constants for in-memory JavaScript module names; native Windows filesystem retained; identical baseline and instrumented runner.',
            'source_sha256':digest(compat_source.read_bytes())})
    union=set();runs_meta=[]
    for number,(requested,expected_error) in enumerate(expected,1):
        prefix=work/f'test_{number:03d}'
        hits=prefix.with_suffix('.hits.tsv');result=prefix.with_suffix('.result.tsv')
        runtime_jdk=jdk
        if cid in ('Lang_2','Time_21'):
            runtime_jdk=jdk7
        baseline_result=prefix.with_suffix('.baseline.result.tsv')
        baseline_log=prefix.with_suffix('.baseline.log')
        platform_args=['-Duser.language=en','-Duser.country=US','-Djava.awt.headless=true']
        baseline_cmd=[runtime_jdk/'bin/java.exe',*platform_args,'-Duser.timezone=America/Los_Angeles','-Dfile.encoding=UTF-8',
             '-cp',cp,runner,requested,baseline_result]
        run(baseline_cmd,root,baseline_log,timeout=120)
        baseline_failure=result_failure(baseline_result,requested)
        args=[runtime_jdk/'bin/java.exe',*platform_args,'-Duser.timezone=America/Los_Angeles','-Dfile.encoding=UTF-8',
              '-javaagent:'+str(agent)+'='+str(whitelist)+'|'+str(hits)+'|'+str(runtime/'coverage-recorder.jar'),'-cp',cp,
              runner,requested,result]
        run(args,root,prefix.with_suffix('.log'),timeout=120)
        actual=result_failure(result,requested)
        require(failure_key(baseline_failure,requested)==failure_key(actual,requested),'Instrumentation changed failure: '+requested)
        archived=(raw/'failing_tests').read_text(encoding='utf-8-sig')
        archived_block=next(block for block in re.split(r'^---\s+',archived,flags=re.M)[1:] if block.splitlines()[0].strip()==requested)
        verify_failure(expected_error,actual,archived_block,prefix.with_suffix('.log').read_text(encoding='utf-8',errors='replace'))
        verify_failure(expected_error,baseline_failure,archived_block,baseline_log.read_text(encoding='utf-8',errors='replace'))
        require(Path(str(hits)+'.errors').read_text(encoding='utf-8')=='','Instrumentation errors')
        lines=hits.read_text(encoding='utf-8').splitlines()
        require(lines,'Empty method coverage')
        selected,unmapped=map_hits(lines,methods)
        union.update(identity(m) for m in selected)
        runs_meta.append(dict(test=requested,expected_failure=expected_error,observed_failure=actual,
            baseline_failure=baseline_failure,baseline_log_sha256=digest(baseline_log.read_bytes()),
            baseline_result_sha256=digest(baseline_result.read_bytes()),result_sha256=digest(result.read_bytes()),
            covered_method_count=len(selected),covered_source_identities=[list(identity(m)) for m in selected],
            hits_file=hits.name,hits_sha256=digest(hits.read_bytes()),
            log_sha256=digest(prefix.with_suffix('.log').read_bytes()),
            compiler_generated_entries_without_declared_candidate=unmapped))
    selected=[m for m in methods if identity(m) in union]
    require(selected,'No covered source methods')
    manifest=dict(case_id=cid,candidate_scope='trigger_test_executed_methods_and_constructors',
        collection='ASM method-entry instrumentation; union of isolated triggering JUnit methods',
        harness='portable javac/JUnit harness, not Defects4J checkout/build',
        jdk=str(runtime_jdk),compiler_jdk=str(jdk),timezone='America/Los_Angeles',runtime_tests_executed=True,
        all_trigger_failures_reproduced=True,original_candidate_count=len(methods),
        uninstrumented_baseline_verified=True,production_build_key=build_key,
        compiled_source_sha256=source_hashes,dependency_sha256=dependency_hashes,
        additional_build_roots=['mockmaker/bytebuddy/main/java'] if extra_prod.is_dir() else [],
        failure_match_policy='Same test, exception category (JUnit AssertionError variants equivalent), normalized message when archived, and application frame; normalize object/generated-class IDs and source line offsets. StackOverflowError requires a shared recursive application method.',
        test_harness_adaptations=adaptations,
        platform_properties=platform_args,
        covered_candidate_count=len(selected),raw_methods_sha256=digest((raw/'snippet.json').read_bytes()),
        trigger_report_sha256=digest((raw/'failing_tests').read_bytes()),
        agent_sha256=digest(agent.read_bytes()),
        recorder_sha256=digest((runtime/'coverage-recorder.jar').read_bytes()),
        covered_source_identities=[list(identity(m)) for m in selected],tests=runs_meta,
        limitations='Setup/teardown and class initialization side-effect calls are included. Implicit constructors and compiler-generated methods without a declared source candidate are excluded. Original archived failure report is preserved; fresh run logs are operator-side.')
    write(work/'coverage.json',manifest)
    print(f'COVERED {cid}: {len(methods)} -> {len(selected)}, triggers={len(expected)}',flush=True)
    return manifest


def main():
    import sys
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8',errors='backslashreplace')
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cache',type=Path,required=True)
    p.add_argument('--d4j',type=Path,required=True)
    p.add_argument('--jdk',type=Path,required=True)
    p.add_argument('--jdk7',type=Path,required=True,help='Java 7 runtime for Lang_2 and Time_21')
    p.add_argument('--runtime',type=Path,default=Path(__file__).resolve().parents[1]/'coverage_runtime')
    p.add_argument('--runs',type=Path,default=Path(__file__).resolve().parents[1]/'coverage_runs')
    p.add_argument('--inputs',type=Path,default=Path(__file__).resolve().parents[2]/'input')
    p.add_argument('--cases',nargs='+',required=True)
    a=p.parse_args()
    for key in ('cache','d4j','jdk','jdk7','runtime','runs','inputs'): setattr(a,key,getattr(a,key).resolve())
    a.runtime.mkdir(parents=True,exist_ok=True)
    agent,junit=setup_agent(a.jdk,a.d4j,a.runtime)
    errors=[]
    for cid in a.cases:
        require(re.fullmatch(r'(Chart|Math|Mockito|Closure|Lang|Time)_[1-9]\d*',cid),'Invalid case ID')
        try: collect(cid,a.cache,a.d4j,a.jdk,a.jdk7,a.runtime,a.runs,a.inputs,agent,junit)
        except Exception as exc:
            errors.append(dict(case_id=cid,error=str(exc)))
            print('FAILED',cid,str(exc),flush=True)
    write(a.runs/'last_collection_errors.json',errors)
    if errors: raise SystemExit(1)


if __name__=='__main__': main()
