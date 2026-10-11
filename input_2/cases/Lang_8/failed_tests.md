# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.time.FastDateFormat_PrinterTest.testCalendarTimezoneRespected()
Resolved declaration: org.apache.commons.lang3.time.FastDatePrinterTest.testCalendarTimezoneRespected()
Source: src/test/java/org/apache/commons/lang3/time/FastDatePrinterTest.java

```java
265 |     @Test
266 |     public void testCalendarTimezoneRespected() {
267 |         String[] availableZones = TimeZone.getAvailableIDs();
268 |         TimeZone currentZone = TimeZone.getDefault();
269 |         
270 |         TimeZone anotherZone = null;
271 |         for (String zone : availableZones) {
272 |             if (!zone.equals(currentZone.getID())) {
273 |                 anotherZone = TimeZone.getTimeZone(zone);
274 |             }
275 |         }
276 |         
277 |         assertNotNull("Cannot find another timezone", anotherZone);
278 |         
279 |         final String pattern = "h:mma z";
280 |         final Calendar cal = Calendar.getInstance(anotherZone);
281 |         
282 |         SimpleDateFormat sdf = new SimpleDateFormat(pattern);
283 |         sdf.setTimeZone(anotherZone);
284 |         String expectedValue = sdf.format(cal.getTime());
285 |         String actualValue = FastDateFormat.getInstance(pattern).format(cal);
286 |         assertEquals(expectedValue, actualValue);
287 |     }
```

## org.apache.commons.lang3.time.FastDatePrinterTest.testCalendarTimezoneRespected()
Resolved declaration: org.apache.commons.lang3.time.FastDatePrinterTest.testCalendarTimezoneRespected()
Source: src/test/java/org/apache/commons/lang3/time/FastDatePrinterTest.java

```java
265 |     @Test
266 |     public void testCalendarTimezoneRespected() {
267 |         String[] availableZones = TimeZone.getAvailableIDs();
268 |         TimeZone currentZone = TimeZone.getDefault();
269 |         
270 |         TimeZone anotherZone = null;
271 |         for (String zone : availableZones) {
272 |             if (!zone.equals(currentZone.getID())) {
273 |                 anotherZone = TimeZone.getTimeZone(zone);
274 |             }
275 |         }
276 |         
277 |         assertNotNull("Cannot find another timezone", anotherZone);
278 |         
279 |         final String pattern = "h:mma z";
280 |         final Calendar cal = Calendar.getInstance(anotherZone);
281 |         
282 |         SimpleDateFormat sdf = new SimpleDateFormat(pattern);
283 |         sdf.setTimeZone(anotherZone);
284 |         String expectedValue = sdf.format(cal.getTime());
285 |         String actualValue = FastDateFormat.getInstance(pattern).format(cal);
286 |         assertEquals(expectedValue, actualValue);
287 |     }
```
