# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.renderer.category.junit.MinMaxCategoryRendererTests.testEquals()
Resolved declaration: org.jfree.chart.renderer.category.junit.MinMaxCategoryRendererTests.testEquals()
Source: tests/org/jfree/chart/renderer/category/junit/MinMaxCategoryRendererTests.java

```java
93 |     public void testEquals() {
94 |         MinMaxCategoryRenderer r1 = new MinMaxCategoryRenderer();
95 |         MinMaxCategoryRenderer r2 = new MinMaxCategoryRenderer();
96 |         assertEquals(r1, r2);
97 |         
98 |         r1.setDrawLines(true);
99 |         assertFalse(r1.equals(r2));
100 |         r2.setDrawLines(true);
101 |         assertTrue(r1.equals(r2));
102 |         
103 |         r1.setGroupPaint(new GradientPaint(1.0f, 2.0f, Color.red, 3.0f, 4.0f, 
104 |                 Color.yellow));
105 |         assertFalse(r1.equals(r2));
106 |         r2.setGroupPaint(new GradientPaint(1.0f, 2.0f, Color.red, 3.0f, 4.0f, 
107 |                 Color.yellow));
108 |         assertTrue(r1.equals(r2));
109 |         
110 |         r1.setGroupStroke(new BasicStroke(1.2f));
111 |         assertFalse(r1.equals(r2));
112 |         r2.setGroupStroke(new BasicStroke(1.2f));
113 |         assertTrue(r1.equals(r2));
114 |     }
```
