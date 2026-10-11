# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.axis.junit.LogAxisTests.testXYAutoRange1()
Resolved declaration: org.jfree.chart.axis.junit.LogAxisTests.testXYAutoRange1()
Source: tests/org/jfree/chart/axis/junit/LogAxisTests.java

```java
253 |     public void testXYAutoRange1() {
254 |         XYSeries series = new XYSeries("Series 1");
255 |         series.add(1.0, 1.0);
256 |         series.add(2.0, 2.0);
257 |         series.add(3.0, 3.0);
258 |         XYSeriesCollection dataset = new XYSeriesCollection();
259 |         dataset.addSeries(series);
260 |         JFreeChart chart = ChartFactory.createScatterPlot(
261 |             "Test",
262 |             "X",
263 |             "Y",
264 |             dataset,
265 |             PlotOrientation.VERTICAL,
266 |             false,
267 |             false,
268 |             false
269 |         );
270 |         XYPlot plot = (XYPlot) chart.getPlot();
271 |         LogAxis axis = new LogAxis("Log(Y)");
272 |         plot.setRangeAxis(axis);
273 |         assertEquals(0.9465508226401592, axis.getLowerBound(), EPSILON);
274 |         assertEquals(3.1694019256486126, axis.getUpperBound(), EPSILON);
275 |     }
```

## org.jfree.chart.axis.junit.LogAxisTests.testXYAutoRange2()
Resolved declaration: org.jfree.chart.axis.junit.LogAxisTests.testXYAutoRange2()
Source: tests/org/jfree/chart/axis/junit/LogAxisTests.java

```java
281 |     public void testXYAutoRange2() {
282 |         XYSeries series = new XYSeries("Series 1");
283 |         series.add(1.0, 1.0);
284 |         series.add(2.0, 2.0);
285 |         series.add(3.0, 3.0);
286 |         XYSeriesCollection dataset = new XYSeriesCollection();
287 |         dataset.addSeries(series);
288 |         JFreeChart chart = ChartFactory.createScatterPlot(
289 |             "Test",
290 |             "X",
291 |             "Y",
292 |             dataset,
293 |             PlotOrientation.VERTICAL,
294 |             false,
295 |             false,
296 |             false
297 |         );
298 |         XYPlot plot = (XYPlot) chart.getPlot();
299 |         LogAxis axis = new LogAxis("Log(Y)");
300 |         plot.setRangeAxis(axis);
301 |         assertEquals(0.9465508226401592, axis.getLowerBound(), EPSILON);
302 |         assertEquals(3.1694019256486126, axis.getUpperBound(), EPSILON);
303 |     }
```

## org.jfree.chart.axis.junit.NumberAxisTests.testXYAutoRange1()
Resolved declaration: org.jfree.chart.axis.junit.NumberAxisTests.testXYAutoRange1()
Source: tests/org/jfree/chart/axis/junit/NumberAxisTests.java

```java
347 |     public void testXYAutoRange1() {
348 |         XYSeries series = new XYSeries("Series 1");
349 |         series.add(1.0, 1.0);
350 |         series.add(2.0, 2.0);
351 |         series.add(3.0, 3.0);
352 |         XYSeriesCollection dataset = new XYSeriesCollection();
353 |         dataset.addSeries(series);
354 |         JFreeChart chart = ChartFactory.createScatterPlot(
355 |             "Test",
356 |             "X",
357 |             "Y",
358 |             dataset,
359 |             PlotOrientation.VERTICAL,
360 |             false,
361 |             false,
362 |             false
363 |         );
364 |         XYPlot plot = (XYPlot) chart.getPlot();
365 |         NumberAxis axis = (NumberAxis) plot.getDomainAxis();
366 |         axis.setAutoRangeIncludesZero(false);
367 |         assertEquals(0.9, axis.getLowerBound(), EPSILON);
368 |         assertEquals(3.1, axis.getUpperBound(), EPSILON);
369 |     }
```

