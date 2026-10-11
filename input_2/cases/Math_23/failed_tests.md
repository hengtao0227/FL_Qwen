# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.univariate.BrentOptimizerTest.testKeepInitIfBest()
Resolved declaration: org.apache.commons.math3.optimization.univariate.BrentOptimizerTest.testKeepInitIfBest()
Source: src/test/java/org/apache/commons/math3/optimization/univariate/BrentOptimizerTest.java

```java
192 |     @Test
193 |     public void testKeepInitIfBest() {
194 |         final double minSin = 3 * Math.PI / 2;
195 |         final double offset = 1e-8;
196 |         final double delta = 1e-7;
197 |         final UnivariateFunction f1 = new Sin();
198 |         final UnivariateFunction f2 = new StepFunction(new double[] { minSin, minSin + offset, minSin + 2 * offset},
199 |                                                        new double[] { 0, -1, 0 });
200 |         final UnivariateFunction f = FunctionUtils.add(f1, f2);
201 |         // A slightly less stringent tolerance would make the test pass
202 |         // even with the previous implementation.
203 |         final double relTol = 1e-8;
204 |         final UnivariateOptimizer optimizer = new BrentOptimizer(relTol, 1e-100);
205 |         final double init = minSin + 1.5 * offset;
206 |         final UnivariatePointValuePair result
207 |             = optimizer.optimize(200, f, GoalType.MINIMIZE,
208 |                                  minSin - 6.789 * delta,
209 |                                  minSin + 9.876 * delta,
210 |                                  init);
211 |         final int numEval = optimizer.getEvaluations();
212 | 
213 |         final double sol = result.getPoint();
214 |         final double expected = init;
215 | 
216 | //         System.out.println("numEval=" + numEval);
217 | //         System.out.println("min=" + init + " f=" + f.value(init));
218 | //         System.out.println("sol=" + sol + " f=" + f.value(sol));
219 | //         System.out.println("exp=" + expected + " f=" + f.value(expected));
220 | 
221 |         Assert.assertTrue("Best point not reported", f.value(sol) <= f.value(expected));
222 |     }
```
