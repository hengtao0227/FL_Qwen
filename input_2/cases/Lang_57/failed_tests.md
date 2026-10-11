# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.LocaleUtilsTest.testAvailableLocaleSet()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testAvailableLocaleSet()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
364 |     public void testAvailableLocaleSet() {
365 |         Set set = LocaleUtils.availableLocaleSet();
366 |         Set set2 = LocaleUtils.availableLocaleSet();
367 |         assertNotNull(set);
368 |         assertSame(set, set2);
369 |         assertUnmodifiableCollection(set);
370 |         
371 |         Locale[] jdkLocaleArray = Locale.getAvailableLocales();
372 |         List jdkLocaleList = Arrays.asList(jdkLocaleArray);
373 |         Set jdkLocaleSet = new HashSet(jdkLocaleList);
374 |         assertEquals(jdkLocaleSet, set);
375 |     }
```

## org.apache.commons.lang.LocaleUtilsTest.testIsAvailableLocale()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testIsAvailableLocale()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
381 |     public void testIsAvailableLocale() {
382 |         Set set = LocaleUtils.availableLocaleSet();
383 |         assertEquals(set.contains(LOCALE_EN), LocaleUtils.isAvailableLocale(LOCALE_EN));
384 |         assertEquals(set.contains(LOCALE_EN_US), LocaleUtils.isAvailableLocale(LOCALE_EN_US));
385 |         assertEquals(set.contains(LOCALE_EN_US_ZZZZ), LocaleUtils.isAvailableLocale(LOCALE_EN_US_ZZZZ));
386 |         assertEquals(set.contains(LOCALE_FR), LocaleUtils.isAvailableLocale(LOCALE_FR));
387 |         assertEquals(set.contains(LOCALE_FR_CA), LocaleUtils.isAvailableLocale(LOCALE_FR_CA));
388 |         assertEquals(set.contains(LOCALE_QQ), LocaleUtils.isAvailableLocale(LOCALE_QQ));
389 |         assertEquals(set.contains(LOCALE_QQ_ZZ), LocaleUtils.isAvailableLocale(LOCALE_QQ_ZZ));
390 |     }
```

## org.apache.commons.lang.LocaleUtilsTest.testAvailableLocaleList()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testAvailableLocaleList()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
348 |     public void testAvailableLocaleList() {
349 |         List list = LocaleUtils.availableLocaleList();
350 |         List list2 = LocaleUtils.availableLocaleList();
351 |         assertNotNull(list);
352 |         assertSame(list, list2);
353 |         assertUnmodifiableCollection(list);
354 |         
355 |         Locale[] jdkLocaleArray = Locale.getAvailableLocales();
356 |         List jdkLocaleList = Arrays.asList(jdkLocaleArray);
357 |         assertEquals(jdkLocaleList, list);
358 |     }
```

## org.apache.commons.lang.LocaleUtilsTest.testCountriesByLanguage()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testCountriesByLanguage()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
479 |     public void testCountriesByLanguage() {
480 |         assertCountriesByLanguage(null, new String[0]);
481 |         assertCountriesByLanguage("de", new String[]{"DE", "CH", "AT", "LU"});
482 |         assertCountriesByLanguage("zz", new String[0]);
483 |         assertCountriesByLanguage("it", new String[]{"IT", "CH"});
484 |     }
```

