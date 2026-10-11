# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.util.MathUtilsTest.testGcd()
Resolved declaration: org.apache.commons.math.util.MathUtilsTest.testGcd()
Source: src/test/org/apache/commons/math/util/MathUtilsTest.java

```java
273 |     public void testGcd() {
274 |         int a = 30;
275 |         int b = 50;
276 |         int c = 77;
277 | 
278 |         assertEquals(0, MathUtils.gcd(0, 0));
279 | 
280 |         assertEquals(b, MathUtils.gcd(0, b));
281 |         assertEquals(a, MathUtils.gcd(a, 0));
282 |         assertEquals(b, MathUtils.gcd(0, -b));
283 |         assertEquals(a, MathUtils.gcd(-a, 0));
284 | 
285 |         assertEquals(10, MathUtils.gcd(a, b));
286 |         assertEquals(10, MathUtils.gcd(-a, b));
287 |         assertEquals(10, MathUtils.gcd(a, -b));
288 |         assertEquals(10, MathUtils.gcd(-a, -b));
289 | 
290 |         assertEquals(1, MathUtils.gcd(a, c));
291 |         assertEquals(1, MathUtils.gcd(-a, c));
292 |         assertEquals(1, MathUtils.gcd(a, -c));
293 |         assertEquals(1, MathUtils.gcd(-a, -c));
294 | 
295 |         assertEquals(3 * (1<<15), MathUtils.gcd(3 * (1<<20), 9 * (1<<15)));
296 | 
297 |     }
```
