# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.fitting.HarmonicFitterTest.testMath844()
Resolved declaration: org.apache.commons.math3.optimization.fitting.HarmonicFitterTest.testMath844()
Source: src/test/java/org/apache/commons/math3/optimization/fitting/HarmonicFitterTest.java

```java
181 |     @Test(expected=MathIllegalStateException.class)
182 |     public void testMath844() {
183 |         final double[] y = { 0, 1, 2, 3, 2, 1,
184 |                              0, -1, -2, -3, -2, -1,
185 |                              0, 1, 2, 3, 2, 1,
186 |                              0, -1, -2, -3, -2, -1,
187 |                              0, 1, 2, 3, 2, 1, 0 };
188 |         final int len = y.length;
189 |         final WeightedObservedPoint[] points = new WeightedObservedPoint[len];
190 |         for (int i = 0; i < len; i++) {
191 |             points[i] = new WeightedObservedPoint(1, i, y[i]);
192 |         }
193 | 
194 |         final HarmonicFitter.ParameterGuesser guesser
195 |             = new HarmonicFitter.ParameterGuesser(points);
196 | 
197 |         // The guesser fails because the function is far from an harmonic
198 |         // function: It is a triangular periodic function with amplitude 3
199 |         // and period 12, and all sample points are taken at integer abscissae
200 |         // so function values all belong to the integer subset {-3, -2, -1, 0,
201 |         // 1, 2, 3}.
202 |         guesser.guess();
203 |     }
```
