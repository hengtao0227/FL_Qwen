# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.renderer.junit.GrayPaintScaleTests.testGetPaint()
Resolved declaration: org.jfree.chart.renderer.junit.GrayPaintScaleTests.testGetPaint()
Source: tests/org/jfree/chart/renderer/junit/GrayPaintScaleTests.java

```java
98 |     public void testGetPaint() {
99 |         GrayPaintScale gps = new GrayPaintScale();
100 |         Color c = (Color) gps.getPaint(0.0);
101 |         assertTrue(c.equals(Color.black));
102 |         c = (Color) gps.getPaint(1.0);
103 |         assertTrue(c.equals(Color.white));
104 |         
105 |         // check lookup values that are outside the bounds - see bug report
106 |         // 1767315
107 |         c = (Color) gps.getPaint(-0.5);
108 |         assertTrue(c.equals(Color.black));
109 |         c = (Color) gps.getPaint(1.5);
110 |         assertTrue(c.equals(Color.white));
111 |     }
```
