# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optim.nonlinear.scalar.gradient.NonLinearConjugateGradientOptimizerTest.testTrivial()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.gradient.NonLinearConjugateGradientOptimizerTest.testTrivial()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/gradient/NonLinearConjugateGradientOptimizerTest.java

```java
124 |     @Test
125 |     public void testTrivial() {
126 |         LinearProblem problem
127 |             = new LinearProblem(new double[][] { { 2 } }, new double[] { 3 });
128 |         NonLinearConjugateGradientOptimizer optimizer
129 |             = new NonLinearConjugateGradientOptimizer(NonLinearConjugateGradientOptimizer.Formula.POLAK_RIBIERE,
130 |                                                       new SimpleValueChecker(1e-6, 1e-6));
131 |         PointValuePair optimum
132 |             = optimizer.optimize(new MaxEval(100),
133 |                                  problem.getObjectiveFunction(),
134 |                                  problem.getObjectiveFunctionGradient(),
135 |                                  GoalType.MINIMIZE,
136 |                                  new InitialGuess(new double[] { 0 }));
137 |         Assert.assertEquals(1.5, optimum.getPoint()[0], 1.0e-10);
138 |         Assert.assertEquals(0.0, optimum.getValue(), 1.0e-10);
139 | 
140 |         // Check that the number of iterations is updated (MATH-949).
141 |         Assert.assertTrue(optimizer.getIterations() > 0);
142 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testConstrainedRosen()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testConstrainedRosen()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
341 |     @Test
342 |     public void testConstrainedRosen() {
343 |         double[] startPoint = point(DIM, 0.1);
344 |         double[] insigma = point(DIM, 0.1);
345 |         double[][] boundaries = boundaries(DIM, -1, 2);
346 |         PointValuePair expected =
347 |             new PointValuePair(point(DIM,1.0),0.0);
348 |         doTest(new Rosen(), startPoint, insigma, boundaries,
349 |                 GoalType.MINIMIZE, 2*LAMBDA, true, 0, 1e-13,
350 |                 1e-13, 1e-6, 100000, expected);
351 |         doTest(new Rosen(), startPoint, insigma, boundaries,
352 |                 GoalType.MINIMIZE, 2*LAMBDA, false, 0, 1e-13,
353 |                 1e-13, 1e-6, 100000, expected);
354 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testElliRotated()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testElliRotated()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
176 |     @Test
177 |     public void testElliRotated() {
178 |         double[] startPoint = point(DIM,1.0);
179 |         double[] insigma = point(DIM,0.1);
180 |         double[][] boundaries = null;
181 |         PointValuePair expected =
182 |             new PointValuePair(point(DIM,0.0),0.0);
183 |         doTest(new ElliRotated(), startPoint, insigma, boundaries,
184 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
185 |                 1e-13, 1e-6, 100000, expected);
186 |         doTest(new ElliRotated(), startPoint, insigma, boundaries,
187 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
188 |                 1e-13, 1e-6, 100000, expected);
189 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testEllipse()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testEllipse()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
161 |     @Test
162 |     public void testEllipse() {
163 |         double[] startPoint = point(DIM,1.0);
164 |         double[] insigma = point(DIM,0.1);
165 |         double[][] boundaries = null;
166 |         PointValuePair expected =
167 |             new PointValuePair(point(DIM,0.0),0.0);
168 |         doTest(new Elli(), startPoint, insigma, boundaries,
169 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
170 |                 1e-13, 1e-6, 100000, expected);
171 |         doTest(new Elli(), startPoint, insigma, boundaries,
172 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
173 |                 1e-13, 1e-6, 100000, expected);
174 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testTwoAxes()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testTwoAxes()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
221 |     @Test
222 |     public void testTwoAxes() {
223 |         double[] startPoint = point(DIM,1.0);
224 |         double[] insigma = point(DIM,0.1);
225 |         double[][] boundaries = null;
226 |         PointValuePair expected =
227 |             new PointValuePair(point(DIM,0.0),0.0);
228 |         doTest(new TwoAxes(), startPoint, insigma, boundaries,
229 |                 GoalType.MINIMIZE, 2*LAMBDA, true, 0, 1e-13,
230 |                 1e-13, 1e-6, 200000, expected);
231 |         doTest(new TwoAxes(), startPoint, insigma, boundaries,
232 |                 GoalType.MINIMIZE, 2*LAMBDA, false, 0, 1e-13,
233 |                 1e-8, 1e-3, 200000, expected);
234 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testCigar()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testCigar()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
191 |     @Test
192 |     public void testCigar() {
193 |         double[] startPoint = point(DIM,1.0);
194 |         double[] insigma = point(DIM,0.1);
195 |         double[][] boundaries = null;
196 |         PointValuePair expected =
197 |             new PointValuePair(point(DIM,0.0),0.0);
198 |         doTest(new Cigar(), startPoint, insigma, boundaries,
199 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
200 |                 1e-13, 1e-6, 200000, expected);
201 |         doTest(new Cigar(), startPoint, insigma, boundaries,
202 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
203 |                 1e-13, 1e-6, 100000, expected);
204 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testRosen()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testRosen()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
124 |     @Test
125 |     @Retry(3)
126 |     public void testRosen() {
127 |         double[] startPoint = point(DIM,0.1);
128 |         double[] insigma = point(DIM,0.1);
129 |         double[][] boundaries = null;
130 |         PointValuePair expected =
131 |             new PointValuePair(point(DIM,1.0),0.0);
132 |         doTest(new Rosen(), startPoint, insigma, boundaries,
133 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
134 |                 1e-13, 1e-6, 100000, expected);
135 |         doTest(new Rosen(), startPoint, insigma, boundaries,
136 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
137 |                 1e-13, 1e-6, 100000, expected);
138 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testRastrigin()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testRastrigin()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
326 |     @Test
327 |     public void testRastrigin() {
328 |         double[] startPoint = point(DIM,0.1);
329 |         double[] insigma = point(DIM,0.1);
330 |         double[][] boundaries = null;
331 |         PointValuePair expected =
332 |             new PointValuePair(point(DIM,0.0),0.0);
333 |         doTest(new Rastrigin(), startPoint, insigma, boundaries,
334 |                 GoalType.MINIMIZE, (int)(200*Math.sqrt(DIM)), true, 0, 1e-13,
335 |                 1e-13, 1e-6, 200000, expected);
336 |         doTest(new Rastrigin(), startPoint, insigma, boundaries,
337 |                 GoalType.MINIMIZE, (int)(200*Math.sqrt(DIM)), false, 0, 1e-13,
338 |                 1e-13, 1e-6, 200000, expected);
339 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testDiagonalRosen()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testDiagonalRosen()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
356 |     @Test
357 |     public void testDiagonalRosen() {
358 |         double[] startPoint = point(DIM,0.1);
359 |         double[] insigma = point(DIM,0.1);
360 |         double[][] boundaries = null;
361 |         PointValuePair expected =
362 |             new PointValuePair(point(DIM,1.0),0.0);
363 |         doTest(new Rosen(), startPoint, insigma, boundaries,
364 |                 GoalType.MINIMIZE, LAMBDA, false, 1, 1e-13,
365 |                 1e-10, 1e-4, 1000000, expected);
366 |      }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testSsDiffPow()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testSsDiffPow()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
296 |     @Test
297 |     public void testSsDiffPow() {
298 |         double[] startPoint = point(DIM,1.0);
299 |         double[] insigma = point(DIM,0.1);
300 |         double[][] boundaries = null;
301 |         PointValuePair expected =
302 |             new PointValuePair(point(DIM,0.0),0.0);
303 |         doTest(new SsDiffPow(), startPoint, insigma, boundaries,
304 |                 GoalType.MINIMIZE, 10, true, 0, 1e-13,
305 |                 1e-4, 1e-1, 200000, expected);
306 |         doTest(new SsDiffPow(), startPoint, insigma, boundaries,
307 |                 GoalType.MINIMIZE, 10, false, 0, 1e-13,
308 |                 1e-4, 1e-1, 200000, expected);
309 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testMaximize()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testMaximize()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
140 |     @Test
141 |     @Retry(3)
142 |     public void testMaximize() {
143 |         double[] startPoint = point(DIM,1.0);
144 |         double[] insigma = point(DIM,0.1);
145 |         double[][] boundaries = null;
146 |         PointValuePair expected =
147 |             new PointValuePair(point(DIM,0.0),1.0);
148 |         doTest(new MinusElli(), startPoint, insigma, boundaries,
149 |                 GoalType.MAXIMIZE, LAMBDA, true, 0, 1.0-1e-13,
150 |                 2e-10, 5e-6, 100000, expected);
151 |         doTest(new MinusElli(), startPoint, insigma, boundaries,
152 |                 GoalType.MAXIMIZE, LAMBDA, false, 0, 1.0-1e-13,
153 |                 2e-10, 5e-6, 100000, expected);
154 |         boundaries = boundaries(DIM,-0.3,0.3); 
155 |         startPoint = point(DIM,0.1);
156 |         doTest(new MinusElli(), startPoint, insigma, boundaries,
157 |                 GoalType.MAXIMIZE, LAMBDA, true, 0, 1.0-1e-13,
158 |                 2e-10, 5e-6, 100000, expected);
159 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testAckley()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testAckley()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
311 |     @Test
312 |     public void testAckley() {
313 |         double[] startPoint = point(DIM,1.0);
314 |         double[] insigma = point(DIM,1.0);
315 |         double[][] boundaries = null;
316 |         PointValuePair expected =
317 |             new PointValuePair(point(DIM,0.0),0.0);
318 |         doTest(new Ackley(), startPoint, insigma, boundaries,
319 |                 GoalType.MINIMIZE, 2*LAMBDA, true, 0, 1e-13,
320 |                 1e-9, 1e-5, 100000, expected);
321 |         doTest(new Ackley(), startPoint, insigma, boundaries,
322 |                 GoalType.MINIMIZE, 2*LAMBDA, false, 0, 1e-13,
323 |                 1e-9, 1e-5, 100000, expected);
324 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testCigTab()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testCigTab()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
236 |     @Test
237 |     public void testCigTab() {
238 |         double[] startPoint = point(DIM,1.0);
239 |         double[] insigma = point(DIM,0.3);
240 |         double[][] boundaries = null;
241 |         PointValuePair expected =
242 |             new PointValuePair(point(DIM,0.0),0.0);
243 |         doTest(new CigTab(), startPoint, insigma, boundaries,
244 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
245 |                 1e-13, 5e-5, 100000, expected);
246 |         doTest(new CigTab(), startPoint, insigma, boundaries,
247 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
248 |                 1e-13, 5e-5, 100000, expected);
249 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testDiffPow()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testDiffPow()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
281 |     @Test
282 |     public void testDiffPow() {
283 |         double[] startPoint = point(DIM,1.0);
284 |         double[] insigma = point(DIM,0.1);
285 |         double[][] boundaries = null;
286 |         PointValuePair expected =
287 |             new PointValuePair(point(DIM,0.0),0.0);
288 |         doTest(new DiffPow(), startPoint, insigma, boundaries,
289 |                 GoalType.MINIMIZE, 10, true, 0, 1e-13,
290 |                 1e-8, 1e-1, 100000, expected);
291 |         doTest(new DiffPow(), startPoint, insigma, boundaries,
292 |                 GoalType.MINIMIZE, 10, false, 0, 1e-13,
293 |                 1e-8, 2e-1, 100000, expected);
294 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testSphere()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testSphere()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
251 |     @Test
252 |     public void testSphere() {
253 |         double[] startPoint = point(DIM,1.0);
254 |         double[] insigma = point(DIM,0.1);
255 |         double[][] boundaries = null;
256 |         PointValuePair expected =
257 |             new PointValuePair(point(DIM,0.0),0.0);
258 |         doTest(new Sphere(), startPoint, insigma, boundaries,
259 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
260 |                 1e-13, 1e-6, 100000, expected);
261 |         doTest(new Sphere(), startPoint, insigma, boundaries,
262 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
263 |                 1e-13, 1e-6, 100000, expected);
264 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testTablet()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testTablet()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
266 |     @Test
267 |     public void testTablet() {
268 |         double[] startPoint = point(DIM,1.0);
269 |         double[] insigma = point(DIM,0.1);
270 |         double[][] boundaries = null;
271 |         PointValuePair expected =
272 |             new PointValuePair(point(DIM,0.0),0.0);
273 |         doTest(new Tablet(), startPoint, insigma, boundaries,
274 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
275 |                 1e-13, 1e-6, 100000, expected);
276 |         doTest(new Tablet(), startPoint, insigma, boundaries,
277 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
278 |                 1e-13, 1e-6, 100000, expected);
279 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testCigarWithBoundaries()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.CMAESOptimizerTest.testCigarWithBoundaries()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/CMAESOptimizerTest.java

```java
206 |     @Test
207 |     public void testCigarWithBoundaries() {
208 |         double[] startPoint = point(DIM,1.0);
209 |         double[] insigma = point(DIM,0.1);
210 |         double[][] boundaries = boundaries(DIM, -1e100, Double.POSITIVE_INFINITY);
211 |         PointValuePair expected =
212 |             new PointValuePair(point(DIM,0.0),0.0);
213 |         doTest(new Cigar(), startPoint, insigma, boundaries,
214 |                 GoalType.MINIMIZE, LAMBDA, true, 0, 1e-13,
215 |                 1e-13, 1e-6, 200000, expected);
216 |         doTest(new Cigar(), startPoint, insigma, boundaries,
217 |                 GoalType.MINIMIZE, LAMBDA, false, 0, 1e-13,
218 |                 1e-13, 1e-6, 100000, expected);
219 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.PowellOptimizerTest.testSumSinc()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.PowellOptimizerTest.testSumSinc()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/PowellOptimizerTest.java

```java
50 |     @Test
51 |     public void testSumSinc() {
52 |         final MultivariateFunction func = new SumSincFunction(-1);
53 | 
54 |         int dim = 2;
55 |         final double[] minPoint = new double[dim];
56 |         for (int i = 0; i < dim; i++) {
57 |             minPoint[i] = 0;
58 |         }
59 | 
60 |         double[] init = new double[dim];
61 | 
62 |         // Initial is minimum.
63 |         for (int i = 0; i < dim; i++) {
64 |             init[i] = minPoint[i];
65 |         }
66 |         doTest(func, minPoint, init, GoalType.MINIMIZE, 1e-9, 1e-9);
67 | 
68 |         // Initial is far from minimum.
69 |         for (int i = 0; i < dim; i++) {
70 |             init[i] = minPoint[i] + 3;
71 |         }
72 |         doTest(func, minPoint, init, GoalType.MINIMIZE, 1e-9, 1e-5);
73 |         // More stringent line search tolerance enhances the precision
74 |         // of the result.
75 |         doTest(func, minPoint, init, GoalType.MINIMIZE, 1e-9, 1e-9, 1e-7);
76 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMaximize1()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMaximize1()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerMultiDirectionalTest.java

```java
90 |     @Test
91 |     public void testMaximize1() {
92 |         SimplexOptimizer optimizer = new SimplexOptimizer(1e-11, 1e-30);
93 |         final FourExtrema fourExtrema = new FourExtrema();
94 | 
95 |         final PointValuePair optimum
96 |             = optimizer.optimize(new MaxEval(200),
97 |                                  new ObjectiveFunction(fourExtrema),
98 |                                  GoalType.MAXIMIZE,
99 |                                  new InitialGuess(new double[] { -3.0, 0.0 }),
100 |                                  new MultiDirectionalSimplex(new double[] { 0.2, 0.2 }));
101 |         Assert.assertEquals(fourExtrema.xM, optimum.getPoint()[0], 7e-7);
102 |         Assert.assertEquals(fourExtrema.yM, optimum.getPoint()[1], 3e-7);
103 |         Assert.assertEquals(fourExtrema.valueXmYm, optimum.getValue(), 2e-14);
104 |         Assert.assertTrue(optimizer.getEvaluations() > 120);
105 |         Assert.assertTrue(optimizer.getEvaluations() < 150);
106 | 
107 |         // Check that the number of iterations is updated (MATH-949).
108 |         Assert.assertTrue(optimizer.getIterations() > 0);
109 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMaximize2()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMaximize2()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerMultiDirectionalTest.java

```java
111 |     @Test
112 |     public void testMaximize2() {
113 |         SimplexOptimizer optimizer = new SimplexOptimizer(new SimpleValueChecker(1e-15, 1e-30));
114 |         final FourExtrema fourExtrema = new FourExtrema();
115 | 
116 |         final PointValuePair optimum
117 |             = optimizer.optimize(new MaxEval(200),
118 |                                  new ObjectiveFunction(fourExtrema),
119 |                                  GoalType.MAXIMIZE,
120 |                                  new InitialGuess(new double[] { 1, 0 }),
121 |                                  new MultiDirectionalSimplex(new double[] { 0.2, 0.2 }));
122 |         Assert.assertEquals(fourExtrema.xP, optimum.getPoint()[0], 2e-8);
123 |         Assert.assertEquals(fourExtrema.yP, optimum.getPoint()[1], 3e-6);
124 |         Assert.assertEquals(fourExtrema.valueXpYp, optimum.getValue(), 2e-12);
125 |         Assert.assertTrue(optimizer.getEvaluations() > 180);
126 |         Assert.assertTrue(optimizer.getEvaluations() < 220);
127 | 
128 |         // Check that the number of iterations is updated (MATH-949).
129 |         Assert.assertTrue(optimizer.getIterations() > 0);
130 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMinimize1()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMinimize1()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerMultiDirectionalTest.java

```java
48 |     @Test
49 |     public void testMinimize1() {
50 |         SimplexOptimizer optimizer = new SimplexOptimizer(1e-11, 1e-30);
51 |         final FourExtrema fourExtrema = new FourExtrema();
52 | 
53 |         final PointValuePair optimum
54 |             = optimizer.optimize(new MaxEval(200),
55 |                                  new ObjectiveFunction(fourExtrema),
56 |                                  GoalType.MINIMIZE,
57 |                                  new InitialGuess(new double[] { -3, 0 }),
58 |                                  new MultiDirectionalSimplex(new double[] { 0.2, 0.2 }));
59 |         Assert.assertEquals(fourExtrema.xM, optimum.getPoint()[0], 4e-6);
60 |         Assert.assertEquals(fourExtrema.yP, optimum.getPoint()[1], 3e-6);
61 |         Assert.assertEquals(fourExtrema.valueXmYp, optimum.getValue(), 8e-13);
62 |         Assert.assertTrue(optimizer.getEvaluations() > 120);
63 |         Assert.assertTrue(optimizer.getEvaluations() < 150);
64 | 
65 |         // Check that the number of iterations is updated (MATH-949).
66 |         Assert.assertTrue(optimizer.getIterations() > 0);
67 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMinimize2()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerMultiDirectionalTest.testMinimize2()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerMultiDirectionalTest.java

```java
69 |     @Test
70 |     public void testMinimize2() {
71 |         SimplexOptimizer optimizer = new SimplexOptimizer(1e-11, 1e-30);
72 |         final FourExtrema fourExtrema = new FourExtrema();
73 | 
74 |         final PointValuePair optimum
75 |             = optimizer.optimize(new MaxEval(200),
76 |                                  new ObjectiveFunction(fourExtrema),
77 |                                  GoalType.MINIMIZE,
78 |                                  new InitialGuess(new double[] { 1, 0 }),
79 |                                  new MultiDirectionalSimplex(new double[] { 0.2, 0.2 }));
80 |         Assert.assertEquals(fourExtrema.xP, optimum.getPoint()[0], 2e-8);
81 |         Assert.assertEquals(fourExtrema.yM, optimum.getPoint()[1], 3e-6);
82 |         Assert.assertEquals(fourExtrema.valueXpYm, optimum.getValue(), 2e-12);
83 |         Assert.assertTrue(optimizer.getEvaluations() > 120);
84 |         Assert.assertTrue(optimizer.getEvaluations() < 150);
85 | 
86 |         // Check that the number of iterations is updated (MATH-949).
87 |         Assert.assertTrue(optimizer.getIterations() > 0);
88 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMaximize1()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMaximize1()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerNelderMeadTest.java

```java
95 |     @Test
96 |     public void testMaximize1() {
97 |         SimplexOptimizer optimizer = new SimplexOptimizer(1e-10, 1e-30);
98 |         final FourExtrema fourExtrema = new FourExtrema();
99 | 
100 |         final PointValuePair optimum
101 |             = optimizer.optimize(new MaxEval(100),
102 |                                  new ObjectiveFunction(fourExtrema),
103 |                                  GoalType.MAXIMIZE,
104 |                                  new InitialGuess(new double[] { -3, 0 }),
105 |                                  new NelderMeadSimplex(new double[] { 0.2, 0.2 }));
106 |         Assert.assertEquals(fourExtrema.xM, optimum.getPoint()[0], 1e-5);
107 |         Assert.assertEquals(fourExtrema.yM, optimum.getPoint()[1], 3e-6);
108 |         Assert.assertEquals(fourExtrema.valueXmYm, optimum.getValue(), 3e-12);
109 |         Assert.assertTrue(optimizer.getEvaluations() > 60);
110 |         Assert.assertTrue(optimizer.getEvaluations() < 90);
111 | 
112 |         // Check that the number of iterations is updated (MATH-949).
113 |         Assert.assertTrue(optimizer.getIterations() > 0);
114 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMaximize2()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMaximize2()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerNelderMeadTest.java

```java
116 |     @Test
117 |     public void testMaximize2() {
118 |         SimplexOptimizer optimizer = new SimplexOptimizer(1e-10, 1e-30);
119 |         final FourExtrema fourExtrema = new FourExtrema();
120 | 
121 |         final PointValuePair optimum
122 |             = optimizer.optimize(new MaxEval(100),
123 |                                  new ObjectiveFunction(fourExtrema),
124 |                                  GoalType.MAXIMIZE,
125 |                                  new InitialGuess(new double[] { 1, 0 }),
126 |                                  new NelderMeadSimplex(new double[] { 0.2, 0.2 }));
127 |         Assert.assertEquals(fourExtrema.xP, optimum.getPoint()[0], 4e-6);
128 |         Assert.assertEquals(fourExtrema.yP, optimum.getPoint()[1], 5e-6);
129 |         Assert.assertEquals(fourExtrema.valueXpYp, optimum.getValue(), 7e-12);
130 |         Assert.assertTrue(optimizer.getEvaluations() > 60);
131 |         Assert.assertTrue(optimizer.getEvaluations() < 90);
132 | 
133 |         // Check that the number of iterations is updated (MATH-949).
134 |         Assert.assertTrue(optimizer.getIterations() > 0);
135 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMinimize1()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMinimize1()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerNelderMeadTest.java

```java
53 |     @Test
54 |     public void testMinimize1() {
55 |         SimplexOptimizer optimizer = new SimplexOptimizer(1e-10, 1e-30);
56 |         final FourExtrema fourExtrema = new FourExtrema();
57 | 
58 |         final PointValuePair optimum
59 |             = optimizer.optimize(new MaxEval(100),
60 |                                  new ObjectiveFunction(fourExtrema),
61 |                                  GoalType.MINIMIZE,
62 |                                  new InitialGuess(new double[] { -3, 0 }),
63 |                                  new NelderMeadSimplex(new double[] { 0.2, 0.2 }));
64 |         Assert.assertEquals(fourExtrema.xM, optimum.getPoint()[0], 2e-7);
65 |         Assert.assertEquals(fourExtrema.yP, optimum.getPoint()[1], 2e-5);
66 |         Assert.assertEquals(fourExtrema.valueXmYp, optimum.getValue(), 6e-12);
67 |         Assert.assertTrue(optimizer.getEvaluations() > 60);
68 |         Assert.assertTrue(optimizer.getEvaluations() < 90);
69 | 
70 |         // Check that the number of iterations is updated (MATH-949).
71 |         Assert.assertTrue(optimizer.getIterations() > 0);
72 |     }
```

## org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMinimize2()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.scalar.noderiv.SimplexOptimizerNelderMeadTest.testMinimize2()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/SimplexOptimizerNelderMeadTest.java

```java
74 |     @Test
75 |     public void testMinimize2() {
76 |         SimplexOptimizer optimizer = new SimplexOptimizer(1e-10, 1e-30);
77 |         final FourExtrema fourExtrema = new FourExtrema();
78 | 
79 |         final PointValuePair optimum
80 |             = optimizer.optimize(new MaxEval(100),
81 |                                  new ObjectiveFunction(fourExtrema),
82 |                                  GoalType.MINIMIZE,
83 |                                  new InitialGuess(new double[] { 1, 0 }),
84 |                                  new NelderMeadSimplex(new double[] { 0.2, 0.2 }));
85 |         Assert.assertEquals(fourExtrema.xP, optimum.getPoint()[0], 5e-6);
86 |         Assert.assertEquals(fourExtrema.yM, optimum.getPoint()[1], 6e-6);
87 |         Assert.assertEquals(fourExtrema.valueXpYm, optimum.getValue(), 1e-11);
88 |         Assert.assertTrue(optimizer.getEvaluations() > 60);
89 |         Assert.assertTrue(optimizer.getEvaluations() < 90);
90 | 
91 |         // Check that the number of iterations is updated (MATH-949).
92 |         Assert.assertTrue(optimizer.getIterations() > 0);
93 |     }
```

## org.apache.commons.math3.optim.nonlinear.vector.jacobian.GaussNewtonOptimizerTest.testGetIterations()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.vector.jacobian.AbstractLeastSquaresOptimizerAbstractTest.testGetIterations()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/vector/jacobian/AbstractLeastSquaresOptimizerAbstractTest.java

```java
108 |     @Test
109 |     public void testGetIterations() {
110 |         AbstractLeastSquaresOptimizer optim = createOptimizer();
111 |         optim.optimize(new MaxEval(100), new Target(new double[] { 1 }),
112 |                        new Weight(new double[] { 1 }),
113 |                        new InitialGuess(new double[] { 3 }),
114 |                        new ModelFunction(new MultivariateVectorFunction() {
115 |                                @Override
116 |                                public double[] value(double[] point) {
117 |                                    return new double[] {
118 |                                        FastMath.pow(point[0], 4)
119 |                                    };
120 |                                }
121 |                            }),
122 |                        new ModelFunctionJacobian(new MultivariateMatrixFunction() {
123 |                                @Override
124 |                                public double[][] value(double[] point) {
125 |                                    return new double[][] {
126 |                                        { 0.25 * FastMath.pow(point[0], 3) }
127 |                                    };
128 |                                }
129 |                            }));
130 | 
131 |         Assert.assertTrue(optim.getIterations() > 0);
132 |     }
```

## org.apache.commons.math3.optim.nonlinear.vector.jacobian.LevenbergMarquardtOptimizerTest.testGetIterations()
Resolved declaration: org.apache.commons.math3.optim.nonlinear.vector.jacobian.AbstractLeastSquaresOptimizerAbstractTest.testGetIterations()
Source: src/test/java/org/apache/commons/math3/optim/nonlinear/vector/jacobian/AbstractLeastSquaresOptimizerAbstractTest.java

```java
108 |     @Test
109 |     public void testGetIterations() {
110 |         AbstractLeastSquaresOptimizer optim = createOptimizer();
111 |         optim.optimize(new MaxEval(100), new Target(new double[] { 1 }),
112 |                        new Weight(new double[] { 1 }),
113 |                        new InitialGuess(new double[] { 3 }),
114 |                        new ModelFunction(new MultivariateVectorFunction() {
115 |                                @Override
116 |                                public double[] value(double[] point) {
117 |                                    return new double[] {
118 |                                        FastMath.pow(point[0], 4)
119 |                                    };
120 |                                }
121 |                            }),
122 |                        new ModelFunctionJacobian(new MultivariateMatrixFunction() {
123 |                                @Override
124 |                                public double[][] value(double[] point) {
125 |                                    return new double[][] {
126 |                                        { 0.25 * FastMath.pow(point[0], 3) }
127 |                                    };
128 |                                }
129 |                            }));
130 | 
131 |         Assert.assertTrue(optim.getIterations() > 0);
132 |     }
```
