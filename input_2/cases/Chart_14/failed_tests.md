# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.plot.junit.CategoryPlotTests.testRemoveRangeMarker()
Resolved declaration: org.jfree.chart.plot.junit.CategoryPlotTests.testRemoveRangeMarker()
Source: tests/org/jfree/chart/plot/junit/CategoryPlotTests.java

```java
778 |     public void testRemoveRangeMarker() {
779 |     	CategoryPlot plot = new CategoryPlot();
780 |     	assertFalse(plot.removeRangeMarker(new ValueMarker(0.5)));
781 |     }
```

## org.jfree.chart.plot.junit.CategoryPlotTests.testRemoveDomainMarker()
Resolved declaration: org.jfree.chart.plot.junit.CategoryPlotTests.testRemoveDomainMarker()
Source: tests/org/jfree/chart/plot/junit/CategoryPlotTests.java

```java
769 |     public void testRemoveDomainMarker() {
770 |     	CategoryPlot plot = new CategoryPlot();
771 |     	assertFalse(plot.removeDomainMarker(new CategoryMarker("Category 1")));
772 |     }
```

## org.jfree.chart.plot.junit.XYPlotTests.testRemoveRangeMarker()
Resolved declaration: org.jfree.chart.plot.junit.XYPlotTests.testRemoveRangeMarker()
Source: tests/org/jfree/chart/plot/junit/XYPlotTests.java

```java
1035 |     public void testRemoveRangeMarker() {
1036 |     	XYPlot plot = new XYPlot();
1037 |     	assertFalse(plot.removeRangeMarker(new ValueMarker(0.5)));
1038 |     }
```

## org.jfree.chart.plot.junit.XYPlotTests.testRemoveDomainMarker()
Resolved declaration: org.jfree.chart.plot.junit.XYPlotTests.testRemoveDomainMarker()
Source: tests/org/jfree/chart/plot/junit/XYPlotTests.java

```java
1026 |     public void testRemoveDomainMarker() {
1027 |     	XYPlot plot = new XYPlot();
1028 |     	assertFalse(plot.removeDomainMarker(new ValueMarker(0.5)));
1029 |     }
```
