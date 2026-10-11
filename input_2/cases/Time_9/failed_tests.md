# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZone.testForOffsetHoursMinutes_int_int()
Resolved declaration: org.joda.time.TestDateTimeZone.testForOffsetHoursMinutes_int_int()
Source: src/test/java/org/joda/time/TestDateTimeZone.java

```java
303 |     public void testForOffsetHoursMinutes_int_int() {
304 |         assertEquals(DateTimeZone.UTC, DateTimeZone.forOffsetHoursMinutes(0, 0));
305 |         assertEquals(DateTimeZone.forID("+23:59"), DateTimeZone.forOffsetHoursMinutes(23, 59));
306 |         assertEquals(DateTimeZone.forID("+03:15"), DateTimeZone.forOffsetHoursMinutes(3, 15));
307 |         assertEquals(DateTimeZone.forID("-02:00"), DateTimeZone.forOffsetHoursMinutes(-2, 0));
308 |         assertEquals(DateTimeZone.forID("-02:30"), DateTimeZone.forOffsetHoursMinutes(-2, 30));
309 |         assertEquals(DateTimeZone.forID("-23:59"), DateTimeZone.forOffsetHoursMinutes(-23, 59));
310 |         try {
311 |             DateTimeZone.forOffsetHoursMinutes(2, 60);
312 |             fail();
313 |         } catch (IllegalArgumentException ex) {}
314 |         try {
315 |             DateTimeZone.forOffsetHoursMinutes(-2, 60);
316 |             fail();
317 |         } catch (IllegalArgumentException ex) {}
318 |         try {
319 |             DateTimeZone.forOffsetHoursMinutes(2, -1);
320 |             fail();
321 |         } catch (IllegalArgumentException ex) {}
322 |         try {
323 |             DateTimeZone.forOffsetHoursMinutes(-2, -1);
324 |             fail();
325 |         } catch (IllegalArgumentException ex) {}
326 |         try {
327 |             DateTimeZone.forOffsetHoursMinutes(24, 0);
328 |             fail();
329 |         } catch (IllegalArgumentException ex) {}
330 |         try {
331 |             DateTimeZone.forOffsetHoursMinutes(-24, 0);
332 |             fail();
333 |         } catch (IllegalArgumentException ex) {}
334 |     }        
```
