# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.analysis.solvers.BisectionSolverTest.testMath369()
Resolved declaration: org.apache.commons.math.analysis.solvers.BisectionSolverTest.testMath369()
Source: src/test/java/org/apache/commons/math/analysis/solvers/BisectionSolverTest.java

```java
98 |     public void testMath369() throws Exception {
99 |         UnivariateRealFunction f = new SinFunction();
100 |         UnivariateRealSolver solver = new BisectionSolver();
101 |         assertEquals(Math.PI, solver.solve(f, 3.0, 3.2, 3.1), solver.getAbsoluteAccuracy());
102 |     }
```
