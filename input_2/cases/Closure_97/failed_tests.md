# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldBitShifts()
Resolved declaration: com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldBitShifts()
Source: test/com/google/javascript/jscomp/PeepholeFoldConstantsTest.java

```java
240 |   public void testFoldBitShifts() {
241 |     fold("x = 1 << 0", "x = 1");
242 |     fold("x = -1 << 0", "x = -1");
243 |     fold("x = 1 << 1", "x = 2");
244 |     fold("x = 3 << 1", "x = 6");
245 |     fold("x = 1 << 8", "x = 256");
246 | 
247 |     fold("x = 1 >> 0", "x = 1");
248 |     fold("x = -1 >> 0", "x = -1");
249 |     fold("x = 1 >> 1", "x = 0");
250 |     fold("x = 2 >> 1", "x = 1");
251 |     fold("x = 5 >> 1", "x = 2");
252 |     fold("x = 127 >> 3", "x = 15");
253 |     fold("x = 3 >> 1", "x = 1");
254 |     fold("x = 3 >> 2", "x = 0");
255 |     fold("x = 10 >> 1", "x = 5");
256 |     fold("x = 10 >> 2", "x = 2");
257 |     fold("x = 10 >> 5", "x = 0");
258 | 
259 |     fold("x = 10 >>> 1", "x = 5");
260 |     fold("x = 10 >>> 2", "x = 2");
261 |     fold("x = 10 >>> 5", "x = 0");
262 |     fold("x = -1 >>> 1", "x = 2147483647"); // 0x7fffffff
263 |     fold("x = -1 >>> 0", "x = 4294967295"); // 0xffffffff
264 |     fold("x = -2 >>> 0", "x = 4294967294"); // 0xfffffffe
265 | 
266 |     fold("3000000000 << 1", "3000000000<<1",
267 |          PeepholeFoldConstants.BITWISE_OPERAND_OUT_OF_RANGE);
268 |     fold("1 << 32", "1<<32",
269 |         PeepholeFoldConstants.SHIFT_AMOUNT_OUT_OF_BOUNDS);
270 |     fold("1 << -1", "1<<32",
271 |         PeepholeFoldConstants.SHIFT_AMOUNT_OUT_OF_BOUNDS);
272 |     fold("3000000000 >> 1", "3000000000>>1",
273 |         PeepholeFoldConstants.BITWISE_OPERAND_OUT_OF_RANGE);
274 |     fold("1 >> 32", "1>>32",
275 |         PeepholeFoldConstants.SHIFT_AMOUNT_OUT_OF_BOUNDS);
276 |     fold("1.5 << 0",  "1.5<<0",
277 |         PeepholeFoldConstants.FRACTIONAL_BITWISE_OPERAND);
278 |     fold("1 << .5",   "1.5<<0",
279 |         PeepholeFoldConstants.FRACTIONAL_BITWISE_OPERAND);
280 |     fold("1.5 >>> 0", "1.5>>>0",
281 |         PeepholeFoldConstants.FRACTIONAL_BITWISE_OPERAND);
282 |     fold("1 >>> .5",  "1.5>>>0",
283 |         PeepholeFoldConstants.FRACTIONAL_BITWISE_OPERAND);
284 |     fold("1.5 >> 0",  "1.5>>0",
285 |         PeepholeFoldConstants.FRACTIONAL_BITWISE_OPERAND);
286 |     fold("1 >> .5",   "1.5>>0",
287 |         PeepholeFoldConstants.FRACTIONAL_BITWISE_OPERAND);
288 |   }
```
