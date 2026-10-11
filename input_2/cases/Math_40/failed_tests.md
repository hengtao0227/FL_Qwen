# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolverTest.testIssue716()
Resolved declaration: org.apache.commons.math.analysis.solvers.BracketingNthOrderBrentSolverTest.testIssue716()
Source: src/test/java/org/apache/commons/math/analysis/solvers/BracketingNthOrderBrentSolverTest.java

```java
84 |     @Test
85 |     public void testIssue716() {
86 |         BracketingNthOrderBrentSolver solver =
87 |                 new BracketingNthOrderBrentSolver(1.0e-12, 1.0e-10, 1.0e-22, 5);
88 |         UnivariateFunction sharpTurn = new UnivariateFunction() {
89 |             public double value(double x) {
90 |                 return (2 * x + 1) / (1.0e9 * (x + 1));
91 |             }
92 |         };
93 |         double result = solver.solve(100, sharpTurn, -0.9999999, 30, 15, AllowedSolution.RIGHT_SIDE);
94 |         Assert.assertEquals(0, sharpTurn.value(result), solver.getFunctionValueAccuracy());
95 |         Assert.assertTrue(sharpTurn.value(result) >= 0);
96 |         Assert.assertEquals(-0.5, result, 1.0e-10);
97 |     }
```
