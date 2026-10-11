# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.junit.AreaChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.AreaChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/AreaChartTests.java

```java
135 |     public void testDrawWithNullInfo() {
136 |         boolean success = false;
137 |         try {
138 |             BufferedImage image = new BufferedImage(200 , 100, 
139 |                     BufferedImage.TYPE_INT_RGB);
140 |             Graphics2D g2 = image.createGraphics();
141 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
142 |                     null);
143 |             g2.dispose();
144 |             success = true;
145 |         }
146 |         catch (Exception e) {
147 |             success = false;
148 |         }
149 |         assertTrue(success);
150 |     }
```

## org.jfree.chart.junit.BarChart3DTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.BarChart3DTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/BarChart3DTests.java

```java
111 |     public void testDrawWithNullInfo() {
112 |         boolean success = false;
113 |         try {
114 |             BufferedImage image = new BufferedImage(200 , 100, 
115 |                     BufferedImage.TYPE_INT_RGB);
116 |             Graphics2D g2 = image.createGraphics();
117 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
118 |                     null);
119 |             g2.dispose();
120 |             success = true;
121 |         }
122 |         catch (Exception e) {
123 |             success = false;
124 |         }
125 |         assertTrue(success);
126 |     }
```

## org.jfree.chart.junit.BarChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.BarChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/BarChartTests.java

```java
111 |     public void testDrawWithNullInfo() {
112 | 
113 |         boolean success = false;
114 | 
115 |         try {
116 |             BufferedImage image = new BufferedImage(200 , 100, 
117 |                     BufferedImage.TYPE_INT_RGB);
118 |             Graphics2D g2 = image.createGraphics();
119 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
120 |                     null);
121 |             g2.dispose();
122 |             success = true;
123 |         }
124 |         catch (Exception e) {
125 |             success = false;
126 |         }
127 | 
128 |         assertTrue(success);
129 | 
130 |     }
```

## org.jfree.chart.junit.GanttChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.GanttChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/GanttChartTests.java

```java
110 |     public void testDrawWithNullInfo() {
111 |         boolean success = false;
112 |         try {
113 |             BufferedImage image = new BufferedImage(200 , 100, 
114 |                     BufferedImage.TYPE_INT_RGB);
115 |             Graphics2D g2 = image.createGraphics();
116 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
117 |                     null);
118 |             g2.dispose();
119 |             success = true;
120 |         }
121 |         catch (Exception e) {
122 |             success = false;
123 |         }
124 |         assertTrue(success);
125 |     }
```

## org.jfree.chart.junit.GanttChartTests.testDrawWithNullInfo2()
Resolved declaration: org.jfree.chart.junit.GanttChartTests.testDrawWithNullInfo2()
Source: tests/org/jfree/chart/junit/GanttChartTests.java

```java
131 |     public void testDrawWithNullInfo2() {
132 |         boolean success = false;
133 |         try {
134 |             JFreeChart chart = createGanttChart();
135 |             CategoryPlot plot = (CategoryPlot) chart.getPlot();
136 |             plot.setDataset(createDataset());
137 |             /* BufferedImage img =*/ chart.createBufferedImage(300, 200, null);
138 |             success = true;
139 |         }
140 |         catch (NullPointerException e) {
141 |             success = false;
142 |         }
143 |         assertTrue(success);
144 |     }
```

## org.jfree.chart.junit.LineChart3DTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.LineChart3DTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/LineChart3DTests.java

```java
108 |     public void testDrawWithNullInfo() {
109 | 
110 |         boolean success = false;
111 |         try {
112 |             BufferedImage image = new BufferedImage(200 , 100, 
113 |                     BufferedImage.TYPE_INT_RGB);
114 |             Graphics2D g2 = image.createGraphics();
115 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
116 |                     null);
117 |             g2.dispose();
118 |             success = true;
119 |         }
120 |         catch (Exception e) {
121 |             success = false;
122 |         }
123 |         assertTrue(success);
124 | 
125 |     }
```

## org.jfree.chart.junit.LineChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.LineChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/LineChartTests.java

