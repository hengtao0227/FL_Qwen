# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.BooleanUtilsTest.test_toBoolean_String()
Resolved declaration: org.apache.commons.lang.BooleanUtilsTest.test_toBoolean_String()
Source: src/test/org/apache/commons/lang/BooleanUtilsTest.java

```java
295 |     public void test_toBoolean_String() {
296 |         assertEquals(false, BooleanUtils.toBoolean((String) null));
297 |         assertEquals(false, BooleanUtils.toBoolean(""));
298 |         assertEquals(false, BooleanUtils.toBoolean("off"));
299 |         assertEquals(false, BooleanUtils.toBoolean("oof"));
300 |         assertEquals(false, BooleanUtils.toBoolean("yep"));
301 |         assertEquals(false, BooleanUtils.toBoolean("trux"));
302 |         assertEquals(false, BooleanUtils.toBoolean("false"));
303 |         assertEquals(false, BooleanUtils.toBoolean("a"));
304 |         assertEquals(true, BooleanUtils.toBoolean("true")); // interned handled differently
305 |         assertEquals(true, BooleanUtils.toBoolean(new StringBuffer("tr").append("ue").toString()));
306 |         assertEquals(true, BooleanUtils.toBoolean("truE"));
307 |         assertEquals(true, BooleanUtils.toBoolean("trUe"));
308 |         assertEquals(true, BooleanUtils.toBoolean("trUE"));
309 |         assertEquals(true, BooleanUtils.toBoolean("tRue"));
310 |         assertEquals(true, BooleanUtils.toBoolean("tRuE"));
311 |         assertEquals(true, BooleanUtils.toBoolean("tRUe"));
312 |         assertEquals(true, BooleanUtils.toBoolean("tRUE"));
313 |         assertEquals(true, BooleanUtils.toBoolean("TRUE"));
314 |         assertEquals(true, BooleanUtils.toBoolean("TRUe"));
315 |         assertEquals(true, BooleanUtils.toBoolean("TRuE"));
316 |         assertEquals(true, BooleanUtils.toBoolean("TRue"));
317 |         assertEquals(true, BooleanUtils.toBoolean("TrUE"));
318 |         assertEquals(true, BooleanUtils.toBoolean("TrUe"));
319 |         assertEquals(true, BooleanUtils.toBoolean("TruE"));
320 |         assertEquals(true, BooleanUtils.toBoolean("True"));
321 |         assertEquals(true, BooleanUtils.toBoolean("on"));
322 |         assertEquals(true, BooleanUtils.toBoolean("oN"));
323 |         assertEquals(true, BooleanUtils.toBoolean("On"));
324 |         assertEquals(true, BooleanUtils.toBoolean("ON"));
325 |         assertEquals(true, BooleanUtils.toBoolean("yes"));
326 |         assertEquals(true, BooleanUtils.toBoolean("yeS"));
327 |         assertEquals(true, BooleanUtils.toBoolean("yEs"));
328 |         assertEquals(true, BooleanUtils.toBoolean("yES"));
329 |         assertEquals(true, BooleanUtils.toBoolean("Yes"));
330 |         assertEquals(true, BooleanUtils.toBoolean("YeS"));
331 |         assertEquals(true, BooleanUtils.toBoolean("YEs"));
332 |         assertEquals(true, BooleanUtils.toBoolean("YES"));
333 |         assertEquals(false, BooleanUtils.toBoolean("yes?"));
334 |         assertEquals(false, BooleanUtils.toBoolean("tru"));
335 |     }
```
