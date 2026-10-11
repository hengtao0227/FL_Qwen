# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.general.junit.DatasetUtilitiesTests.testBug2849731_2()
Resolved declaration: org.jfree.data.general.junit.DatasetUtilitiesTests.testBug2849731_2()
Source: tests/org/jfree/data/general/junit/DatasetUtilitiesTests.java

```java
1266 |     public void testBug2849731_2() {
1267 |         XYIntervalSeriesCollection d = new XYIntervalSeriesCollection();
1268 |         XYIntervalSeries s = new XYIntervalSeries("S1");
1269 |         s.add(1.0, Double.NaN, Double.NaN, Double.NaN, 1.5, Double.NaN);
1270 |         d.addSeries(s);
1271 |         Range r = DatasetUtilities.iterateDomainBounds(d);
1272 |         assertEquals(1.0, r.getLowerBound(), EPSILON);
1273 |         assertEquals(1.0, r.getUpperBound(), EPSILON);
1274 | 
1275 |         s.add(1.0, 1.5, Double.NaN, Double.NaN, 1.5, Double.NaN);
1276 |         r = DatasetUtilities.iterateDomainBounds(d);
1277 |         assertEquals(1.0, r.getLowerBound(), EPSILON);
1278 |         assertEquals(1.5, r.getUpperBound(), EPSILON);
1279 | 
1280 |         s.add(1.0, Double.NaN, 0.5, Double.NaN, 1.5, Double.NaN);
1281 |         r = DatasetUtilities.iterateDomainBounds(d);
1282 |         assertEquals(0.5, r.getLowerBound(), EPSILON);
1283 |         assertEquals(1.5, r.getUpperBound(), EPSILON);
1284 |     }
```

## org.jfree.data.general.junit.DatasetUtilitiesTests.testBug2849731_3()
Resolved declaration: org.jfree.data.general.junit.DatasetUtilitiesTests.testBug2849731_3()
Source: tests/org/jfree/data/general/junit/DatasetUtilitiesTests.java

```java
1289 |     public void testBug2849731_3() {
1290 |         XYIntervalSeriesCollection d = new XYIntervalSeriesCollection();
1291 |         XYIntervalSeries s = new XYIntervalSeries("S1");
1292 |         s.add(1.0, Double.NaN, Double.NaN, 1.5, Double.NaN, Double.NaN);
1293 |         d.addSeries(s);
1294 |         Range r = DatasetUtilities.iterateRangeBounds(d);
1295 |         assertEquals(1.5, r.getLowerBound(), EPSILON);
1296 |         assertEquals(1.5, r.getUpperBound(), EPSILON);
1297 | 
1298 |         s.add(1.0, 1.5, Double.NaN, Double.NaN, Double.NaN, 2.5);
1299 |         r = DatasetUtilities.iterateRangeBounds(d);
1300 |         assertEquals(1.5, r.getLowerBound(), EPSILON);
1301 |         assertEquals(2.5, r.getUpperBound(), EPSILON);
1302 | 
1303 |         s.add(1.0, Double.NaN, 0.5, Double.NaN, 3.5, Double.NaN);
1304 |         r = DatasetUtilities.iterateRangeBounds(d);
1305 |         assertEquals(1.5, r.getLowerBound(), EPSILON);
1306 |         assertEquals(3.5, r.getUpperBound(), EPSILON);
1307 |     }
```
