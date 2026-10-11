# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.distribution.BinomialDistributionTest.testMath718()
Resolved declaration: org.apache.commons.math3.distribution.BinomialDistributionTest.testMath718()
Source: src/test/java/org/apache/commons/math3/distribution/BinomialDistributionTest.java

```java
132 |     @Test
133 |     public void testMath718() {
134 |         // for large trials the evaluation of ContinuedFraction was inaccurate
135 |         // do a sweep over several large trials to test if the current implementation is
136 |         // numerically stable.
137 | 
138 |         for (int trials = 500000; trials < 20000000; trials += 100000) {
139 |             BinomialDistribution dist = new BinomialDistribution(trials, 0.5);
140 |             int p = dist.inverseCumulativeProbability(0.5);
141 |             Assert.assertEquals(trials / 2, p);
142 |         }
143 | 
144 |     }
```

## org.apache.commons.math3.distribution.FDistributionTest.testMath785()
Resolved declaration: org.apache.commons.math3.distribution.FDistributionTest.testMath785()
Source: src/test/java/org/apache/commons/math3/distribution/FDistributionTest.java

```java
146 |     @Test
147 |     public void testMath785() {
148 |         // this test was failing due to inaccurate results from ContinuedFraction.
149 | 
150 |         try {
151 |             double prob = 0.01;
152 |             FDistribution f = new FDistribution(200000, 200000);
153 |             double result = f.inverseCumulativeProbability(prob);
154 |             Assert.assertTrue(result < 1.0);
155 |         } catch (Exception e) {
156 |             Assert.fail("Failing to calculate inverse cumulative probability");
157 |         }
158 |     }
```
