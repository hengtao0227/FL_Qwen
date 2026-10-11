# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestMutableDateTime_Adds.testAddYears_int_dstOverlapWinter_addZero()
Resolved declaration: org.joda.time.TestMutableDateTime_Adds.testAddYears_int_dstOverlapWinter_addZero()
Source: src/test/java/org/joda/time/TestMutableDateTime_Adds.java

```java
222 |     public void testAddYears_int_dstOverlapWinter_addZero() {
223 |         MutableDateTime test = new MutableDateTime(2011, 10, 30, 2, 30, 0, 0, DateTimeZone.forID("Europe/Berlin"));
224 |         test.addHours(1);
225 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
226 |         test.addYears(0);
227 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
228 |     }
```

## org.joda.time.TestMutableDateTime_Adds.testAddDays_int_dstOverlapWinter_addZero()
Resolved declaration: org.joda.time.TestMutableDateTime_Adds.testAddDays_int_dstOverlapWinter_addZero()
Source: src/test/java/org/joda/time/TestMutableDateTime_Adds.java

```java
266 |     public void testAddDays_int_dstOverlapWinter_addZero() {
267 |         MutableDateTime test = new MutableDateTime(2011, 10, 30, 2, 30, 0, 0, DateTimeZone.forID("Europe/Berlin"));
268 |         test.addHours(1);
269 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
270 |         test.addDays(0);
271 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
272 |     }
```

## org.joda.time.TestMutableDateTime_Adds.testAddWeeks_int_dstOverlapWinter_addZero()
Resolved declaration: org.joda.time.TestMutableDateTime_Adds.testAddWeeks_int_dstOverlapWinter_addZero()
Source: src/test/java/org/joda/time/TestMutableDateTime_Adds.java

```java
295 |     public void testAddWeeks_int_dstOverlapWinter_addZero() {
296 |         MutableDateTime test = new MutableDateTime(2011, 10, 30, 2, 30, 0, 0, DateTimeZone.forID("Europe/Berlin"));
297 |         test.addHours(1);
298 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
299 |         test.addWeeks(0);
300 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
301 |     }
```

## org.joda.time.TestMutableDateTime_Adds.testAdd_DurationFieldType_int_dstOverlapWinter_addZero()
Resolved declaration: org.joda.time.TestMutableDateTime_Adds.testAdd_DurationFieldType_int_dstOverlapWinter_addZero()
Source: src/test/java/org/joda/time/TestMutableDateTime_Adds.java

```java
182 |     public void testAdd_DurationFieldType_int_dstOverlapWinter_addZero() {
183 |         MutableDateTime test = new MutableDateTime(2011, 10, 30, 2, 30, 0, 0, DateTimeZone.forID("Europe/Berlin"));
184 |         test.addHours(1);
185 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
186 |         test.add(DurationFieldType.years(), 0);
187 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
188 |     }
```

## org.joda.time.TestMutableDateTime_Adds.testAddMonths_int_dstOverlapWinter_addZero()
Resolved declaration: org.joda.time.TestMutableDateTime_Adds.testAddMonths_int_dstOverlapWinter_addZero()
Source: src/test/java/org/joda/time/TestMutableDateTime_Adds.java

```java
244 |     public void testAddMonths_int_dstOverlapWinter_addZero() {
245 |         MutableDateTime test = new MutableDateTime(2011, 10, 30, 2, 30, 0, 0, DateTimeZone.forID("Europe/Berlin"));
246 |         test.addHours(1);
247 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
248 |         test.addMonths(0);
249 |         assertEquals("2011-10-30T02:30:00.000+01:00", test.toString());
250 |     }
```
