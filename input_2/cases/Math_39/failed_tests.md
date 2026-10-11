# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.ode.nonstiff.DormandPrince853IntegratorTest.testTooLargeFirstStep()
Resolved declaration: org.apache.commons.math.ode.nonstiff.DormandPrince853IntegratorTest.testTooLargeFirstStep()
Source: src/test/java/org/apache/commons/math/ode/nonstiff/DormandPrince853IntegratorTest.java

```java
179 |   @Test
180 |   public void testTooLargeFirstStep() {
181 | 
182 |       AdaptiveStepsizeIntegrator integ =
183 |               new DormandPrince853Integrator(0, Double.POSITIVE_INFINITY, Double.NaN, Double.NaN);
184 |       final double start = 0.0;
185 |       final double end   = 0.001;
186 |       FirstOrderDifferentialEquations equations = new FirstOrderDifferentialEquations() {
187 | 
188 |           public int getDimension() {
189 |               return 1;
190 |           }
191 | 
192 |           public void computeDerivatives(double t, double[] y, double[] yDot) {
193 |               Assert.assertTrue(t >= FastMath.nextAfter(start, Double.NEGATIVE_INFINITY));
194 |               Assert.assertTrue(t <= FastMath.nextAfter(end,   Double.POSITIVE_INFINITY));
195 |               yDot[0] = -100.0 * y[0];
196 |           }
197 | 
198 |       };
199 | 
200 |       integ.setStepSizeControl(0, 1.0, 1.0e-6, 1.0e-8);
201 |       integ.integrate(equations, start, new double[] { 1.0 }, end, new double[1]);
202 | 
203 |   }
```
