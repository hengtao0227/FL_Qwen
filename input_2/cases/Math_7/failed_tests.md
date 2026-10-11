# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.ode.nonstiff.DormandPrince853IntegratorTest.testEventsScheduling()
Resolved declaration: org.apache.commons.math3.ode.nonstiff.DormandPrince853IntegratorTest.testEventsScheduling()
Source: src/test/java/org/apache/commons/math3/ode/nonstiff/DormandPrince853IntegratorTest.java

```java
336 |   @Test
337 |   public void testEventsScheduling() {
338 | 
339 |       FirstOrderDifferentialEquations sincos = new FirstOrderDifferentialEquations() {
340 | 
341 |           public int getDimension() {
342 |               return 2;
343 |           }
344 | 
345 |           public void computeDerivatives(double t, double[] y, double[] yDot) {
346 |               yDot[0] =  y[1];
347 |               yDot[1] = -y[0];
348 |           }
349 | 
350 |       };
351 | 
352 |       SchedulingChecker sinChecker = new SchedulingChecker(0); // events at 0, PI, 2PI ...
353 |       SchedulingChecker cosChecker = new SchedulingChecker(1); // events at PI/2, 3PI/2, 5PI/2 ...
354 | 
355 |       FirstOrderIntegrator integ =
356 |               new DormandPrince853Integrator(0.001, 1.0, 1.0e-12, 0.0);
357 |       integ.addEventHandler(sinChecker, 0.01, 1.0e-7, 100);
358 |       integ.addStepHandler(sinChecker);
359 |       integ.addEventHandler(cosChecker, 0.01, 1.0e-7, 100);
360 |       integ.addStepHandler(cosChecker);
361 |       double   t0 = 0.5;
362 |       double[] y0 = new double[] { FastMath.sin(t0), FastMath.cos(t0) };
363 |       double   t  = 10.0;
364 |       double[] y  = new double[2];
365 |       integ.integrate(sincos, t0, y0, t, y);
366 | 
367 |   }
```
