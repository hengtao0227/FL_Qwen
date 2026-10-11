# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.linear.OpenMapRealMatrixTest.testMath679()
Resolved declaration: org.apache.commons.math.linear.OpenMapRealMatrixTest.testMath679()
Source: src/test/java/org/apache/commons/math/linear/OpenMapRealMatrixTest.java

```java
24 |     @Test(expected=NumberIsTooLargeException.class)
25 |     public void testMath679() {
26 |         new OpenMapRealMatrix(3, Integer.MAX_VALUE);
27 |     }
```