## org.jfree.chart.axis.junit.NumberAxisTests.testXYAutoRange2()
Resolved declaration: org.jfree.chart.axis.junit.NumberAxisTests.testXYAutoRange2()
Source: tests/org/jfree/chart/axis/junit/NumberAxisTests.java

```java
375 |     public void testXYAutoRange2() {
376 |         XYSeries series = new XYSeries("Series 1");
377 |         series.add(1.0, 1.0);
378 |         series.add(2.0, 2.0);
379 |         series.add(3.0, 3.0);
380 |         XYSeriesCollection dataset = new XYSeriesCollection();
381 |         dataset.addSeries(series);
382 |         JFreeChart chart = ChartFactory.createScatterPlot(
383 |             "Test",
384 |             "X",
385 |             "Y",
386 |             dataset,
387 |             PlotOrientation.VERTICAL,
388 |             false,
389 |             false,
390 |             false
391 |         );
392 |         XYPlot plot = (XYPlot) chart.getPlot();
393 |         NumberAxis axis = (NumberAxis) plot.getRangeAxis();
394 |         axis.setAutoRangeIncludesZero(false);
395 |         assertEquals(0.9, axis.getLowerBound(), EPSILON);
396 |         assertEquals(3.1, axis.getUpperBound(), EPSILON);
397 |     }
```

## org.jfree.chart.axis.junit.ValueAxisTests.testAxisMargins()
Resolved declaration: org.jfree.chart.axis.junit.ValueAxisTests.testAxisMargins()
Source: tests/org/jfree/chart/axis/junit/ValueAxisTests.java

```java
228 |     public void testAxisMargins() {
229 |         XYSeries series = new XYSeries("S1");
230 |         series.add(100.0, 1.1);
231 |         series.add(200.0, 2.2);
232 |         XYSeriesCollection dataset = new XYSeriesCollection(series);
233 |         dataset.setIntervalWidth(0.0);
234 |         JFreeChart chart = ChartFactory.createScatterPlot(
235 |             "Title", "X", "Y", dataset, PlotOrientation.VERTICAL,
236 |             false, false, false
237 |         );
238 |         ValueAxis domainAxis = ((XYPlot) chart.getPlot()).getDomainAxis();
239 |         Range r = domainAxis.getRange();
240 |         assertEquals(110.0, r.getLength(), EPSILON);
241 |         domainAxis.setLowerMargin(0.10);
242 |         domainAxis.setUpperMargin(0.10);
243 |         r = domainAxis.getRange();
244 |         assertEquals(120.0, r.getLength(), EPSILON);
245 |     }
```

## org.jfree.chart.junit.JFreeChartTests.testSerialization4()
Resolved declaration: org.jfree.chart.junit.JFreeChartTests.testSerialization4()
Source: tests/org/jfree/chart/junit/JFreeChartTests.java

```java
438 |     public void testSerialization4() {
439 | 
440 |         RegularTimePeriod t = new Day();
441 |         TimeSeries series = new TimeSeries("Series 1");
442 |         series.add(t, 36.4);
443 |         t = t.next();
444 |         series.add(t, 63.5);
445 |         TimeSeriesCollection dataset = new TimeSeriesCollection();
446 |         dataset.addSeries(series);
447 | 
448 |         JFreeChart c1 = ChartFactory.createTimeSeriesChart("Test", "Date",
449 |                 "Value", dataset, true, true, true);
450 |         JFreeChart c2 = null;
451 | 
452 |         try {
453 |             ByteArrayOutputStream buffer = new ByteArrayOutputStream();
454 |             ObjectOutput out = new ObjectOutputStream(buffer);
455 |             out.writeObject(c1);
456 |             out.close();
457 | 
458 |             ObjectInput in = new ObjectInputStream(new ByteArrayInputStream(
459 |                     buffer.toByteArray()));
460 |             c2 = (JFreeChart) in.readObject();
461 |             in.close();
462 |         }
463 |         catch (Exception e) {
464 |             e.printStackTrace();
465 |         }
466 |         assertEquals(c1, c2);
467 | 
468 |     }
```

