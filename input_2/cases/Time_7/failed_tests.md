# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_feb29_newYork_startOfYear()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_feb29_newYork_startOfYear()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
929 |     public void testParseInto_monthDay_feb29_newYork_startOfYear() {
930 |         DateTimeFormatter f = DateTimeFormat.forPattern("M d").withLocale(Locale.UK);
931 |         MutableDateTime result = new MutableDateTime(2004, 1, 1, 0, 0, 0, 0, NEWYORK);
932 |         assertEquals(4, f.parseInto(result, "2 29", 0));
933 |         assertEquals(new MutableDateTime(2004, 2, 29, 0, 0, 0, 0, NEWYORK), result);
934 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_feb29_tokyo_endOfYear()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_feb29_tokyo_endOfYear()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
957 |     public void testParseInto_monthDay_feb29_tokyo_endOfYear() {
958 |         DateTimeFormatter f = DateTimeFormat.forPattern("M d").withLocale(Locale.UK);
959 |         MutableDateTime result = new MutableDateTime(2004, 12, 31, 23, 59, 59, 999, TOKYO);
960 |         assertEquals(4, f.parseInto(result, "2 29", 0));
961 |         assertEquals(new MutableDateTime(2004, 2, 29, 23, 59, 59, 999, TOKYO), result);
962 |     }
```
