# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.direct.BOBYQAOptimizerTest.testConstrainedRosenWithMoreInterpolationPoints()
Resolved declaration: org.apache.commons.math.optimization.direct.BOBYQAOptimizerTest.testConstrainedRosenWithMoreInterpolationPoints()
Source: src/test/java/org/apache/commons/math/optimization/direct/BOBYQAOptimizerTest.java

```java
235 |     @Test
236 |     public void testConstrainedRosenWithMoreInterpolationPoints() {
237 |         final double[] startPoint = point(DIM, 0.1);
238 |         final double[][] boundaries = boundaries(DIM, -1, 2);
239 |         final RealPointValuePair expected = new RealPointValuePair(point(DIM, 1.0), 0.0);
240 | 
241 |         // This should have been 78 because in the code the hard limit is
242 |         // said to be
243 |         //   ((DIM + 1) * (DIM + 2)) / 2 - (2 * DIM + 1)
244 |         // i.e. 78 in this case, but the test fails for 48, 59, 62, 63, 64,
245 |         // 65, 66, ...
246 |         final int maxAdditionalPoints = 47;
247 | 
248 |         for (int num = 1; num <= maxAdditionalPoints; num++) {
249 |             doTest(new Rosen(), startPoint, boundaries,
250 |                    GoalType.MINIMIZE,
251 |                    1e-12, 1e-6, 2000,
252 |                    num,
253 |                    expected,
254 |                    "num=" + num);
255 |         }
256 |     }
```
