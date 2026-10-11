# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.direct.CMAESOptimizerTest.testMath864()
Resolved declaration: org.apache.commons.math3.optimization.direct.CMAESOptimizerTest.testMath864()
Source: src/test/java/org/apache/commons/math3/optimization/direct/CMAESOptimizerTest.java

```java
375 |     @Test
376 |     public void testMath864() {
377 |         final CMAESOptimizer optimizer = new CMAESOptimizer();
378 |         final MultivariateFunction fitnessFunction = new MultivariateFunction() {
379 |                 @Override
380 |                 public double value(double[] parameters) {
381 |                     final double target = 1;
382 |                     final double error = target - parameters[0];
383 |                     return error * error;
384 |                 }
385 |             };
386 | 
387 |         final double[] start = { 0 };
388 |         final double[] lower = { -1e6 };
389 |         final double[] upper = { 0.5 };
390 |         final double[] result = optimizer.optimize(10000, fitnessFunction, GoalType.MINIMIZE,
391 |                                                    start, lower, upper).getPoint();
392 |         Assert.assertTrue("Out of bounds (" + result[0] + " > " + upper[0] + ")",
393 |                           result[0] <= upper[0]);
394 |     }
```
