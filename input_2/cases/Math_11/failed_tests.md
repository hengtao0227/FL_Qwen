# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.distribution.MultivariateNormalDistributionTest.testUnivariateDistribution()
Resolved declaration: org.apache.commons.math3.distribution.MultivariateNormalDistributionTest.testUnivariateDistribution()
Source: src/test/java/org/apache/commons/math3/distribution/MultivariateNormalDistributionTest.java

```java
138 |     @Test
139 |     public void testUnivariateDistribution() {
140 |         final double[] mu = { -1.5 };
141 |         final double[][] sigma = { { 1 } };
142 |  
143 |         final MultivariateNormalDistribution multi = new MultivariateNormalDistribution(mu, sigma);
144 | 
145 |         final NormalDistribution uni = new NormalDistribution(mu[0], sigma[0][0]);
146 |         final Random rng = new Random();
147 |         final int numCases = 100;
148 |         final double tol = Math.ulp(1d);
149 |         for (int i = 0; i < numCases; i++) {
150 |             final double v = rng.nextDouble() * 10 - 5;
151 |             Assert.assertEquals(uni.density(v), multi.density(new double[] { v }), tol);
152 |         }
153 |     }
```
