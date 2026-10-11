# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestPartial_Constructors.testConstructorEx7_TypeArray_intArray()
Resolved declaration: org.joda.time.TestPartial_Constructors.testConstructorEx7_TypeArray_intArray()
Source: src/test/java/org/joda/time/TestPartial_Constructors.java

```java
260 |     public void testConstructorEx7_TypeArray_intArray() throws Throwable {
261 |         int[] values = new int[] {1, 1, 1};
262 |         DateTimeFieldType[] types = new DateTimeFieldType[] {
263 |             DateTimeFieldType.dayOfMonth(), DateTimeFieldType.year(), DateTimeFieldType.monthOfYear() };
264 |         try {
265 |             new Partial(types, values);
266 |             fail();
267 |         } catch (IllegalArgumentException ex) {
268 |             assertMessageContains(ex, "must be in order", "largest-smallest");
269 |         }
270 |         
271 |         types = new DateTimeFieldType[] {
272 |             DateTimeFieldType.year(), DateTimeFieldType.dayOfMonth(), DateTimeFieldType.monthOfYear() };
273 |         try {
274 |             new Partial(types, values);
275 |             fail();
276 |         } catch (IllegalArgumentException ex) {
277 |             assertMessageContains(ex, "must be in order", "largest-smallest");
278 |         }
279 |         
280 |         types = new DateTimeFieldType[] {
281 |             DateTimeFieldType.year(), DateTimeFieldType.era(), DateTimeFieldType.monthOfYear() };
282 |         try {
283 |             new Partial(types, values);
284 |             fail();
285 |         } catch (IllegalArgumentException ex) {
286 |             assertMessageContains(ex, "must be in order", "largest-smallest");
287 |         }
288 |         
289 |         types = new DateTimeFieldType[] {
290 |             DateTimeFieldType.year(), DateTimeFieldType.dayOfMonth(), DateTimeFieldType.era() };
291 |         try {
292 |             new Partial(types, values);
293 |             fail();
294 |         } catch (IllegalArgumentException ex) {
295 |             assertMessageContains(ex, "must be in order", "largest-smallest");
296 |         }
297 |         
298 |         types = new DateTimeFieldType[] {
299 |             DateTimeFieldType.year(), DateTimeFieldType.dayOfMonth(), DateTimeFieldType.dayOfYear() };
300 |         try {
301 |             new Partial(types, values);
302 |             fail();
303 |         } catch (IllegalArgumentException ex) {
304 |             assertMessageContains(ex, "must be in order", "largest-smallest");
305 |         }
306 |         
307 |         types = new DateTimeFieldType[] {
308 |             DateTimeFieldType.yearOfEra(), DateTimeFieldType.year(), DateTimeFieldType.dayOfYear() };
309 |         try {
310 |             new Partial(types, values);
311 |             fail();
312 |         } catch (IllegalArgumentException ex) {
313 |             assertMessageContains(ex, "must be in order", "largest-smallest");
314 |         }
315 |     }
```
