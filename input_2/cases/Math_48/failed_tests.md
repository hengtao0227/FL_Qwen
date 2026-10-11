# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.analysis.solvers.RegulaFalsiSolverTest.testIssue631()
Resolved declaration: org.apache.commons.math.analysis.solvers.RegulaFalsiSolverTest.testIssue631()
Source: src/test/java/org/apache/commons/math/analysis/solvers/RegulaFalsiSolverTest.java

```java
44 |     @Test(expected=ConvergenceException.class)
45 |     public void testIssue631() {
46 |         final UnivariateRealFunction f = new UnivariateRealFunction() {
47 |                 /** {@inheritDoc} */
48 |                 public double value(double x) {
49 |                     return Math.exp(x) - Math.pow(Math.PI, 3.0);
50 |                 }
51 |             };
52 | 
53 |         final UnivariateRealSolver solver = new RegulaFalsiSolver();
54 |         final double root = solver.solve(3624, f, 1, 10);
55 |         Assert.assertEquals(3.4341896575482003, root, 1e-15);
56 | 	}
```
