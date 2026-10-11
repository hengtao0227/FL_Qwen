# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.StringUtilsEqualsIndexOfTest.testContainsIgnoreCase_LocaleIndependence()
Resolved declaration: org.apache.commons.lang.StringUtilsEqualsIndexOfTest.testContainsIgnoreCase_LocaleIndependence()
Source: src/test/org/apache/commons/lang/StringUtilsEqualsIndexOfTest.java

```java
316 |     public void testContainsIgnoreCase_LocaleIndependence() {
317 |         Locale orig = Locale.getDefault();
318 | 
319 |         Locale[] locales = { Locale.ENGLISH, new Locale("tr"), Locale.getDefault() };
320 | 
321 |         String[][] tdata = { 
322 |             { "i", "I" },
323 |             { "I", "i" },
324 |             { "\u03C2", "\u03C3" },
325 |             { "\u03A3", "\u03C2" },
326 |             { "\u03A3", "\u03C3" },
327 |         };
328 | 
329 |         String[][] fdata = { 
330 |             { "\u00DF", "SS" },
331 |         };
332 | 
333 |         try {
334 |             for (int i = 0; i < locales.length; i++) {
335 |                 Locale.setDefault(locales[i]);
336 |                 for (int j = 0; j < tdata.length; j++) {
337 |                     assertTrue(Locale.getDefault() + ": " + j + " " + tdata[j][0] + " " + tdata[j][1], StringUtils
338 |                             .containsIgnoreCase(tdata[j][0], tdata[j][1]));
339 |                 }
340 |                 for (int j = 0; j < fdata.length; j++) {
341 |                     assertFalse(Locale.getDefault() + ": " + j + " " + fdata[j][0] + " " + fdata[j][1], StringUtils
342 |                             .containsIgnoreCase(fdata[j][0], fdata[j][1]));
343 |                 }
344 |             }
345 |         } finally {
346 |             Locale.setDefault(orig);
347 |         }
348 |     }
```
