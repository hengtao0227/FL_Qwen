# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.analysis.BrentSolverTest.testRootEndpoints()
Resolved declaration: org.apache.commons.math.analysis.BrentSolverTest.testRootEndpoints()
Source: src/test/org/apache/commons/math/analysis/BrentSolverTest.java

```java
271 |     public void testRootEndpoints() throws Exception {
272 |         UnivariateRealFunction f = new SinFunction();
273 |         UnivariateRealSolver solver = new BrentSolver(f);
274 |         
275 |         // endpoint is root
276 |         double result = solver.solve(Math.PI, 4);
277 |         assertEquals(result, Math.PI, solver.getAbsoluteAccuracy());
278 | 
279 |         result = solver.solve(3, Math.PI);
280 |         assertEquals(result, Math.PI, solver.getAbsoluteAccuracy());
281 |     }
```
