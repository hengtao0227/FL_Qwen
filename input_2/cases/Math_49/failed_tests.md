# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.linear.SparseRealVectorTest.testConcurrentModification()
Resolved declaration: org.apache.commons.math.linear.SparseRealVectorTest.testConcurrentModification()
Source: src/test/java/org/apache/commons/math/linear/SparseRealVectorTest.java

```java
1003 |     @Test
1004 |     public void testConcurrentModification() {
1005 |         final RealVector u = new OpenMapRealVector(3, 1e-6);
1006 |         u.setEntry(0, 1);
1007 |         u.setEntry(1, 0);
1008 |         u.setEntry(2, 2);
1009 | 
1010 |         final RealVector v1 = new OpenMapRealVector(3, 1e-6);
1011 |         final double[] v2 = new double[3];
1012 |         v1.setEntry(0, 0);
1013 |         v2[0] = 0;
1014 |         v1.setEntry(1, 3);
1015 |         v2[1] = 3;
1016 |         v1.setEntry(2, 0);
1017 |         v2[2] = 0;
1018 | 
1019 |         RealVector w;
1020 | 
1021 |         w = u.ebeMultiply(v1);
1022 |         w = u.ebeMultiply(v2);
1023 | 
1024 |         w = u.ebeDivide(v1);
1025 |         w = u.ebeDivide(v2);
1026 |     }
```
