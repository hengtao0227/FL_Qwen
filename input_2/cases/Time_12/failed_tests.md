# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestLocalDateTime_Constructors.testFactory_fromDateFields_beforeYearZero1()
Resolved declaration: org.joda.time.TestLocalDateTime_Constructors.testFactory_fromDateFields_beforeYearZero1()
Source: src/test/java/org/joda/time/TestLocalDateTime_Constructors.java

```java
150 |     public void testFactory_fromDateFields_beforeYearZero1() throws Exception {
151 |         GregorianCalendar cal = new GregorianCalendar(1, 1, 3, 4, 5, 6);
152 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
153 |         cal.set(Calendar.MILLISECOND, 7);
154 |         LocalDateTime expected = new LocalDateTime(0, 2, 3, 4, 5, 6, 7);
155 |         assertEquals(expected, LocalDateTime.fromDateFields(cal.getTime()));
156 |     }
```

## org.joda.time.TestLocalDateTime_Constructors.testFactory_fromDateFields_beforeYearZero3()
Resolved declaration: org.joda.time.TestLocalDateTime_Constructors.testFactory_fromDateFields_beforeYearZero3()
Source: src/test/java/org/joda/time/TestLocalDateTime_Constructors.java

```java
158 |     public void testFactory_fromDateFields_beforeYearZero3() throws Exception {
159 |         GregorianCalendar cal = new GregorianCalendar(3, 1, 3, 4, 5, 6);
160 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
161 |         cal.set(Calendar.MILLISECOND, 7);
162 |         LocalDateTime expected = new LocalDateTime(-2, 2, 3, 4, 5, 6, 7);
163 |         assertEquals(expected, LocalDateTime.fromDateFields(cal.getTime()));
164 |     }
```

## org.joda.time.TestLocalDateTime_Constructors.testFactory_fromCalendarFields_beforeYearZero1()
Resolved declaration: org.joda.time.TestLocalDateTime_Constructors.testFactory_fromCalendarFields_beforeYearZero1()
Source: src/test/java/org/joda/time/TestLocalDateTime_Constructors.java

```java
112 |     public void testFactory_fromCalendarFields_beforeYearZero1() throws Exception {
113 |         GregorianCalendar cal = new GregorianCalendar(1, 1, 3, 4, 5, 6);
114 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
115 |         cal.set(Calendar.MILLISECOND, 7);
116 |         LocalDateTime expected = new LocalDateTime(0, 2, 3, 4, 5, 6, 7);
117 |         assertEquals(expected, LocalDateTime.fromCalendarFields(cal));
118 |     }
```

## org.joda.time.TestLocalDateTime_Constructors.testFactory_fromCalendarFields_beforeYearZero3()
Resolved declaration: org.joda.time.TestLocalDateTime_Constructors.testFactory_fromCalendarFields_beforeYearZero3()
Source: src/test/java/org/joda/time/TestLocalDateTime_Constructors.java

```java
120 |     public void testFactory_fromCalendarFields_beforeYearZero3() throws Exception {
121 |         GregorianCalendar cal = new GregorianCalendar(3, 1, 3, 4, 5, 6);
122 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
123 |         cal.set(Calendar.MILLISECOND, 7);
124 |         LocalDateTime expected = new LocalDateTime(-2, 2, 3, 4, 5, 6, 7);
125 |         assertEquals(expected, LocalDateTime.fromCalendarFields(cal));
126 |     }
```

## org.joda.time.TestLocalDate_Constructors.testFactory_fromDateFields_beforeYearZero1()
Resolved declaration: org.joda.time.TestLocalDate_Constructors.testFactory_fromDateFields_beforeYearZero1()
Source: src/test/java/org/joda/time/TestLocalDate_Constructors.java

```java
142 |     public void testFactory_fromDateFields_beforeYearZero1() throws Exception {
143 |         GregorianCalendar cal = new GregorianCalendar(1, 1, 3, 4, 5, 6);
144 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
145 |         cal.set(Calendar.MILLISECOND, 7);
146 |         LocalDate expected = new LocalDate(0, 2, 3);
147 |         assertEquals(expected, LocalDate.fromDateFields(cal.getTime()));
148 |     }
```

## org.joda.time.TestLocalDate_Constructors.testFactory_fromDateFields_beforeYearZero3()
Resolved declaration: org.joda.time.TestLocalDate_Constructors.testFactory_fromDateFields_beforeYearZero3()
Source: src/test/java/org/joda/time/TestLocalDate_Constructors.java

```java
150 |     public void testFactory_fromDateFields_beforeYearZero3() throws Exception {
151 |         GregorianCalendar cal = new GregorianCalendar(3, 1, 3, 4, 5, 6);
152 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
153 |         cal.set(Calendar.MILLISECOND, 7);
154 |         LocalDate expected = new LocalDate(-2, 2, 3);
155 |         assertEquals(expected, LocalDate.fromDateFields(cal.getTime()));
156 |     }
```

## org.joda.time.TestLocalDate_Constructors.testFactory_fromCalendarFields_beforeYearZero1()
Resolved declaration: org.joda.time.TestLocalDate_Constructors.testFactory_fromCalendarFields_beforeYearZero1()
Source: src/test/java/org/joda/time/TestLocalDate_Constructors.java

```java
104 |     public void testFactory_fromCalendarFields_beforeYearZero1() throws Exception {
105 |         GregorianCalendar cal = new GregorianCalendar(1, 1, 3, 4, 5, 6);
106 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
107 |         cal.set(Calendar.MILLISECOND, 7);
108 |         LocalDate expected = new LocalDate(0, 2, 3);
109 |         assertEquals(expected, LocalDate.fromCalendarFields(cal));
110 |     }
```

## org.joda.time.TestLocalDate_Constructors.testFactory_fromCalendarFields_beforeYearZero3()
Resolved declaration: org.joda.time.TestLocalDate_Constructors.testFactory_fromCalendarFields_beforeYearZero3()
Source: src/test/java/org/joda/time/TestLocalDate_Constructors.java

```java
112 |     public void testFactory_fromCalendarFields_beforeYearZero3() throws Exception {
113 |         GregorianCalendar cal = new GregorianCalendar(3, 1, 3, 4, 5, 6);
114 |         cal.set(Calendar.ERA, GregorianCalendar.BC);
115 |         cal.set(Calendar.MILLISECOND, 7);
116 |         LocalDate expected = new LocalDate(-2, 2, 3);
117 |         assertEquals(expected, LocalDate.fromCalendarFields(cal));
118 |     }
```
