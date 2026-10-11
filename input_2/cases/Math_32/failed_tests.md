# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.geometry.euclidean.threed.PolyhedronsSetTest.testIssue780()
Resolved declaration: org.apache.commons.math3.geometry.euclidean.threed.PolyhedronsSetTest.testIssue780()
Source: src/test/java/org/apache/commons/math3/geometry/euclidean/threed/PolyhedronsSetTest.java

```java
236 |     @Test
237 |     public void testIssue780() {
238 |         float[] coords = {
239 |             1.000000f, -1.000000f, -1.000000f, 
240 |             1.000000f, -1.000000f, 1.000000f, 
241 |             -1.000000f, -1.000000f, 1.000000f, 
242 |             -1.000000f, -1.000000f, -1.000000f, 
243 |             1.000000f, 1.000000f, -1f, 
244 |             0.999999f, 1.000000f, 1.000000f,   // 1.000000f, 1.000000f, 1.000000f, 
245 |             -1.000000f, 1.000000f, 1.000000f, 
246 |             -1.000000f, 1.000000f, -1.000000f};
247 |         int[] indices = {
248 |             0, 1, 2, 0, 2, 3, 
249 |             4, 7, 6, 4, 6, 5, 
250 |             0, 4, 5, 0, 5, 1, 
251 |             1, 5, 6, 1, 6, 2, 
252 |             2, 6, 7, 2, 7, 3, 
253 |             4, 0, 3, 4, 3, 7};
254 |         ArrayList<SubHyperplane<Euclidean3D>> subHyperplaneList = new ArrayList<SubHyperplane<Euclidean3D>>();
255 |         for (int idx = 0; idx < indices.length; idx += 3) {
256 |             int idxA = indices[idx] * 3;
257 |             int idxB = indices[idx + 1] * 3;
258 |             int idxC = indices[idx + 2] * 3;
259 |             Vector3D v_1 = new Vector3D(coords[idxA], coords[idxA + 1], coords[idxA + 2]);
260 |             Vector3D v_2 = new Vector3D(coords[idxB], coords[idxB + 1], coords[idxB + 2]);
261 |             Vector3D v_3 = new Vector3D(coords[idxC], coords[idxC + 1], coords[idxC + 2]);
262 |             Vector3D[] vertices = {v_1, v_2, v_3};
263 |             Plane polyPlane = new Plane(v_1, v_2, v_3);
264 |             ArrayList<SubHyperplane<Euclidean2D>> lines = new ArrayList<SubHyperplane<Euclidean2D>>();
265 | 
266 |             Vector2D[] projPts = new Vector2D[vertices.length];
267 |             for (int ptIdx = 0; ptIdx < projPts.length; ptIdx++) {
268 |                 projPts[ptIdx] = polyPlane.toSubSpace(vertices[ptIdx]);
269 |             }
270 | 
271 |             SubLine lineInPlane = null;
272 |             for (int ptIdx = 0; ptIdx < projPts.length; ptIdx++) {
273 |                 lineInPlane = new SubLine(projPts[ptIdx], projPts[(ptIdx + 1) % projPts.length]);
274 |                 lines.add(lineInPlane);
275 |             }
276 |             Region<Euclidean2D> polyRegion = new PolygonsSet(lines);
277 |             SubPlane polygon = new SubPlane(polyPlane, polyRegion);
278 |             subHyperplaneList.add(polygon);
279 |         }
280 |         PolyhedronsSet polyhedronsSet = new PolyhedronsSet(subHyperplaneList);
281 |         Assert.assertEquals( 8.0, polyhedronsSet.getSize(), 3.0e-6);
282 |         Assert.assertEquals(24.0, polyhedronsSet.getBoundarySize(), 5.0e-6);
283 |     }
```
