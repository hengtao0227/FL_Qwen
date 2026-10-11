# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.junit.KeyedObjects2DTests.testRemoveColumnByKey()
Resolved declaration: org.jfree.data.junit.KeyedObjects2DTests.testRemoveColumnByKey()
Source: tests/org/jfree/data/junit/KeyedObjects2DTests.java

```java
387 |     public void testRemoveColumnByKey() {
388 |         KeyedObjects2D data = new KeyedObjects2D();
389 |         data.setObject("Obj1", "R1", "C1");
390 |         data.setObject("Obj2", "R2", "C2");
391 |         data.removeColumn("C2");
392 |         assertEquals(1, data.getColumnCount());
393 |         assertEquals("Obj1", data.getObject(0, 0));
394 |         
395 |         // try unknown column key
396 |         boolean pass = false;
397 |         try {
398 |             data.removeColumn("XXX");
399 |         }
400 |         catch (UnknownKeyException e) {
401 |             pass = true;
402 |         }
403 |         assertTrue(pass);
404 |         
405 |         // try null column key
406 |         pass = false;
407 |         try {
408 |             data.removeColumn(null);
409 |         }
410 |         catch (IllegalArgumentException e) {
411 |             pass = true;
412 |         }
413 |         assertTrue(pass);
414 |     }
```

## org.jfree.data.junit.KeyedObjects2DTests.testRemoveValue()
Resolved declaration: org.jfree.data.junit.KeyedObjects2DTests.testRemoveValue()
Source: tests/org/jfree/data/junit/KeyedObjects2DTests.java

```java
419 |     public void testRemoveValue() {
420 |         KeyedObjects2D data = new KeyedObjects2D();
421 |         data.setObject("Obj1", "R1", "C1");
422 |         data.setObject("Obj2", "R2", "C2");
423 |         data.removeObject("R2", "C2");
424 |         assertEquals(1, data.getRowCount());
425 |         assertEquals(1, data.getColumnCount());
426 |         assertEquals("Obj1", data.getObject(0, 0));
427 |     }
```

## org.jfree.data.junit.KeyedObjects2DTests.testGetValueByKey()
Resolved declaration: org.jfree.data.junit.KeyedObjects2DTests.testGetValueByKey()
Source: tests/org/jfree/data/junit/KeyedObjects2DTests.java

```java
205 |     public void testGetValueByKey() {
206 |         KeyedObjects2D data = new KeyedObjects2D();
207 |         data.addObject("Obj1", "R1", "C1");
208 |         data.addObject("Obj2", "R2", "C2");
209 |         assertEquals("Obj1", data.getObject("R1", "C1"));
210 |         assertEquals("Obj2", data.getObject("R2", "C2"));
211 |         assertNull(data.getObject("R1", "C2"));
212 |         assertNull(data.getObject("R2", "C1"));
213 |         
214 |         // check invalid indices
215 |         boolean pass = false;
216 |         try {
217 |             data.getObject("XX", "C1");
218 |         }
219 |         catch (UnknownKeyException e) {
220 |             pass = true;
221 |         }
222 |         assertTrue(pass);
223 |         
224 |         pass = false;
225 |         try {
226 |             data.getObject("R1", "XX");
227 |         }
228 |         catch (UnknownKeyException e) {
229 |             pass = true;
230 |         }
231 |         assertTrue(pass);
232 | 
233 |         pass = false;
234 |         try {
235 |             data.getObject("XX", "C1");
236 |         }
237 |         catch (UnknownKeyException e) {
238 |             pass = true;
239 |         }
240 |         assertTrue(pass);
241 | 
242 |         pass = false;
243 |         try {
244 |             data.getObject("R1", "XX");
245 |         }
246 |         catch (UnknownKeyException e) {
247 |             pass = true;
248 |         }
249 |         assertTrue(pass);
250 |     }
```

