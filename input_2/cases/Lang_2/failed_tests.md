# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.LocaleUtilsTest.testParseAllLocales()
Resolved declaration: org.apache.commons.lang3.LocaleUtilsTest.testParseAllLocales()
Source: src/test/java/org/apache/commons/lang3/LocaleUtilsTest.java

```java
545 |     @Test
546 |     public void testParseAllLocales() {
547 |         Locale[] locales = Locale.getAvailableLocales();
548 |         int failures = 0;
549 |         for (Locale l : locales) {
550 |             // Check if it's possible to recreate the Locale using just the standard constructor
551 |             Locale locale = new Locale(l.getLanguage(), l.getCountry(), l.getVariant());
552 |             if (l.equals(locale)) { // it is possible for LocaleUtils.toLocale to handle these Locales
553 |                 String str = l.toString();
554 |                 // Look for the script/extension suffix
555 |                 int suff = str.indexOf("_#");
556 |                 if (suff == - 1) {
557 |                     suff = str.indexOf("#");
558 |                 }
559 |                 if (suff >= 0) { // we have a suffix
560 |                     try {
561 |                         LocaleUtils.toLocale(str); // shouuld cause IAE
562 |                         System.out.println("Should not have parsed: " + str);
563 |                         failures++;
564 |                         continue; // try next Locale
565 |                     } catch (IllegalArgumentException iae) {
566 |                         // expected; try without suffix
567 |                         str = str.substring(0, suff);
568 |                     }
569 |                 }
570 |                 Locale loc = LocaleUtils.toLocale(str);
571 |                 if (!l.equals(loc)) {
572 |                     System.out.println("Failed to parse: " + str);
573 |                     failures++;
574 |                 }                    
575 |             }
576 |         }
577 |         if (failures > 0) {
578 |             fail("Failed "+failures+" test(s)");
579 |         }
580 |     }
```
