"""Executable regression: distinguish overloads, anonymous methods and thrown exits."""
import argparse
from pathlib import Path
import tempfile
from collect_method_coverage import javac, run, map_hits, normalize_failure, failure_key, result_failure
from case_io import require


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--jdk',type=Path,required=True)
    p.add_argument('--runtime',type=Path,required=True)
    a=p.parse_args(); a.jdk=a.jdk.resolve(); a.runtime=a.runtime.resolve()
    with tempfile.TemporaryDirectory(prefix='coverage_regression_',dir=a.runtime) as temp:
        root=Path(temp)
        code='''public class CoverageFixture {
    public CoverageFixture() {}
    public void overloaded(int n) {}
    public void overloaded(String n) {}
    public void unused() {}
    public void throwsNow() { throw new IllegalStateException("expected"); }
    public Runnable callback() { return new Runnable() { public void run() {} }; }
    public static void main(String[] args) { CoverageFixture f = new CoverageFixture(); f.overloaded(1); try { f.throwsNow(); } catch (IllegalStateException expected) {} f.callback().run(); }
}
'''
        source=root/'CoverageFixture.java';source.write_text(code,encoding='utf-8')
        classes=root/'classes'
        javac(a.jdk,[source],classes,[],[],root,'compile')
        names=root/'classes.txt';names.write_text('\n'.join(p.stem for p in classes.glob('*.class')),encoding='utf-8')
        hits=root/'hits.tsv';agent=a.runtime/'method-entry-agent.jar';recorder=a.runtime/'coverage-recorder.jar'
        run([a.jdk/'bin/java.exe','-javaagent:'+str(agent)+'='+str(names)+'|'+str(hits)+'|'+str(recorder),
             '-cp',classes,'CoverageFixture'],root,root/'run.log')
        require(Path(str(hits)+'.errors').read_text()=='','Fixture instrumentation failed')
        rows=[]
        for signature,line in [('CoverageFixture()',2),('overloaded(int)',3),('overloaded(String)',4),('unused()',5),
                ('throwsNow()',6),('callback()',7),('anonymous_L7.run()',7),('main(String[])',8)]:
            cls='CoverageFixture.anonymous_L7' if signature.startswith('anonymous') else 'CoverageFixture'
            rows.append(dict(src_path='CoverageFixture.java',class_name=cls,signature='CoverageFixture.'+signature,
                             begin_line=line,end_line=line))
        selected,implicit=map_hits(hits.read_text().splitlines(),rows)
        got={r['signature'] for r in selected}
        expected={r['signature'] for r in rows if r['begin_line'] not in (4,5)}
        require(got==expected,'Wrong coverage: '+str(got))
        require(any('\t<init>\t' in h for h in implicit),'Implicit constructor was not handled')
        require(normalize_failure('java.lang.AssertionError: expected:<1> but was:<0>') !=
                normalize_failure('junit.framework.AssertionFailedError: expected:<1> but was:<2>'),
                'Normalization hides meaningful assertion differences')
        nested=[dict(src_path='p/X.java',class_name='p.X',signature='p.X.visit()',begin_line=10,end_line=30),
                dict(src_path='p/X.java',class_name='p.X.anonymous_L15',signature='p.X.anonymous_L15.visit()',begin_line=16,end_line=20)]
        mapped,_=map_hits(['p/X$1\tX.java\tvisit\t()V\t17,18,19'],nested)
        require(mapped==[nested[1]],'Nested same-name method incorrectly mapped to enclosing method')
        vertical=root/'vertical.tsv'
        vertical.write_text('counts\t1\t1\t0\nfailure\tp.T\ttest\tjava.lang.AssertionError\ta\v1 trailing text\n',encoding='utf-8')
        require(result_failure(vertical,'p.T::test').endswith('a\v1 trailing text'),'Vertical tab truncated failure message')
        test='org.apache.commons.math3.optimization.direct.CMAESOptimizerTest::testMath864'
        require(failure_key('java.lang.AssertionError: Out of bounds (0.52 > 0.5)',test)==
                failure_key('junit.framework.AssertionFailedError: Out of bounds (0.55 > 0.5)',test),'Valid stochastic failure mismatch')
        try: failure_key('java.lang.AssertionError: Out of bounds (0.2 > 0.5)',test)
        except ValueError: pass
        else: raise AssertionError('Invalid stochastic failure accepted')
        test='org.apache.commons.math3.distribution.HypergeometricDistributionTest::testMath1021'
        require(failure_key('java.lang.AssertionError: sample=-49',test)==
                failure_key('junit.framework.AssertionFailedError: sample=-50',test),'Negative sample mismatch')
        try: failure_key('java.lang.AssertionError: sample=49',test)
        except ValueError: pass
        else: raise AssertionError('Nonnegative sample accepted as the negative-sample failure')
        print('PASS: executed constructor, exact overload, thrown method, anonymous method; unused methods excluded')


if __name__=='__main__': main()
