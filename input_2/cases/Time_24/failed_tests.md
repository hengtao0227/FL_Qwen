# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_weekyear_month_week_2010()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_weekyear_month_week_2010()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
425 |     public void testParseLocalDate_weekyear_month_week_2010() {
426 |         Chronology chrono = GJChronology.getInstanceUTC();
427 |         DateTimeFormatter f = DateTimeFormat.forPattern("xxxx-MM-ww").withChronology(chrono);
428 |         assertEquals(new LocalDate(2010, 1, 4, chrono), f.parseLocalDate("2010-01-01"));
429 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_weekyear_month_week_2011()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_weekyear_month_week_2011()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
431 |     public void testParseLocalDate_weekyear_month_week_2011() {
432 |         Chronology chrono = GJChronology.getInstanceUTC();
433 |         DateTimeFormatter f = DateTimeFormat.forPattern("xxxx-MM-ww").withChronology(chrono);
434 |         assertEquals(new LocalDate(2011, 1, 3, chrono), f.parseLocalDate("2011-01-01"));
435 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_weekyear_month_week_2012()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_weekyear_month_week_2012()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
437 |     public void testParseLocalDate_weekyear_month_week_2012() {
438 |         Chronology chrono = GJChronology.getInstanceUTC();
439 |         DateTimeFormatter f = DateTimeFormat.forPattern("xxxx-MM-ww").withChronology(chrono);
440 |         assertEquals(new LocalDate(2012, 1, 2, chrono), f.parseLocalDate("2012-01-01"));
441 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2010()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2010()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
451 |     public void testParseLocalDate_year_month_week_2010() {
452 |         Chronology chrono = GJChronology.getInstanceUTC();
453 |         DateTimeFormatter f = DateTimeFormat.forPattern("yyyy-MM-ww").withChronology(chrono);
454 |         assertEquals(new LocalDate(2010, 1, 4, chrono), f.parseLocalDate("2010-01-01"));
455 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2011()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2011()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
457 |     public void testParseLocalDate_year_month_week_2011() {
458 |         Chronology chrono = GJChronology.getInstanceUTC();
459 |         DateTimeFormatter f = DateTimeFormat.forPattern("yyyy-MM-ww").withChronology(chrono);
460 |         assertEquals(new LocalDate(2011, 1, 3, chrono), f.parseLocalDate("2011-01-01"));
461 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2012()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2012()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
463 |     public void testParseLocalDate_year_month_week_2012() {
464 |         Chronology chrono = GJChronology.getInstanceUTC();
465 |         DateTimeFormatter f = DateTimeFormat.forPattern("yyyy-MM-ww").withChronology(chrono);
466 |         assertEquals(new LocalDate(2012, 1, 2, chrono), f.parseLocalDate("2012-01-01"));
467 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2016()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseLocalDate_year_month_week_2016()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
487 |     public void testParseLocalDate_year_month_week_2016() {
488 |         Chronology chrono = GJChronology.getInstanceUTC();
489 |         DateTimeFormatter f = DateTimeFormat.forPattern("yyyy-MM-ww").withChronology(chrono);
490 |         assertEquals(new LocalDate(2016, 1, 4, chrono), f.parseLocalDate("2016-01-01"));
491 |     }
```
