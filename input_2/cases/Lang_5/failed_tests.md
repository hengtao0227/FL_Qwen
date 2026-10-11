# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.LocaleUtilsTest.testLang865()
Resolved declaration: org.apache.commons.lang3.LocaleUtilsTest.testLang865()
Source: src/test/java/org/apache/commons/lang3/LocaleUtilsTest.java

```java
503 |     @Test
504 |     public void testLang865() {
505 |         assertValidToLocale("_GB", "", "GB", "");
506 |         assertValidToLocale("_GB_P", "", "GB", "P");
507 |         assertValidToLocale("_GB_POSIX", "", "GB", "POSIX");
508 |         try {
509 |             LocaleUtils.toLocale("_G");
510 |             fail("Must be at least 3 chars if starts with underscore");
511 |         } catch (final IllegalArgumentException iae) {
512 |         }
513 |         try {
514 |             LocaleUtils.toLocale("_Gb");
515 |             fail("Must be uppercase if starts with underscore");
516 |         } catch (final IllegalArgumentException iae) {
517 |         }
518 |         try {
519 |             LocaleUtils.toLocale("_gB");
520 |             fail("Must be uppercase if starts with underscore");
521 |         } catch (final IllegalArgumentException iae) {
522 |         }
523 |         try {
524 |             LocaleUtils.toLocale("_1B");
525 |             fail("Must be letter if starts with underscore");
526 |         } catch (final IllegalArgumentException iae) {
527 |         }
528 |         try {
529 |             LocaleUtils.toLocale("_G1");
530 |             fail("Must be letter if starts with underscore");
531 |         } catch (final IllegalArgumentException iae) {
532 |         }
533 |         try {
534 |             LocaleUtils.toLocale("_GB_");
535 |             fail("Must be at least 5 chars if starts with underscore");
536 |         } catch (final IllegalArgumentException iae) {
537 |         }
538 |         try {
539 |             LocaleUtils.toLocale("_GBAP");
540 |             fail("Must have underscore after the country if starts with underscore and is at least 5 chars");
541 |         } catch (final IllegalArgumentException iae) {
542 |         }
543 |     }
```
