# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.estimation.GaussNewtonEstimatorTest.testBoundParameters()
Resolved declaration: org.apache.commons.math.estimation.GaussNewtonEstimatorTest.testBoundParameters()
Source: src/test/org/apache/commons/math/estimation/GaussNewtonEstimatorTest.java

```java
451 |   public void testBoundParameters() throws EstimationException {
452 |       EstimatedParameter[] p = {
453 |         new EstimatedParameter("unbound0", 2, false),
454 |         new EstimatedParameter("unbound1", 2, false),
455 |         new EstimatedParameter("bound",    2, true)
456 |       };
457 |       LinearProblem problem = new LinearProblem(new LinearMeasurement[] {
458 |         new LinearMeasurement(new double[] { 1.0, 1.0, 1.0 },
459 |                               new EstimatedParameter[] { p[0], p[1], p[2] },
460 |                               3.0),
461 |         new LinearMeasurement(new double[] { 1.0, -1.0, 1.0 },
462 |                               new EstimatedParameter[] { p[0], p[1], p[2] },
463 |                               1.0),
464 |         new LinearMeasurement(new double[] { 1.0, 3.0, 2.0 },
465 |                               new EstimatedParameter[] { p[0], p[1], p[2] },
466 |                               7.0)
467 |       });
468 | 
469 |       GaussNewtonEstimator estimator = new GaussNewtonEstimator(100, 1.0e-6, 1.0e-6);
470 |       estimator.estimate(problem);
471 |       assertTrue(estimator.getRMS(problem) < 1.0e-10);
472 |       double[][] covariances = estimator.getCovariances(problem);
473 |       int i0 = 0, i1 = 1;
474 |       if (problem.getUnboundParameters()[0].getName().endsWith("1")) {
475 |           i0 = 1;
476 |           i1 = 0;
477 |       }
478 |       assertEquals(11.0 / 24, covariances[i0][i0], 1.0e-10);
479 |       assertEquals(-3.0 / 24, covariances[i0][i1], 1.0e-10);
480 |       assertEquals(-3.0 / 24, covariances[i1][i0], 1.0e-10);
481 |       assertEquals( 3.0 / 24, covariances[i1][i1], 1.0e-10);
482 | 
483 |       double[] errors = estimator.guessParametersErrors(problem);
484 |       assertEquals(0, errors[i0], 1.0e-10);
485 |       assertEquals(0, errors[i1], 1.0e-10);
486 | 
487 |   }
```
