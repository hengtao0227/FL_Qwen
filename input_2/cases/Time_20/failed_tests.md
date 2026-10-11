# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.format.TestDateTimeFormatterBuilder.test_printParseZoneDawsonCreek()
Resolved declaration: org.joda.time.format.TestDateTimeFormatterBuilder.test_printParseZoneDawsonCreek()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatterBuilder.java

```java
255 |     public void test_printParseZoneDawsonCreek() {  // clashes with shorter Dawson
256 |         DateTimeFormatterBuilder bld = new DateTimeFormatterBuilder()
257 |             .appendPattern("yyyy-MM-dd HH:mm ").appendTimeZoneId();
258 |         DateTimeFormatter f = bld.toFormatter();
259 |         
260 |         DateTime dt = new DateTime(2007, 3, 4, 12, 30, 0, DateTimeZone.forID("America/Dawson_Creek"));
261 |         assertEquals("2007-03-04 12:30 America/Dawson_Creek", f.print(dt));
262 |         assertEquals(dt, f.parseDateTime("2007-03-04 12:30 America/Dawson_Creek"));
263 |     }
```
