# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDuration_Basics.testToPeriod_fixedZone()
Resolved declaration: org.joda.time.TestDuration_Basics.testToPeriod_fixedZone()
Source: src/test/java/org/joda/time/TestDuration_Basics.java

```java
470 |     public void testToPeriod_fixedZone() throws Throwable {
471 |         DateTimeZone zone = DateTimeZone.getDefault();
472 |         try {
473 |             DateTimeZone.setDefault(DateTimeZone.forOffsetHours(2));
474 |             long length =
475 |                 (4L + (3L * 7L) + (2L * 30L) + 365L) * DateTimeConstants.MILLIS_PER_DAY +
476 |                 5L * DateTimeConstants.MILLIS_PER_HOUR +
477 |                 6L * DateTimeConstants.MILLIS_PER_MINUTE +
478 |                 7L * DateTimeConstants.MILLIS_PER_SECOND + 8L;
479 |             Duration dur = new Duration(length);
480 |             Period test = dur.toPeriod();
481 |             assertEquals(0, test.getYears());  // (4 + (3 * 7) + (2 * 30) + 365) == 450
482 |             assertEquals(0, test.getMonths());
483 |             assertEquals(0, test.getWeeks());
484 |             assertEquals(0, test.getDays());
485 |             assertEquals((450 * 24) + 5, test.getHours());
486 |             assertEquals(6, test.getMinutes());
487 |             assertEquals(7, test.getSeconds());
488 |             assertEquals(8, test.getMillis());
489 |         } finally {
490 |             DateTimeZone.setDefault(zone);
491 |         }
492 |     }
```

## org.joda.time.TestPeriod_Constructors.testConstructor_long_fixedZone()
Resolved declaration: org.joda.time.TestPeriod_Constructors.testConstructor_long_fixedZone()
Source: src/test/java/org/joda/time/TestPeriod_Constructors.java

```java
174 |     public void testConstructor_long_fixedZone() throws Throwable {
175 |         DateTimeZone zone = DateTimeZone.getDefault();
176 |         try {
177 |             DateTimeZone.setDefault(DateTimeZone.forOffsetHours(2));
178 |             long length =
179 |                 (4L + (3L * 7L) + (2L * 30L) + 365L) * DateTimeConstants.MILLIS_PER_DAY +
180 |                 5L * DateTimeConstants.MILLIS_PER_HOUR +
181 |                 6L * DateTimeConstants.MILLIS_PER_MINUTE +
182 |                 7L * DateTimeConstants.MILLIS_PER_SECOND + 8L;
183 |             Period test = new Period(length);
184 |             assertEquals(PeriodType.standard(), test.getPeriodType());
185 |             // only time fields are precise in AllType
186 |             assertEquals(0, test.getYears());  // (4 + (3 * 7) + (2 * 30) + 365) == 450
187 |             assertEquals(0, test.getMonths());
188 |             assertEquals(0, test.getWeeks());
189 |             assertEquals(0, test.getDays());
190 |             assertEquals((450 * 24) + 5, test.getHours());
191 |             assertEquals(6, test.getMinutes());
192 |             assertEquals(7, test.getSeconds());
193 |             assertEquals(8, test.getMillis());
194 |         } finally {
195 |             DateTimeZone.setDefault(zone);
196 |         }
197 |     }
```