```java
108 |     public void testDrawWithNullInfo() {
109 | 
110 |         boolean success = false;
111 |         try {
112 |             BufferedImage image = new BufferedImage(200 , 100, 
113 |                     BufferedImage.TYPE_INT_RGB);
114 |             Graphics2D g2 = image.createGraphics();
115 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
116 |                     null);
117 |             g2.dispose();
118 |             success = true;
119 |         }
120 |         catch (Exception e) {
121 |             success = false;
122 |         }
123 |         assertTrue(success);
124 | 
125 |     }
```

## org.jfree.chart.junit.StackedAreaChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.StackedAreaChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/StackedAreaChartTests.java

```java
108 |     public void testDrawWithNullInfo() {
109 | 
110 |         boolean success = false;
111 |         try {
112 |             BufferedImage image = new BufferedImage(200 , 100, 
113 |                     BufferedImage.TYPE_INT_RGB);
114 |             Graphics2D g2 = image.createGraphics();
115 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
116 |                     null);
117 |             g2.dispose();
118 |             success = true;
119 |         }
120 |         catch (Exception e) {
121 |           success = false;
122 |         }
123 |         assertTrue(success);
124 | 
125 |     }
```

## org.jfree.chart.junit.StackedBarChart3DTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.StackedBarChart3DTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/StackedBarChart3DTests.java

```java
108 |     public void testDrawWithNullInfo() {
109 | 
110 |         boolean success = false;
111 |         try {
112 |             BufferedImage image = new BufferedImage(200 , 100, 
113 |                     BufferedImage.TYPE_INT_RGB);
114 |             Graphics2D g2 = image.createGraphics();
115 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null,
116 |                     null);
117 |             g2.dispose();
118 |             success = true;
119 |         }
120 |         catch (Exception e) {
121 |           success = false;
122 |         }
123 |         assertTrue(success);
124 | 
125 |     }
```

## org.jfree.chart.junit.StackedBarChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.StackedBarChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/StackedBarChartTests.java

```java
112 |     public void testDrawWithNullInfo() {
113 | 
114 |         boolean success = false;
115 | 
116 |         try {
117 |             BufferedImage image = new BufferedImage(200 , 100, 
118 |                     BufferedImage.TYPE_INT_RGB);
119 |             Graphics2D g2 = image.createGraphics();
120 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
121 |                     null);
122 |             g2.dispose();
123 |             success = true;
124 |         }
125 |         catch (Exception e) {
126 |           success = false;
127 |         }
128 | 
129 |         assertTrue(success);
130 | 
131 |     }
```

## org.jfree.chart.junit.WaterfallChartTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.junit.WaterfallChartTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/junit/WaterfallChartTests.java

```java
104 |     public void testDrawWithNullInfo() {
105 | 
106 |         boolean success = false;
107 | 
108 |         try {
109 |             BufferedImage image = new BufferedImage(200 , 100, 
110 |                     BufferedImage.TYPE_INT_RGB);
111 |             Graphics2D g2 = image.createGraphics();
112 |             this.chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, 
113 |                     null);
114 |             g2.dispose();
115 |             success = true;
116 |         }
117 |         catch (Exception e) {
118 |             success = false;
119 |         }
120 | 
121 |         assertTrue(success);
122 | 
123 |     }
```

## org.jfree.chart.plot.junit.CategoryPlotTests.test1654215()
Resolved declaration: org.jfree.chart.plot.junit.CategoryPlotTests.test1654215()
Source: tests/org/jfree/chart/plot/junit/CategoryPlotTests.java

