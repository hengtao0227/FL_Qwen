# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.ode.nonstiff.ClassicalRungeKuttaIntegratorTest.testMissedEndEvent()
Resolved declaration: org.apache.commons.math.ode.nonstiff.ClassicalRungeKuttaIntegratorTest.testMissedEndEvent()
Source: src/test/java/org/apache/commons/math/ode/nonstiff/ClassicalRungeKuttaIntegratorTest.java

```java
44 |   public void testMissedEndEvent() throws IntegratorException, DerivativeException {
45 |       final double   t0     = 1878250320.0000029;
46 |       final double   tEvent = 1878250379.9999986;
47 |       final double[] k      = { 1.0e-4, 1.0e-5, 1.0e-6 };
48 |       FirstOrderDifferentialEquations ode = new FirstOrderDifferentialEquations() {
49 | 
50 |           public int getDimension() {
51 |               return k.length;
52 |           }
53 | 
54 |           public void computeDerivatives(double t, double[] y, double[] yDot) {
55 |               for (int i = 0; i < y.length; ++i) {
56 |                   yDot[i] = k[i] * y[i];
57 |               }
58 |           }
59 |       };
60 | 
61 |       ClassicalRungeKuttaIntegrator integrator = new ClassicalRungeKuttaIntegrator(60.0);
62 | 
63 |       double[] y0   = new double[k.length];
64 |       for (int i = 0; i < y0.length; ++i) {
65 |           y0[i] = i + 1;
66 |       }
67 |       double[] y    = new double[k.length];
68 | 
69 |       double finalT = integrator.integrate(ode, t0, y0, tEvent, y);
70 |       Assert.assertEquals(tEvent, finalT, 5.0e-6);
71 |       for (int i = 0; i < y.length; ++i) {
72 |           Assert.assertEquals(y0[i] * Math.exp(k[i] * (finalT - t0)), y[i], 1.0e-9);
73 |       }
74 | 
75 |       integrator.addEventHandler(new EventHandler() {
76 | 
77 |           public void resetState(double t, double[] y) {
78 |           }
79 | 
80 |           public double g(double t, double[] y) {
81 |               return t - tEvent;
82 |           }
83 | 
84 |           public int eventOccurred(double t, double[] y, boolean increasing) {
85 |               Assert.assertEquals(tEvent, t, 5.0e-6);
86 |               return CONTINUE;
87 |           }
88 |       }, Double.POSITIVE_INFINITY, 1.0e-20, 100);
89 |       finalT = integrator.integrate(ode, t0, y0, tEvent + 120, y);
90 |       Assert.assertEquals(tEvent + 120, finalT, 5.0e-6);
91 |       for (int i = 0; i < y.length; ++i) {
92 |           Assert.assertEquals(y0[i] * Math.exp(k[i] * (finalT - t0)), y[i], 1.0e-9);
93 |       }
94 | 
95 |   }
```

## org.apache.commons.math.ode.nonstiff.DormandPrince853IntegratorTest.testMissedEndEvent()
Resolved declaration: org.apache.commons.math.ode.nonstiff.DormandPrince853IntegratorTest.testMissedEndEvent()
Source: src/test/java/org/apache/commons/math/ode/nonstiff/DormandPrince853IntegratorTest.java

```java
44 |   public void testMissedEndEvent() throws IntegratorException, DerivativeException {
45 |       final double   t0     = 1878250320.0000029;
46 |       final double   tEvent = 1878250379.9999986;
47 |       final double[] k  = { 1.0e-4, 1.0e-5, 1.0e-6 };
48 |       FirstOrderDifferentialEquations ode = new FirstOrderDifferentialEquations() {
49 | 
50 |           public int getDimension() {
51 |               return k.length;
52 |           }
53 | 
54 |           public void computeDerivatives(double t, double[] y, double[] yDot) {
55 |               for (int i = 0; i < y.length; ++i) {
56 |                   yDot[i] = k[i] * y[i];
57 |               }
58 |           }
59 |       };
60 | 
61 |       DormandPrince853Integrator integrator = new DormandPrince853Integrator(0.0, 100.0,
62 |                                                                              1.0e-10, 1.0e-10);
63 | 
64 |       double[] y0   = new double[k.length];
65 |       for (int i = 0; i < y0.length; ++i) {
66 |           y0[i] = i + 1;
67 |       }
68 |       double[] y    = new double[k.length];
69 | 
70 |       integrator.setInitialStepSize(60.0);
71 |       double finalT = integrator.integrate(ode, t0, y0, tEvent, y);
72 |       Assert.assertEquals(tEvent, finalT, 5.0e-6);
73 |       for (int i = 0; i < y.length; ++i) {
74 |           Assert.assertEquals(y0[i] * Math.exp(k[i] * (finalT - t0)), y[i], 1.0e-9);
75 |       }
76 | 
77 |       integrator.setInitialStepSize(60.0);
78 |       integrator.addEventHandler(new EventHandler() {
79 | 
80 |           public void resetState(double t, double[] y) {
81 |           }
82 | 
83 |           public double g(double t, double[] y) {
84 |               return t - tEvent;
85 |           }
86 | 
87 |           public int eventOccurred(double t, double[] y, boolean increasing) {
88 |               Assert.assertEquals(tEvent, t, 5.0e-6);
89 |               return CONTINUE;
90 |           }
91 |       }, Double.POSITIVE_INFINITY, 1.0e-20, 100);
92 |       finalT = integrator.integrate(ode, t0, y0, tEvent + 120, y);
93 |       Assert.assertEquals(tEvent + 120, finalT, 5.0e-6);
94 |       for (int i = 0; i < y.length; ++i) {
95 |           Assert.assertEquals(y0[i] * Math.exp(k[i] * (finalT - t0)), y[i], 1.0e-9);
96 |       }
97 | 
98 |   }
```
