# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.statistics.junit.DefaultBoxAndWhiskerCategoryDatasetTests.testGetRangeBounds()
Resolved declaration: org.jfree.data.statistics.junit.DefaultBoxAndWhiskerCategoryDatasetTests.testGetRangeBounds()
Source: tests/org/jfree/data/statistics/junit/DefaultBoxAndWhiskerCategoryDatasetTests.java

```java
270 |     public void testGetRangeBounds() {
271 |         DefaultBoxAndWhiskerCategoryDataset d1 
272 |                 = new DefaultBoxAndWhiskerCategoryDataset();
273 |         d1.add(new BoxAndWhiskerItem(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 
274 |                 new ArrayList()), "R1", "C1");
275 |         assertEquals(new Range(7.0, 8.0), d1.getRangeBounds(false));
276 |         assertEquals(new Range(7.0, 8.0), d1.getRangeBounds(true));
277 |         
278 |         d1.add(new BoxAndWhiskerItem(1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 
279 |                 new ArrayList()), "R1", "C1");
280 |         assertEquals(new Range(7.5, 8.5), d1.getRangeBounds(false));
281 |         assertEquals(new Range(7.5, 8.5), d1.getRangeBounds(true));
282 |         
283 |         d1.add(new BoxAndWhiskerItem(2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 
284 |                 new ArrayList()), "R2", "C1");
285 |         assertEquals(new Range(7.5, 9.5), d1.getRangeBounds(false));
286 |         assertEquals(new Range(7.5, 9.5), d1.getRangeBounds(true));
287 |         
288 |         // this replaces the entry with the current minimum value, but the new
289 |         // minimum value is now in a different item
290 |         d1.add(new BoxAndWhiskerItem(1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 8.6, 9.6, 
291 |                 new ArrayList()), "R1", "C1");
292 |         assertEquals(new Range(8.5, 9.6), d1.getRangeBounds(false));
293 |         assertEquals(new Range(8.5, 9.6), d1.getRangeBounds(true));
294 |     }
```