## org.jfree.chart.junit.ScatterPlotTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.ScatterPlotTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/ScatterPlotTests.java

```java
105 |     public void testDrawWithNullInfo() {
106 | 
107 |         boolean success = false;
108 | 
109 |         try {
110 |             BufferedImage image = new BufferedImage(200 , 100,
111 |                     BufferedImage.TYPE_INT_RGB);
112 |             Graphics2D g2 = image.createGraphics();
113 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null,
114 |                     null);
115 |             g2.dispose();
116 |             success = true;
117 |         }
118 |         catch (Exception e) {
119 |           success = false;
120 |           e.printStackTrace();
121 |         }
122 | 
123 |         assertTrue(success);
124 | 
125 |     }
```

## org.jfree.chart.junit.ScatterPlotTests.testSetSeriesToolTipGenerator()
Resolved declaration: org.jfree.chart.junit.ScatterPlotTests.testSetSeriesToolTipGenerator()
Source: tests/org/jfree/chart/junit/ScatterPlotTests.java

```java
157 |     public void testSetSeriesToolTipGenerator() {
158 |         XYPlot plot = (XYPlot) this.chart.getPlot();
159 |         XYItemRenderer renderer = plot.getRenderer();
160 |         StandardXYToolTipGenerator tt = new StandardXYToolTipGenerator();
161 |         renderer.setSeriesToolTipGenerator(0, tt);
162 |         XYToolTipGenerator tt2 = renderer.getToolTipGenerator(0, 0, false);
163 |         assertTrue(tt2 == tt);
164 |     }
```

## org.jfree.chart.junit.ScatterPlotTests.testReplaceDataset()
Resolved declaration: org.jfree.chart.junit.ScatterPlotTests.testReplaceDataset()
Source: tests/org/jfree/chart/junit/ScatterPlotTests.java

```java
130 |     public void testReplaceDataset() {
131 | 
132 |         // create a dataset...
133 |         XYSeries series1 = new XYSeries("Series 1");
134 |         series1.add(10.0, 10.0);
135 |         series1.add(20.0, 20.0);
136 |         series1.add(30.0, 30.0);
137 |         XYDataset dataset = new XYSeriesCollection(series1);
138 | 
139 |         LocalListener l = new LocalListener();
140 |         this.chart.addChangeListener(l);
141 |         XYPlot plot = (XYPlot) this.chart.getPlot();
142 |         plot.setDataset(dataset);
143 |         assertEquals(true, l.flag);
144 |         ValueAxis axis = plot.getRangeAxis();
145 |         Range range = axis.getRange();
146 |         assertTrue("Expecting the lower bound of the range to be around 10: "
147 |                    + range.getLowerBound(), range.getLowerBound() <= 10);
148 |         assertTrue("Expecting the upper bound of the range to be around 30: "
149 |                    + range.getUpperBound(), range.getUpperBound() >= 30);
150 | 
151 |     }
```

## org.jfree.chart.junit.TimeSeriesChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.TimeSeriesChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/TimeSeriesChartTests.java

```java
102 |     public void testDrawWithNullInfo() {
103 | 
104 |         boolean success = false;
105 |         try {
106 |             BufferedImage image = new BufferedImage(200 , 100,
107 |                     BufferedImage.TYPE_INT_RGB);
108 |             Graphics2D g2 = image.createGraphics();
109 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null,
110 |                     null);
111 |             g2.dispose();
112 |             success = true;
113 |         }
114 |         catch (Exception e) {
115 |           success = false;
116 |           e.printStackTrace();
117 |         }
118 |         assertTrue(success);
119 | 
120 |     }
```

## org.jfree.chart.junit.TimeSeriesChartTests.testSetSeriesToolTipGenerator()
Resolved declaration: org.jfree.chart.junit.TimeSeriesChartTests.testSetSeriesToolTipGenerator()
Source: tests/org/jfree/chart/junit/TimeSeriesChartTests.java

