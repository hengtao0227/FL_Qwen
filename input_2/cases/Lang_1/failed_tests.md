# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.NumberUtilsTest.TestLang747()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.TestLang747()
Source: src/test/java/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
249 |     @Test
250 |     public void TestLang747() {
251 |         assertEquals(Integer.valueOf(0x8000),      NumberUtils.createNumber("0x8000"));
252 |         assertEquals(Integer.valueOf(0x80000),     NumberUtils.createNumber("0x80000"));
253 |         assertEquals(Integer.valueOf(0x800000),    NumberUtils.createNumber("0x800000"));
254 |         assertEquals(Integer.valueOf(0x8000000),   NumberUtils.createNumber("0x8000000"));
255 |         assertEquals(Integer.valueOf(0x7FFFFFFF),  NumberUtils.createNumber("0x7FFFFFFF"));
256 |         assertEquals(Long.valueOf(0x80000000L),    NumberUtils.createNumber("0x80000000"));
257 |         assertEquals(Long.valueOf(0xFFFFFFFFL),    NumberUtils.createNumber("0xFFFFFFFF"));
258 | 
259 |         // Leading zero tests
260 |         assertEquals(Integer.valueOf(0x8000000),   NumberUtils.createNumber("0x08000000"));
261 |         assertEquals(Integer.valueOf(0x7FFFFFFF),  NumberUtils.createNumber("0x007FFFFFFF"));
262 |         assertEquals(Long.valueOf(0x80000000L),    NumberUtils.createNumber("0x080000000"));
263 |         assertEquals(Long.valueOf(0xFFFFFFFFL),    NumberUtils.createNumber("0x00FFFFFFFF"));
264 | 
265 |         assertEquals(Long.valueOf(0x800000000L),        NumberUtils.createNumber("0x800000000"));
266 |         assertEquals(Long.valueOf(0x8000000000L),       NumberUtils.createNumber("0x8000000000"));
267 |         assertEquals(Long.valueOf(0x80000000000L),      NumberUtils.createNumber("0x80000000000"));
268 |         assertEquals(Long.valueOf(0x800000000000L),     NumberUtils.createNumber("0x800000000000"));
269 |         assertEquals(Long.valueOf(0x8000000000000L),    NumberUtils.createNumber("0x8000000000000"));
270 |         assertEquals(Long.valueOf(0x80000000000000L),   NumberUtils.createNumber("0x80000000000000"));
271 |         assertEquals(Long.valueOf(0x800000000000000L),  NumberUtils.createNumber("0x800000000000000"));
272 |         assertEquals(Long.valueOf(0x7FFFFFFFFFFFFFFFL), NumberUtils.createNumber("0x7FFFFFFFFFFFFFFF"));
273 |         // N.B. Cannot use a hex constant such as 0x8000000000000000L here as that is interpreted as a negative long
274 |         assertEquals(new BigInteger("8000000000000000", 16), NumberUtils.createNumber("0x8000000000000000"));
275 |         assertEquals(new BigInteger("FFFFFFFFFFFFFFFF", 16), NumberUtils.createNumber("0xFFFFFFFFFFFFFFFF"));
276 | 
277 |         // Leading zero tests
278 |         assertEquals(Long.valueOf(0x80000000000000L),   NumberUtils.createNumber("0x00080000000000000"));
279 |         assertEquals(Long.valueOf(0x800000000000000L),  NumberUtils.createNumber("0x0800000000000000"));
280 |         assertEquals(Long.valueOf(0x7FFFFFFFFFFFFFFFL), NumberUtils.createNumber("0x07FFFFFFFFFFFFFFF"));
281 |         // N.B. Cannot use a hex constant such as 0x8000000000000000L here as that is interpreted as a negative long
282 |         assertEquals(new BigInteger("8000000000000000", 16), NumberUtils.createNumber("0x00008000000000000000"));
283 |         assertEquals(new BigInteger("FFFFFFFFFFFFFFFF", 16), NumberUtils.createNumber("0x0FFFFFFFFFFFFFFFF"));
284 |     }
```
