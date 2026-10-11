# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestPartial_Basics.testWith3()
Resolved declaration: org.joda.time.TestPartial_Basics.testWith3()
Source: src/test/java/org/joda/time/TestPartial_Basics.java

```java
360 |     public void testWith3() {
361 |         Partial test = createHourMinPartial();
362 |         try {
363 |             test.with(DateTimeFieldType.clockhourOfDay(), 6);
364 |             fail();
365 |         } catch (IllegalArgumentException ex) {}
366 |         check(test, 10, 20);
367 |     }
```
