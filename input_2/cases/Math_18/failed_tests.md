# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.direct.CMAESOptimizerTest.testFitAccuracyDependsOnBoundary()
Resolved declaration: org.apache.commons.math3.optimization.direct.CMAESOptimizerTest.testFitAccuracyDependsOnBoundary()
Source: src/test/java/org/apache/commons/math3/optimization/direct/CMAESOptimizerTest.java

```java
430 |     @Test
431 |     public void testFitAccuracyDependsOnBoundary() {
432 |         final CMAESOptimizer optimizer = new CMAESOptimizer();
433 |         final MultivariateFunction fitnessFunction = new MultivariateFunction() {
434 |                 public double value(double[] parameters) {
435 |                     final double target = 11.1;
436 |                     final double error = target - parameters[0];
437 |                     return error * error;
438 |                 }
439 |             };
440 | 
441 |         final double[] start = { 1 };
442 |  
443 |         // No bounds.
444 |         PointValuePair result = optimizer.optimize(100000, fitnessFunction, GoalType.MINIMIZE,
445 |                                                    start);
446 |         final double resNoBound = result.getPoint()[0];
447 | 
448 |         // Optimum is near the lower bound.
449 |         final double[] lower = { -20 };
450 |         final double[] upper = { 5e16 };
451 |         result = optimizer.optimize(100000, fitnessFunction, GoalType.MINIMIZE,
452 |                                     start, lower, upper);
453 |         final double resNearLo = result.getPoint()[0];
454 | 
455 |         // Optimum is near the upper bound.
456 |         lower[0] = -5e16;
457 |         upper[0] = 20;
458 |         result = optimizer.optimize(100000, fitnessFunction, GoalType.MINIMIZE,
459 |                                     start, lower, upper);
460 |         final double resNearHi = result.getPoint()[0];
461 | 
462 |         // System.out.println("resNoBound=" + resNoBound +
463 |         //                    " resNearLo=" + resNearLo +
464 |         //                    " resNearHi=" + resNearHi);
465 | 
466 |         // The two values currently differ by a substantial amount, indicating that
467 |         // the bounds definition can prevent reaching the optimum.
468 |         Assert.assertEquals(resNoBound, resNearLo, 1e-3);
469 |         Assert.assertEquals(resNoBound, resNearHi, 1e-3);
470 |     }
```