## org.apache.commons.lang.LocaleUtilsTest.testLocaleLookupList_LocaleLocale()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testLocaleLookupList_LocaleLocale()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
294 |     public void testLocaleLookupList_LocaleLocale() {
295 |         assertLocaleLookupList(LOCALE_QQ, LOCALE_QQ, 
296 |                 new Locale[]{LOCALE_QQ});
297 |         assertLocaleLookupList(LOCALE_EN, LOCALE_EN, 
298 |                 new Locale[]{LOCALE_EN});
299 |         
300 |         assertLocaleLookupList(LOCALE_EN_US, LOCALE_EN_US, 
301 |             new Locale[]{
302 |                 LOCALE_EN_US,
303 |                 LOCALE_EN});
304 |         assertLocaleLookupList(LOCALE_EN_US, LOCALE_QQ,
305 |             new Locale[] {
306 |                 LOCALE_EN_US,
307 |                 LOCALE_EN,
308 |                 LOCALE_QQ});
309 |         assertLocaleLookupList(LOCALE_EN_US, LOCALE_QQ_ZZ,
310 |             new Locale[] {
311 |                 LOCALE_EN_US,
312 |                 LOCALE_EN,
313 |                 LOCALE_QQ_ZZ});
314 |         
315 |         assertLocaleLookupList(LOCALE_EN_US_ZZZZ, null,
316 |             new Locale[] {
317 |                 LOCALE_EN_US_ZZZZ,
318 |                 LOCALE_EN_US,
319 |                 LOCALE_EN});
320 |         assertLocaleLookupList(LOCALE_EN_US_ZZZZ, LOCALE_EN_US_ZZZZ,
321 |             new Locale[] {
322 |                 LOCALE_EN_US_ZZZZ,
323 |                 LOCALE_EN_US,
324 |                 LOCALE_EN});
325 |         assertLocaleLookupList(LOCALE_EN_US_ZZZZ, LOCALE_QQ,
326 |             new Locale[] {
327 |                 LOCALE_EN_US_ZZZZ,
328 |                 LOCALE_EN_US,
329 |                 LOCALE_EN,
330 |                 LOCALE_QQ});
331 |         assertLocaleLookupList(LOCALE_EN_US_ZZZZ, LOCALE_QQ_ZZ,
332 |             new Locale[] {
333 |                 LOCALE_EN_US_ZZZZ,
334 |                 LOCALE_EN_US,
335 |                 LOCALE_EN,
336 |                 LOCALE_QQ_ZZ});
337 |         assertLocaleLookupList(LOCALE_FR_CA, LOCALE_EN,
338 |             new Locale[] {
339 |                 LOCALE_FR_CA,
340 |                 LOCALE_FR,
341 |                 LOCALE_EN});
342 |     }
```

## org.apache.commons.lang.LocaleUtilsTest.testLanguagesByCountry()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testLanguagesByCountry()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
432 |     public void testLanguagesByCountry() {
433 |         assertLanguageByCountry(null, new String[0]);
434 |         assertLanguageByCountry("GB", new String[]{"en"});
435 |         assertLanguageByCountry("ZZ", new String[0]);
436 |         assertLanguageByCountry("CH", new String[]{"fr", "de", "it"});
437 |     }
```

## org.apache.commons.lang.LocaleUtilsTest.testToLocale_1Part()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testToLocale_1Part()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
151 |     public void testToLocale_1Part() {
152 |         assertEquals(null, LocaleUtils.toLocale((String) null));
153 |         
154 |         assertValidToLocale("us");
155 |         assertValidToLocale("fr");
156 |         assertValidToLocale("de");
157 |         assertValidToLocale("zh");
158 |         // Valid format but lang doesnt exist, should make instance anyway
159 |         assertValidToLocale("qq");
160 |         
161 |         try {
162 |             LocaleUtils.toLocale("Us");
163 |             fail("Should fail if not lowercase");
164 |         } catch (IllegalArgumentException iae) {}
165 |         try {
166 |             LocaleUtils.toLocale("US");
167 |             fail("Should fail if not lowercase");
168 |         } catch (IllegalArgumentException iae) {}
169 |         try {
170 |             LocaleUtils.toLocale("uS");
171 |             fail("Should fail if not lowercase");
172 |         } catch (IllegalArgumentException iae) {}
173 |         try {
174 |             LocaleUtils.toLocale("u#");
175 |             fail("Should fail if not lowercase");
176 |         } catch (IllegalArgumentException iae) {}
177 |         
178 |         try {
179 |             LocaleUtils.toLocale("u");
180 |             fail("Must be 2 chars if less than 5");
181 |         } catch (IllegalArgumentException iae) {}
182 |        
183 |         try {
184 |             LocaleUtils.toLocale("uuu");
185 |             fail("Must be 2 chars if less than 5");
186 |         } catch (IllegalArgumentException iae) {}
187 | 
188 |         try {
189 |             LocaleUtils.toLocale("uu_U");
190 |             fail("Must be 2 chars if less than 5");
191 |         } catch (IllegalArgumentException iae) {}
192 |     }        
```

## org.apache.commons.lang.LocaleUtilsTest.testToLocale_2Part()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testToLocale_2Part()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
197 |     public void testToLocale_2Part() {
198 |         assertValidToLocale("us_EN", "us", "EN");
199 |         //valid though doesnt exist
200 |         assertValidToLocale("us_ZH", "us", "ZH");
201 |         
202 |         try {
203 |             LocaleUtils.toLocale("us-EN");
204 |             fail("Should fail as not underscore");
205 |         } catch (IllegalArgumentException iae) {}
206 |         try {
207 |             LocaleUtils.toLocale("us_En");
208 |             fail("Should fail second part not uppercase");
209 |         } catch (IllegalArgumentException iae) {}
210 |         try {
211 |             LocaleUtils.toLocale("us_en");
212 |             fail("Should fail second part not uppercase");
213 |         } catch (IllegalArgumentException iae) {}
214 |         try {
215 |             LocaleUtils.toLocale("us_eN");
216 |             fail("Should fail second part not uppercase");
217 |         } catch (IllegalArgumentException iae) {}
218 |         try {
219 |             LocaleUtils.toLocale("uS_EN");
220 |             fail("Should fail first part not lowercase");
221 |         } catch (IllegalArgumentException iae) {}
222 |         try {
223 |             LocaleUtils.toLocale("us_E3");
224 |             fail("Should fail second part not uppercase");
225 |         } catch (IllegalArgumentException iae) {}
226 |     }        
```

