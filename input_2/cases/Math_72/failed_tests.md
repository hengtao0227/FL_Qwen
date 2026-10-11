# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.analysis.solvers.BrentSolverTest.testRootEndpoints()
Resolved declaration: org.apache.commons.math.analysis.solvers.BrentSolverTest.testRootEndpoints()
Source: src/test/java/org/apache/commons/math/analysis/solvers/BrentSolverTest.java

```java
305 |     public void testRootEndpoints() throws Exception {
306 |         UnivariateRealFunction f = new SinFunction();
307 |         UnivariateRealSolver solver = new BrentSolver();
308 | 
309 |         // endpoint is root
310 |         double result = solver.solve(f, Math.PI, 4);
311 |         assertEquals(Math.PI, result, solver.getAbsoluteAccuracy());
312 | 
313 |         result = solver.solve(f, 3, Math.PI);
314 |         assertEquals(Math.PI, result, solver.getAbsoluteAccuracy());
315 | 
316 |         result = solver.solve(f, Math.PI, 4, 3.5);
317 |         assertEquals(Math.PI, result, solver.getAbsoluteAccuracy());
318 | 
319 |         result = solver.solve(f, 3, Math.PI, 3.07);
320 |         assertEquals(Math.PI, result, solver.getAbsoluteAccuracy());
321 | 
322 |     }
```
