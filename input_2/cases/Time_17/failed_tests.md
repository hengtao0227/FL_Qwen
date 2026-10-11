# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZoneCutover.testBug3476684_adjustOffset()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testBug3476684_adjustOffset()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1249 |     public void testBug3476684_adjustOffset() {
1250 |         final DateTimeZone zone = DateTimeZone.forID("America/Sao_Paulo");
1251 |         DateTime base = new DateTime(2012, 2, 25, 22, 15, zone);
1252 |         DateTime baseBefore = base.plusHours(1);  // 23:15 (first)
1253 |         DateTime baseAfter = base.plusHours(2);  // 23:15 (second)
1254 |         
1255 |         assertSame(base, base.withEarlierOffsetAtOverlap());
1256 |         assertSame(base, base.withLaterOffsetAtOverlap());
1257 |         
1258 |         assertSame(baseBefore, baseBefore.withEarlierOffsetAtOverlap());
1259 |         assertEquals(baseAfter, baseBefore.withLaterOffsetAtOverlap());
1260 |         
1261 |         assertSame(baseAfter, baseAfter.withLaterOffsetAtOverlap());
1262 |         assertEquals(baseBefore, baseAfter.withEarlierOffsetAtOverlap());
1263 |     }
```
