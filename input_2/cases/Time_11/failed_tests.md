# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.tz.TestCompiler.testDateTimeZoneBuilder()
Resolved declaration: org.joda.time.tz.TestCompiler.testDateTimeZoneBuilder()
Source: src/test/java/org/joda/time/tz/TestCompiler.java

```java
88 |     public void testDateTimeZoneBuilder() throws Exception {
89 |         // test multithreading, issue #18
90 |         getTestDataTimeZoneBuilder().toDateTimeZone("TestDTZ1", true);
91 |         final DateTimeZone[] zone = new DateTimeZone[1];
92 |         Thread t = new Thread(new Runnable() {
93 |             public void run() {
94 |                 zone[0] = getTestDataTimeZoneBuilder().toDateTimeZone("TestDTZ2", true);
95 |             }
96 |         });
97 |         t.start();
98 |         t.join();
99 |         assertNotNull(zone[0]);
100 |     }
```
