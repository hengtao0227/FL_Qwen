# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.clustering.KMeansPlusPlusClustererTest.testSmallDistances()
Resolved declaration: org.apache.commons.math.stat.clustering.KMeansPlusPlusClustererTest.testSmallDistances()
Source: src/test/java/org/apache/commons/math/stat/clustering/KMeansPlusPlusClustererTest.java

```java
214 |     @Test
215 |     public void testSmallDistances() {
216 |         // Create a bunch of CloseIntegerPoints. Most are identical, but one is different by a
217 |         // small distance.
218 |         int[] repeatedArray = { 0 };
219 |         int[] uniqueArray = { 1 };
220 |         CloseIntegerPoint repeatedPoint =
221 |             new CloseIntegerPoint(new EuclideanIntegerPoint(repeatedArray));
222 |         CloseIntegerPoint uniquePoint =
223 |             new CloseIntegerPoint(new EuclideanIntegerPoint(uniqueArray));
224 | 
225 |         Collection<CloseIntegerPoint> points = new ArrayList<CloseIntegerPoint>();
226 |         final int NUM_REPEATED_POINTS = 10 * 1000;
227 |         for (int i = 0; i < NUM_REPEATED_POINTS; ++i) {
228 |             points.add(repeatedPoint);
229 |         }
230 |         points.add(uniquePoint);
231 | 
232 |         // Ask a KMeansPlusPlusClusterer to run zero iterations (i.e., to simply choose initial
233 |         // cluster centers).
234 |         final long RANDOM_SEED = 0;
235 |         final int NUM_CLUSTERS = 2;
236 |         final int NUM_ITERATIONS = 0;
237 |         KMeansPlusPlusClusterer<CloseIntegerPoint> clusterer =
238 |             new KMeansPlusPlusClusterer<CloseIntegerPoint>(new Random(RANDOM_SEED));
239 |         List<Cluster<CloseIntegerPoint>> clusters =
240 |             clusterer.cluster(points, NUM_CLUSTERS, NUM_ITERATIONS);
241 | 
242 |         // Check that one of the chosen centers is the unique point.
243 |         boolean uniquePointIsCenter = false;
244 |         for (Cluster<CloseIntegerPoint> cluster : clusters) {
245 |             if (cluster.getCenter().equals(uniquePoint)) {
246 |                 uniquePointIsCenter = true;
247 |             }
248 |         }
249 |         assertTrue(uniquePointIsCenter);
250 |     }
```
