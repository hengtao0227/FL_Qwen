# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.util.FastMathTest.testMath904()
Resolved declaration: org.apache.commons.math3.util.FastMathTest.testMath904()
Source: src/test/java/org/apache/commons/math3/util/FastMathTest.java

```java
160 |     @Test
161 |     public void testMath904() {
162 |         final double x = -1;
163 |         final double y = (5 + 1e-15) * 1e15;
164 |         Assert.assertEquals(Math.pow(x, y),
165 |                             FastMath.pow(x, y), 0);
166 |         Assert.assertEquals(Math.pow(x, -y),
167 |                             FastMath.pow(x, -y), 0);
168 |     }
```
