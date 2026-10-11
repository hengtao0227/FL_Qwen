# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.distribution.FDistributionTest.testSmallDegreesOfFreedom()
Resolved declaration: org.apache.commons.math.distribution.FDistributionTest.testSmallDegreesOfFreedom()
Source: src/test/org/apache/commons/math/distribution/FDistributionTest.java

```java
109 |     public void testSmallDegreesOfFreedom() throws Exception {
110 |         org.apache.commons.math.distribution.FDistributionImpl fd =
111 |             new org.apache.commons.math.distribution.FDistributionImpl(
112 |                 1.0, 1.0);
113 |         double p = fd.cumulativeProbability(0.975);
114 |         double x = fd.inverseCumulativeProbability(p);
115 |         assertEquals(0.975, x, 1.0e-5);
116 | 
117 |         fd.setDenominatorDegreesOfFreedom(2.0);
118 |         p = fd.cumulativeProbability(0.975);
119 |         x = fd.inverseCumulativeProbability(p);
120 |         assertEquals(0.975, x, 1.0e-5);
121 |     }
```
