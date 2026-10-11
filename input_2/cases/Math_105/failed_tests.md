# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.regression.SimpleRegressionTest.testSSENonNegative()
Resolved declaration: org.apache.commons.math.stat.regression.SimpleRegressionTest.testSSENonNegative()
Source: src/test/org/apache/commons/math/stat/regression/SimpleRegressionTest.java

```java
268 |     public void testSSENonNegative() {
269 |         double[] y = { 8915.102, 8919.302, 8923.502 };
270 |         double[] x = { 1.107178495E2, 1.107264895E2, 1.107351295E2 };
271 |         SimpleRegression reg = new SimpleRegression();
272 |         for (int i = 0; i < x.length; i++) {
273 |             reg.addData(x[i], y[i]);
274 |         }
275 |         assertTrue(reg.getSumSquaredErrors() >= 0.0);
276 |     } 
```
