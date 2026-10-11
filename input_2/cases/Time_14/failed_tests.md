# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestMonthDay_Basics.testPlusMonths_int_negativeFromLeap()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testPlusMonths_int_negativeFromLeap()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
458 |     public void testPlusMonths_int_negativeFromLeap() {
459 |         MonthDay test = new MonthDay(2, 29, ISOChronology.getInstanceUTC());
460 |         MonthDay result = test.plusMonths(-1);
461 |         MonthDay expected = new MonthDay(1, 29, ISOChronology.getInstance());
462 |         assertEquals(expected, result);
463 |     }
```

## org.joda.time.TestMonthDay_Basics.testMinusDays_int_negativeFromLeap()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testMinusDays_int_negativeFromLeap()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
608 |     public void testMinusDays_int_negativeFromLeap() {
609 |         MonthDay test = new MonthDay(2, 29, ISOChronology.getInstanceUTC());
610 |         MonthDay result = test.minusDays(-1);
611 |         MonthDay expected = new MonthDay(3, 1, ISOChronology.getInstance());
612 |         assertEquals(expected, result);
613 |     }
```

## org.joda.time.TestMonthDay_Basics.testPlusMonths_int_fromLeap()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testPlusMonths_int_fromLeap()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
451 |     public void testPlusMonths_int_fromLeap() {
452 |         MonthDay test = new MonthDay(2, 29, ISOChronology.getInstanceUTC());
453 |         MonthDay result = test.plusMonths(1);
454 |         MonthDay expected = new MonthDay(3, 29, ISOChronology.getInstance());
455 |         assertEquals(expected, result);
456 |     }
```

## org.joda.time.TestMonthDay_Basics.testPlusMonths_int_negativeEndOfMonthAdjust()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testPlusMonths_int_negativeEndOfMonthAdjust()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
472 |     public void testPlusMonths_int_negativeEndOfMonthAdjust() {
473 |         MonthDay test = new MonthDay(3, 31, ISOChronology.getInstanceUTC());
474 |         MonthDay result = test.plusMonths(-1);
475 |         MonthDay expected = new MonthDay(2, 29, ISOChronology.getInstance());
476 |         assertEquals(expected, result);
477 |     }
```

## org.joda.time.TestMonthDay_Basics.testMinusMonths_int_endOfMonthAdjust()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testMinusMonths_int_endOfMonthAdjust()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
559 |     public void testMinusMonths_int_endOfMonthAdjust() {
560 |         MonthDay test = new MonthDay(3, 31, ISOChronology.getInstanceUTC());
561 |         MonthDay result = test.minusMonths(1);
562 |         MonthDay expected = new MonthDay(2, 29, ISOChronology.getInstance());
563 |         assertEquals(expected, result);
564 |     }
```

## org.joda.time.TestMonthDay_Basics.testMinusMonths_int_negativeFromLeap()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testMinusMonths_int_negativeFromLeap()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
552 |     public void testMinusMonths_int_negativeFromLeap() {
553 |         MonthDay test = new MonthDay(2, 29, ISOChronology.getInstanceUTC());
554 |         MonthDay result = test.minusMonths(-1);
555 |         MonthDay expected = new MonthDay(3, 29, ISOChronology.getInstance());
556 |         assertEquals(expected, result);
557 |     }
```

## org.joda.time.TestMonthDay_Basics.testMinusMonths_int_fromLeap()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testMinusMonths_int_fromLeap()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
545 |     public void testMinusMonths_int_fromLeap() {
546 |         MonthDay test = new MonthDay(2, 29, ISOChronology.getInstanceUTC());
547 |         MonthDay result = test.minusMonths(1);
548 |         MonthDay expected = new MonthDay(1, 29, ISOChronology.getInstance());
549 |         assertEquals(expected, result);
550 |     }
```

## org.joda.time.TestMonthDay_Basics.testPlusDays_int_fromLeap()
Resolved declaration: org.joda.time.TestMonthDay_Basics.testPlusDays_int_fromLeap()
Source: src/test/java/org/joda/time/TestMonthDay_Basics.java

```java
507 |     public void testPlusDays_int_fromLeap() {
508 |         MonthDay test = new MonthDay(2, 29, ISOChronology.getInstanceUTC());
509 |         MonthDay result = test.plusDays(1);
510 |         MonthDay expected = new MonthDay(3, 1, ISOChronology.getInstance());
511 |         assertEquals(expected, result);
512 |     }
```
