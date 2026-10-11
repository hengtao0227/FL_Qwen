# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.builder.ToStringBuilderTest.testObjectCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testObjectCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
827 |     public void testObjectCycle() {
828 |         ObjectCycle a = new ObjectCycle();
829 |         ObjectCycle b = new ObjectCycle();
830 |         a.obj = b;
831 |         b.obj = a;
832 | 
833 |         String expected = toBaseString(a) + "[" + toBaseString(b) + "[" + toBaseString(a) + "]]";
834 |         assertEquals(expected, a.toString());
835 |         validateNullToStringStyleRegistry();
836 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionHierarchy()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionHierarchy()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
311 |     public void testReflectionHierarchy() {
312 |         ReflectionTestFixtureA baseA = new ReflectionTestFixtureA();
313 |         String baseStr = this.toBaseString(baseA);
314 |         assertEquals(baseStr + "[a=a]", ToStringBuilder.reflectionToString(baseA));
315 |         assertEquals(baseStr + "[a=a]", ToStringBuilder.reflectionToString(baseA, null));
316 |         assertEquals(baseStr + "[a=a]", ToStringBuilder.reflectionToString(baseA, null, false));
317 |         assertEquals(baseStr + "[a=a,transientA=t]", ToStringBuilder.reflectionToString(baseA, null, true));
318 |         assertEquals(baseStr + "[a=a]", ToStringBuilder.reflectionToString(baseA, null, false, null));
319 |         assertEquals(baseStr + "[a=a]", ToStringBuilder.reflectionToString(baseA, null, false, Object.class));
320 |         assertEquals(baseStr + "[a=a]", ToStringBuilder.reflectionToString(baseA, null, false, ReflectionTestFixtureA.class));
321 | 
322 |         ReflectionTestFixtureB baseB = new ReflectionTestFixtureB();
323 |         baseStr = this.toBaseString(baseB);
324 |         assertEquals(baseStr + "[b=b,a=a]", ToStringBuilder.reflectionToString(baseB));
325 |         assertEquals(baseStr + "[b=b,a=a]", ToStringBuilder.reflectionToString(baseB));
326 |         assertEquals(baseStr + "[b=b,a=a]", ToStringBuilder.reflectionToString(baseB, null));
327 |         assertEquals(baseStr + "[b=b,a=a]", ToStringBuilder.reflectionToString(baseB, null, false));
328 |         assertEquals(baseStr + "[b=b,transientB=t,a=a,transientA=t]", ToStringBuilder.reflectionToString(baseB, null, true));
329 |         assertEquals(baseStr + "[b=b,a=a]", ToStringBuilder.reflectionToString(baseB, null, false, null));
330 |         assertEquals(baseStr + "[b=b,a=a]", ToStringBuilder.reflectionToString(baseB, null, false, Object.class));
331 |         assertEquals(baseStr + "[b=b,a=a]", ToStringBuilder.reflectionToString(baseB, null, false, ReflectionTestFixtureA.class));
332 |         assertEquals(baseStr + "[b=b]", ToStringBuilder.reflectionToString(baseB, null, false, ReflectionTestFixtureB.class));
333 |         this.validateNullToStringStyleRegistry();
334 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testSelfInstanceTwoVarsReflectionObjectCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testSelfInstanceTwoVarsReflectionObjectCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
528 |     public void testSelfInstanceTwoVarsReflectionObjectCycle() throws Exception {
529 |         SelfInstanceTwoVarsReflectionTestFixture test = new SelfInstanceTwoVarsReflectionTestFixture();
530 |         assertEquals(this.toBaseString(test) + "[typeIsSelf=" + this.toBaseString(test) + ",otherType=" + test.getOtherType().toString() + "]", test.toString());
531 |         this.validateNullToStringStyleRegistry();
532 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
374 |     public void testReflectionArrayCycle() throws Exception {
375 |         Object[] objects = new Object[1];
376 |         objects[0] = objects;
377 |         assertEquals(
378 |             this.toBaseString(objects) + "[{" + this.toBaseString(objects) + "}]",
379 |             ToStringBuilder.reflectionToString(objects));
380 |         this.validateNullToStringStyleRegistry();
381 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionLongArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionLongArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
237 |     public void testReflectionLongArrayArray() {
238 |         long[][] array = new long[][] { { 1, 2 }, null, { 5 } };
239 |         String baseStr = this.toBaseString(array);
240 |         assertEquals(baseStr + "[{{1,2},<null>,{5}}]", ToStringBuilder.reflectionToString(array));
241 |         array = null;
242 |         assertReflectionArray("<null>", array);
243 |         this.validateNullToStringStyleRegistry();
244 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayArrayCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayArrayCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
400 |     public void testReflectionArrayArrayCycle() throws Exception {
401 |         Object[][] objects = new Object[2][2];
402 |         objects[0][0] = objects;
403 |         objects[0][1] = objects;
404 |         objects[1][0] = objects;
405 |         objects[1][1] = objects;
406 |         String basicToString = this.toBaseString(objects);
407 |         assertEquals(
408 |             basicToString
409 |                 + "[{{"
410 |                 + basicToString
411 |                 + ","
412 |                 + basicToString
413 |                 + "},{"
414 |                 + basicToString
415 |                 + ","
416 |                 + basicToString
417 |                 + "}}]",
418 |             ToStringBuilder.reflectionToString(objects));
419 |         this.validateNullToStringStyleRegistry();
420 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionFloatArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionFloatArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
207 |     public void testReflectionFloatArray() {
208 |         float[] array = new float[] { 1.0f, 2.9876f, -3.00001f, 4.3f };
209 |         String baseStr = this.toBaseString(array);
210 |         assertEquals(baseStr + "[{1.0,2.9876,-3.00001,4.3}]", ToStringBuilder.reflectionToString(array));
211 |         array = null;
212 |         assertReflectionArray("<null>", array);
213 |         this.validateNullToStringStyleRegistry();
214 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionDoubleArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionDoubleArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
282 |     public void testReflectionDoubleArrayArray() {
283 |         double[][] array = new double[][] { { 1.0, 2.29686 }, null, { Double.NaN } };
284 |         String baseStr = this.toBaseString(array);
285 |         assertEquals(baseStr + "[{{1.0,2.29686},<null>,{NaN}}]", ToStringBuilder.reflectionToString(array));
286 |         array = null;
287 |         assertReflectionArray("<null>", array);
288 |         this.validateNullToStringStyleRegistry();
289 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionBooleanArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionBooleanArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
216 |     public void testReflectionBooleanArray() {
217 |         boolean[] array = new boolean[] { true, false, false };
218 |         String baseStr = this.toBaseString(array);
219 |         assertEquals(baseStr + "[{true,false,false}]", ToStringBuilder.reflectionToString(array));
220 |         array = null;
221 |         assertReflectionArray("<null>", array);
222 |         this.validateNullToStringStyleRegistry();
223 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionyteArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionyteArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
180 |     public void testReflectionyteArray() {
181 |         byte[] array = new byte[] { 1, 2, -3, 4 };
182 |         String baseStr = this.toBaseString(array);
183 |         assertEquals(baseStr + "[{1,2,-3,4}]", ToStringBuilder.reflectionToString(array));
184 |         array = null;
185 |         assertReflectionArray("<null>", array);
186 |         this.validateNullToStringStyleRegistry();
187 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionDoubleArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionDoubleArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
198 |     public void testReflectionDoubleArray() {
199 |         double[] array = new double[] { 1.0, 2.9876, -3.00001, 4.3 };
200 |         String baseStr = this.toBaseString(array);
201 |         assertEquals(baseStr + "[{1.0,2.9876,-3.00001,4.3}]", ToStringBuilder.reflectionToString(array));
202 |         array = null;
203 |         assertReflectionArray("<null>", array);
204 |         this.validateNullToStringStyleRegistry();
205 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionIntArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionIntArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
246 |     public void testReflectionIntArrayArray() {
247 |         int[][] array = new int[][] { { 1, 2 }, null, { 5 } };
248 |         String baseStr = this.toBaseString(array);
249 |         assertEquals(baseStr + "[{{1,2},<null>,{5}}]", ToStringBuilder.reflectionToString(array));
250 |         array = null;
251 |         assertReflectionArray("<null>", array);
252 |         this.validateNullToStringStyleRegistry();
253 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionLongArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionLongArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
153 |     public void testReflectionLongArray() {
154 |         long[] array = new long[] { 1, 2, -3, 4 };
155 |         String baseStr = this.toBaseString(array);
156 |         assertEquals(baseStr + "[{1,2,-3,4}]", ToStringBuilder.reflectionToString(array));
157 |         array = null;
158 |         assertReflectionArray("<null>", array);
159 |         this.validateNullToStringStyleRegistry();
160 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionhortArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionhortArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
255 |     public void testReflectionhortArrayArray() {
256 |         short[][] array = new short[][] { { 1, 2 }, null, { 5 } };
257 |         String baseStr = this.toBaseString(array);
258 |         assertEquals(baseStr + "[{{1,2},<null>,{5}}]", ToStringBuilder.reflectionToString(array));
259 |         array = null;
260 |         assertReflectionArray("<null>", array);
261 |         this.validateNullToStringStyleRegistry();
262 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionObjectArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionObjectArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
144 |     public void testReflectionObjectArray() {
145 |         Object[] array = new Object[] { null, base, new int[] { 3, 6 } };
146 |         String baseStr = this.toBaseString(array);
147 |         assertEquals(baseStr + "[{<null>,5,{3,6}}]", ToStringBuilder.reflectionToString(array));
148 |         array = null;
149 |         assertReflectionArray("<null>", array);
150 |         this.validateNullToStringStyleRegistry();
151 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionObjectCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionObjectCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
540 |     public void testReflectionObjectCycle() throws Exception {
541 |         ReflectionTestCycleA a = new ReflectionTestCycleA();
542 |         ReflectionTestCycleB b = new ReflectionTestCycleB();
543 |         a.b = b;
544 |         b.a = a;
545 |         assertEquals(
546 |             this.toBaseString(a) + "[b=" + this.toBaseString(b) + "[a=" + this.toBaseString(a) + "]]",
547 |             a.toString());
548 |         this.validateNullToStringStyleRegistry();
549 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionBooleanArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionBooleanArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
291 |     public void testReflectionBooleanArrayArray() {
292 |         boolean[][] array = new boolean[][] { { true, false }, null, { false } };
293 |         String baseStr = this.toBaseString(array);
294 |         assertEquals(baseStr + "[{{true,false},<null>,{false}}]", ToStringBuilder.reflectionToString(array));
295 |         assertEquals(baseStr + "[{{true,false},<null>,{false}}]", ToStringBuilder.reflectionToString(array));
296 |         array = null;
297 |         assertReflectionArray("<null>", array);
298 |         this.validateNullToStringStyleRegistry();
299 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testSimpleReflectionObjectCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testSimpleReflectionObjectCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
504 |     public void testSimpleReflectionObjectCycle() throws Exception {
505 |         SimpleReflectionTestFixture simple = new SimpleReflectionTestFixture();
506 |         simple.o = simple;
507 |         assertEquals(this.toBaseString(simple) + "[o=" + this.toBaseString(simple) + "]", simple.toString());
508 |         this.validateNullToStringStyleRegistry();
509 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionByteArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionByteArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
264 |     public void testReflectionByteArrayArray() {
265 |         byte[][] array = new byte[][] { { 1, 2 }, null, { 5 } };
266 |         String baseStr = this.toBaseString(array);
267 |         assertEquals(baseStr + "[{{1,2},<null>,{5}}]", ToStringBuilder.reflectionToString(array));
268 |         array = null;
269 |         assertReflectionArray("<null>", array);
270 |         this.validateNullToStringStyleRegistry();
271 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayCycleLevel2()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayCycleLevel2()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
386 |     public void testReflectionArrayCycleLevel2() throws Exception {
387 |         Object[] objects = new Object[1];
388 |         Object[] objectsLevel2 = new Object[1];
389 |         objects[0] = objectsLevel2;
390 |         objectsLevel2[0] = objects;
391 |         assertEquals(
392 |             this.toBaseString(objects) + "[{{" + this.toBaseString(objects) + "}}]",
393 |             ToStringBuilder.reflectionToString(objects));
394 |         assertEquals(
395 |             this.toBaseString(objectsLevel2) + "[{{" + this.toBaseString(objectsLevel2) + "}}]",
396 |             ToStringBuilder.reflectionToString(objectsLevel2));
397 |         this.validateNullToStringStyleRegistry();
398 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayAndObjectCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionArrayAndObjectCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
557 |     public void testReflectionArrayAndObjectCycle() throws Exception {
558 |         Object[] objects = new Object[1];
559 |         SimpleReflectionTestFixture simple = new SimpleReflectionTestFixture(objects);
560 |         objects[0] = simple;
561 |         assertEquals(
562 |             this.toBaseString(objects)
563 |                 + "[{"
564 |                 + this.toBaseString(simple)
565 |                 + "[o="
566 |                 + this.toBaseString(objects)
567 |                 + "]"
568 |                 + "}]",
569 |             ToStringBuilder.reflectionToString(objects));
570 |         assertEquals(
571 |             this.toBaseString(simple)
572 |                 + "[o={"
573 |                 + this.toBaseString(simple)
574 |                 + "}]",
575 |             ToStringBuilder.reflectionToString(simple));
576 |         this.validateNullToStringStyleRegistry();
577 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionCharArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionCharArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
273 |     public void testReflectionCharArrayArray() {
274 |         char[][] array = new char[][] { { 'A', 'B' }, null, { 'p' } };
275 |         String baseStr = this.toBaseString(array);
276 |         assertEquals(baseStr + "[{{A,B},<null>,{p}}]", ToStringBuilder.reflectionToString(array));
277 |         array = null;
278 |         assertReflectionArray("<null>", array);
279 |         this.validateNullToStringStyleRegistry();
280 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionShortArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionShortArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
171 |     public void testReflectionShortArray() {
172 |         short[] array = new short[] { 1, 2, -3, 4 };
173 |         String baseStr = this.toBaseString(array);
174 |         assertEquals(baseStr + "[{1,2,-3,4}]", ToStringBuilder.reflectionToString(array));
175 |         array = null;
176 |         assertReflectionArray("<null>", array);
177 |         this.validateNullToStringStyleRegistry();
178 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testSelfInstanceVarReflectionObjectCycle()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testSelfInstanceVarReflectionObjectCycle()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
516 |     public void testSelfInstanceVarReflectionObjectCycle() throws Exception {
517 |         SelfInstanceVarReflectionTestFixture test = new SelfInstanceVarReflectionTestFixture();
518 |         assertEquals(this.toBaseString(test) + "[typeIsSelf=" + this.toBaseString(test) + "]", test.toString());
519 |         this.validateNullToStringStyleRegistry();
520 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionIntArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionIntArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
162 |     public void testReflectionIntArray() {
163 |         int[] array = new int[] { 1, 2, -3, 4 };
164 |         String baseStr = this.toBaseString(array);
165 |         assertEquals(baseStr + "[{1,2,-3,4}]", ToStringBuilder.reflectionToString(array));
166 |         array = null;
167 |         assertReflectionArray("<null>", array);
168 |         this.validateNullToStringStyleRegistry();
169 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionCharArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionCharArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
189 |     public void testReflectionCharArray() {
190 |         char[] array = new char[] { 'A', '2', '_', 'D' };
191 |         String baseStr = this.toBaseString(array);
192 |         assertEquals(baseStr + "[{A,2,_,D}]", ToStringBuilder.reflectionToString(array));
193 |         array = null;
194 |         assertReflectionArray("<null>", array);
195 |         this.validateNullToStringStyleRegistry();
196 |     }
```

## org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionFloatArrayArray()
Resolved declaration: org.apache.commons.lang3.builder.ToStringBuilderTest.testReflectionFloatArrayArray()
Source: src/test/java/org/apache/commons/lang3/builder/ToStringBuilderTest.java

```java
227 |     public void testReflectionFloatArrayArray() {
228 |         float[][] array = new float[][] { { 1.0f, 2.29686f }, null, { Float.NaN } };
229 |         String baseStr = this.toBaseString(array);
230 |         assertEquals(baseStr + "[{{1.0,2.29686},<null>,{NaN}}]", ToStringBuilder.reflectionToString(array));
231 |         array = null;
232 |         assertReflectionArray("<null>", array);
233 |         this.validateNullToStringStyleRegistry();
234 |     }
```
