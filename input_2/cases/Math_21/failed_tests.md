# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.linear.RectangularCholeskyDecompositionTest.testMath789()
Resolved declaration: org.apache.commons.math3.linear.RectangularCholeskyDecompositionTest.testMath789()
Source: src/test/java/org/apache/commons/math3/linear/RectangularCholeskyDecompositionTest.java

```java
75 |     @Test
76 |     public void testMath789() {
77 | 
78 |         final RealMatrix m1 = MatrixUtils.createRealMatrix(new double[][]{
79 |             {0.013445532, 0.010394690, 0.009881156, 0.010499559},
80 |             {0.010394690, 0.023006616, 0.008196856, 0.010732709},
81 |             {0.009881156, 0.008196856, 0.019023866, 0.009210099},
82 |             {0.010499559, 0.010732709, 0.009210099, 0.019107243}
83 |         });
84 |         RealMatrix root1 = new RectangularCholeskyDecomposition(m1, 1.0e-10).getRootMatrix();
85 |         RealMatrix rebuiltM1 = root1.multiply(root1.transpose());
86 |         Assert.assertEquals(0.0, m1.subtract(rebuiltM1).getNorm(), 1.0e-16);
87 | 
88 |         final RealMatrix m2 = MatrixUtils.createRealMatrix(new double[][]{
89 |             {0.0, 0.0, 0.0, 0.0, 0.0},
90 |             {0.0, 0.013445532, 0.010394690, 0.009881156, 0.010499559},
91 |             {0.0, 0.010394690, 0.023006616, 0.008196856, 0.010732709},
92 |             {0.0, 0.009881156, 0.008196856, 0.019023866, 0.009210099},
93 |             {0.0, 0.010499559, 0.010732709, 0.009210099, 0.019107243}
94 |         });
95 |         RealMatrix root2 = new RectangularCholeskyDecomposition(m2, 1.0e-10).getRootMatrix();
96 |         RealMatrix rebuiltM2 = root2.multiply(root2.transpose());
97 |         Assert.assertEquals(0.0, m2.subtract(rebuiltM2).getNorm(), 1.0e-16);
98 | 
99 |         final RealMatrix m3 = MatrixUtils.createRealMatrix(new double[][]{
100 |             {0.013445532, 0.010394690, 0.0, 0.009881156, 0.010499559},
101 |             {0.010394690, 0.023006616, 0.0, 0.008196856, 0.010732709},
102 |             {0.0, 0.0, 0.0, 0.0, 0.0},
103 |             {0.009881156, 0.008196856, 0.0, 0.019023866, 0.009210099},
104 |             {0.010499559, 0.010732709, 0.0, 0.009210099, 0.019107243}
105 |         });
106 |         RealMatrix root3 = new RectangularCholeskyDecomposition(m3, 1.0e-10).getRootMatrix();
107 |         RealMatrix rebuiltM3 = root3.multiply(root3.transpose());
108 |         Assert.assertEquals(0.0, m3.subtract(rebuiltM3).getNorm(), 1.0e-16);
109 | 
110 |     }
```

## org.apache.commons.math3.linear.RectangularCholeskyDecompositionTest.testFullRank()
Resolved declaration: org.apache.commons.math3.linear.RectangularCholeskyDecompositionTest.testFullRank()
Source: src/test/java/org/apache/commons/math3/linear/RectangularCholeskyDecompositionTest.java

```java
50 |     @Test
51 |     public void testFullRank() {
52 | 
53 |         RealMatrix base = MatrixUtils.createRealMatrix(new double[][] {
54 |             { 0.1159548705,      0.,           0.,           0.      },
55 |             { 0.0896442724, 0.1223540781,      0.,           0.      },
56 |             { 0.0852155322, 4.558668e-3,  0.1083577299,      0.      },
57 |             { 0.0905486674, 0.0213768077, 0.0128878333, 0.1014155693 }
58 |         });
59 | 
60 |         RealMatrix m = base.multiply(base.transpose());
61 | 
62 |         RectangularCholeskyDecomposition d =
63 |                 new RectangularCholeskyDecomposition(m, 1.0e-10);
64 | 
65 |         RealMatrix root = d.getRootMatrix();
66 |         RealMatrix rebuiltM = root.multiply(root.transpose());
67 |         Assert.assertEquals(0.0, m.subtract(rebuiltM).getNorm(), 1.0e-15);
68 | 
69 |         // the pivoted Cholesky decomposition is *not* unique. Here, the root is
70 |         // not equal to the original trianbular base matrix
71 |         Assert.assertTrue(root.subtract(base).getNorm() > 0.3);
72 | 
73 |     }
```
