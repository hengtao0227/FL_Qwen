# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.fraction.BigFractionTest.testFloatValueForLargeNumeratorAndDenominator()
Resolved declaration: org.apache.commons.math.fraction.BigFractionTest.testFloatValueForLargeNumeratorAndDenominator()
Source: src/test/java/org/apache/commons/math/fraction/BigFractionTest.java

```java
214 |     @Test
215 |     public void testFloatValueForLargeNumeratorAndDenominator() {
216 |         final BigInteger pow400 = BigInteger.TEN.pow(400);
217 |         final BigInteger pow401 = BigInteger.TEN.pow(401);
218 |         final BigInteger two = new BigInteger("2");
219 |         final BigFraction large = new BigFraction(pow401.add(BigInteger.ONE),
220 |                                                   pow400.multiply(two));
221 | 
222 |         Assert.assertEquals(5, large.floatValue(), 1e-15);
223 |     }
```

## org.apache.commons.math.fraction.BigFractionTest.testDoubleValueForLargeNumeratorAndDenominator()
Resolved declaration: org.apache.commons.math.fraction.BigFractionTest.testDoubleValueForLargeNumeratorAndDenominator()
Source: src/test/java/org/apache/commons/math/fraction/BigFractionTest.java

```java
202 |     @Test
203 |     public void testDoubleValueForLargeNumeratorAndDenominator() {
204 |         final BigInteger pow400 = BigInteger.TEN.pow(400);
205 |         final BigInteger pow401 = BigInteger.TEN.pow(401);
206 |         final BigInteger two = new BigInteger("2");
207 |         final BigFraction large = new BigFraction(pow401.add(BigInteger.ONE),
208 |                                                   pow400.multiply(two));
209 | 
210 |         Assert.assertEquals(5, large.doubleValue(), 1e-15);
211 |     }
```