```java
686 |     public void test1654215() {
687 |         DefaultCategoryDataset dataset = new DefaultCategoryDataset();
688 |         JFreeChart chart = ChartFactory.createLineChart("Title", "X", "Y",
689 |                 dataset, PlotOrientation.VERTICAL, true, false, false);
690 |         CategoryPlot plot = (CategoryPlot) chart.getPlot();
691 |         plot.setRenderer(1, new LineAndShapeRenderer());
692 |         boolean success = false;
693 |         try {
694 |             BufferedImage image = new BufferedImage(200 , 100, 
695 |                     BufferedImage.TYPE_INT_RGB);
696 |             Graphics2D g2 = image.createGraphics();
697 |             chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, null);
698 |             g2.dispose();
699 |             success = true;
700 |         }
701 |         catch (Exception e) {
702 |             e.printStackTrace();
703 |             success = false;
704 |         }
705 |         assertTrue(success);
706 |     }
```

## org.jfree.chart.plot.junit.CategoryPlotTests.testSerialization3()
Resolved declaration: org.jfree.chart.plot.junit.CategoryPlotTests.testSerialization3()
Source: tests/org/jfree/chart/plot/junit/CategoryPlotTests.java

```java
475 |     public void testSerialization3() {
476 |         DefaultCategoryDataset dataset = new DefaultCategoryDataset();
477 |         JFreeChart chart = ChartFactory.createBarChart(
478 |             "Test Chart",
479 |             "Category Axis",
480 |             "Value Axis",
481 |             dataset,
482 |             PlotOrientation.VERTICAL,
483 |             true,
484 |             true,
485 |             false
486 |         );
487 |         JFreeChart chart2 = null;
488 |         
489 |         // serialize and deserialize the chart....
490 |         try {
491 |             ByteArrayOutputStream buffer = new ByteArrayOutputStream();
492 |             ObjectOutput out = new ObjectOutputStream(buffer);
493 |             out.writeObject(chart);
494 |             out.close();
495 | 
496 |             ObjectInput in = new ObjectInputStream(
497 |                     new ByteArrayInputStream(buffer.toByteArray()));
498 |             chart2 = (JFreeChart) in.readObject();
499 |             in.close();
500 |         }
501 |         catch (Exception e) {
502 |             fail(e.toString());
503 |         }
504 | 
505 |         // now check that the chart is usable...
506 |         boolean passed = true;
507 |         try {
508 |             chart2.createBufferedImage(300, 200);
509 |         }
510 |         catch (Exception e) {
511 |             passed = false;  
512 |             e.printStackTrace();            
513 |         }
514 |         assertTrue(passed);
515 |     }
```

## org.jfree.chart.plot.junit.CategoryPlotTests.testSerialization4()
Resolved declaration: org.jfree.chart.plot.junit.CategoryPlotTests.testSerialization4()
Source: tests/org/jfree/chart/plot/junit/CategoryPlotTests.java

```java
520 |     public void testSerialization4() {
521 |         DefaultCategoryDataset dataset = new DefaultCategoryDataset();
522 |         JFreeChart chart = ChartFactory.createBarChart(
523 |             "Test Chart",
524 |             "Category Axis",
525 |             "Value Axis",
526 |             dataset,
527 |             PlotOrientation.VERTICAL,
528 |             true,
529 |             true,
530 |             false
531 |         );
532 |         CategoryPlot plot = (CategoryPlot) chart.getPlot();
533 |         plot.addRangeMarker(new ValueMarker(1.1), Layer.FOREGROUND);
534 |         plot.addRangeMarker(new IntervalMarker(2.2, 3.3), Layer.BACKGROUND);
535 |         JFreeChart chart2 = null;
536 |         
537 |         // serialize and deserialize the chart....
538 |         try {
539 |             ByteArrayOutputStream buffer = new ByteArrayOutputStream();
540 |             ObjectOutput out = new ObjectOutputStream(buffer);
541 |             out.writeObject(chart);
542 |             out.close();
543 | 
544 |             ObjectInput in = new ObjectInputStream(
545 |                     new ByteArrayInputStream(buffer.toByteArray()));
546 |             chart2 = (JFreeChart) in.readObject();
547 |             in.close();
548 |         }
549 |         catch (Exception e) {
550 |             fail(e.toString());
551 |         }
552 |         assertEquals(chart, chart2);
553 |         
554 |         // now check that the chart is usable...
555 |         boolean passed = true;
556 |         try {
557 |             chart2.createBufferedImage(300, 200);
558 |         }
559 |         catch (Exception e) {
560 |             passed = false;  
561 |             e.printStackTrace();            
562 |         }
563 |         assertTrue(passed);
564 |     }
```

