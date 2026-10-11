# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.util.MathArraysTest.testLinearCombinationWithSingleElementArray()
Resolved declaration: org.apache.commons.math3.util.MathArraysTest.testLinearCombinationWithSingleElementArray()
Source: src/test/java/org/apache/commons/math3/util/MathArraysTest.java

```java
586 |     @Test
587 |     public void testLinearCombinationWithSingleElementArray() {
588 |         final double[] a = { 1.23456789 };
589 |         final double[] b = { 98765432.1 };
590 | 
591 |         Assert.assertEquals(a[0] * b[0], MathArrays.linearCombination(a, b), 0d);
592 |     }
```
