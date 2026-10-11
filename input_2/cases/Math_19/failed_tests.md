# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.direct.CMAESOptimizerTest.testBoundaryRangeTooLarge()
Resolved declaration: org.apache.commons.math3.optimization.direct.CMAESOptimizerTest.testBoundaryRangeTooLarge()
Source: src/test/java/org/apache/commons/math3/optimization/direct/CMAESOptimizerTest.java

```java
400 |     @Test(expected=NumberIsTooLargeException.class)
401 |     public void testBoundaryRangeTooLarge() {
402 |         final CMAESOptimizer optimizer = new CMAESOptimizer();
403 |         final MultivariateFunction fitnessFunction = new MultivariateFunction() {
404 |                 public double value(double[] parameters) {
405 |                     if (Double.isNaN(parameters[0])) {
406 |                         throw new MathIllegalStateException();
407 |                     }
408 |                     final double target = 1;
409 |                     final double error = target - parameters[0];
410 |                     return error * error;
411 |                 }
412 |             };
413 | 
414 |         final double[] start = { 0 };
415 | 
416 |         // The difference between upper and lower bounds is used to used
417 |         // normalize the variables: In case of overflow, NaN is produced.
418 |         final double max = Double.MAX_VALUE / 2;
419 |         final double tooLarge = FastMath.nextUp(max);
420 |         final double[] lower = { -tooLarge };
421 |         final double[] upper = { tooLarge };
422 |         final double[] result = optimizer.optimize(10000, fitnessFunction, GoalType.MINIMIZE,
423 |                                                    start, lower, upper).getPoint();
424 |     }
```
