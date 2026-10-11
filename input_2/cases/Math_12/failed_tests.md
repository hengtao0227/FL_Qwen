# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.distribution.GammaDistributionTest.testDistributionClone()
Resolved declaration: org.apache.commons.math3.distribution.RealDistributionAbstractTest.testDistributionClone()
Source: src/test/java/org/apache/commons/math3/distribution/RealDistributionAbstractTest.java

```java
379 |     @Test
380 |     public void testDistributionClone()
381 |         throws IOException,
382 |                ClassNotFoundException {
383 |         // Construct a distribution and initialize its internal random
384 |         // generator, using a fixed seed for deterministic results.
385 |         distribution.reseedRandomGenerator(123);
386 |         distribution.sample();
387 | 
388 |         // Clone the distribution.
389 |         final RealDistribution cloned = deepClone();
390 | 
391 |         // Make sure they still produce the same samples.
392 |         final double s1 = distribution.sample();
393 |         final double s2 = cloned.sample();
394 |         Assert.assertEquals(s1, s2, 0d);
395 |     }
```

## org.apache.commons.math3.distribution.LogNormalDistributionTest.testDistributionClone()
Resolved declaration: org.apache.commons.math3.distribution.RealDistributionAbstractTest.testDistributionClone()
Source: src/test/java/org/apache/commons/math3/distribution/RealDistributionAbstractTest.java

```java
379 |     @Test
380 |     public void testDistributionClone()
381 |         throws IOException,
382 |                ClassNotFoundException {
383 |         // Construct a distribution and initialize its internal random
384 |         // generator, using a fixed seed for deterministic results.
385 |         distribution.reseedRandomGenerator(123);
386 |         distribution.sample();
387 | 
388 |         // Clone the distribution.
389 |         final RealDistribution cloned = deepClone();
390 | 
391 |         // Make sure they still produce the same samples.
392 |         final double s1 = distribution.sample();
393 |         final double s2 = cloned.sample();
394 |         Assert.assertEquals(s1, s2, 0d);
395 |     }
```

## org.apache.commons.math3.distribution.NormalDistributionTest.testDistributionClone()
Resolved declaration: org.apache.commons.math3.distribution.RealDistributionAbstractTest.testDistributionClone()
Source: src/test/java/org/apache/commons/math3/distribution/RealDistributionAbstractTest.java

```java
379 |     @Test
380 |     public void testDistributionClone()
381 |         throws IOException,
382 |                ClassNotFoundException {
383 |         // Construct a distribution and initialize its internal random
384 |         // generator, using a fixed seed for deterministic results.
385 |         distribution.reseedRandomGenerator(123);
386 |         distribution.sample();
387 | 
388 |         // Clone the distribution.
389 |         final RealDistribution cloned = deepClone();
390 | 
391 |         // Make sure they still produce the same samples.
392 |         final double s1 = distribution.sample();
393 |         final double s2 = cloned.sample();
394 |         Assert.assertEquals(s1, s2, 0d);
395 |     }
```
