# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.univariate.MultiStartUnivariateRealOptimizerTest.testQuinticMin()
Resolved declaration: org.apache.commons.math.optimization.univariate.MultiStartUnivariateRealOptimizerTest.testQuinticMin()
Source: src/test/java/org/apache/commons/math/optimization/univariate/MultiStartUnivariateRealOptimizerTest.java

```java
57 |     @Test
58 |     public void testQuinticMin() throws MathException {
59 |         // The quintic function has zeros at 0, +-0.5 and +-1.
60 |         // The function has extrema (first derivative is zero) at 0.27195613 and 0.82221643,
61 |         UnivariateRealFunction f = new QuinticFunction();
62 |         UnivariateRealOptimizer underlying = new BrentOptimizer(1e-9, 1e-14);
63 |         underlying.setMaxEvaluations(300);
64 |         JDKRandomGenerator g = new JDKRandomGenerator();
65 |         g.setSeed(4312000053L);
66 |         MultiStartUnivariateRealOptimizer optimizer =
67 |             new MultiStartUnivariateRealOptimizer(underlying, 5, g);
68 | 
69 |         UnivariateRealPointValuePair optimum
70 |             = optimizer.optimize(f, GoalType.MINIMIZE, -0.3, -0.2);
71 |         assertEquals(-0.2719561293, optimum.getPoint(), 1e-9);
72 |         assertEquals(-0.0443342695, optimum.getValue(), 1e-9);
73 | 
74 |         UnivariateRealPointValuePair[] optima = optimizer.getOptima();
75 |         for (int i = 0; i < optima.length; ++i) {
76 |             assertEquals(f.value(optima[i].getPoint()), optima[i].getValue(), 1e-9);
77 |         }
78 |         assertTrue(optimizer.getEvaluations() >= 50);
79 |         assertTrue(optimizer.getEvaluations() <= 100);
80 |     }
```
