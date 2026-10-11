# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.direct.MultiDirectionalTest.testMinimizeMaximize()
Resolved declaration: org.apache.commons.math.optimization.direct.MultiDirectionalTest.testMinimizeMaximize()
Source: src/test/java/org/apache/commons/math/optimization/direct/MultiDirectionalTest.java

```java
69 |   @Test
70 |   public void testMinimizeMaximize()
71 |       throws FunctionEvaluationException, ConvergenceException {
72 | 
73 |       // the following function has 4 local extrema:
74 |       final double xM        = -3.841947088256863675365;
75 |       final double yM        = -1.391745200270734924416;
76 |       final double xP        =  0.2286682237349059125691;
77 |       final double yP        = -yM;
78 |       final double valueXmYm =  0.2373295333134216789769; // local  maximum
79 |       final double valueXmYp = -valueXmYm;                // local  minimum
80 |       final double valueXpYm = -0.7290400707055187115322; // global minimum
81 |       final double valueXpYp = -valueXpYm;                // global maximum
82 |       MultivariateRealFunction fourExtrema = new MultivariateRealFunction() {
83 |           private static final long serialVersionUID = -7039124064449091152L;
84 |           public double value(double[] variables) throws FunctionEvaluationException {
85 |               final double x = variables[0];
86 |               final double y = variables[1];
87 |               return ((x == 0) || (y == 0)) ? 0 : (Math.atan(x) * Math.atan(x + 2) * Math.atan(y) * Math.atan(y) / (x * y));
88 |           }
89 |       };
90 | 
91 |       MultiDirectional optimizer = new MultiDirectional();
92 |       optimizer.setConvergenceChecker(new SimpleScalarValueChecker(1.0e-11, 1.0e-30));
93 |       optimizer.setMaxIterations(200);
94 |       optimizer.setStartConfiguration(new double[] { 0.2, 0.2 });
95 |       RealPointValuePair optimum;
96 | 
97 |       // minimization
98 |       optimum = optimizer.optimize(fourExtrema, GoalType.MINIMIZE, new double[] { -3.0, 0 });
99 |       Assert.assertEquals(xM,        optimum.getPoint()[0], 4.0e-6);
100 |       Assert.assertEquals(yP,        optimum.getPoint()[1], 3.0e-6);
101 |       Assert.assertEquals(valueXmYp, optimum.getValue(),    8.0e-13);
102 |       Assert.assertTrue(optimizer.getEvaluations() > 120);
103 |       Assert.assertTrue(optimizer.getEvaluations() < 150);
104 | 
105 |       optimum = optimizer.optimize(fourExtrema, GoalType.MINIMIZE, new double[] { +1, 0 });
106 |       Assert.assertEquals(xP,        optimum.getPoint()[0], 2.0e-8);
107 |       Assert.assertEquals(yM,        optimum.getPoint()[1], 3.0e-6);
108 |       Assert.assertEquals(valueXpYm, optimum.getValue(),    2.0e-12);              
109 |       Assert.assertTrue(optimizer.getEvaluations() > 120);
110 |       Assert.assertTrue(optimizer.getEvaluations() < 150);
111 | 
112 |       // maximization
113 |       optimum = optimizer.optimize(fourExtrema, GoalType.MAXIMIZE, new double[] { -3.0, 0.0 });
114 |       Assert.assertEquals(xM,        optimum.getPoint()[0], 7.0e-7);
115 |       Assert.assertEquals(yM,        optimum.getPoint()[1], 3.0e-7);
116 |       Assert.assertEquals(valueXmYm, optimum.getValue(),    2.0e-14);
117 |       Assert.assertTrue(optimizer.getEvaluations() > 120);
118 |       Assert.assertTrue(optimizer.getEvaluations() < 150);
119 | 
120 |       optimizer.setConvergenceChecker(new SimpleScalarValueChecker(1.0e-15, 1.0e-30));
121 |       optimum = optimizer.optimize(fourExtrema, GoalType.MAXIMIZE, new double[] { +1, 0 });
122 |       Assert.assertEquals(xP,        optimum.getPoint()[0], 2.0e-8);
123 |       Assert.assertEquals(yP,        optimum.getPoint()[1], 3.0e-6);
124 |       Assert.assertEquals(valueXpYp, optimum.getValue(),    2.0e-12);
125 |       Assert.assertTrue(optimizer.getEvaluations() > 180);
126 |       Assert.assertTrue(optimizer.getEvaluations() < 220);
127 | 
128 |   }
```

## org.apache.commons.math.optimization.direct.MultiDirectionalTest.testMath283()
Resolved declaration: org.apache.commons.math.optimization.direct.MultiDirectionalTest.testMath283()
Source: src/test/java/org/apache/commons/math/optimization/direct/MultiDirectionalTest.java

```java
192 |   @Test
193 |   public void testMath283()
194 |       throws FunctionEvaluationException, OptimizationException {
195 |       // fails because MultiDirectional.iterateSimplex is looping forever
196 |       // the while(true) should be replaced with a convergence check
197 |       MultiDirectional multiDirectional = new MultiDirectional();
198 |       multiDirectional.setMaxIterations(100);
199 |       multiDirectional.setMaxEvaluations(1000);
200 | 
201 |       final Gaussian2D function = new Gaussian2D(0.0, 0.0, 1.0);
202 | 
203 |       RealPointValuePair estimate = multiDirectional.optimize(function,
204 |                                     GoalType.MAXIMIZE, function.getMaximumPosition());
205 | 
206 |       final double EPSILON = 1e-5;
207 | 
208 |       final double expectedMaximum = function.getMaximum();
209 |       final double actualMaximum = estimate.getValue();
210 |       Assert.assertEquals(expectedMaximum, actualMaximum, EPSILON);
211 | 
212 |       final double[] expectedPosition = function.getMaximumPosition();
213 |       final double[] actualPosition = estimate.getPoint();
214 |       Assert.assertEquals(expectedPosition[0], actualPosition[0], EPSILON );
215 |       Assert.assertEquals(expectedPosition[1], actualPosition[1], EPSILON );
216 |       
217 |   }
```
