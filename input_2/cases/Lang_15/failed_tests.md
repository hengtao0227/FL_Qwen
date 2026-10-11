# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.reflect.TypeUtilsTest.testGetTypeArguments()
Resolved declaration: org.apache.commons.lang3.reflect.TypeUtilsTest.testGetTypeArguments()
Source: src/test/java/org/apache/commons/lang3/reflect/TypeUtilsTest.java

```java
471 |     @Test
472 |     public void testGetTypeArguments() {
473 |         Map<TypeVariable<?>, Type> typeVarAssigns;
474 |         TypeVariable<?> treeSetTypeVar;
475 |         Type typeArg;
476 | 
477 |         typeVarAssigns = TypeUtils.getTypeArguments(Integer.class, Comparable.class);
478 |         treeSetTypeVar = Comparable.class.getTypeParameters()[0];
479 |         Assert.assertTrue("Type var assigns for Comparable from Integer: " + typeVarAssigns,
480 |                 typeVarAssigns.containsKey(treeSetTypeVar));
481 |         typeArg = typeVarAssigns.get(treeSetTypeVar);
482 |         Assert.assertEquals("Type argument of Comparable from Integer: " + typeArg, Integer.class,
483 |                 typeVarAssigns.get(treeSetTypeVar));
484 | 
485 |         typeVarAssigns = TypeUtils.getTypeArguments(int.class, Comparable.class);
486 |         treeSetTypeVar = Comparable.class.getTypeParameters()[0];
487 |         Assert.assertTrue("Type var assigns for Comparable from int: " + typeVarAssigns,
488 |                 typeVarAssigns.containsKey(treeSetTypeVar));
489 |         typeArg = typeVarAssigns.get(treeSetTypeVar);
490 |         Assert.assertEquals("Type argument of Comparable from int: " + typeArg, Integer.class,
491 |                 typeVarAssigns.get(treeSetTypeVar));
492 | 
493 |         Collection<Integer> col = Arrays.asList(new Integer[0]);
494 |         typeVarAssigns = TypeUtils.getTypeArguments(List.class, Collection.class);
495 |         treeSetTypeVar = Comparable.class.getTypeParameters()[0];
496 |         Assert.assertFalse("Type var assigns for Collection from List: " + typeVarAssigns,
497 |                 typeVarAssigns.containsKey(treeSetTypeVar));
498 | 
499 |         typeVarAssigns = TypeUtils.getTypeArguments(AAAClass.BBBClass.class, AAClass.BBClass.class);
500 |         Assert.assertTrue(typeVarAssigns.size() == 2);
501 |         Assert.assertEquals(String.class, typeVarAssigns.get(AAClass.class.getTypeParameters()[0]));
502 |         Assert.assertEquals(String.class, typeVarAssigns.get(AAClass.BBClass.class.getTypeParameters()[0]));
503 | 
504 |         typeVarAssigns = TypeUtils.getTypeArguments(Other.class, This.class);
505 |         Assert.assertEquals(2, typeVarAssigns.size());
506 |         Assert.assertEquals(String.class, typeVarAssigns.get(This.class.getTypeParameters()[0]));
507 |         Assert.assertEquals(Other.class.getTypeParameters()[0], typeVarAssigns.get(This.class.getTypeParameters()[1]));
508 |     }
```

## org.apache.commons.lang3.reflect.TypeUtilsTest.testIsAssignable()
Resolved declaration: org.apache.commons.lang3.reflect.TypeUtilsTest.testIsAssignable()
Source: src/test/java/org/apache/commons/lang3/reflect/TypeUtilsTest.java

