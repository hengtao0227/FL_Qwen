# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.fitting.PolynomialFitterTest.testLargeSample()
Resolved declaration: org.apache.commons.math3.fitting.PolynomialFitterTest.testLargeSample()
Source: src/test/java/org/apache/commons/math3/fitting/PolynomialFitterTest.java

```java
223 |     @Test
224 |     public void testLargeSample() {
225 |         Random randomizer = new Random(0x5551480dca5b369bl);
226 |         double maxError = 0;
227 |         for (int degree = 0; degree < 10; ++degree) {
228 |             PolynomialFunction p = buildRandomPolynomial(degree, randomizer);
229 | 
230 |             PolynomialFitter fitter = new PolynomialFitter(new LevenbergMarquardtOptimizer());
231 |             for (int i = 0; i < 40000; ++i) {
232 |                 double x = -1.0 + i / 20000.0;
233 |                 fitter.addObservedPoint(1.0, x,
234 |                                         p.value(x) + 0.1 * randomizer.nextGaussian());
235 |             }
236 | 
237 |             final double[] init = new double[degree + 1];
238 |             PolynomialFunction fitted = new PolynomialFunction(fitter.fit(init));
239 | 
240 |             for (double x = -1.0; x < 1.0; x += 0.01) {
241 |                 double error = FastMath.abs(p.value(x) - fitted.value(x)) /
242 |                               (1.0 + FastMath.abs(p.value(x)));
243 |                 maxError = FastMath.max(maxError, error);
244 |                 Assert.assertTrue(FastMath.abs(error) < 0.01);
245 |             }
246 |         }
247 |         Assert.assertTrue(maxError > 0.001);
248 |     }
```
