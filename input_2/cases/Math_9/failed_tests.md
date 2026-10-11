# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.geometry.euclidean.threed.LineTest.testRevert()
Resolved declaration: org.apache.commons.math3.geometry.euclidean.threed.LineTest.testRevert()
Source: src/test/java/org/apache/commons/math3/geometry/euclidean/threed/LineTest.java

```java
132 |     @Test
133 |     public void testRevert() {
134 |         
135 |         // setup
136 |         Line line = new Line(new Vector3D(1653345.6696423641, 6170370.041579291, 90000),
137 |                              new Vector3D(1650757.5050732433, 6160710.879908984, 0.9));
138 |         Vector3D expected = line.getDirection().negate();
139 | 
140 |         // action
141 |         Line reverted = line.revert();
142 | 
143 |         // verify
144 |         Assert.assertArrayEquals(expected.toArray(), reverted.getDirection().toArray(), 0);
145 | 
146 |     }
```
