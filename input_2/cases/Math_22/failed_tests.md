# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.distribution.FDistributionTest.testIsSupportLowerBoundInclusive()
Resolved declaration: org.apache.commons.math3.distribution.RealDistributionAbstractTest.testIsSupportLowerBoundInclusive()
Source: src/test/java/org/apache/commons/math3/distribution/RealDistributionAbstractTest.java

```java
346 |     @Test
347 |     public void testIsSupportLowerBoundInclusive() {
348 |         final double lowerBound = distribution.getSupportLowerBound();
349 |         double result = Double.NaN;
350 |         result = distribution.density(lowerBound);
351 |         Assert.assertEquals(
352 |                 !Double.isInfinite(lowerBound) && !Double.isNaN(result) &&
353 |                 !Double.isInfinite(result),
354 |                 distribution.isSupportLowerBoundInclusive());
355 |          
356 |     }
```

## org.apache.commons.math3.distribution.UniformRealDistributionTest.testIsSupportUpperBoundInclusive()
Resolved declaration: org.apache.commons.math3.distribution.RealDistributionAbstractTest.testIsSupportUpperBoundInclusive()
Source: src/test/java/org/apache/commons/math3/distribution/RealDistributionAbstractTest.java

```java
362 |     @Test
363 |     public void testIsSupportUpperBoundInclusive() {
364 |         final double upperBound = distribution.getSupportUpperBound();
365 |         double result = Double.NaN;
366 |         result = distribution.density(upperBound);
367 |         Assert.assertEquals(
368 |                 !Double.isInfinite(upperBound) && !Double.isNaN(result) &&
369 |                 !Double.isInfinite(result),
370 |                 distribution.isSupportUpperBoundInclusive());
371 |          
372 |     }
```