```java
106 |     @SuppressWarnings("boxing") // deliberately used here
107 |     @Test
108 |     public void testIsAssignable() throws SecurityException, NoSuchMethodException,
109 |             NoSuchFieldException {
110 |         List list0 = null;
111 |         List<Object> list1 = null;
112 |         List<?> list2 = null;
113 |         List<? super Object> list3 = null;
114 |         List<String> list4 = null;
115 |         List<? extends String> list5 = null;
116 |         List<? super String> list6 = null;
117 |         List[] list7 = null;
118 |         List<Object>[] list8 = null;
119 |         List<?>[] list9 = null;
120 |         List<? super Object>[] list10 = null;
121 |         List<String>[] list11 = null;
122 |         List<? extends String>[] list12 = null;
123 |         List<? super String>[] list13;
124 |         Class<?> clazz = getClass();
125 |         Method method = clazz.getMethod("dummyMethod", List.class, List.class, List.class,
126 |                 List.class, List.class, List.class, List.class, List[].class, List[].class,
127 |                 List[].class, List[].class, List[].class, List[].class, List[].class);
128 |         Type[] types = method.getGenericParameterTypes();
129 | //        list0 = list0;
130 |         delegateBooleanAssertion(types, 0, 0, true);
131 |         list1 = list0;
132 |         delegateBooleanAssertion(types, 0, 1, true);
133 |         list0 = list1;
134 |         delegateBooleanAssertion(types, 1, 0, true);
135 |         list2 = list0;
136 |         delegateBooleanAssertion(types, 0, 2, true);
137 |         list0 = list2;
138 |         delegateBooleanAssertion(types, 2, 0, true);
139 |         list3 = list0;
140 |         delegateBooleanAssertion(types, 0, 3, true);
141 |         list0 = list3;
142 |         delegateBooleanAssertion(types, 3, 0, true);
143 |         list4 = list0;
144 |         delegateBooleanAssertion(types, 0, 4, true);
145 |         list0 = list4;
146 |         delegateBooleanAssertion(types, 4, 0, true);
147 |         list5 = list0;
148 |         delegateBooleanAssertion(types, 0, 5, true);
149 |         list0 = list5;
150 |         delegateBooleanAssertion(types, 5, 0, true);
151 |         list6 = list0;
152 |         delegateBooleanAssertion(types, 0, 6, true);
153 |         list0 = list6;
154 |         delegateBooleanAssertion(types, 6, 0, true);
155 | //        list1 = list1;
156 |         delegateBooleanAssertion(types, 1, 1, true);
157 |         list2 = list1;
158 |         delegateBooleanAssertion(types, 1, 2, true);
159 |         list1 = (List<Object>) list2;
160 |         delegateBooleanAssertion(types, 2, 1, false);
161 |         list3 = list1;
162 |         delegateBooleanAssertion(types, 1, 3, true);
163 |         list1 = (List<Object>) list3;
164 |         delegateBooleanAssertion(types, 3, 1, false);
165 |         // list4 = list1;
166 |         delegateBooleanAssertion(types, 1, 4, false);
167 |         // list1 = list4;
168 |         delegateBooleanAssertion(types, 4, 1, false);
169 |         // list5 = list1;
170 |         delegateBooleanAssertion(types, 1, 5, false);
171 |         // list1 = list5;
172 |         delegateBooleanAssertion(types, 5, 1, false);
173 |         list6 = list1;
174 |         delegateBooleanAssertion(types, 1, 6, true);
175 |         list1 = (List<Object>) list6;
176 |         delegateBooleanAssertion(types, 6, 1, false);
177 | //        list2 = list2;
178 |         delegateBooleanAssertion(types, 2, 2, true);
179 |         list2 = list3;
180 |         delegateBooleanAssertion(types, 2, 3, false);
181 |         list2 = list4;
182 |         delegateBooleanAssertion(types, 3, 2, true);
183 |         list3 = (List<? super Object>) list2;
184 |         delegateBooleanAssertion(types, 2, 4, false);
185 |         list2 = list5;
186 |         delegateBooleanAssertion(types, 4, 2, true);
187 |         list4 = (List<String>) list2;
188 |         delegateBooleanAssertion(types, 2, 5, false);
189 |         list2 = list6;
190 |         delegateBooleanAssertion(types, 5, 2, true);
191 |         list5 = (List<? extends String>) list2;
192 |         delegateBooleanAssertion(types, 2, 6, false);
193 | //        list3 = list3;
194 |         delegateBooleanAssertion(types, 6, 2, true);
195 |         list6 = (List<? super String>) list2;
196 |         delegateBooleanAssertion(types, 3, 3, true);
197 |         // list4 = list3;
198 |         delegateBooleanAssertion(types, 3, 4, false);
199 |         // list3 = list4;
200 |         delegateBooleanAssertion(types, 4, 3, false);
201 |         // list5 = list3;
202 |         delegateBooleanAssertion(types, 3, 5, false);
203 |         // list3 = list5;
204 |         delegateBooleanAssertion(types, 5, 3, false);
205 |         list6 = list3;
206 |         delegateBooleanAssertion(types, 3, 6, true);
207 |         list3 = (List<? super Object>) list6;
208 |         delegateBooleanAssertion(types, 6, 3, false);
209 | //        list4 = list4;
210 |         delegateBooleanAssertion(types, 4, 4, true);
211 |         list5 = list4;
212 |         delegateBooleanAssertion(types, 4, 5, true);
213 |         list4 = (List<String>) list5;
214 |         delegateBooleanAssertion(types, 5, 4, false);
215 |         list6 = list4;
216 |         delegateBooleanAssertion(types, 4, 6, true);
217 |         list4 = (List<String>) list6;
218 |         delegateBooleanAssertion(types, 6, 4, false);
219 | //        list5 = list5;
220 |         delegateBooleanAssertion(types, 5, 5, true);
221 |         list6 = (List<? super String>) list5;
222 |         delegateBooleanAssertion(types, 5, 6, false);
223 |         list5 = (List<? extends String>) list6;
224 |         delegateBooleanAssertion(types, 6, 5, false);
225 | //        list6 = list6;
226 |         delegateBooleanAssertion(types, 6, 6, true);
227 | 
228 | //        list7 = list7;
229 |         delegateBooleanAssertion(types, 7, 7, true);
230 |         list8 = list7;
231 |         delegateBooleanAssertion(types, 7, 8, true);
232 |         list7 = list8;
233 |         delegateBooleanAssertion(types, 8, 7, true);
234 |         list9 = list7;
235 |         delegateBooleanAssertion(types, 7, 9, true);
236 |         list7 = list9;
237 |         delegateBooleanAssertion(types, 9, 7, true);
238 |         list10 = list7;
239 |         delegateBooleanAssertion(types, 7, 10, true);
240 |         list7 = list10;
241 |         delegateBooleanAssertion(types, 10, 7, true);
242 |         list11 = list7;
243 |         delegateBooleanAssertion(types, 7, 11, true);
244 |         list7 = list11;
245 |         delegateBooleanAssertion(types, 11, 7, true);
246 |         list12 = list7;
247 |         delegateBooleanAssertion(types, 7, 12, true);
248 |         list7 = list12;
249 |         delegateBooleanAssertion(types, 12, 7, true);
250 |         list13 = list7;
251 |         delegateBooleanAssertion(types, 7, 13, true);
252 |         list7 = list13;
253 |         delegateBooleanAssertion(types, 13, 7, true);
254 | //        list8 = list8;
255 |         delegateBooleanAssertion(types, 8, 8, true);
256 |         list9 = list8;
257 |         delegateBooleanAssertion(types, 8, 9, true);
258 |         list8 = (List<Object>[]) list9;
259 |         delegateBooleanAssertion(types, 9, 8, false);
260 |         list10 = list8;
261 |         delegateBooleanAssertion(types, 8, 10, true);
262 |         list8 = (List<Object>[]) list10; // NOTE cast is required by Sun Java, but not by Eclipse
263 |         delegateBooleanAssertion(types, 10, 8, false);
264 |         // list11 = list8;
265 |         delegateBooleanAssertion(types, 8, 11, false);
266 |         // list8 = list11;
267 |         delegateBooleanAssertion(types, 11, 8, false);
268 |         // list12 = list8;
269 |         delegateBooleanAssertion(types, 8, 12, false);
270 |         // list8 = list12;
271 |         delegateBooleanAssertion(types, 12, 8, false);
272 |         list13 = list8;
273 |         delegateBooleanAssertion(types, 8, 13, true);
274 |         list8 = (List<Object>[]) list13;
275 |         delegateBooleanAssertion(types, 13, 8, false);
276 | //        list9 = list9;
277 |         delegateBooleanAssertion(types, 9, 9, true);
278 |         list10 = (List<? super Object>[]) list9;
279 |         delegateBooleanAssertion(types, 9, 10, false);
280 |         list9 = list10;
281 |         delegateBooleanAssertion(types, 10, 9, true);
282 |         list11 = (List<String>[]) list9;
283 |         delegateBooleanAssertion(types, 9, 11, false);
284 |         list9 = list11;
285 |         delegateBooleanAssertion(types, 11, 9, true);
286 |         list12 = (List<? extends String>[]) list9;
287 |         delegateBooleanAssertion(types, 9, 12, false);
288 |         list9 = list12;
289 |         delegateBooleanAssertion(types, 12, 9, true);
290 |         list13 = (List<? super String>[]) list9;
291 |         delegateBooleanAssertion(types, 9, 13, false);
292 |         list9 = list13;
293 |         delegateBooleanAssertion(types, 13, 9, true);
294 | //        list10 = list10;
295 |         delegateBooleanAssertion(types, 10, 10, true);
296 |         // list11 = list10;
297 |         delegateBooleanAssertion(types, 10, 11, false);
298 |         // list10 = list11;
299 |         delegateBooleanAssertion(types, 11, 10, false);
300 |         // list12 = list10;
301 |         delegateBooleanAssertion(types, 10, 12, false);
302 |         // list10 = list12;
303 |         delegateBooleanAssertion(types, 12, 10, false);
304 |         list13 = list10;
305 |         delegateBooleanAssertion(types, 10, 13, true);
306 |         list10 = (List<? super Object>[]) list13;
307 |         delegateBooleanAssertion(types, 13, 10, false);
308 | //        list11 = list11;
309 |         delegateBooleanAssertion(types, 11, 11, true);
310 |         list12 = list11;
311 |         delegateBooleanAssertion(types, 11, 12, true);
312 |         list11 = (List<String>[]) list12;
313 |         delegateBooleanAssertion(types, 12, 11, false);
314 |         list13 = list11;
315 |         delegateBooleanAssertion(types, 11, 13, true);
316 |         list11 = (List<String>[]) list13;
317 |         delegateBooleanAssertion(types, 13, 11, false);
318 | //        list12 = list12;
319 |         delegateBooleanAssertion(types, 12, 12, true);
320 |         list13 = (List<? super String>[]) list12;
321 |         delegateBooleanAssertion(types, 12, 13, false);
322 |         list12 = (List<? extends String>[]) list13;
323 |         delegateBooleanAssertion(types, 13, 12, false);
324 | //        list13 = list13;
325 |         delegateBooleanAssertion(types, 13, 13, true);
326 |         Type disType = getClass().getField("dis").getGenericType();
327 |         // Reporter.log( ( ( ParameterizedType ) disType
328 |         // ).getOwnerType().getClass().toString() );
329 |         Type datType = getClass().getField("dat").getGenericType();
330 |         Type daType = getClass().getField("da").getGenericType();
331 |         Type uhderType = getClass().getField("uhder").getGenericType();
332 |         Type dingType = getClass().getField("ding").getGenericType();
333 |         Type testerType = getClass().getField("tester").getGenericType();
334 |         Type tester2Type = getClass().getField("tester2").getGenericType();
335 |         Type dat2Type = getClass().getField("dat2").getGenericType();
336 |         Type dat3Type = getClass().getField("dat3").getGenericType();
337 |         dis = dat;
338 |         Assert.assertTrue(TypeUtils.isAssignable(datType, disType));
339 |         // dis = da;
340 |         Assert.assertFalse(TypeUtils.isAssignable(daType, disType));
341 |         dis = uhder;
342 |         Assert.assertTrue(TypeUtils.isAssignable(uhderType, disType));
343 |         dis = ding;
344 |         Assert.assertFalse(String.format("type %s not assignable to %s!", dingType, disType),
345 |                 TypeUtils.isAssignable(dingType, disType));
346 |         dis = tester;
347 |         Assert.assertTrue(TypeUtils.isAssignable(testerType, disType));
348 |         // dis = tester2;
349 |         Assert.assertFalse(TypeUtils.isAssignable(tester2Type, disType));
350 |         // dat = dat2;
351 |         Assert.assertFalse(TypeUtils.isAssignable(dat2Type, datType));
352 |         // dat2 = dat;
353 |         Assert.assertFalse(TypeUtils.isAssignable(datType, dat2Type));
354 |         // dat = dat3;
355 |         Assert.assertFalse(TypeUtils.isAssignable(dat3Type, datType));
356 |         char ch = 0;
357 |         boolean bo = false;
358 |         byte by = 0;
359 |         short sh = 0;
360 |         int in = 0;
361 |         long lo = 0;
362 |         float fl = 0;
363 |         double du = 0;
364 |         du = ch;
365 |         Assert.assertTrue(TypeUtils.isAssignable(char.class, double.class));
366 |         du = by;
367 |         Assert.assertTrue(TypeUtils.isAssignable(byte.class, double.class));
368 |         du = sh;
369 |         Assert.assertTrue(TypeUtils.isAssignable(short.class, double.class));
370 |         du = in;
371 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, double.class));
372 |         du = lo;
373 |         Assert.assertTrue(TypeUtils.isAssignable(long.class, double.class));
374 |         du = fl;
375 |         Assert.assertTrue(TypeUtils.isAssignable(float.class, double.class));
376 |         lo = in;
377 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, long.class));
378 |         lo = Integer.valueOf(0);
379 |         Assert.assertTrue(TypeUtils.isAssignable(Integer.class, long.class));
380 |         // Long lngW = 1;
381 |         Assert.assertFalse(TypeUtils.isAssignable(int.class, Long.class));
382 |         // lngW = Integer.valueOf( 0 );
383 |         Assert.assertFalse(TypeUtils.isAssignable(Integer.class, Long.class));
384 |         in = Integer.valueOf(0);
385 |         Assert.assertTrue(TypeUtils.isAssignable(Integer.class, int.class));
386 |         Integer inte = in;
387 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, Integer.class));
388 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, Number.class));
389 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, Object.class));
390 |         Type intComparableType = getClass().getField("intComparable").getGenericType();
391 |         intComparable = 1;
392 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, intComparableType));
393 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, Comparable.class));
394 |         Serializable ser = 1;
395 |         Assert.assertTrue(TypeUtils.isAssignable(int.class, Serializable.class));
396 |         Type longComparableType = getClass().getField("longComparable").getGenericType();
397 |         // longComparable = 1;
398 |         Assert.assertFalse(TypeUtils.isAssignable(int.class, longComparableType));
399 |         // longComparable = Integer.valueOf( 0 );
400 |         Assert.assertFalse(TypeUtils.isAssignable(Integer.class, longComparableType));
401 |         // int[] ia;
402 |         // long[] la = ia;
403 |         Assert.assertFalse(TypeUtils.isAssignable(int[].class, long[].class));
404 |         Integer[] ia = null;
405 |         Type caType = getClass().getField("intWildcardComparable").getGenericType();
406 |         intWildcardComparable = ia;
407 |         Assert.assertTrue(TypeUtils.isAssignable(Integer[].class, caType));
408 |         // int[] ina = ia;
409 |         Assert.assertFalse(TypeUtils.isAssignable(Integer[].class, int[].class));
410 |         int[] ina = null;
411 |         Object[] oa;
412 |         // oa = ina;
413 |         Assert.assertFalse(TypeUtils.isAssignable(int[].class, Object[].class));
414 |         oa = new Integer[0];
415 |         Assert.assertTrue(TypeUtils.isAssignable(Integer[].class, Object[].class));
416 |         Type bClassType = AClass.class.getField("bClass").getGenericType();
417 |         Type cClassType = AClass.class.getField("cClass").getGenericType();
418 |         Type dClassType = AClass.class.getField("dClass").getGenericType();
419 |         Type eClassType = AClass.class.getField("eClass").getGenericType();
420 |         Type fClassType = AClass.class.getField("fClass").getGenericType();
421 |         AClass aClass = new AClass(new AAClass<String>());
422 |         aClass.bClass = aClass.cClass;
423 |         Assert.assertTrue(TypeUtils.isAssignable(cClassType, bClassType));
424 |         aClass.bClass = aClass.dClass;
425 |         Assert.assertTrue(TypeUtils.isAssignable(dClassType, bClassType));
426 |         aClass.bClass = aClass.eClass;
427 |         Assert.assertTrue(TypeUtils.isAssignable(eClassType, bClassType));
428 |         aClass.bClass = aClass.fClass;
429 |         Assert.assertTrue(TypeUtils.isAssignable(fClassType, bClassType));
430 |         aClass.cClass = aClass.dClass;
431 |         Assert.assertTrue(TypeUtils.isAssignable(dClassType, cClassType));
432 |         aClass.cClass = aClass.eClass;
433 |         Assert.assertTrue(TypeUtils.isAssignable(eClassType, cClassType));
434 |         aClass.cClass = aClass.fClass;
435 |         Assert.assertTrue(TypeUtils.isAssignable(fClassType, cClassType));
436 |         aClass.dClass = aClass.eClass;
437 |         Assert.assertTrue(TypeUtils.isAssignable(eClassType, dClassType));
438 |         aClass.dClass = aClass.fClass;
439 |         Assert.assertTrue(TypeUtils.isAssignable(fClassType, dClassType));
440 |         aClass.eClass = aClass.fClass;
441 |         Assert.assertTrue(TypeUtils.isAssignable(fClassType, eClassType));
442 |     }
```
