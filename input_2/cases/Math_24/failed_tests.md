# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.univariate.BrentOptimizerTest.testMath855()
Resolved declaration: org.apache.commons.math3.optimization.univariate.BrentOptimizerTest.testMath855()
Source: src/test/java/org/apache/commons/math3/optimization/univariate/BrentOptimizerTest.java

```java
192 |     @Test
193 |     public void testMath855() {
194 |         final double minSin = 3 * Math.PI / 2;
195 |         final double offset = 1e-8;
196 |         final double delta = 1e-7;
197 |         final UnivariateFunction f1 = new Sin();
198 |         final UnivariateFunction f2 = new StepFunction(new double[] { minSin, minSin + offset, minSin + 5 * offset },
199 |                                                        new double[] { 0, -1, 0 });
200 |         final UnivariateFunction f = FunctionUtils.add(f1, f2);
201 |         final UnivariateOptimizer optimizer = new BrentOptimizer(1e-8, 1e-100);
202 |         final UnivariatePointValuePair result
203 |             = optimizer.optimize(200, f, GoalType.MINIMIZE, minSin - 6.789 * delta, minSin + 9.876 * delta);
204 |         final int numEval = optimizer.getEvaluations();
205 | 
206 |         final double sol = result.getPoint();
207 |         final double expected = 4.712389027602411;
208 | 
209 |         // System.out.println("min=" + (minSin + offset) + " f=" + f.value(minSin + offset));
210 |         // System.out.println("sol=" + sol + " f=" + f.value(sol));
211 |         // System.out.println("exp=" + expected + " f=" + f.value(expected));
212 | 
213 |         Assert.assertTrue("Best point not reported", f.value(sol) <= f.value(expected));
214 |     }
```
