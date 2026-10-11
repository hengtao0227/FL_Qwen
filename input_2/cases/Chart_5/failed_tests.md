# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.xy.junit.XYSeriesTests.testBug1955483()
Resolved declaration: org.jfree.data.xy.junit.XYSeriesTests.testBug1955483()
Source: tests/org/jfree/data/xy/junit/XYSeriesTests.java

```java
476 |     public void testBug1955483() {
477 |         XYSeries series = new XYSeries("Series", true, true);
478 |         series.addOrUpdate(1.0, 1.0);
479 |         series.addOrUpdate(1.0, 2.0);
480 |         assertEquals(new Double(1.0), series.getY(0));
481 |         assertEquals(new Double(2.0), series.getY(1));
482 |         assertEquals(2, series.getItemCount());
483 |     }
```
