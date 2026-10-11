# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.geometry.Vector3DTest.testCrossProductCancellation()
Resolved declaration: org.apache.commons.math.geometry.Vector3DTest.testCrossProductCancellation()
Source: src/test/java/org/apache/commons/math/geometry/Vector3DTest.java

```java
155 |     @Test
156 |     public void testCrossProductCancellation() {
157 |         Vector3D v1 = new Vector3D(9070467121.0, 4535233560.0, 1);
158 |         Vector3D v2 = new Vector3D(9070467123.0, 4535233561.0, 1);
159 |         checkVector(Vector3D.crossProduct(v1, v2), -1, 2, 1);
160 | 
161 |         double scale    = FastMath.scalb(1.0, 100);
162 |         Vector3D big1   = new Vector3D(scale, v1);
163 |         Vector3D small2 = new Vector3D(1 / scale, v2);
164 |         checkVector(Vector3D.crossProduct(big1, small2), -1, 2, 1);
165 | 
166 |     }
```
