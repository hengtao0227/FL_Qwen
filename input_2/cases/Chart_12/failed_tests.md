# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.plot.junit.MultiplePiePlotTests.testConstructor()
Resolved declaration: org.jfree.chart.plot.junit.MultiplePiePlotTests.testConstructor()
Source: tests/org/jfree/chart/plot/junit/MultiplePiePlotTests.java

```java
104 |     public void testConstructor() {
105 |     	MultiplePiePlot plot = new MultiplePiePlot();
106 |     	assertNull(plot.getDataset());
107 | 
108 |     	// the following checks that the plot registers itself as a listener
109 |     	// with the dataset passed to the constructor - see patch 1943021
110 |     	DefaultCategoryDataset dataset = new DefaultCategoryDataset();
111 |     	plot = new MultiplePiePlot(dataset);
112 |     	assertTrue(dataset.hasListener(plot));
113 |     }
```
