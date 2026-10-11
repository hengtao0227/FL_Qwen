# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDays.testFactory_daysBetween_RPartial_MonthDay()
Resolved declaration: org.joda.time.TestDays.testFactory_daysBetween_RPartial_MonthDay()
Source: src/test/java/org/joda/time/TestDays.java

```java
123 |     public void testFactory_daysBetween_RPartial_MonthDay() {
124 |         MonthDay start1 = new MonthDay(2, 1);
125 |         MonthDay start2 = new MonthDay(2, 28);
126 |         MonthDay end1 = new MonthDay(2, 28);
127 |         MonthDay end2 = new MonthDay(2, 29);
128 |         
129 |         assertEquals(27, Days.daysBetween(start1, end1).getDays());
130 |         assertEquals(28, Days.daysBetween(start1, end2).getDays());
131 |         assertEquals(0, Days.daysBetween(start2, end1).getDays());
132 |         assertEquals(1, Days.daysBetween(start2, end2).getDays());
133 |         
134 |         assertEquals(-27, Days.daysBetween(end1, start1).getDays());
135 |         assertEquals(-28, Days.daysBetween(end2, start1).getDays());
136 |         assertEquals(0, Days.daysBetween(end1, start2).getDays());
137 |         assertEquals(-1, Days.daysBetween(end2, start2).getDays());
138 |     }
```

## org.joda.time.TestMonths.testFactory_monthsBetween_RPartial_MonthDay()
Resolved declaration: org.joda.time.TestMonths.testFactory_monthsBetween_RPartial_MonthDay()
Source: src/test/java/org/joda/time/TestMonths.java

```java
130 |     public void testFactory_monthsBetween_RPartial_MonthDay() {
131 |         MonthDay start = new MonthDay(2, 1);
132 |         MonthDay end1 = new MonthDay(2, 28);
133 |         MonthDay end2 = new MonthDay(2, 29);
134 |         MonthDay end3 = new MonthDay(3, 1);
135 |         
136 |         assertEquals(0, Months.monthsBetween(start, end1).getMonths());
137 |         assertEquals(0, Months.monthsBetween(start, end2).getMonths());
138 |         assertEquals(1, Months.monthsBetween(start, end3).getMonths());
139 |         
140 |         assertEquals(0, Months.monthsBetween(end1, start).getMonths());
141 |         assertEquals(0, Months.monthsBetween(end2, start).getMonths());
142 |         assertEquals(-1, Months.monthsBetween(end3, start).getMonths());
143 |     }
```