## org.apache.commons.lang.LocaleUtilsTest.testToLocale_3Part()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testToLocale_3Part()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
231 |     public void testToLocale_3Part() {
232 |         assertValidToLocale("us_EN_A", "us", "EN", "A");
233 |         // this isn't pretty, but was caused by a jdk bug it seems
234 |         // http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4210525
235 |         if (SystemUtils.isJavaVersionAtLeast(1.4f)) {
236 |             assertValidToLocale("us_EN_a", "us", "EN", "a");
237 |             assertValidToLocale("us_EN_SFsafdFDsdfF", "us", "EN", "SFsafdFDsdfF");
238 |         } else {
239 |             assertValidToLocale("us_EN_a", "us", "EN", "A");
240 |             assertValidToLocale("us_EN_SFsafdFDsdfF", "us", "EN", "SFSAFDFDSDFF");
241 |         }
242 |         
243 |         try {
244 |             LocaleUtils.toLocale("us_EN-a");
245 |             fail("Should fail as not underscore");
246 |         } catch (IllegalArgumentException iae) {}
247 |         try {
248 |             LocaleUtils.toLocale("uu_UU_");
249 |             fail("Must be 3, 5 or 7+ in length");
250 |         } catch (IllegalArgumentException iae) {}
251 |     }
```

## org.apache.commons.lang.LocaleUtilsTest.testLocaleLookupList_Locale()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testLocaleLookupList_Locale()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
275 |     public void testLocaleLookupList_Locale() {
276 |         assertLocaleLookupList(null, null, new Locale[0]);
277 |         assertLocaleLookupList(LOCALE_QQ, null, new Locale[]{LOCALE_QQ});
278 |         assertLocaleLookupList(LOCALE_EN, null, new Locale[]{LOCALE_EN});
279 |         assertLocaleLookupList(LOCALE_EN, null, new Locale[]{LOCALE_EN});
280 |         assertLocaleLookupList(LOCALE_EN_US, null,
281 |             new Locale[] {
282 |                 LOCALE_EN_US,
283 |                 LOCALE_EN});
284 |         assertLocaleLookupList(LOCALE_EN_US_ZZZZ, null,
285 |             new Locale[] {
286 |                 LOCALE_EN_US_ZZZZ,
287 |                 LOCALE_EN_US,
288 |                 LOCALE_EN});
289 |     }        
```

## org.apache.commons.lang.LocaleUtilsTest.testConstructor()
Resolved declaration: org.apache.commons.lang.LocaleUtilsTest.testConstructor()
Source: src/test/org/apache/commons/lang/LocaleUtilsTest.java

```java
89 |     public void testConstructor() {
90 |         assertNotNull(new LocaleUtils());
91 |         Constructor[] cons = LocaleUtils.class.getDeclaredConstructors();
92 |         assertEquals(1, cons.length);
93 |         assertEquals(true, Modifier.isPublic(cons[0].getModifiers()));
94 |         assertEquals(true, Modifier.isPublic(LocaleUtils.class.getModifiers()));
95 |         assertEquals(false, Modifier.isFinal(LocaleUtils.class.getModifiers()));
96 |     }
```
