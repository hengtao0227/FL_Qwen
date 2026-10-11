# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.field.TestFieldUtils.testSafeMultiplyLongInt()
Resolved declaration: org.joda.time.field.TestFieldUtils.testSafeMultiplyLongInt()
Source: src/test/java/org/joda/time/field/TestFieldUtils.java

```java
241 |     public void testSafeMultiplyLongInt() {
242 |         assertEquals(0L, FieldUtils.safeMultiply(0L, 0));
243 |         
244 |         assertEquals(1L, FieldUtils.safeMultiply(1L, 1));
245 |         assertEquals(3L, FieldUtils.safeMultiply(1L, 3));
246 |         assertEquals(3L, FieldUtils.safeMultiply(3L, 1));
247 |         
248 |         assertEquals(6L, FieldUtils.safeMultiply(2L, 3));
249 |         assertEquals(-6L, FieldUtils.safeMultiply(2L, -3));
250 |         assertEquals(-6L, FieldUtils.safeMultiply(-2L, 3));
251 |         assertEquals(6L, FieldUtils.safeMultiply(-2L, -3));
252 |         
253 |         assertEquals(-1L * Integer.MIN_VALUE, FieldUtils.safeMultiply(-1L, Integer.MIN_VALUE));
254 |         
255 |         assertEquals(Long.MAX_VALUE, FieldUtils.safeMultiply(Long.MAX_VALUE, 1));
256 |         assertEquals(Long.MIN_VALUE, FieldUtils.safeMultiply(Long.MIN_VALUE, 1));
257 |         assertEquals(-Long.MAX_VALUE, FieldUtils.safeMultiply(Long.MAX_VALUE, -1));
258 |         
259 |         try {
260 |             FieldUtils.safeMultiply(Long.MIN_VALUE, -1);
261 |             fail();
262 |         } catch (ArithmeticException e) {
263 |         }
264 |         
265 |         try {
266 |             FieldUtils.safeMultiply(Long.MIN_VALUE, 100);
267 |             fail();
268 |         } catch (ArithmeticException e) {
269 |         }
270 |         
271 |         try {
272 |             FieldUtils.safeMultiply(Long.MIN_VALUE, Integer.MAX_VALUE);
273 |             fail();
274 |         } catch (ArithmeticException e) {
275 |         }
276 |         
277 |         try {
278 |             FieldUtils.safeMultiply(Long.MAX_VALUE, Integer.MIN_VALUE);
279 |             fail();
280 |         } catch (ArithmeticException e) {
281 |         }
282 |     }
```
