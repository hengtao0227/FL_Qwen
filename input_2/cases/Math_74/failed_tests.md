# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest.polynomial()
Resolved declaration: org.apache.commons.math.ode.nonstiff.AdamsMoultonIntegratorTest.polynomial()
Source: src/test/java/org/apache/commons/math/ode/nonstiff/AdamsMoultonIntegratorTest.java

```java
135 |     @Test
136 |     public void polynomial() throws DerivativeException, IntegratorException {
137 |         TestProblem6 pb = new TestProblem6();
138 |         double range = Math.abs(pb.getFinalTime() - pb.getInitialTime());
139 | 
140 |         for (int nSteps = 1; nSteps < 7; ++nSteps) {
141 |             AdamsMoultonIntegrator integ =
142 |                 new AdamsMoultonIntegrator(nSteps, 1.0e-6 * range, 0.1 * range, 1.0e-9, 1.0e-9);
143 |             TestProblemHandler handler = new TestProblemHandler(pb, integ);
144 |             integ.addStepHandler(handler);
145 |             integ.integrate(pb, pb.getInitialTime(), pb.getInitialState(),
146 |                             pb.getFinalTime(), new double[pb.getDimension()]);
147 |             if (nSteps < 4) {
148 |                 assertTrue(integ.getEvaluations() > 140);
149 |             } else {
150 |                 assertTrue(integ.getEvaluations() < 90);
151 |             }
152 |         }
153 | 
154 |     }
```
