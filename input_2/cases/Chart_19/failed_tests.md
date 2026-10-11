# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.plot.junit.CategoryPlotTests.testGetRangeAxisIndex()
Resolved declaration: org.jfree.chart.plot.junit.CategoryPlotTests.testGetRangeAxisIndex()
Source: tests/org/jfree/chart/plot/junit/CategoryPlotTests.java

```java
741 |     public void testGetRangeAxisIndex() {
742 |         CategoryAxis domainAxis1 = new CategoryAxis("X1");
743 |         NumberAxis rangeAxis1 = new NumberAxis("Y1");
744 |         NumberAxis rangeAxis2 = new NumberAxis("Y2");
745 |         CategoryPlot plot = new CategoryPlot(null, domainAxis1, rangeAxis1, 
746 |                 null);
747 |         assertEquals(0, plot.getRangeAxisIndex(rangeAxis1));
748 |         assertEquals(-1, plot.getRangeAxisIndex(rangeAxis2));
749 |         plot.setRangeAxis(1, rangeAxis2);
750 |         assertEquals(1, plot.getRangeAxisIndex(rangeAxis2));
751 |         assertEquals(-1, plot.getRangeAxisIndex(new NumberAxis("Y2")));
752 |         boolean pass = false;
753 |         try {
754 |             plot.getRangeAxisIndex(null);
755 |         }
756 |         catch (IllegalArgumentException e) {
757 |             pass = true;
758 |         }
759 |         assertTrue(pass);
760 |     }
```

## org.jfree.chart.plot.junit.CategoryPlotTests.testGetDomainAxisIndex()
Resolved declaration: org.jfree.chart.plot.junit.CategoryPlotTests.testGetDomainAxisIndex()
Source: tests/org/jfree/chart/plot/junit/CategoryPlotTests.java

```java
717 |     public void testGetDomainAxisIndex() {
718 |         CategoryAxis domainAxis1 = new CategoryAxis("X1");
719 |         CategoryAxis domainAxis2 = new CategoryAxis("X2");
720 |         NumberAxis rangeAxis1 = new NumberAxis("Y1");
721 |         CategoryPlot plot = new CategoryPlot(null, domainAxis1, rangeAxis1, 
722 |                 null);
723 |         assertEquals(0, plot.getDomainAxisIndex(domainAxis1));
724 |         assertEquals(-1, plot.getDomainAxisIndex(domainAxis2));
725 |         plot.setDomainAxis(1, domainAxis2);
726 |         assertEquals(1, plot.getDomainAxisIndex(domainAxis2));
727 |         assertEquals(-1, plot.getDomainAxisIndex(new CategoryAxis("X2")));
728 |         boolean pass = false;
729 |         try {
730 |             plot.getDomainAxisIndex(null);
731 |         }
732 |         catch (IllegalArgumentException e) {
733 |             pass = true;
734 |         }
735 |         assertTrue(pass);
736 |     }
```
