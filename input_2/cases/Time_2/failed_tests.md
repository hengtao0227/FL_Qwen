# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestPartial_Basics.testWith_baseAndArgHaveNoRange()
Resolved declaration: org.joda.time.TestPartial_Basics.testWith_baseAndArgHaveNoRange()
Source: src/test/java/org/joda/time/TestPartial_Basics.java

```java
467 |     public void testWith_baseAndArgHaveNoRange() {
468 |         Partial test = new Partial(DateTimeFieldType.year(), 1);
469 |         Partial result = test.with(DateTimeFieldType.era(), 1);
470 |         assertEquals(2, result.size());
471 |         assertEquals(0, result.indexOf(DateTimeFieldType.era()));
472 |         assertEquals(1, result.indexOf(DateTimeFieldType.year()));
473 |     }
```
