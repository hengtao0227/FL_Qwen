# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.geometry.euclidean.threed.SubLineTest.testIntersectionNotIntersecting()
Resolved declaration: org.apache.commons.math3.geometry.euclidean.threed.SubLineTest.testIntersectionNotIntersecting()
Source: src/test/java/org/apache/commons/math3/geometry/euclidean/threed/SubLineTest.java

```java
156 |     @Test
157 |     public void testIntersectionNotIntersecting() throws MathIllegalArgumentException {
158 |         SubLine sub1 = new SubLine(new Vector3D(1, 1, 1), new Vector3D(1.5, 1, 1));
159 |         SubLine sub2 = new SubLine(new Vector3D(2, 3, 0), new Vector3D(2, 3, 0.5));
160 |         Assert.assertNull(sub1.intersection(sub2, true));
161 |         Assert.assertNull(sub1.intersection(sub2, false));
162 |     }
```

## org.apache.commons.math3.geometry.euclidean.twod.SubLineTest.testIntersectionParallel()
Resolved declaration: org.apache.commons.math3.geometry.euclidean.twod.SubLineTest.testIntersectionParallel()
Source: src/test/java/org/apache/commons/math3/geometry/euclidean/twod/SubLineTest.java

```java
147 |     @Test
148 |     public void testIntersectionParallel() {
149 |         final SubLine sub1 = new SubLine(new Vector2D(0, 1), new Vector2D(0, 2));
150 |         final SubLine sub2 = new SubLine(new Vector2D(66, 3), new Vector2D(66, 4));
151 |         Assert.assertNull(sub1.intersection(sub2, true));
152 |         Assert.assertNull(sub1.intersection(sub2, false));
153 |     }
```
