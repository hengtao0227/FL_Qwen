# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.ode.events.EventStateTest.closeEvents()
Resolved declaration: org.apache.commons.math.ode.events.EventStateTest.closeEvents()
Source: src/test/java/org/apache/commons/math/ode/events/EventStateTest.java

```java
31 |     @Test
32 |     public void closeEvents()
33 |         throws EventException, ConvergenceException, DerivativeException {
34 | 
35 |         final double r1  = 90.0;
36 |         final double r2  = 135.0;
37 |         final double gap = r2 - r1;
38 |         EventHandler closeEventsGenerator = new EventHandler() {
39 |             public void resetState(double t, double[] y) {
40 |             }
41 |             public double g(double t, double[] y) {
42 |                 return (t - r1) * (r2 - t);
43 |             }
44 |             public int eventOccurred(double t, double[] y, boolean increasing) {
45 |                 return CONTINUE;
46 |             }
47 |         };
48 | 
49 |         final double tolerance = 0.1;
50 |         EventState es = new EventState(closeEventsGenerator, 1.5 * gap, tolerance, 10);
51 | 
52 |         double t0 = r1 - 0.5 * gap;
53 |         es.reinitializeBegin(t0, new double[0]);
54 |         AbstractStepInterpolator interpolator =
55 |             new DummyStepInterpolator(new double[0], true);
56 |         interpolator.storeTime(t0);
57 | 
58 |         interpolator.shift();
59 |         interpolator.storeTime(0.5 * (r1 + r2));
60 |         Assert.assertTrue(es.evaluateStep(interpolator));
61 |         Assert.assertEquals(r1, es.getEventTime(), tolerance);
62 |         es.stepAccepted(es.getEventTime(), new double[0]);
63 | 
64 |         interpolator.shift();
65 |         interpolator.storeTime(r2 + 0.4 * gap);
66 |         Assert.assertTrue(es.evaluateStep(interpolator));
67 |         Assert.assertEquals(r2, es.getEventTime(), tolerance);
68 | 
69 |     }
```
