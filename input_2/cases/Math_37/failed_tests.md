# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.complex.ComplexTest.testTanhInf()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testTanhInf()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
1050 |     @Test
1051 |     public void testTanhInf() {
1052 |         TestUtils.assertSame(Complex.NaN, oneInf.tanh());
1053 |         TestUtils.assertSame(Complex.NaN, oneNegInf.tanh());
1054 |         TestUtils.assertSame(Complex.valueOf(1.0, 0.0), infOne.tanh());
1055 |         TestUtils.assertSame(Complex.valueOf(-1.0, 0.0), negInfOne.tanh());
1056 |         TestUtils.assertSame(Complex.NaN, infInf.tanh());
1057 |         TestUtils.assertSame(Complex.NaN, infNegInf.tanh());
1058 |         TestUtils.assertSame(Complex.NaN, negInfInf.tanh());
1059 |         TestUtils.assertSame(Complex.NaN, negInfNegInf.tanh());
1060 |     }
```

## org.apache.commons.math.complex.ComplexTest.testTan()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testTan()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
994 |     @Test
995 |     public void testTan() {
996 |         Complex z = new Complex(3, 4);
997 |         Complex expected = new Complex(-0.000187346, 0.999356);
998 |         TestUtils.assertEquals(expected, z.tan(), 1.0e-5);
999 |         /* Check that no overflow occurs (MATH-722) */
1000 |         Complex actual = new Complex(3.0, 1E10).tan();
1001 |         expected = new Complex(0, 1);
1002 |         TestUtils.assertEquals(expected, actual, 1.0e-5);
1003 |         actual = new Complex(3.0, -1E10).tan();
1004 |         expected = new Complex(0, -1);
1005 |         TestUtils.assertEquals(expected, actual, 1.0e-5);
1006 |     }
```

## org.apache.commons.math.complex.ComplexTest.testTanh()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testTanh()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
1031 |     @Test
1032 |     public void testTanh() {
1033 |         Complex z = new Complex(3, 4);
1034 |         Complex expected = new Complex(1.00071, 0.00490826);
1035 |         TestUtils.assertEquals(expected, z.tanh(), 1.0e-5);
1036 |         /* Check that no overflow occurs (MATH-722) */
1037 |         Complex actual = new Complex(1E10, 3.0).tanh();
1038 |         expected = new Complex(1, 0);
1039 |         TestUtils.assertEquals(expected, actual, 1.0e-5);
1040 |         actual = new Complex(-1E10, 3.0).tanh();
1041 |         expected = new Complex(-1, 0);
1042 |         TestUtils.assertEquals(expected, actual, 1.0e-5);
1043 |     }
```

## org.apache.commons.math.complex.ComplexTest.testTanInf()
Resolved declaration: org.apache.commons.math.complex.ComplexTest.testTanInf()
Source: src/test/java/org/apache/commons/math/complex/ComplexTest.java

```java
1013 |     @Test
1014 |     public void testTanInf() {
1015 |         TestUtils.assertSame(Complex.valueOf(0.0, 1.0), oneInf.tan());
1016 |         TestUtils.assertSame(Complex.valueOf(0.0, -1.0), oneNegInf.tan());
1017 |         TestUtils.assertSame(Complex.NaN, infOne.tan());
1018 |         TestUtils.assertSame(Complex.NaN, negInfOne.tan());
1019 |         TestUtils.assertSame(Complex.NaN, infInf.tan());
1020 |         TestUtils.assertSame(Complex.NaN, infNegInf.tan());
1021 |         TestUtils.assertSame(Complex.NaN, negInfInf.tan());
1022 |         TestUtils.assertSame(Complex.NaN, negInfNegInf.tan());
1023 |     }
```
