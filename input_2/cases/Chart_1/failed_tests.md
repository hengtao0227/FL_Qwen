# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.renderer.category.junit.AbstractCategoryItemRendererTests.test2947660()
Resolved declaration: org.jfree.chart.renderer.category.junit.AbstractCategoryItemRendererTests.test2947660()
Source: tests/org/jfree/chart/renderer/category/junit/AbstractCategoryItemRendererTests.java

```java
396 |     public void test2947660() {
397 |         AbstractCategoryItemRenderer r = new LineAndShapeRenderer();
398 |         assertNotNull(r.getLegendItems());
399 |         assertEquals(0, r.getLegendItems().getItemCount());
400 | 
401 |         DefaultCategoryDataset dataset = new DefaultCategoryDataset();
402 |         CategoryPlot plot = new CategoryPlot();
403 |         plot.setDataset(dataset);
404 |         plot.setRenderer(r);
405 |         assertEquals(0, r.getLegendItems().getItemCount());
406 | 
407 |         dataset.addValue(1.0, "S1", "C1");
408 |         LegendItemCollection lic = r.getLegendItems();
409 |         assertEquals(1, lic.getItemCount());
410 |         assertEquals("S1", lic.get(0).getLabel());
411 |     }
```
