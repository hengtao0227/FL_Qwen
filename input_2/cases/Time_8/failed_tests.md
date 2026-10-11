# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZone.testForOffsetHoursMinutes_int_int()
Resolved declaration: org.joda.time.TestDateTimeZone.testForOffsetHoursMinutes_int_int()
Source: src/test/java/org/joda/time/TestDateTimeZone.java

```java
303 |     public void testForOffsetHoursMinutes_int_int() {
304 |         assertEquals(DateTimeZone.UTC, DateTimeZone.forOffsetHoursMinutes(0, 0));
305 |         assertEquals(DateTimeZone.forID("+23:59"), DateTimeZone.forOffsetHoursMinutes(23, 59));
306 |         
307 |         assertEquals(DateTimeZone.forID("+02:15"), DateTimeZone.forOffsetHoursMinutes(2, 15));
308 |         assertEquals(DateTimeZone.forID("+02:00"), DateTimeZone.forOffsetHoursMinutes(2, 0));
309 |         try {
310 |             DateTimeZone.forOffsetHoursMinutes(2, -15);
311 |             fail();
312 |         } catch (IllegalArgumentException ex) {}
313 |         
314 |         assertEquals(DateTimeZone.forID("+00:15"), DateTimeZone.forOffsetHoursMinutes(0, 15));
315 |         assertEquals(DateTimeZone.forID("+00:00"), DateTimeZone.forOffsetHoursMinutes(0, 0));
316 |         assertEquals(DateTimeZone.forID("-00:15"), DateTimeZone.forOffsetHoursMinutes(0, -15));
317 |         
318 |         assertEquals(DateTimeZone.forID("-02:00"), DateTimeZone.forOffsetHoursMinutes(-2, 0));
319 |         assertEquals(DateTimeZone.forID("-02:15"), DateTimeZone.forOffsetHoursMinutes(-2, -15));
320 |         assertEquals(DateTimeZone.forID("-02:15"), DateTimeZone.forOffsetHoursMinutes(-2, 15));
321 |         
322 |         assertEquals(DateTimeZone.forID("-23:59"), DateTimeZone.forOffsetHoursMinutes(-23, 59));
323 |         try {
324 |             DateTimeZone.forOffsetHoursMinutes(2, 60);
325 |             fail();
326 |         } catch (IllegalArgumentException ex) {}
327 |         try {
328 |             DateTimeZone.forOffsetHoursMinutes(-2, 60);
329 |             fail();
330 |         } catch (IllegalArgumentException ex) {}
331 |         try {
332 |             DateTimeZone.forOffsetHoursMinutes(24, 0);
333 |             fail();
334 |         } catch (IllegalArgumentException ex) {}
335 |         try {
336 |             DateTimeZone.forOffsetHoursMinutes(-24, 0);
337 |             fail();
338 |         } catch (IllegalArgumentException ex) {}
339 |     }        
```