```java
152 |     public void testSetSeriesToolTipGenerator() {
153 |         XYPlot plot = (XYPlot) this.chart.getPlot();
154 |         XYItemRenderer renderer = plot.getRenderer();
155 |         StandardXYToolTipGenerator tt = new StandardXYToolTipGenerator();
156 |         renderer.setSeriesToolTipGenerator(0, tt);
157 |         XYToolTipGenerator tt2 = renderer.getToolTipGenerator(0, 0, false);
158 |         assertTrue(tt2 == tt);
159 |     }
```

## org.jfree.chart.junit.TimeSeriesChartTests.testReplaceDataset()
Resolved declaration: org.jfree.chart.junit.TimeSeriesChartTests.testReplaceDataset()
Source: tests/org/jfree/chart/junit/TimeSeriesChartTests.java

```java
125 |     public void testReplaceDataset() {
126 | 
127 |         // create a dataset...
128 |         XYSeries series1 = new XYSeries("Series 1");
129 |         series1.add(10.0, 10.0);
130 |         series1.add(20.0, 20.0);
131 |         series1.add(30.0, 30.0);
132 |         XYDataset dataset = new XYSeriesCollection(series1);
133 | 
134 |         LocalListener l = new LocalListener();
135 |         this.chart.addChangeListener(l);
136 |         XYPlot plot = (XYPlot) this.chart.getPlot();
137 |         plot.setDataset(dataset);
138 |         assertEquals(true, l.flag);
139 |         ValueAxis axis = plot.getRangeAxis();
140 |         Range range = axis.getRange();
141 |         assertTrue("Expecting the lower bound of the range to be around 10: "
142 |                    + range.getLowerBound(), range.getLowerBound() <= 10);
143 |         assertTrue("Expecting the upper bound of the range to be around 30: "
144 |                    + range.getUpperBound(), range.getUpperBound() >= 30);
145 | 
146 |     }
```

## org.jfree.chart.junit.XYAreaChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.XYAreaChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/XYAreaChartTests.java

```java
103 |     public void testDrawWithNullInfo() {
104 | 
105 |         boolean success = false;
106 |         try {
107 |             BufferedImage image = new BufferedImage(200 , 100,
108 |                     BufferedImage.TYPE_INT_RGB);
109 |             Graphics2D g2 = image.createGraphics();
110 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null,
111 |                     null);
112 |             g2.dispose();
113 |             success = true;
114 |         }
115 |         catch (Exception e) {
116 |           success = false;
117 |           e.printStackTrace();
118 |         }
119 |         assertTrue(success);
120 | 
121 |     }
```

## org.jfree.chart.junit.XYAreaChartTests.testSetSeriesToolTipGenerator()
Resolved declaration: org.jfree.chart.junit.XYAreaChartTests.testSetSeriesToolTipGenerator()
Source: tests/org/jfree/chart/junit/XYAreaChartTests.java

```java
153 |     public void testSetSeriesToolTipGenerator() {
154 |         XYPlot plot = (XYPlot) this.chart.getPlot();
155 |         XYItemRenderer renderer = plot.getRenderer();
156 |         StandardXYToolTipGenerator tt = new StandardXYToolTipGenerator();
157 |         renderer.setSeriesToolTipGenerator(0, tt);
158 |         XYToolTipGenerator tt2 = renderer.getToolTipGenerator(0, 0,
159 |                 false);
160 |         assertTrue(tt2 == tt);
161 |     }
```

## org.jfree.chart.junit.XYAreaChartTests.testReplaceDataset()
Resolved declaration: org.jfree.chart.junit.XYAreaChartTests.testReplaceDataset()
Source: tests/org/jfree/chart/junit/XYAreaChartTests.java

