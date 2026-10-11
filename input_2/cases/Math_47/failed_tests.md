# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.complex.ComplexTest.testAtanI()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testAtanI()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
574 |     @Test
575 |     public void testAtanI() {
576 |         for (int i = -10; i < 10; i++) {
577 |             System.out.println(new Complex(0, 1 - 0.1 * i).atan());
578 |         }
579 |         Assert.assertTrue(Complex.I.atan().isInfinite());
580 |     }
```

## org.apache.commons.math.complex.ComplexTest.testDivideZero()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testDivideZero()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
228 |     @Test
229 |     public void testDivideZero() {
230 |         Complex x = new Complex(3.0, 4.0);
231 |         Complex z = x.divide(Complex.ZERO);
232 |         Assert.assertEquals(z, Complex.INF);
233 |     }
```
