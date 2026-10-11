# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.clustering.KMeansPlusPlusClustererTest.testPerformClusterAnalysisDegenerate()
Resolved declaration: org.apache.commons.math.stat.clustering.KMeansPlusPlusClustererTest.testPerformClusterAnalysisDegenerate()
Source: src/test/java/org/apache/commons/math/stat/clustering/KMeansPlusPlusClustererTest.java

```java
102 |     @Test
103 |     public void testPerformClusterAnalysisDegenerate() {
104 |         KMeansPlusPlusClusterer<EuclideanIntegerPoint> transformer = new KMeansPlusPlusClusterer<EuclideanIntegerPoint>(
105 |                 new Random(1746432956321l));
106 |         EuclideanIntegerPoint[] points = new EuclideanIntegerPoint[] {
107 |                 new EuclideanIntegerPoint(new int[] { 1959, 325100 }),
108 |                 new EuclideanIntegerPoint(new int[] { 1960, 373200 }), };
109 |         List<Cluster<EuclideanIntegerPoint>> clusters = transformer.cluster(Arrays.asList(points), 1, 1);
110 |         assertEquals(1, clusters.size());
111 |         assertEquals(2, (clusters.get(0).getPoints().size()));
112 |         EuclideanIntegerPoint pt1 = new EuclideanIntegerPoint(new int[] { 1959, 325100 });
113 |         EuclideanIntegerPoint pt2 = new EuclideanIntegerPoint(new int[] { 1960, 373200 });
114 |         assertTrue(clusters.get(0).getPoints().contains(pt1));
115 |         assertTrue(clusters.get(0).getPoints().contains(pt2));
116 | 
117 |     } 
```