```java
126 |     public void testReplaceDataset() {
127 | 
128 |         // create a dataset...
129 |         XYSeries series1 = new XYSeries("Series 1");
130 |         series1.add(10.0, 10.0);
131 |         series1.add(20.0, 20.0);
132 |         series1.add(30.0, 30.0);
133 |         XYDataset dataset = new XYSeriesCollection(series1);
134 | 
135 |         LocalListener l = new LocalListener();
136 |         this.chart.addChangeListener(l);
137 |         XYPlot plot = (XYPlot) this.chart.getPlot();
138 |         plot.setDataset(dataset);
139 |         assertEquals(true, l.flag);
140 |         ValueAxis axis = plot.getRangeAxis();
141 |         Range range = axis.getRange();
142 |         assertTrue("Expecting the lower bound of the range to be around 10: "
143 |                    + range.getLowerBound(), range.getLowerBound() <= 10);
144 |         assertTrue("Expecting the upper bound of the range to be around 30: "
145 |                    + range.getUpperBound(), range.getUpperBound() >= 30);
146 | 
147 |     }
```

## org.jfree.chart.junit.XYStepAreaChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.XYStepAreaChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/XYStepAreaChartTests.java

```java
103 |     public void testDrawWithNullInfo() {
104 | 
105 |         boolean success = false;
106 |         try {
107 |             BufferedImage image = new BufferedImage(200 , 100,
108 |                     BufferedImage.TYPE_INT_RGB);
109 |             Graphics2D g2 = image.createGraphics();
110 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null,
111 |                     null);
112 |             g2.dispose();
113 |             success = true;
114 |         }
115 |         catch (Exception e) {
116 |           success = false;
117 |           e.printStackTrace();
118 |         }
119 |         assertTrue(success);
120 | 
121 |     }
```

## org.jfree.chart.junit.XYStepAreaChartTests.testSetSeriesToolTipGenerator()
Resolved declaration: org.jfree.chart.junit.XYStepAreaChartTests.testSetSeriesToolTipGenerator()
Source: tests/org/jfree/chart/junit/XYStepAreaChartTests.java

```java
153 |     public void testSetSeriesToolTipGenerator() {
154 |         XYPlot plot = (XYPlot) this.chart.getPlot();
155 |         XYItemRenderer renderer = plot.getRenderer();
156 |         StandardXYToolTipGenerator tt = new StandardXYToolTipGenerator();
157 |         renderer.setSeriesToolTipGenerator(0, tt);
158 |         XYToolTipGenerator tt2 = renderer.getToolTipGenerator(0, 0, false);
159 |         assertTrue(tt2 == tt);
160 |     }
```

## org.jfree.chart.junit.XYStepAreaChartTests.testReplaceDataset()
Resolved declaration: org.jfree.chart.junit.XYStepAreaChartTests.testReplaceDataset()
Source: tests/org/jfree/chart/junit/XYStepAreaChartTests.java

```java
126 |     public void testReplaceDataset() {
127 | 
128 |         // create a dataset...
129 |         XYSeries series1 = new XYSeries("Series 1");
130 |         series1.add(10.0, 10.0);
131 |         series1.add(20.0, 20.0);
132 |         series1.add(30.0, 30.0);
133 |         XYDataset dataset = new XYSeriesCollection(series1);
134 | 
135 |         LocalListener l = new LocalListener();
136 |         this.chart.addChangeListener(l);
137 |         XYPlot plot = (XYPlot) this.chart.getPlot();
138 |         plot.setDataset(dataset);
139 |         assertEquals(true, l.flag);
140 |         ValueAxis axis = plot.getRangeAxis();
141 |         Range range = axis.getRange();
142 |         assertTrue("Expecting the lower bound of the range to be around 10: "
143 |                    + range.getLowerBound(), range.getLowerBound() <= 10);
144 |         assertTrue("Expecting the upper bound of the range to be around 30: "
145 |                    + range.getUpperBound(), range.getUpperBound() >= 30);
146 | 
147 |     }
```

## org.jfree.chart.junit.XYStepChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.XYStepChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/XYStepChartTests.java

