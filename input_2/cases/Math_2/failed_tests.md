# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.distribution.HypergeometricDistributionTest.testMath1021()
Resolved declaration: org.apache.commons.math3.distribution.HypergeometricDistributionTest.testMath1021()
Source: src/test/java/org/apache/commons/math3/distribution/HypergeometricDistributionTest.java

```java
288 |     @Test
289 |     public void testMath1021() {
290 |         final int N = 43130568;
291 |         final int m = 42976365;
292 |         final int n = 50;
293 |         final HypergeometricDistribution dist = new HypergeometricDistribution(N, m, n);
294 | 
295 |         for (int i = 0; i < 100; i++) {
296 |             final int sample = dist.sample();
297 |             Assert.assertTrue("sample=" + sample, 0 <= sample);
298 |             Assert.assertTrue("sample=" + sample, sample <= n);
299 |         }
300 |     }
```
