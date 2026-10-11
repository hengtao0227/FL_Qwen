# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideMeanWithMathClass()
Resolved declaration: org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideMeanWithMathClass()
Source: src/test/java/org/apache/commons/math/stat/descriptive/SummaryStatisticsTest.java

```java
327 |     @Test
328 |     public void testOverrideMeanWithMathClass() throws Exception {
329 |         double[] scores = {1, 2, 3, 4};
330 |         SummaryStatistics stats = new SummaryStatistics();
331 |         stats.setMeanImpl(new Mean()); 
332 |         for(double i : scores) {
333 |           stats.addValue(i);
334 |         }
335 |         Assert.assertEquals((new Mean()).evaluate(scores),stats.getMean(), 0); 
336 |     }
```

## org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideGeoMeanWithMathClass()
Resolved declaration: org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideGeoMeanWithMathClass()
Source: src/test/java/org/apache/commons/math/stat/descriptive/SummaryStatisticsTest.java

```java
338 |     @Test
339 |     public void testOverrideGeoMeanWithMathClass() throws Exception {
340 |         double[] scores = {1, 2, 3, 4};
341 |         SummaryStatistics stats = new SummaryStatistics();
342 |         stats.setGeoMeanImpl(new GeometricMean()); 
343 |         for(double i : scores) {
344 |           stats.addValue(i);
345 |         }
346 |         Assert.assertEquals((new GeometricMean()).evaluate(scores),stats.getGeometricMean(), 0); 
347 |     }
```

## org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideVarianceWithMathClass()
Resolved declaration: org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideVarianceWithMathClass()
Source: src/test/java/org/apache/commons/math/stat/descriptive/SummaryStatisticsTest.java

```java
316 |     @Test
317 |     public void testOverrideVarianceWithMathClass() throws Exception {
318 |         double[] scores = {1, 2, 3, 4};
319 |         SummaryStatistics stats = new SummaryStatistics();
320 |         stats.setVarianceImpl(new Variance(false)); //use "population variance"
321 |         for(double i : scores) {
322 |           stats.addValue(i);
323 |         }
324 |         Assert.assertEquals((new Variance(false)).evaluate(scores),stats.getVariance(), 0); 
325 |     }
```

## org.apache.commons.math.stat.descriptive.SynchronizedSummaryStatisticsTest.testOverrideMeanWithMathClass()
Resolved declaration: org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideMeanWithMathClass()
Source: src/test/java/org/apache/commons/math/stat/descriptive/SummaryStatisticsTest.java

```java
327 |     @Test
328 |     public void testOverrideMeanWithMathClass() throws Exception {
329 |         double[] scores = {1, 2, 3, 4};
330 |         SummaryStatistics stats = new SummaryStatistics();
331 |         stats.setMeanImpl(new Mean()); 
332 |         for(double i : scores) {
333 |           stats.addValue(i);
334 |         }
335 |         Assert.assertEquals((new Mean()).evaluate(scores),stats.getMean(), 0); 
336 |     }
```

## org.apache.commons.math.stat.descriptive.SynchronizedSummaryStatisticsTest.testOverrideGeoMeanWithMathClass()
Resolved declaration: org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideGeoMeanWithMathClass()
Source: src/test/java/org/apache/commons/math/stat/descriptive/SummaryStatisticsTest.java

```java
338 |     @Test
339 |     public void testOverrideGeoMeanWithMathClass() throws Exception {
340 |         double[] scores = {1, 2, 3, 4};
341 |         SummaryStatistics stats = new SummaryStatistics();
342 |         stats.setGeoMeanImpl(new GeometricMean()); 
343 |         for(double i : scores) {
344 |           stats.addValue(i);
345 |         }
346 |         Assert.assertEquals((new GeometricMean()).evaluate(scores),stats.getGeometricMean(), 0); 
347 |     }
```

## org.apache.commons.math.stat.descriptive.SynchronizedSummaryStatisticsTest.testOverrideVarianceWithMathClass()
Resolved declaration: org.apache.commons.math.stat.descriptive.SummaryStatisticsTest.testOverrideVarianceWithMathClass()
Source: src/test/java/org/apache/commons/math/stat/descriptive/SummaryStatisticsTest.java

```java
316 |     @Test
317 |     public void testOverrideVarianceWithMathClass() throws Exception {
318 |         double[] scores = {1, 2, 3, 4};
319 |         SummaryStatistics stats = new SummaryStatistics();
320 |         stats.setVarianceImpl(new Variance(false)); //use "population variance"
321 |         for(double i : scores) {
322 |           stats.addValue(i);
323 |         }
324 |         Assert.assertEquals((new Variance(false)).evaluate(scores),stats.getVariance(), 0); 
325 |     }
```
