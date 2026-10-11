# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestPeriod_Basics.testNormalizedStandard_periodType_months1()
Resolved declaration: org.joda.time.TestPeriod_Basics.testNormalizedStandard_periodType_months1()
Source: src/test/java/org/joda/time/TestPeriod_Basics.java

```java
1520 |     public void testNormalizedStandard_periodType_months1() {
1521 |         Period test = new Period(1, 15, 0, 0, 0, 0, 0, 0);
1522 |         Period result = test.normalizedStandard(PeriodType.months());
1523 |         assertEquals(new Period(1, 15, 0, 0, 0, 0, 0, 0), test);
1524 |         assertEquals(new Period(0, 27, 0, 0, 0, 0, 0, 0, PeriodType.months()), result);
1525 |     }
```

## org.joda.time.TestPeriod_Basics.testNormalizedStandard_periodType_months2()
Resolved declaration: org.joda.time.TestPeriod_Basics.testNormalizedStandard_periodType_months2()
Source: src/test/java/org/joda/time/TestPeriod_Basics.java

```java
1527 |     public void testNormalizedStandard_periodType_months2() {
1528 |         Period test = new Period(-2, 15, 0, 0, 0, 0, 0, 0);
1529 |         Period result = test.normalizedStandard(PeriodType.months());
1530 |         assertEquals(new Period(-2, 15, 0, 0, 0, 0, 0, 0), test);
1531 |         assertEquals(new Period(0, -9, 0, 0, 0, 0, 0, 0, PeriodType.months()), result);
1532 |     }
```

## org.joda.time.TestPeriod_Basics.testNormalizedStandard_periodType_monthsWeeks()
Resolved declaration: org.joda.time.TestPeriod_Basics.testNormalizedStandard_periodType_monthsWeeks()
Source: src/test/java/org/joda/time/TestPeriod_Basics.java

```java
1551 |     public void testNormalizedStandard_periodType_monthsWeeks() {
1552 |         PeriodType type = PeriodType.forFields(new DurationFieldType[]{
1553 |                         DurationFieldType.months(),
1554 |                         DurationFieldType.weeks(),
1555 |                         DurationFieldType.days()});
1556 |         Period test = new Period(2, 4, 6, 0, 0, 0, 0, 0);
1557 |         Period result = test.normalizedStandard(type);
1558 |         assertEquals(new Period(2, 4, 6, 0, 0, 0, 0, 0), test);
1559 |         assertEquals(new Period(0, 28, 6, 0, 0, 0, 0, 0, type), result);
1560 |     }
```
