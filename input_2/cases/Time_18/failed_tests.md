# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.chrono.TestGJChronology.testLeapYearRulesConstruction()
Resolved declaration: org.joda.time.chrono.TestGJChronology.testLeapYearRulesConstruction()
Source: src/test/java/org/joda/time/chrono/TestGJChronology.java

```java
494 |     public void testLeapYearRulesConstruction() {
495 |         // 1500 not leap in Gregorian, but is leap in Julian
496 |         DateMidnight dt = new DateMidnight(1500, 2, 29, GJChronology.getInstanceUTC());
497 |         assertEquals(dt.getYear(), 1500);
498 |         assertEquals(dt.getMonthOfYear(), 2);
499 |         assertEquals(dt.getDayOfMonth(), 29);
500 |     }
```
