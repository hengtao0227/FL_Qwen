# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.chrono.TestGJDate.test_cutoverPreZero()
Resolved declaration: org.joda.time.chrono.TestGJDate.test_cutoverPreZero()
Source: src/test/java/org/joda/time/chrono/TestGJDate.java

```java
128 |     public void test_cutoverPreZero() {
129 |         DateTime cutover = new LocalDate(-2, 6, 30, ISOChronology.getInstanceUTC()).toDateTimeAtStartOfDay(DateTimeZone.UTC);
130 |         try {
131 |             GJChronology.getInstance(DateTimeZone.UTC, cutover);
132 |             fail();
133 |         } catch (IllegalArgumentException ex) {
134 |             // expected
135 |         }
136 |     }
```

## org.joda.time.chrono.TestGJDate.test_plusWeekyears_positiveToNegative_crossCutover()
Resolved declaration: org.joda.time.chrono.TestGJDate.test_plusWeekyears_positiveToNegative_crossCutover()
Source: src/test/java/org/joda/time/chrono/TestGJDate.java

```java
121 |     public void test_plusWeekyears_positiveToNegative_crossCutover() {
122 |         LocalDate date = new LocalDate(2003, 6, 30, GJ_CHRONOLOGY);
123 |         LocalDate expected = new LocalDate(-2, 6, 30, GJ_CHRONOLOGY).withWeekOfWeekyear(date.getWeekOfWeekyear()).withDayOfWeek(date.getDayOfWeek());
124 |         assertEquals(expected, date.weekyear().addToCopy(-2004));
125 |     }
```

## org.joda.time.chrono.TestGJDate.test_plusYears_positiveToZero_crossCutover()
Resolved declaration: org.joda.time.chrono.TestGJDate.test_plusYears_positiveToZero_crossCutover()
Source: src/test/java/org/joda/time/chrono/TestGJDate.java

```java
96 |     public void test_plusYears_positiveToZero_crossCutover() {
97 |         LocalDate date = new LocalDate(2003, 6, 30, GJ_CHRONOLOGY);
98 |         LocalDate expected = new LocalDate(-1, 6, 30, GJ_CHRONOLOGY);
99 |         assertEquals(expected, date.plusYears(-2003));
100 |     }
```

## org.joda.time.chrono.TestGJDate.test_plusYears_positiveToNegative_crossCutover()
Resolved declaration: org.joda.time.chrono.TestGJDate.test_plusYears_positiveToNegative_crossCutover()
Source: src/test/java/org/joda/time/chrono/TestGJDate.java

```java
102 |     public void test_plusYears_positiveToNegative_crossCutover() {
103 |         LocalDate date = new LocalDate(2003, 6, 30, GJ_CHRONOLOGY);
104 |         LocalDate expected = new LocalDate(-2, 6, 30, GJ_CHRONOLOGY);
105 |         assertEquals(expected, date.plusYears(-2004));
106 |     }
```

## org.joda.time.chrono.TestGJDate.test_plusWeekyears_positiveToZero_crossCutover()
Resolved declaration: org.joda.time.chrono.TestGJDate.test_plusWeekyears_positiveToZero_crossCutover()
Source: src/test/java/org/joda/time/chrono/TestGJDate.java

```java
115 |     public void test_plusWeekyears_positiveToZero_crossCutover() {
116 |         LocalDate date = new LocalDate(2003, 6, 30, GJ_CHRONOLOGY);
117 |         LocalDate expected = new LocalDate(-1, 6, 30, GJ_CHRONOLOGY).withWeekOfWeekyear(date.getWeekOfWeekyear()).withDayOfWeek(date.getDayOfWeek());
118 |         assertEquals(expected, date.weekyear().addToCopy(-2003));
119 |     }
```
