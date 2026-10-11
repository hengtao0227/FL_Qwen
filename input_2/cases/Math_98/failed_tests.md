# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.linear.BigMatrixImplTest.testMath209()
Resolved declaration: org.apache.commons.math.linear.BigMatrixImplTest.testMath209()
Source: src/test/org/apache/commons/math/linear/BigMatrixImplTest.java

```java
440 |     public void testMath209() {
441 |         BigMatrix a = new BigMatrixImpl(new BigDecimal[][] {
442 |                 { new BigDecimal(1), new BigDecimal(2) },
443 |                 { new BigDecimal(3), new BigDecimal(4) },
444 |                 { new BigDecimal(5), new BigDecimal(6) }
445 |         }, false);
446 |         BigDecimal[] b = a.operate(new BigDecimal[] { new BigDecimal(1), new BigDecimal(1) });
447 |         assertEquals(a.getRowDimension(), b.length);
448 |         assertEquals( 3.0, b[0].doubleValue(), 1.0e-12);
449 |         assertEquals( 7.0, b[1].doubleValue(), 1.0e-12);
450 |         assertEquals(11.0, b[2].doubleValue(), 1.0e-12);
451 |     }
```

## org.apache.commons.math.linear.RealMatrixImplTest.testMath209()
Resolved declaration: org.apache.commons.math.linear.RealMatrixImplTest.testMath209()
Source: src/test/org/apache/commons/math/linear/RealMatrixImplTest.java

```java
347 |     public void testMath209() {
348 |         RealMatrix a = new RealMatrixImpl(new double[][] {
349 |                 { 1, 2 }, { 3, 4 }, { 5, 6 }
350 |         }, false);
351 |         double[] b = a.operate(new double[] { 1, 1 });
352 |         assertEquals(a.getRowDimension(), b.length);
353 |         assertEquals( 3.0, b[0], 1.0e-12);
354 |         assertEquals( 7.0, b[1], 1.0e-12);
355 |         assertEquals(11.0, b[2], 1.0e-12);
356 |     }
```
