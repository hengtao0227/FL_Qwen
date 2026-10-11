# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.format.TestPeriodFormatterBuilder.testBug2495455()
Resolved declaration: org.joda.time.format.TestPeriodFormatterBuilder.testBug2495455()
Source: src/test/java/org/joda/time/format/TestPeriodFormatterBuilder.java

```java
846 |     public void testBug2495455() {
847 |         PeriodFormatter pfmt1 = new PeriodFormatterBuilder()
848 |             .appendLiteral("P")
849 |             .appendYears()
850 |             .appendSuffix("Y")
851 |             .appendMonths()
852 |             .appendSuffix("M")
853 |             .appendWeeks()
854 |             .appendSuffix("W")
855 |             .appendDays()
856 |             .appendSuffix("D")
857 |             .appendSeparatorIfFieldsAfter("T")
858 |             .appendHours()
859 |             .appendSuffix("H")
860 |             .appendMinutes()
861 |             .appendSuffix("M")
862 |             .appendSecondsWithOptionalMillis()
863 |             .appendSuffix("S")
864 |             .toFormatter();
865 |         PeriodFormatter pfmt2 = new PeriodFormatterBuilder()
866 |             .append(ISOPeriodFormat.standard())
867 |             .toFormatter();
868 |         pfmt1.parsePeriod("PT1003199059S");
869 |         pfmt2.parsePeriod("PT1003199059S");
870 |     }
```
