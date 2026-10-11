# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.plot.junit.ValueMarkerTests.test1808376()
Resolved declaration: org.jfree.chart.plot.junit.ValueMarkerTests.test1808376()
Source: tests/org/jfree/chart/plot/junit/ValueMarkerTests.java

```java
289 |     public void test1808376() {
290 |         Stroke stroke = new BasicStroke(1.0f);
291 |         Stroke outlineStroke = new BasicStroke(2.0f);
292 |         ValueMarker m = new ValueMarker(1.0, Color.red, stroke, Color.blue, 
293 |                 outlineStroke, 0.5f);
294 |         assertEquals(1.0, m.getValue(), EPSILON);
295 |         assertEquals(Color.red, m.getPaint());
296 |         assertEquals(stroke, m.getStroke());
297 |         assertEquals(Color.blue, m.getOutlinePaint());
298 |         assertEquals(outlineStroke, m.getOutlineStroke());
299 |         assertEquals(0.5f, m.getAlpha(), EPSILON);
300 |     }
```