## org.jfree.chart.renderer.category.junit.BoxAndWhiskerRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.BoxAndWhiskerRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/BoxAndWhiskerRendererTests.java

```java
188 |     public void testDrawWithNullInfo() {
189 |         boolean success = false;
190 |         try {
191 |             DefaultBoxAndWhiskerCategoryDataset dataset 
192 |                 = new DefaultBoxAndWhiskerCategoryDataset();
193 |             dataset.add(new BoxAndWhiskerItem(new Double(1.0), new Double(2.0),
194 |                     new Double(0.0), new Double(4.0), new Double(0.5), 
195 |                     new Double(4.5), new Double(-0.5), new Double(5.5), 
196 |                     null), "S1", "C1");
197 |             CategoryPlot plot = new CategoryPlot(dataset, 
198 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
199 |                     new BoxAndWhiskerRenderer());
200 |             JFreeChart chart = new JFreeChart(plot);
201 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
202 |                     null);
203 |             success = true;
204 |         }
205 |         catch (NullPointerException e) {
206 |             success = false;
207 |         }
208 |         assertTrue(success);
209 |     }
```

## org.jfree.chart.renderer.category.junit.GroupedStackedBarRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.GroupedStackedBarRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/GroupedStackedBarRendererTests.java

```java
154 |     public void testDrawWithNullInfo() {
155 |         boolean success = false;
156 |         try {
157 |             DefaultCategoryDataset dataset = new DefaultCategoryDataset();
158 |             dataset.addValue(1.0, "S1", "C1");
159 |             dataset.addValue(2.0, "S1", "C2");
160 |             dataset.addValue(3.0, "S2", "C1");
161 |             dataset.addValue(4.0, "S2", "C2");
162 |             GroupedStackedBarRenderer renderer 
163 |                 = new GroupedStackedBarRenderer();
164 |             CategoryPlot plot = new CategoryPlot(dataset, 
165 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
166 |                     renderer);
167 |             JFreeChart chart = new JFreeChart(plot);
168 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
169 |                     null);
170 |             success = true;
171 |         }
172 |         catch (NullPointerException e) {
173 |             e.printStackTrace();
174 |             success = false;
175 |         }
176 |         assertTrue(success);
177 |     }
```

## org.jfree.chart.renderer.category.junit.IntervalBarRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.IntervalBarRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/IntervalBarRendererTests.java

```java
155 |     public void testDrawWithNullInfo() {
156 |         boolean success = false;
157 |         try {
158 |             double[][] starts = new double[][] {{0.1, 0.2, 0.3}, 
159 |                     {0.3, 0.4, 0.5}};
160 |             double[][] ends = new double[][] {{0.5, 0.6, 0.7}, {0.7, 0.8, 0.9}};
161 |             DefaultIntervalCategoryDataset dataset 
162 |                 = new DefaultIntervalCategoryDataset(starts, ends);        
163 |             IntervalBarRenderer renderer = new IntervalBarRenderer();
164 |             CategoryPlot plot = new CategoryPlot(dataset, 
165 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
166 |                     renderer);
167 |             JFreeChart chart = new JFreeChart(plot);
168 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
169 |                     null);
170 |             success = true;
171 |         }
172 |         catch (NullPointerException e) {
173 |             e.printStackTrace();
174 |             success = false;
175 |         }
176 |         assertTrue(success);
177 |     }
```

## org.jfree.chart.renderer.category.junit.LayeredBarRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.LayeredBarRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/LayeredBarRendererTests.java

