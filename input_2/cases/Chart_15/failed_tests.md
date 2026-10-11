# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.plot.junit.PiePlot3DTests.testDrawWithNullDataset()
Resolved declaration: org.jfree.chart.plot.junit.PiePlot3DTests.testDrawWithNullDataset()
Source: tests/org/jfree/chart/plot/junit/PiePlot3DTests.java

```java
136 |     public void testDrawWithNullDataset() {
137 |         JFreeChart chart = ChartFactory.createPieChart3D("Test", null, true, 
138 |                 false, false);
139 |         boolean success = false;
140 |         try {
141 |             BufferedImage image = new BufferedImage(200 , 100, 
142 |                     BufferedImage.TYPE_INT_RGB);
143 |             Graphics2D g2 = image.createGraphics();
144 |             chart.draw(g2, new Rectangle2D.Double(0, 0, 200, 100), null, null);
145 |             g2.dispose();
146 |             success = true;
147 |         }
148 |         catch (Exception e) {
149 |             success = false;
150 |         }
151 |         assertTrue(success);
152 |     }
```
