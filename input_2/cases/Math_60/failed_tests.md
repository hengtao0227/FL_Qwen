# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.distribution.NormalDistributionTest.testExtremeValues()
Resolved declaration: org.apache.commons.math.distribution.NormalDistributionTest.testExtremeValues()
Source: src/test/java/org/apache/commons/math/distribution/NormalDistributionTest.java

```java
157 |     public void testExtremeValues() throws Exception {
158 |         NormalDistribution distribution = new NormalDistributionImpl(0, 1);
159 |         for (int i = 0; i < 100; i++) { // make sure no convergence exception
160 |             double lowerTail = distribution.cumulativeProbability(-i);
161 |             double upperTail = distribution.cumulativeProbability(i);
162 |             if (i < 9) { // make sure not top-coded 
163 |                 // For i = 10, due to bad tail precision in erf (MATH-364), 1 is returned
164 |                 // TODO: once MATH-364 is resolved, replace 9 with 30
165 |                 assertTrue(lowerTail > 0.0d);
166 |                 assertTrue(upperTail < 1.0d);
167 |             }
168 |             else { // make sure top coding not reversed
169 |                 assertTrue(lowerTail < 0.00001);
170 |                 assertTrue(upperTail > 0.99999);
171 |             }
172 |         }
173 |         
174 |         assertEquals(distribution.cumulativeProbability(Double.MAX_VALUE), 1, 0);
175 |         assertEquals(distribution.cumulativeProbability(-Double.MAX_VALUE), 0, 0);
176 |         assertEquals(distribution.cumulativeProbability(Double.POSITIVE_INFINITY), 1, 0);
177 |         assertEquals(distribution.cumulativeProbability(Double.NEGATIVE_INFINITY), 0, 0);
178 |         
179 |    }
```
