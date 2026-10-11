# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizerTest.testCircleFitting()
Resolved declaration: org.apache.commons.math.optimization.general.LevenbergMarquardtOptimizerTest.testCircleFitting()
Source: src/test/java/org/apache/commons/math/optimization/general/LevenbergMarquardtOptimizerTest.java

```java
398 |     public void testCircleFitting() throws FunctionEvaluationException, OptimizationException {
399 |         Circle circle = new Circle();
400 |         circle.addPoint( 30.0,  68.0);
401 |         circle.addPoint( 50.0,  -6.0);
402 |         circle.addPoint(110.0, -20.0);
403 |         circle.addPoint( 35.0,  15.0);
404 |         circle.addPoint( 45.0,  97.0);
405 |         LevenbergMarquardtOptimizer optimizer = new LevenbergMarquardtOptimizer();
406 |         VectorialPointValuePair optimum =
407 |             optimizer.optimize(circle, new double[] { 0, 0, 0, 0, 0 }, new double[] { 1, 1, 1, 1, 1 },
408 |                                new double[] { 98.680, 47.345 });
409 |         assertTrue(optimizer.getEvaluations() < 10);
410 |         assertTrue(optimizer.getJacobianEvaluations() < 10);
411 |         double rms = optimizer.getRMS();
412 |         assertEquals(1.768262623567235,  Math.sqrt(circle.getN()) * rms,  1.0e-10);
413 |         Point2D.Double center = new Point2D.Double(optimum.getPointRef()[0], optimum.getPointRef()[1]);
414 |         assertEquals(69.96016176931406, circle.getRadius(center), 1.0e-10);
415 |         assertEquals(96.07590211815305, center.x,      1.0e-10);
416 |         assertEquals(48.13516790438953, center.y,      1.0e-10);
417 |         double[][] cov = optimizer.getCovariances();
418 |         assertEquals(1.839, cov[0][0], 0.001);
419 |         assertEquals(0.731, cov[0][1], 0.001);
420 |         assertEquals(cov[0][1], cov[1][0], 1.0e-14);
421 |         assertEquals(0.786, cov[1][1], 0.001);
422 |         double[] errors = optimizer.guessParametersErrors();
423 |         assertEquals(1.384, errors[0], 0.001);
424 |         assertEquals(0.905, errors[1], 0.001);
425 | 
426 |         // add perfect measurements and check errors are reduced
427 |         double  r = circle.getRadius(center);
428 |         for (double d= 0; d < 2 * Math.PI; d += 0.01) {
429 |             circle.addPoint(center.x + r * Math.cos(d), center.y + r * Math.sin(d));
430 |         }
431 |         double[] target = new double[circle.getN()];
432 |         Arrays.fill(target, 0.0);
433 |         double[] weights = new double[circle.getN()];
434 |         Arrays.fill(weights, 2.0);
435 |         optimizer.optimize(circle, target, weights, new double[] { 98.680, 47.345 });
436 |         cov = optimizer.getCovariances();
437 |         assertEquals(0.0016, cov[0][0], 0.001);
438 |         assertEquals(3.2e-7, cov[0][1], 1.0e-9);
439 |         assertEquals(cov[0][1], cov[1][0], 1.0e-14);
440 |         assertEquals(0.0016, cov[1][1], 0.001);
441 |         errors = optimizer.guessParametersErrors();
442 |         assertEquals(0.004, errors[0], 0.001);
443 |         assertEquals(0.004, errors[1], 0.001);
444 | 
445 |     }
```
