# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.fraction.FractionTest.testMath835()
Resolved declaration: org.apache.commons.math3.fraction.FractionTest.testMath835()
Source: src/test/java/org/apache/commons/math3/fraction/FractionTest.java

```java
245 |     @Test
246 |     public void testMath835() {
247 |         final int numer = Integer.MAX_VALUE / 99;
248 |         final int denom = 1;
249 |         final double percentage = 100 * ((double) numer) / denom;
250 |         final Fraction frac = new Fraction(numer, denom);
251 |         // With the implementation that preceded the fix suggested in MATH-835,
252 |         // this test was failing, due to overflow.
253 |         Assert.assertEquals(percentage, frac.percentageValue(), Math.ulp(percentage));
254 |     }
```
