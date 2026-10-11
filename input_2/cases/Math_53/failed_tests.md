# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.complex.ComplexTest.testAddNaN()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testAddNaN()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
109 |     @Test
110 |     public void testAddNaN() {
111 |         Complex x = new Complex(3.0, 4.0);
112 |         Complex z = x.add(Complex.NaN);
113 |         Assert.assertTrue(z.isNaN());
114 |         z = new Complex(1, nan);
115 |         Complex w = x.add(z);
116 |         Assert.assertTrue(Double.isNaN(w.getReal()));
117 |         Assert.assertTrue(Double.isNaN(w.getImaginary()));
118 |     }
```