```java
155 |     public void testDrawWithNullInfo() {
156 |         boolean success = false;
157 |         try {
158 |             DefaultCategoryDataset dataset = new DefaultCategoryDataset();
159 |             dataset.addValue(1.0, "S1", "C1");
160 |             CategoryPlot plot = new CategoryPlot(dataset, 
161 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
162 |                     new LayeredBarRenderer());
163 |             JFreeChart chart = new JFreeChart(plot);
164 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
165 |                     null);
166 |             success = true;
167 |         }
168 |         catch (NullPointerException e) {
169 |             e.printStackTrace();
170 |             success = false;
171 |         }
172 |         assertTrue(success);
173 |     }
```

## org.jfree.chart.renderer.category.junit.LevelRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.LevelRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/LevelRendererTests.java

```java
196 |     public void testDrawWithNullInfo() {
197 |         boolean success = false;
198 |         try {
199 |             DefaultCategoryDataset dataset = new DefaultCategoryDataset();
200 |             dataset.addValue(1.0, "S1", "C1");
201 |             CategoryPlot plot = new CategoryPlot(dataset, 
202 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
203 |                     new LevelRenderer());
204 |             JFreeChart chart = new JFreeChart(plot);
205 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
206 |                     null);
207 |             success = true;
208 |         }
209 |         catch (NullPointerException e) {
210 |             e.printStackTrace();
211 |             success = false;
212 |         }
213 |         assertTrue(success);
214 |     }
```

## org.jfree.chart.renderer.category.junit.MinMaxCategoryRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.MinMaxCategoryRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/MinMaxCategoryRendererTests.java

```java
154 |     public void testDrawWithNullInfo() {
155 |         boolean success = false;
156 |         try {
157 |             DefaultCategoryDataset dataset = new DefaultCategoryDataset();
158 |             dataset.addValue(1.0, "S1", "C1");
159 |             CategoryPlot plot = new CategoryPlot(dataset, 
160 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
161 |                     new MinMaxCategoryRenderer());
162 |             JFreeChart chart = new JFreeChart(plot);
163 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
164 |                     null);
165 |             success = true;
166 |         }
167 |         catch (NullPointerException e) {
168 |             e.printStackTrace();
169 |             success = false;
170 |         }
171 |         assertTrue(success);
172 |     }
```

## org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/StatisticalBarRendererTests.java

```java
161 |     public void testDrawWithNullInfo() {
162 |         boolean success = false;
163 |         try {
164 |             DefaultStatisticalCategoryDataset dataset 
165 |                 = new DefaultStatisticalCategoryDataset();
166 |             dataset.add(1.0, 2.0, "S1", "C1");
167 |             dataset.add(3.0, 4.0, "S1", "C2");
168 |             CategoryPlot plot = new CategoryPlot(dataset, 
169 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
170 |                     new StatisticalBarRenderer());
171 |             JFreeChart chart = new JFreeChart(plot);
172 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
173 |                     null);
174 |             success = true;
175 |         }
176 |         catch (NullPointerException e) {
177 |             e.printStackTrace();
178 |             success = false;
179 |         }
180 |         assertTrue(success);
181 |     }
```

## org.jfree.chart.renderer.category.junit.StatisticalLineAndShapeRendererTests.testDrawWithNullInfo()
Resolved declaration: org.jfree.chart.renderer.category.junit.StatisticalLineAndShapeRendererTests.testDrawWithNullInfo()
Source: tests/org/jfree/chart/renderer/category/junit/StatisticalLineAndShapeRendererTests.java

```java
168 |     public void testDrawWithNullInfo() {
169 |         boolean success = false;
170 |         try {
171 |             DefaultStatisticalCategoryDataset dataset 
172 |                 = new DefaultStatisticalCategoryDataset();
173 |             dataset.add(1.0, 2.0, "S1", "C1");
174 |             dataset.add(3.0, 4.0, "S1", "C2");
175 |             CategoryPlot plot = new CategoryPlot(dataset, 
176 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
177 |                     new StatisticalLineAndShapeRenderer());
178 |             JFreeChart chart = new JFreeChart(plot);
179 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
180 |                     null);
181 |             success = true;
182 |         }
183 |         catch (NullPointerException e) {
184 |             e.printStackTrace();
185 |             success = false;
186 |         }
187 |         assertTrue(success);
188 |     }
```
