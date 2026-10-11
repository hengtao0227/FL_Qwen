# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.ode.events.EventStateTest.testIssue695()
Resolved declaration: org.apache.commons.math.ode.events.EventStateTest.testIssue695()
Source: src/test/java/org/apache/commons/math/ode/events/EventStateTest.java

```java
79 |     @Test
80 |     public void testIssue695() {
81 | 
82 |         FirstOrderDifferentialEquations equation = new FirstOrderDifferentialEquations() {
83 |             
84 |             public int getDimension() {
85 |                 return 1;
86 |             }
87 |             
88 |             public void computeDerivatives(double t, double[] y, double[] yDot) {
89 |                 yDot[0] = 1.0;
90 |             }
91 |         };
92 | 
93 |         DormandPrince853Integrator integrator = new DormandPrince853Integrator(0.001, 1000, 1.0e-14, 1.0e-14);
94 |         integrator.addEventHandler(new ResettingEvent(10.99), 0.1, 1.0e-9, 1000);
95 |         integrator.addEventHandler(new ResettingEvent(11.01), 0.1, 1.0e-9, 1000);
96 |         integrator.setInitialStepSize(3.0);
97 | 
98 |         double target = 30.0;
99 |         double[] y = new double[1];
100 |         double tEnd = integrator.integrate(equation, 0.0, y, target, y);
101 |         Assert.assertEquals(target, tEnd, 1.0e-10);
102 |         Assert.assertEquals(32.0, y[0], 1.0e-10);
103 | 
104 |     }
```
