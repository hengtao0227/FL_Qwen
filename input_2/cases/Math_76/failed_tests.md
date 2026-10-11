# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.linear.SingularValueSolverTest.testMath320A()
Resolved declaration: org.apache.commons.math.linear.SingularValueSolverTest.testMath320A()
Source: src/test/java/org/apache/commons/math/linear/SingularValueSolverTest.java

```java
167 |     @Test
168 |     public void testMath320A() {
169 |         RealMatrix rm = new Array2DRowRealMatrix(new double[][] {
170 |             { 1.0, 2.0, 3.0 }, { 2.0, 3.0, 4.0 }, { 3.0, 5.0, 7.0 }
171 |         });
172 |         double s439  = Math.sqrt(439.0);
173 |         double[] reference = new double[] {
174 |             Math.sqrt(3.0 * (21.0 + s439)), Math.sqrt(3.0 * (21.0 - s439))
175 |         };
176 |         SingularValueDecomposition svd =
177 |             new SingularValueDecompositionImpl(rm);
178 | 
179 |         // check we get the expected theoretical singular values
180 |         double[] singularValues = svd.getSingularValues();
181 |         Assert.assertEquals(reference.length, singularValues.length);
182 |         for (int i = 0; i < reference.length; ++i) {
183 |             Assert.assertEquals(reference[i], singularValues[i], 4.0e-13);
184 |         }
185 | 
186 |         // check the decomposition allows to recover the original matrix
187 |         RealMatrix recomposed = svd.getU().multiply(svd.getS()).multiply(svd.getVT());
188 |         Assert.assertEquals(0.0, recomposed.subtract(rm).getNorm(), 5.0e-13);
189 | 
190 |         // check we can solve a singular system
191 |         double[] b = new double[] { 5.0, 6.0, 7.0 };
192 |         double[] resSVD = svd.getSolver().solve(b);
193 |         Assert.assertEquals(rm.getColumnDimension(), resSVD.length);
194 | 
195 |         // check the solution really minimizes the residuals
196 |         double svdMinResidual = residual(rm, resSVD, b);
197 |         double epsilon = 2 * Math.ulp(svdMinResidual);
198 |         double h = 0.1;
199 |         int    k = 3;
200 |         for (double d0 = -k * h; d0 <= k * h; d0 += h) {
201 |             for (double d1 = -k * h ; d1 <= k * h; d1 += h) {
202 |                 for (double d2 = -k * h; d2 <= k * h; d2 += h) {
203 |                     double[] x = new double[] { resSVD[0] + d0, resSVD[1] + d1, resSVD[2] + d2 };
204 |                     Assert.assertTrue((residual(rm, x, b) - svdMinResidual) > -epsilon);
205 |                 }
206 |             }
207 |         }
208 | 
209 |     }
```

## org.apache.commons.math.linear.SingularValueSolverTest.testMath320B()
Resolved declaration: org.apache.commons.math.linear.SingularValueSolverTest.testMath320B()
Source: src/test/java/org/apache/commons/math/linear/SingularValueSolverTest.java

```java
211 |     @Test
212 |     public void testMath320B() {
213 |         RealMatrix rm = new Array2DRowRealMatrix(new double[][] {
214 |             { 1.0, 2.0 }, { 1.0, 2.0 }
215 |         });
216 |         SingularValueDecomposition svd =
217 |             new SingularValueDecompositionImpl(rm);
218 |         RealMatrix recomposed = svd.getU().multiply(svd.getS()).multiply(svd.getVT());
219 |         Assert.assertEquals(0.0, recomposed.subtract(rm).getNorm(), 2.0e-15);
220 |     }
```
