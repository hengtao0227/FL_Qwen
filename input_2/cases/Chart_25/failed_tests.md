# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullMeanVertical()
Resolved declaration: org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullMeanVertical()
Source: tests/org/jfree/chart/renderer/category/junit/StatisticalBarRendererTests.java

```java
189 |     public void testDrawWithNullMeanVertical() {
190 |         boolean success = false;
191 |         try {
192 |             DefaultStatisticalCategoryDataset dataset 
193 |                     = new DefaultStatisticalCategoryDataset();
194 |             dataset.add(1.0, 2.0, "S1", "C1");
195 |             dataset.add(null, new Double(4.0), "S1", "C2");
196 |             CategoryPlot plot = new CategoryPlot(dataset, 
197 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
198 |                     new StatisticalBarRenderer());
199 |             JFreeChart chart = new JFreeChart(plot);
200 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
201 |                     null);
202 |             success = true;
203 |         }
204 |         catch (NullPointerException e) {
205 |             e.printStackTrace();
206 |             success = false;
207 |         }
208 |         assertTrue(success);
209 |     }
```

## org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullDeviationVertical()
Resolved declaration: org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullDeviationVertical()
Source: tests/org/jfree/chart/renderer/category/junit/StatisticalBarRendererTests.java

```java
244 |     public void testDrawWithNullDeviationVertical() {
245 |         boolean success = false;
246 |         try {
247 |             DefaultStatisticalCategoryDataset dataset 
248 |                     = new DefaultStatisticalCategoryDataset();
249 |             dataset.add(1.0, 2.0, "S1", "C1");
250 |             dataset.add(new Double(4.0), null, "S1", "C2");
251 |             CategoryPlot plot = new CategoryPlot(dataset, 
252 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
253 |                     new StatisticalBarRenderer());
254 |             JFreeChart chart = new JFreeChart(plot);
255 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
256 |                     null);
257 |             success = true;
258 |         }
259 |         catch (NullPointerException e) {
260 |             e.printStackTrace();
261 |             success = false;
262 |         }
263 |         assertTrue(success);
264 |     }
```

## org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullMeanHorizontal()
Resolved declaration: org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullMeanHorizontal()
Source: tests/org/jfree/chart/renderer/category/junit/StatisticalBarRendererTests.java

```java
216 |     public void testDrawWithNullMeanHorizontal() {
217 |         boolean success = false;
218 |         try {
219 |             DefaultStatisticalCategoryDataset dataset 
220 |                     = new DefaultStatisticalCategoryDataset();
221 |             dataset.add(1.0, 2.0, "S1", "C1");
222 |             dataset.add(null, new Double(4.0), "S1", "C2");
223 |             CategoryPlot plot = new CategoryPlot(dataset, 
224 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
225 |                     new StatisticalBarRenderer());
226 |             plot.setOrientation(PlotOrientation.HORIZONTAL);
227 |             JFreeChart chart = new JFreeChart(plot);
228 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
229 |                     null);
230 |             success = true;
231 |         }
232 |         catch (NullPointerException e) {
233 |             e.printStackTrace();
234 |             success = false;
235 |         }
236 |         assertTrue(success);
237 |     }
```

## org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullDeviationHorizontal()
Resolved declaration: org.jfree.chart.renderer.category.junit.StatisticalBarRendererTests.testDrawWithNullDeviationHorizontal()
Source: tests/org/jfree/chart/renderer/category/junit/StatisticalBarRendererTests.java

```java
271 |     public void testDrawWithNullDeviationHorizontal() {
272 |         boolean success = false;
273 |         try {
274 |             DefaultStatisticalCategoryDataset dataset 
275 |                     = new DefaultStatisticalCategoryDataset();
276 |             dataset.add(1.0, 2.0, "S1", "C1");
277 |             dataset.add(new Double(4.0), null, "S1", "C2");
278 |             CategoryPlot plot = new CategoryPlot(dataset, 
279 |                     new CategoryAxis("Category"), new NumberAxis("Value"), 
280 |                     new StatisticalBarRenderer());
281 |             plot.setOrientation(PlotOrientation.HORIZONTAL);
282 |             JFreeChart chart = new JFreeChart(plot);
283 |             /* BufferedImage image = */ chart.createBufferedImage(300, 200, 
284 |                     null);
285 |             success = true;
286 |         }
287 |         catch (NullPointerException e) {
288 |             e.printStackTrace();
289 |             success = false;
290 |         }
291 |         assertTrue(success);
292 |     }
```
