# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.distribution.PoissonDistributionTest.testMean()
Resolved declaration: org.apache.commons.math.distribution.PoissonDistributionTest.testMean()
Source: src/test/java/org/apache/commons/math/distribution/PoissonDistributionTest.java

```java
137 |     public void testMean() {
138 |         PoissonDistribution dist;
139 |         try {
140 |             dist = new PoissonDistributionImpl(-1);
141 |             fail("negative mean: NotStrictlyPositiveException expected");
142 |         } catch(NotStrictlyPositiveException ex) {
143 |             // Expected.
144 |         }
145 | 
146 |         dist = new PoissonDistributionImpl(10.0);
147 |         assertEquals(10.0, dist.getMean(), 0.0);
148 |     }
```
