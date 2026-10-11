# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.linear.CholeskyDecompositionImplTest.testMath274()
Resolved declaration: org.apache.commons.math.linear.CholeskyDecompositionImplTest.testMath274()
Source: src/test/org/apache/commons/math/linear/CholeskyDecompositionImplTest.java

```java
81 |     @Test(expected = NotPositiveDefiniteMatrixException.class)
82 |     public void testMath274() throws MathException {
83 |         new CholeskyDecompositionImpl(MatrixUtils.createRealMatrix(new double[][] {
84 |                 { 0.40434286, -0.09376327, 0.30328980, 0.04909388 },
85 |                 {-0.09376327,  0.10400408, 0.07137959, 0.04762857 },
86 |                 { 0.30328980,  0.07137959, 0.30458776, 0.04882449 },
87 |                 { 0.04909388,  0.04762857, 0.04882449, 0.07543265 }
88 |             
89 |         }));
90 |     }
```

## org.apache.commons.math.linear.CholeskyDecompositionImplTest.testNotPositiveDefinite()
Resolved declaration: org.apache.commons.math.linear.CholeskyDecompositionImplTest.testNotPositiveDefinite()
Source: src/test/org/apache/commons/math/linear/CholeskyDecompositionImplTest.java

```java
69 |     @Test(expected = NotPositiveDefiniteMatrixException.class)
70 |     public void testNotPositiveDefinite() throws MathException {
71 |         CholeskyDecomposition cd = new CholeskyDecompositionImpl(MatrixUtils.createRealMatrix(new double[][] {
72 |                 { 14, 11, 13, 15, 24 },
73 |                 { 11, 34, 13, 8,  25 },
74 |                 { 13, 13, 14, 15, 21 },
75 |                 { 15, 8,  15, 18, 23 },
76 |                 { 24, 25, 21, 23, 45 }
77 |         }));
78 |         System.out.println(cd.getL().multiply(cd.getLT()));
79 |     }
```
