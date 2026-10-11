# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZoneCutover.testDateTimeCreation_london()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testDateTimeCreation_london()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1263 |     public void testDateTimeCreation_london() {
1264 |         DateTimeZone zone = DateTimeZone.forID("Europe/London");
1265 |         DateTime base = new DateTime(2011, 10, 30, 1, 15, zone);
1266 |         assertEquals("2011-10-30T01:15:00.000+01:00", base.toString());
1267 |         assertEquals("2011-10-30T01:15:00.000Z", base.plusHours(1).toString());
1268 |     }
```
