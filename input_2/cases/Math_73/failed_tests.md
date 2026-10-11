# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.analysis.solvers.BrentSolverTest.testBadEndpoints()
Resolved declaration: org.apache.commons.math.analysis.solvers.BrentSolverTest.testBadEndpoints()
Source: src/test/java/org/apache/commons/math/analysis/solvers/BrentSolverTest.java

```java
317 |     public void testBadEndpoints() throws Exception {
318 |         UnivariateRealFunction f = new SinFunction();
319 |         UnivariateRealSolver solver = new BrentSolver();
320 |         try {  // bad interval
321 |             solver.solve(f, 1, -1);
322 |             fail("Expecting IllegalArgumentException - bad interval");
323 |         } catch (IllegalArgumentException ex) {
324 |             // expected
325 |         }
326 |         try {  // no bracket
327 |             solver.solve(f, 1, 1.5);
328 |             fail("Expecting IllegalArgumentException - non-bracketing");
329 |         } catch (IllegalArgumentException ex) {
330 |             // expected
331 |         }
332 |         try {  // no bracket
333 |             solver.solve(f, 1, 1.5, 1.2);
334 |             fail("Expecting IllegalArgumentException - non-bracketing");
335 |         } catch (IllegalArgumentException ex) {
336 |             // expected
337 |         }
338 |     }
```
