# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.WordUtilsTest.testAbbreviate()
Resolved declaration: org.apache.commons.lang.WordUtilsTest.testAbbreviate()
Source: src/test/org/apache/commons/lang/WordUtilsTest.java

```java
366 |     public void testAbbreviate() {
367 |         // check null and empty are returned respectively
368 |         assertNull(WordUtils.abbreviate(null, 1,-1,""));
369 |         assertEquals(StringUtils.EMPTY, WordUtils.abbreviate("", 1,-1,""));
370 | 
371 |         // test upper limit
372 |         assertEquals("01234", WordUtils.abbreviate("0123456789", 0,5,""));
373 |         assertEquals("01234", WordUtils.abbreviate("0123456789", 5, 2,""));
374 |         assertEquals("012", WordUtils.abbreviate("012 3456789", 2, 5,""));
375 |         assertEquals("012 3", WordUtils.abbreviate("012 3456789", 5, 2,""));
376 |         assertEquals("0123456789", WordUtils.abbreviate("0123456789", 0,-1,""));
377 | 
378 |         // test upper limit + append string
379 |         assertEquals("01234-", WordUtils.abbreviate("0123456789", 0,5,"-"));
380 |         assertEquals("01234-", WordUtils.abbreviate("0123456789", 5, 2,"-"));
381 |         assertEquals("012", WordUtils.abbreviate("012 3456789", 2, 5, null));
382 |         assertEquals("012 3", WordUtils.abbreviate("012 3456789", 5, 2,""));
383 |         assertEquals("0123456789", WordUtils.abbreviate("0123456789", 0,-1,""));
384 | 
385 |         // test lower value
386 |         assertEquals("012", WordUtils.abbreviate("012 3456789", 0,5, null));
387 |         assertEquals("01234", WordUtils.abbreviate("01234 56789", 5, 10, null));
388 |         assertEquals("01 23 45 67", WordUtils.abbreviate("01 23 45 67 89", 9, -1, null));
389 |         assertEquals("01 23 45 6", WordUtils.abbreviate("01 23 45 67 89", 9, 10, null));
390 |         assertEquals("0123456789", WordUtils.abbreviate("0123456789", 15, 20, null));
391 | 
392 |         // test lower value + append
393 |         assertEquals("012", WordUtils.abbreviate("012 3456789", 0,5, null));
394 |         assertEquals("01234-", WordUtils.abbreviate("01234 56789", 5, 10, "-"));
395 |         assertEquals("01 23 45 67abc", WordUtils.abbreviate("01 23 45 67 89", 9, -1, "abc"));
396 |         assertEquals("01 23 45 6", WordUtils.abbreviate("01 23 45 67 89", 9, 10, ""));
397 | 
398 |         // others
399 |         assertEquals("", WordUtils.abbreviate("0123456790", 0,0,""));
400 |         assertEquals("", WordUtils.abbreviate(" 0123456790", 0,-1,""));
401 |     }
```
