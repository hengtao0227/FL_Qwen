# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.FractionTest.testReducedFactory_int_int()
Resolved declaration: org.apache.commons.lang3.math.FractionTest.testReducedFactory_int_int()
Source: src/test/java/org/apache/commons/lang3/math/FractionTest.java

```java
250 |     public void testReducedFactory_int_int() {
251 |         Fraction f = null;
252 |         
253 |         // zero
254 |         f = Fraction.getReducedFraction(0, 1);
255 |         assertEquals(0, f.getNumerator());
256 |         assertEquals(1, f.getDenominator());
257 |         
258 |         // normal
259 |         f = Fraction.getReducedFraction(1, 1);
260 |         assertEquals(1, f.getNumerator());
261 |         assertEquals(1, f.getDenominator());
262 |         
263 |         f = Fraction.getReducedFraction(2, 1);
264 |         assertEquals(2, f.getNumerator());
265 |         assertEquals(1, f.getDenominator());
266 |         
267 |         // improper
268 |         f = Fraction.getReducedFraction(22, 7);
269 |         assertEquals(22, f.getNumerator());
270 |         assertEquals(7, f.getDenominator());
271 |         
272 |         // negatives
273 |         f = Fraction.getReducedFraction(-6, 10);
274 |         assertEquals(-3, f.getNumerator());
275 |         assertEquals(5, f.getDenominator());
276 |         
277 |         f = Fraction.getReducedFraction(6, -10);
278 |         assertEquals(-3, f.getNumerator());
279 |         assertEquals(5, f.getDenominator());
280 |         
281 |         f = Fraction.getReducedFraction(-6, -10);
282 |         assertEquals(3, f.getNumerator());
283 |         assertEquals(5, f.getDenominator());
284 |         
285 |         // zero denominator
286 |         try {
287 |             f = Fraction.getReducedFraction(1, 0);
288 |             fail("expecting ArithmeticException");
289 |         } catch (ArithmeticException ex) {}
290 |         
291 |         try {
292 |             f = Fraction.getReducedFraction(2, 0);
293 |             fail("expecting ArithmeticException");
294 |         } catch (ArithmeticException ex) {}
295 |         
296 |         try {
297 |             f = Fraction.getReducedFraction(-3, 0);
298 |             fail("expecting ArithmeticException");
299 |         } catch (ArithmeticException ex) {}
300 | 
301 |         // reduced        
302 |         f = Fraction.getReducedFraction(0, 2);
303 |         assertEquals(0, f.getNumerator());
304 |         assertEquals(1, f.getDenominator());
305 |         
306 |         f = Fraction.getReducedFraction(2, 2);
307 |         assertEquals(1, f.getNumerator());
308 |         assertEquals(1, f.getDenominator());
309 |         
310 |         f = Fraction.getReducedFraction(2, 4);
311 |         assertEquals(1, f.getNumerator());
312 |         assertEquals(2, f.getDenominator());
313 |         
314 |         f = Fraction.getReducedFraction(15, 10);
315 |         assertEquals(3, f.getNumerator());
316 |         assertEquals(2, f.getDenominator());
317 |         
318 |         f = Fraction.getReducedFraction(121, 22);
319 |         assertEquals(11, f.getNumerator());
320 |         assertEquals(2, f.getDenominator());
321 |         
322 |         // Extreme values 
323 |         // OK, can reduce before negating
324 |         f = Fraction.getReducedFraction(-2, Integer.MIN_VALUE);
325 |         assertEquals(1, f.getNumerator());
326 |         assertEquals(-(Integer.MIN_VALUE / 2), f.getDenominator());
327 |         
328 |         // Can't reduce, negation will throw
329 |         try { 
330 |             f = Fraction.getReducedFraction(-7, Integer.MIN_VALUE);  
331 |             fail("Expecting ArithmeticException");
332 |         } catch (ArithmeticException ex) {}      
333 | 
334 |         // LANG-662
335 |         f = Fraction.getReducedFraction(Integer.MIN_VALUE, 2);
336 |         assertEquals(Integer.MIN_VALUE / 2, f.getNumerator());
337 |         assertEquals(1, f.getDenominator());
338 |     }
```

## org.apache.commons.lang3.math.FractionTest.testReduce()
Resolved declaration: org.apache.commons.lang3.math.FractionTest.testReduce()
Source: src/test/java/org/apache/commons/lang3/math/FractionTest.java

```java
610 |     public void testReduce() {
611 |         Fraction f = null;
612 |         
613 |         f = Fraction.getFraction(50, 75);
614 |         Fraction result = f.reduce();
615 |         assertEquals(2, result.getNumerator());
616 |         assertEquals(3, result.getDenominator());
617 | 
618 |         f = Fraction.getFraction(-2, -3);
619 |         result = f.reduce();
620 |         assertEquals(2, result.getNumerator());
621 |         assertEquals(3, result.getDenominator());
622 | 
623 |         f = Fraction.getFraction(2, -3);
624 |         result = f.reduce();
625 |         assertEquals(-2, result.getNumerator());
626 |         assertEquals(3, result.getDenominator());
627 | 
628 |         f = Fraction.getFraction(-2, 3);
629 |         result = f.reduce();
630 |         assertEquals(-2, result.getNumerator());
631 |         assertEquals(3, result.getDenominator());
632 |         assertSame(f, result);
633 | 
634 |         f = Fraction.getFraction(2, 3);
635 |         result = f.reduce();
636 |         assertEquals(2, result.getNumerator());
637 |         assertEquals(3, result.getDenominator());
638 |         assertSame(f, result);
639 | 
640 |         f = Fraction.getFraction(0, 1);
641 |         result = f.reduce();
642 |         assertEquals(0, result.getNumerator());
643 |         assertEquals(1, result.getDenominator());
644 |         assertSame(f, result);
645 | 
646 |         f = Fraction.getFraction(0, 100);
647 |         result = f.reduce();
648 |         assertEquals(0, result.getNumerator());
649 |         assertEquals(1, result.getDenominator());
650 |         assertSame(result, Fraction.ZERO);
651 | 
652 |         f = Fraction.getFraction(Integer.MIN_VALUE, 2);
653 |         result = f.reduce();
654 |         assertEquals(Integer.MIN_VALUE / 2, result.getNumerator());
655 |         assertEquals(1, result.getDenominator());
656 |     }
```
