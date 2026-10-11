# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.util.MathUtilsTest.testFactorial()
Resolved declaration: org.apache.commons.math.util.MathUtilsTest.testFactorial()
Source: src/test/org/apache/commons/math/util/MathUtilsTest.java

```java
234 |     public void testFactorial() {
235 |         for (int i = 1; i < 21; i++) {
236 |             assertEquals(i + "! ", factorial(i), MathUtils.factorial(i));
237 |             assertEquals(i + "! ", (double)factorial(i), MathUtils.factorialDouble(i), Double.MIN_VALUE);
238 |             assertEquals(i + "! ", Math.log((double)factorial(i)), MathUtils.factorialLog(i), 10E-12);
239 |         }
240 |         
241 |         assertEquals("0", 1, MathUtils.factorial(0));
242 |         assertEquals("0", 1.0d, MathUtils.factorialDouble(0), 1E-14);
243 |         assertEquals("0", 0.0d, MathUtils.factorialLog(0), 1E-14);
244 |     }
```