## org.jfree.data.junit.KeyedObjects2DTests.testRemoveColumnByIndex()
Resolved declaration: org.jfree.data.junit.KeyedObjects2DTests.testRemoveColumnByIndex()
Source: tests/org/jfree/data/junit/KeyedObjects2DTests.java

```java
323 |     public void testRemoveColumnByIndex() {
324 |         KeyedObjects2D data = new KeyedObjects2D();
325 |         data.setObject("Obj1", "R1", "C1");
326 |         data.setObject("Obj2", "R2", "C2");
327 |         data.removeColumn(0);
328 |         assertEquals(1, data.getColumnCount());
329 |         assertEquals("Obj2", data.getObject(1, 0));
330 |         
331 |         // try negative column index
332 |         boolean pass = false;
333 |         try {
334 |             data.removeColumn(-1);
335 |         }
336 |         catch (IndexOutOfBoundsException e) {
337 |             pass = true;
338 |         }
339 |         assertTrue(pass);
340 |         
341 |         // try column index too high
342 |         pass = false;
343 |         try {
344 |             data.removeColumn(data.getColumnCount());
345 |         }
346 |         catch (IndexOutOfBoundsException e) {
347 |             pass = true;
348 |         }
349 |         assertTrue(pass);
350 |     }
```

## org.jfree.data.junit.KeyedObjects2DTests.testSetObject()
Resolved declaration: org.jfree.data.junit.KeyedObjects2DTests.testSetObject()
Source: tests/org/jfree/data/junit/KeyedObjects2DTests.java

```java
255 |     public void testSetObject() {
256 |         KeyedObjects2D data = new KeyedObjects2D();
257 |         data.setObject("Obj1", "R1", "C1");
258 |         data.setObject("Obj2", "R2", "C2");
259 |         assertEquals("Obj1", data.getObject("R1", "C1"));
260 |         assertEquals("Obj2", data.getObject("R2", "C2"));
261 |         assertNull(data.getObject("R1", "C2"));
262 |         assertNull(data.getObject("R2", "C1"));
263 |         
264 |         // confirm overwriting an existing value
265 |         data.setObject("ABC", "R2", "C2");
266 |         assertEquals("ABC", data.getObject("R2", "C2"));
267 |         
268 |         // try null keys
269 |         boolean pass = false;
270 |         try {
271 |             data.setObject("X", null, "C1");
272 |         }
273 |         catch (IllegalArgumentException e) {
274 |             pass = true;
275 |         }
276 |         assertTrue(pass);
277 |         
278 |         pass = false;
279 |         try {
280 |             data.setObject("X", "R1", null);
281 |         }
282 |         catch (IllegalArgumentException e) {
283 |             pass = true;
284 |         }
285 |         assertTrue(pass);
286 |     }
```

## org.jfree.data.junit.KeyedObjects2DTests.testRemoveRowByKey()
Resolved declaration: org.jfree.data.junit.KeyedObjects2DTests.testRemoveRowByKey()
Source: tests/org/jfree/data/junit/KeyedObjects2DTests.java

```java
355 |     public void testRemoveRowByKey() {
356 |         KeyedObjects2D data = new KeyedObjects2D();
357 |         data.setObject("Obj1", "R1", "C1");
358 |         data.setObject("Obj2", "R2", "C2");
359 |         data.removeRow("R2");
360 |         assertEquals(1, data.getRowCount());
361 |         assertEquals("Obj1", data.getObject(0, 0));
362 |         
363 |         // try unknown row key
364 |         boolean pass = false;
365 |         try {
366 |             data.removeRow("XXX");
367 |         }
368 |         catch (UnknownKeyException e) {
369 |             pass = true;
370 |         }
371 |         assertTrue(pass);
372 |         
373 |         // try null row key
374 |         pass = false;
375 |         try {
376 |             data.removeRow(null);
377 |         }
378 |         catch (IllegalArgumentException e) {
379 |             pass = true;
380 |         }
381 |         assertTrue(pass);
382 |     }
```
