# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.time.junit.TimePeriodValuesTests.testGetMaxMiddleIndex()
Resolved declaration: org.jfree.data.time.junit.TimePeriodValuesTests.testGetMaxMiddleIndex()
Source: tests/org/jfree/data/time/junit/TimePeriodValuesTests.java

```java
367 |     public void testGetMaxMiddleIndex() {
368 |         TimePeriodValues s = new TimePeriodValues("Test");
369 |         assertEquals(-1, s.getMaxMiddleIndex());
370 |         s.add(new SimpleTimePeriod(100L, 200L), 1.0);
371 |         assertEquals(0, s.getMaxMiddleIndex());
372 |         s.add(new SimpleTimePeriod(300L, 400L), 2.0);
373 |         assertEquals(1, s.getMaxMiddleIndex());
374 |         s.add(new SimpleTimePeriod(0L, 50L), 3.0);
375 |         assertEquals(1, s.getMaxMiddleIndex());
376 |         s.add(new SimpleTimePeriod(150L, 200L), 4.0);
377 |         assertEquals(1, s.getMaxMiddleIndex());
378 |     }
```
