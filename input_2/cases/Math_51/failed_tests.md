# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.analysis.solvers.RegulaFalsiSolverTest.testIssue631()
Resolved declaration: org.apache.commons.math.analysis.solvers.RegulaFalsiSolverTest.testIssue631()
Source: src/test/java/org/apache/commons/math/analysis/solvers/RegulaFalsiSolverTest.java

```java
43 |     @Test
44 |     public void testIssue631() {
45 |         final UnivariateRealFunction f = new UnivariateRealFunction() {
46 |                 @Override
47 |                 public double value(double x) {
48 |                     return Math.exp(x) - Math.pow(Math.PI, 3.0);
49 |                 }
50 |             };
51 | 
52 |         final UnivariateRealSolver solver = new RegulaFalsiSolver();
53 |         final double root = solver.solve(3624, f, 1, 10);
54 |         Assert.assertEquals(3.4341896575482003, root, 1e-15);
55 | 	}
```
