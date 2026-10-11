# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.time.StopWatchTest.testLang315()
Resolved declaration: org.apache.commons.lang.time.StopWatchTest.testLang315()
Source: src/test/org/apache/commons/lang/time/StopWatchTest.java

```java
111 |     public void testLang315() {
112 |         StopWatch watch = new StopWatch();
113 |         watch.start();
114 |             try {Thread.sleep(200);} catch (InterruptedException ex) {}
115 |         watch.suspend();
116 |         long suspendTime = watch.getTime();
117 |             try {Thread.sleep(200);} catch (InterruptedException ex) {}
118 |         watch.stop();
119 |         long totalTime = watch.getTime();
120 |         assertTrue( suspendTime == totalTime );
121 |     }
```
