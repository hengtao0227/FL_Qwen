# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.distribution.DiscreteRealDistributionTest.testIssue942()
Resolved declaration: org.apache.commons.math3.distribution.DiscreteRealDistributionTest.testIssue942()
Source: src/test/java/org/apache/commons/math3/distribution/DiscreteRealDistributionTest.java

```java
207 |     @Test
208 |     public void testIssue942() {
209 |         List<Pair<Object,Double>> list = new ArrayList<Pair<Object, Double>>();
210 |         list.add(new Pair<Object, Double>(new Object() {}, new Double(0)));
211 |         list.add(new Pair<Object, Double>(new Object() {}, new Double(1)));
212 |         Assert.assertEquals(1, new DiscreteDistribution<Object>(list).sample(1).length);
213 |     }
```
