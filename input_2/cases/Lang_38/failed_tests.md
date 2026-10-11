# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.time.FastDateFormatTest.testLang538()
Resolved declaration: org.apache.commons.lang3.time.FastDateFormatTest.testLang538()
Source: src/test/org/apache/commons/lang3/time/FastDateFormatTest.java

```java
337 |     public void testLang538() {
338 |         final String dateTime = "2009-10-16T16:42:16.000Z";
339 | 
340 |         // more commonly constructed with: cal = new GregorianCalendar(2009, 9, 16, 8, 42, 16)
341 |         // for the unit test to work in any time zone, constructing with GMT-8 rather than default locale time zone
342 |         GregorianCalendar cal = new GregorianCalendar(TimeZone.getTimeZone("GMT-8"));
343 |         cal.clear();
344 |         cal.set(2009, 9, 16, 8, 42, 16);
345 | 
346 |         FastDateFormat format = FastDateFormat.getInstance("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'", TimeZone.getTimeZone("GMT"));
347 |         assertEquals("dateTime", dateTime, format.format(cal));
348 |     }
```
