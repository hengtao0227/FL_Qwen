# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.distribution.NormalDistributionTest.testMath280()
Resolved declaration: org.apache.commons.math.distribution.NormalDistributionTest.testMath280()
Source: src/test/org/apache/commons/math/distribution/NormalDistributionTest.java

```java
167 |     public void testMath280() throws MathException {
168 |         NormalDistribution normal = new NormalDistributionImpl(0,1);
169 |         double result = normal.inverseCumulativeProbability(0.9772498680518209);
170 |         assertEquals(2.0, result, 1.0e-12);
171 |     }
```
