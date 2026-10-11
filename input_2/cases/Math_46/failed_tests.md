# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.complex.ComplexTest.testAtanI()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testAtanI()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
575 |     @Test
576 |     public void testAtanI() {
577 |         Assert.assertTrue(Complex.I.atan().isNaN());
578 |     }
```

## org.apache.commons.math.complex.ComplexTest.testDivideZero()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testDivideZero()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
228 |     @Test
229 |     public void testDivideZero() {
230 |         Complex x = new Complex(3.0, 4.0);
231 |         Complex z = x.divide(Complex.ZERO);
232 |         // Assert.assertEquals(z, Complex.INF); // See MATH-657
233 |         Assert.assertEquals(z, Complex.NaN);
234 |     }
```
