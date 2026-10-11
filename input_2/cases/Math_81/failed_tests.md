# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.linear.EigenDecompositionImplTest.testMath308()
Resolved declaration: org.apache.commons.math.linear.EigenDecompositionImplTest.testMath308()
Source: src/test/java/org/apache/commons/math/linear/EigenDecompositionImplTest.java

```java
112 |     public void testMath308() {
113 | 
114 |         double[] mainTridiagonal = {
115 |             22.330154644539597, 46.65485522478641, 17.393672330044705, 54.46687435351116, 80.17800767709437
116 |         };
117 |         double[] secondaryTridiagonal = {
118 |             13.04450406501361, -5.977590941539671, 2.9040909856707517, 7.1570352792841225
119 |         };
120 | 
121 |         // the reference values have been computed using routine DSTEMR
122 |         // from the fortran library LAPACK version 3.2.1
123 |         double[] refEigenValues = {
124 |             82.044413207204002, 53.456697699894512, 52.536278520113882, 18.847969733754262, 14.138204224043099
125 |         };
126 |         RealVector[] refEigenVectors = {
127 |             new ArrayRealVector(new double[] { -0.000462690386766, -0.002118073109055,  0.011530080757413,  0.252322434584915,  0.967572088232592 }),
128 |             new ArrayRealVector(new double[] {  0.314647769490148,  0.750806415553905, -0.167700312025760, -0.537092972407375,  0.143854968127780 }),
129 |             new ArrayRealVector(new double[] {  0.222368839324646,  0.514921891363332, -0.021377019336614,  0.801196801016305, -0.207446991247740 }),
130 |             new ArrayRealVector(new double[] {  0.713933751051495, -0.190582113553930,  0.671410443368332, -0.056056055955050,  0.006541576993581 }),
131 |             new ArrayRealVector(new double[] {  0.584677060845929, -0.367177264979103, -0.721453187784497,  0.052971054621812, -0.005740715188257 })
132 |         };
133 | 
134 |         EigenDecomposition decomposition =
135 |             new EigenDecompositionImpl(mainTridiagonal, secondaryTridiagonal, MathUtils.SAFE_MIN);
136 | 
137 |         double[] eigenValues = decomposition.getRealEigenvalues();
138 |         for (int i = 0; i < refEigenValues.length; ++i) {
139 |             assertEquals(refEigenValues[i], eigenValues[i], 1.0e-5);
140 |             assertEquals(0, refEigenVectors[i].subtract(decomposition.getEigenvector(i)).getNorm(), 2.0e-7);
141 |         }
142 | 
143 |     }
```
