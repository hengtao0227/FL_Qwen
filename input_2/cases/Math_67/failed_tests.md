# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.MultiStartUnivariateRealOptimizerTest.testQuinticMin()
Resolved declaration: org.apache.commons.math.optimization.MultiStartUnivariateRealOptimizerTest.testQuinticMin()
Source: src/test/java/org/apache/commons/math/optimization/MultiStartUnivariateRealOptimizerTest.java

```java
55 |     @Test
56 |     public void testQuinticMin() throws MathException {
57 |         // The quintic function has zeros at 0, +-0.5 and +-1.
58 |         // The function has extrema (first derivative is zero) at 0.27195613 and 0.82221643,
59 |         UnivariateRealFunction f = new QuinticFunction();
60 |         UnivariateRealOptimizer underlying = new BrentOptimizer();
61 |         JDKRandomGenerator g = new JDKRandomGenerator();
62 |         g.setSeed(4312000053l);
63 |         MultiStartUnivariateRealOptimizer minimizer =
64 |             new MultiStartUnivariateRealOptimizer(underlying, 5, g);
65 |         minimizer.setAbsoluteAccuracy(10 * minimizer.getAbsoluteAccuracy());
66 |         minimizer.setRelativeAccuracy(10 * minimizer.getRelativeAccuracy());
67 | 
68 |         try {
69 |             minimizer.getOptima();
70 |             fail("an exception should have been thrown");
71 |         } catch (IllegalStateException ise) {
72 |             // expected
73 |         } catch (Exception e) {
74 |             fail("wrong exception caught");
75 |         }
76 |         try {
77 |             minimizer.getOptimaValues();
78 |             fail("an exception should have been thrown");
79 |         } catch (IllegalStateException ise) {
80 |             // expected
81 |         } catch (Exception e) {
82 |             fail("wrong exception caught");
83 |         }
84 | 
85 |         assertEquals(-0.27195612846834, minimizer.optimize(f, GoalType.MINIMIZE, -0.3, -0.2), 1.0e-13);
86 |         assertEquals(-0.27195612846834, minimizer.getResult(), 1.0e-13);
87 |         assertEquals(-0.04433426954946, minimizer.getFunctionValue(), 1.0e-13);
88 | 
89 |         double[] optima = minimizer.getOptima();
90 |         double[] optimaValues = minimizer.getOptimaValues();
91 |         for (int i = 0; i < optima.length; ++i) {
92 |             assertEquals(f.value(optima[i]), optimaValues[i], 1.0e-10);
93 |         }
94 | 
95 |         assertTrue(minimizer.getEvaluations()    >= 510);
96 |         assertTrue(minimizer.getEvaluations()    <= 530);
97 |         assertTrue(minimizer.getIterationCount() >= 150);
98 |         assertTrue(minimizer.getIterationCount() <= 170);
99 | 
100 |     }
```
