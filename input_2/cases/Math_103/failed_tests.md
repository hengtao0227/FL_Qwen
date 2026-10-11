# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.distribution.NormalDistributionTest.testExtremeValues()
Resolved declaration: org.apache.commons.math.distribution.NormalDistributionTest.testExtremeValues()
Source: src/test/org/apache/commons/math/distribution/NormalDistributionTest.java

```java
128 |     public void testExtremeValues() throws Exception {
129 |         NormalDistribution distribution = (NormalDistribution) getDistribution();
130 |         distribution.setMean(0);
131 |         distribution.setStandardDeviation(1);
132 |         for (int i = 0; i < 100; i+=5) { // make sure no convergence exception
133 |             double lowerTail = distribution.cumulativeProbability((double)-i);
134 |             double upperTail = distribution.cumulativeProbability((double) i);
135 |             if (i < 10) { // make sure not top-coded
136 |                 assertTrue(lowerTail > 0.0d);
137 |                 assertTrue(upperTail < 1.0d);
138 |             }
139 |             else { // make sure top coding not reversed
140 |                 assertTrue(lowerTail < 0.00001);
141 |                 assertTrue(upperTail > 0.99999);
142 |             }
143 |         } 
144 |    }
```