```java
103 |     public void testDrawWithNullInfo() {
104 | 
105 |         boolean success = false;
106 |         try {
107 |             BufferedImage image = new BufferedImage(200 , 100,
108 |                     BufferedImage.TYPE_INT_RGB);
109 |             Graphics2D g2 = image.createGraphics();
110 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null,
111 |                     null);
112 |             g2.dispose();
113 |             success = true;
114 |         }
115 |         catch (Exception e) {
116 |           success = false;
117 |           e.printStackTrace();
118 |         }
119 |         assertTrue(success);
120 | 
121 |     }
```

## org.jfree.chart.junit.XYStepChartTests.testSetSeriesToolTipGenerator()
Resolved declaration: org.jfree.chart.junit.XYStepChartTests.testSetSeriesToolTipGenerator()
Source: tests/org/jfree/chart/junit/XYStepChartTests.java

```java
153 |     public void testSetSeriesToolTipGenerator() {
154 |         XYPlot plot = (XYPlot) this.chart.getPlot();
155 |         XYItemRenderer renderer = plot.getRenderer();
156 |         StandardXYToolTipGenerator tt = new StandardXYToolTipGenerator();
157 |         renderer.setSeriesToolTipGenerator(0, tt);
158 |         XYToolTipGenerator tt2 = renderer.getToolTipGenerator(0, 0, false);
159 |         assertTrue(tt2 == tt);
160 |     }
```

## org.jfree.chart.junit.XYStepChartTests.testReplaceDataset()
Resolved declaration: org.jfree.chart.junit.XYStepChartTests.testReplaceDataset()
Source: tests/org/jfree/chart/junit/XYStepChartTests.java

```java
126 |     public void testReplaceDataset() {
127 | 
128 |         // create a dataset...
129 |         XYSeries series1 = new XYSeries("Series 1");
130 |         series1.add(10.0, 10.0);
131 |         series1.add(20.0, 20.0);
132 |         series1.add(30.0, 30.0);
133 |         XYDataset dataset = new XYSeriesCollection(series1);
134 | 
135 |         LocalListener l = new LocalListener();
136 |         this.chart.addChangeListener(l);
137 |         XYPlot plot = (XYPlot) this.chart.getPlot();
138 |         plot.setDataset(dataset);
139 |         assertEquals(true, l.flag);
140 |         ValueAxis axis = plot.getRangeAxis();
141 |         Range range = axis.getRange();
142 |         assertTrue("Expecting the lower bound of the range to be around 10: "
143 |                    + range.getLowerBound(), range.getLowerBound() <= 10);
144 |         assertTrue("Expecting the upper bound of the range to be around 30: "
145 |                    + range.getUpperBound(), range.getUpperBound() >= 30);
146 | 
147 |     }
```

## org.jfree.chart.plot.junit.XYPlotTests.testDrawRangeGridlines()
Resolved declaration: org.jfree.chart.plot.junit.XYPlotTests.testDrawRangeGridlines()
Source: tests/org/jfree/chart/plot/junit/XYPlotTests.java

```java
1051 |     public void testDrawRangeGridlines() {
1052 |         DefaultXYDataset dataset = new DefaultXYDataset();
1053 |         JFreeChart chart = ChartFactory.createXYLineChart("Title", "X", "Y",
1054 |                 dataset, PlotOrientation.VERTICAL, true, false, false);
1055 |         XYPlot plot = (XYPlot) chart.getPlot();
1056 |         plot.setRenderer(null);
1057 |         boolean success = false;
1058 |         try {
1059 |             BufferedImage image = new BufferedImage(200 , 100,
1060 |                     BufferedImage.TYPE_INT_RGB);
1061 |             Graphics2D g2 = image.createGraphics();
1062 |             chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, null);
1063 |             g2.dispose();
1064 |             success = true;
1065 |         }
1066 |         catch (Exception e) {
1067 |             e.printStackTrace();
1068 |             success = false;
1069 |         }
1070 |         assertTrue(success);
1071 |     }
```
