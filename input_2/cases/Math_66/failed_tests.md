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
61 |         underlying.setRelativeAccuracy(1e-15);
62 |         JDKRandomGenerator g = new JDKRandomGenerator();
63 |         g.setSeed(4312000053L);
64 |         MultiStartUnivariateRealOptimizer minimizer =
65 |             new MultiStartUnivariateRealOptimizer(underlying, 5, g);
66 |         minimizer.setAbsoluteAccuracy(10 * minimizer.getAbsoluteAccuracy());
67 |         minimizer.setRelativeAccuracy(10 * minimizer.getRelativeAccuracy());
68 | 
69 |         try {
70 |             minimizer.getOptima();
71 |             fail("an exception should have been thrown");
72 |         } catch (IllegalStateException ise) {
73 |             // expected
74 |         } catch (Exception e) {
75 |             fail("wrong exception caught");
76 |         }
77 |         try {
78 |             minimizer.getOptimaValues();
79 |             fail("an exception should have been thrown");
80 |         } catch (IllegalStateException ise) {
81 |             // expected
82 |         } catch (Exception e) {
83 |             fail("wrong exception caught");
84 |         }
85 | 
86 |         double result = minimizer.optimize(f, GoalType.MINIMIZE, -0.3, -0.2);
87 |         assertEquals(-0.2719561270319131, result, 1.0e-13);
88 |         assertEquals(-0.2719561270319131, minimizer.getResult(), 1.0e-13);
89 |         assertEquals(-0.04433426954946637, minimizer.getFunctionValue(), 1.0e-13);
90 | 
91 |         double[] optima = minimizer.getOptima();
92 |         double[] optimaValues = minimizer.getOptimaValues();
93 |         for (int i = 0; i < optima.length; ++i) {
94 |             assertEquals(f.value(optima[i]), optimaValues[i], 1.0e-10);
95 |         }
96 |         assertTrue(minimizer.getEvaluations()    >= 120);
97 |         assertTrue(minimizer.getEvaluations()    <= 170);
98 |         assertTrue(minimizer.getIterationCount() >= 120);
99 |         assertTrue(minimizer.getIterationCount() <= 170);
100 |     }
```

## org.apache.commons.math.optimization.MultiStartUnivariateRealOptimizerTest.testSinMin()
Resolved declaration: org.apache.commons.math.optimization.MultiStartUnivariateRealOptimizerTest.testSinMin()
Source: src/test/java/org/apache/commons/math/optimization/MultiStartUnivariateRealOptimizerTest.java

```java
34 |     @Test
35 |     public void testSinMin() throws MathException {
36 |         UnivariateRealFunction f = new SinFunction();
37 |         UnivariateRealOptimizer underlying = new BrentOptimizer();
38 |         JDKRandomGenerator g = new JDKRandomGenerator();
39 |         g.setSeed(44428400075l);
40 |         MultiStartUnivariateRealOptimizer minimizer =
41 |             new MultiStartUnivariateRealOptimizer(underlying, 10, g);
42 |         minimizer.optimize(f, GoalType.MINIMIZE, -100.0, 100.0);
43 |         double[] optima = minimizer.getOptima();
44 |         double[] optimaValues = minimizer.getOptimaValues();
45 |         for (int i = 1; i < optima.length; ++i) {
46 |             double d = (optima[i] - optima[i-1]) / (2 * Math.PI);
47 |             assertTrue (Math.abs(d - Math.rint(d)) < 1.0e-8);
48 |             assertEquals(-1.0, f.value(optima[i]), 1.0e-10);
49 |             assertEquals(f.value(optima[i]), optimaValues[i], 1.0e-10);
50 |         }
51 |         assertTrue(minimizer.getEvaluations() > 150);
52 |         assertTrue(minimizer.getEvaluations() < 250);
53 |     }
```

## org.apache.commons.math.optimization.univariate.BrentOptimizerTest.testQuinticMinStatistics()
Resolved declaration: org.apache.commons.math.optimization.univariate.BrentOptimizerTest.testQuinticMinStatistics()
Source: src/test/java/org/apache/commons/math/optimization/univariate/BrentOptimizerTest.java

```java
85 |     @Test
86 |     public void testQuinticMinStatistics() throws MathException {
87 |         // The function has local minima at -0.27195613 and 0.82221643.
88 |         UnivariateRealFunction f = new QuinticFunction();
89 |         UnivariateRealOptimizer minimizer = new BrentOptimizer();
90 |         minimizer.setRelativeAccuracy(1e-10);
91 |         minimizer.setAbsoluteAccuracy(1e-11);
92 | 
93 |         final DescriptiveStatistics[] stat = new DescriptiveStatistics[3];
94 |         for (int i = 0; i < stat.length; i++) {
95 |             stat[i] = new DescriptiveStatistics();
96 |         }
97 | 
98 |         final double min = -0.75;
99 |         final double max = 0.25;
100 |         final int nSamples = 200;
101 |         final double delta = (max - min) / nSamples;
102 |         for (int i = 0; i < nSamples; i++) {
103 |             final double start = min + i * delta;
104 |             stat[0].addValue(minimizer.optimize(f, GoalType.MINIMIZE, min, max, start));
105 |             stat[1].addValue(minimizer.getIterationCount());
106 |             stat[2].addValue(minimizer.getEvaluations());
107 |         }
108 | 
109 |         final double meanOptValue = stat[0].getMean();
110 |         final double medianIter = stat[1].getPercentile(50);
111 |         final double medianEval = stat[2].getPercentile(50);
112 |         assertTrue(meanOptValue > -0.27195612812 && meanOptValue < -0.27195612811);
113 |         assertEquals(medianIter, 17, Math.ulp(1d));
114 |         assertEquals(medianEval, 18, Math.ulp(1d));
115 |     }
```

## org.apache.commons.math.optimization.univariate.BrentOptimizerTest.testSinMin()
Resolved declaration: org.apache.commons.math.optimization.univariate.BrentOptimizerTest.testSinMin()
Source: src/test/java/org/apache/commons/math/optimization/univariate/BrentOptimizerTest.java

```java
40 |     @Test
41 |     public void testSinMin() throws MathException {
42 |         UnivariateRealFunction f = new SinFunction();
43 |         UnivariateRealOptimizer minimizer = new BrentOptimizer();
44 |         minimizer.setMaxEvaluations(200);
45 |         assertEquals(200, minimizer.getMaxEvaluations());
46 |         try {
47 |             minimizer.getResult();
48 |             fail("an exception should have been thrown");
49 |         } catch (NoDataException ise) {
50 |             // expected
51 |         } catch (Exception e) {
52 |             fail("wrong exception caught");
53 |         }
54 |         assertEquals(3 * Math.PI / 2, minimizer.optimize(f, GoalType.MINIMIZE, 4, 5), 10 * minimizer.getRelativeAccuracy());
55 |         assertTrue(minimizer.getIterationCount() <= 50);
56 |         assertEquals(3 * Math.PI / 2, minimizer.optimize(f, GoalType.MINIMIZE, 1, 5), 10 * minimizer.getRelativeAccuracy());
57 |         assertTrue(minimizer.getIterationCount() <= 50);
58 |         assertTrue(minimizer.getEvaluations()    <= 100);
59 |         assertTrue(minimizer.getEvaluations()    >=  15);
60 |         minimizer.setMaxEvaluations(10);
61 |         try {
62 |             minimizer.optimize(f, GoalType.MINIMIZE, 4, 5);
63 |             fail("an exception should have been thrown");
64 |         } catch (FunctionEvaluationException fee) {
65 |             // expected
66 |         } catch (Exception e) {
67 |             fail("wrong exception caught");
68 |         }
69 |     }
```
