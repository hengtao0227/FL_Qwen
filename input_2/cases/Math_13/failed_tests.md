# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.fitting.PolynomialFitterTest.testLargeSample()
Resolved declaration: org.apache.commons.math3.optimization.fitting.PolynomialFitterTest.testLargeSample()
Source: src/test/java/org/apache/commons/math3/optimization/fitting/PolynomialFitterTest.java

```java
226 |     @Test
227 |     public void testLargeSample() {
228 |         Random randomizer = new Random(0x5551480dca5b369bl);
229 |         double maxError = 0;
230 |         for (int degree = 0; degree < 10; ++degree) {
231 |             PolynomialFunction p = buildRandomPolynomial(degree, randomizer);
232 | 
233 |             PolynomialFitter fitter = new PolynomialFitter(new LevenbergMarquardtOptimizer());
234 |             for (int i = 0; i < 40000; ++i) {
235 |                 double x = -1.0 + i / 20000.0;
236 |                 fitter.addObservedPoint(1.0, x,
237 |                                         p.value(x) + 0.1 * randomizer.nextGaussian());
238 |             }
239 | 
240 |             final double[] init = new double[degree + 1];
241 |             PolynomialFunction fitted = new PolynomialFunction(fitter.fit(init));
242 | 
243 |             for (double x = -1.0; x < 1.0; x += 0.01) {
244 |                 double error = FastMath.abs(p.value(x) - fitted.value(x)) /
245 |                               (1.0 + FastMath.abs(p.value(x)));
246 |                 maxError = FastMath.max(maxError, error);
247 |                 Assert.assertTrue(FastMath.abs(error) < 0.01);
248 |             }
249 |         }
250 |         Assert.assertTrue(maxError > 0.001);
251 |     }
```
