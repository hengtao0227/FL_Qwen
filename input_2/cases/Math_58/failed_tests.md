# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.fitting.GaussianFitterTest.testMath519()
Resolved declaration: org.apache.commons.math.optimization.fitting.GaussianFitterTest.testMath519()
Source: src/test/java/org/apache/commons/math/optimization/fitting/GaussianFitterTest.java

```java
297 |     @Test
298 |     public void testMath519() {
299 |         // The optimizer will try negative sigma values but "GaussianFitter"
300 |         // will catch the raised exceptions and return NaN values instead.
301 | 
302 |         final double[] data = { 
303 |             1.1143831578403364E-29,
304 |             4.95281403484594E-28,
305 |             1.1171347211930288E-26,
306 |             1.7044813962636277E-25,
307 |             1.9784716574832164E-24,
308 |             1.8630236407866774E-23,
309 |             1.4820532905097742E-22,
310 |             1.0241963854632831E-21,
311 |             6.275077366673128E-21,
312 |             3.461808994532493E-20,
313 |             1.7407124684715706E-19,
314 |             8.056687953553974E-19,
315 |             3.460193945992071E-18,
316 |             1.3883326374011525E-17,
317 |             5.233894983671116E-17,
318 |             1.8630791465263745E-16,
319 |             6.288759227922111E-16,
320 |             2.0204433920597856E-15,
321 |             6.198768938576155E-15,
322 |             1.821419346860626E-14,
323 |             5.139176445538471E-14,
324 |             1.3956427429045787E-13,
325 |             3.655705706448139E-13,
326 |             9.253753324779779E-13,
327 |             2.267636001476696E-12,
328 |             5.3880460095836855E-12,
329 |             1.2431632654852931E-11
330 |         };
331 | 
332 |         GaussianFitter fitter = new GaussianFitter(new LevenbergMarquardtOptimizer());
333 |         for (int i = 0; i < data.length; i++) {
334 |             fitter.addObservedPoint(i, data[i]);
335 |         }
336 |         final double[] p = fitter.fit();
337 | 
338 |         Assert.assertEquals(53.1572792, p[1], 1e-7);
339 |         Assert.assertEquals(5.75214622, p[2], 1e-8);
340 |     }
```
