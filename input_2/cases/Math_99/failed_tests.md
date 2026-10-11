# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.util.MathUtilsTest.testGcd()
Resolved declaration: org.apache.commons.math.util.MathUtilsTest.testGcd()
Source: src/test/org/apache/commons/math/util/MathUtilsTest.java

```java
407 |     public void testGcd() {
408 |         int a = 30;
409 |         int b = 50;
410 |         int c = 77;
411 | 
412 |         assertEquals(0, MathUtils.gcd(0, 0));
413 | 
414 |         assertEquals(b, MathUtils.gcd(0, b));
415 |         assertEquals(a, MathUtils.gcd(a, 0));
416 |         assertEquals(b, MathUtils.gcd(0, -b));
417 |         assertEquals(a, MathUtils.gcd(-a, 0));
418 | 
419 |         assertEquals(10, MathUtils.gcd(a, b));
420 |         assertEquals(10, MathUtils.gcd(-a, b));
421 |         assertEquals(10, MathUtils.gcd(a, -b));
422 |         assertEquals(10, MathUtils.gcd(-a, -b));
423 | 
424 |         assertEquals(1, MathUtils.gcd(a, c));
425 |         assertEquals(1, MathUtils.gcd(-a, c));
426 |         assertEquals(1, MathUtils.gcd(a, -c));
427 |         assertEquals(1, MathUtils.gcd(-a, -c));
428 | 
429 |         assertEquals(3 * (1<<15), MathUtils.gcd(3 * (1<<20), 9 * (1<<15)));
430 | 
431 |         assertEquals(Integer.MAX_VALUE, MathUtils.gcd(Integer.MAX_VALUE, 0));
432 |         assertEquals(Integer.MAX_VALUE, MathUtils.gcd(-Integer.MAX_VALUE, 0));
433 |         assertEquals(1<<30, MathUtils.gcd(1<<30, -Integer.MIN_VALUE));
434 |         try {
435 |             // gcd(Integer.MIN_VALUE, 0) > Integer.MAX_VALUE
436 |             MathUtils.gcd(Integer.MIN_VALUE, 0);
437 |             fail("expecting ArithmeticException");
438 |         } catch (ArithmeticException expected) {
439 |             // expected
440 |         }
441 |         try {
442 |             // gcd(0, Integer.MIN_VALUE) > Integer.MAX_VALUE
443 |             MathUtils.gcd(0, Integer.MIN_VALUE);
444 |             fail("expecting ArithmeticException");
445 |         } catch (ArithmeticException expected) {
446 |             // expected
447 |         }
448 |         try {
449 |             // gcd(Integer.MIN_VALUE, Integer.MIN_VALUE) > Integer.MAX_VALUE
450 |             MathUtils.gcd(Integer.MIN_VALUE, Integer.MIN_VALUE);
451 |             fail("expecting ArithmeticException");
452 |         } catch (ArithmeticException expected) {
453 |             // expected
454 |         }
455 |     }
```

## org.apache.commons.math.util.MathUtilsTest.testLcm()
Resolved declaration: org.apache.commons.math.util.MathUtilsTest.testLcm()
Source: src/test/org/apache/commons/math/util/MathUtilsTest.java

```java
565 |     public void testLcm() {
566 |         int a = 30;
567 |         int b = 50;
568 |         int c = 77;
569 | 
570 |         assertEquals(0, MathUtils.lcm(0, b));
571 |         assertEquals(0, MathUtils.lcm(a, 0));
572 |         assertEquals(b, MathUtils.lcm(1, b));
573 |         assertEquals(a, MathUtils.lcm(a, 1));
574 |         assertEquals(150, MathUtils.lcm(a, b));
575 |         assertEquals(150, MathUtils.lcm(-a, b));
576 |         assertEquals(150, MathUtils.lcm(a, -b));
577 |         assertEquals(150, MathUtils.lcm(-a, -b));
578 |         assertEquals(2310, MathUtils.lcm(a, c));
579 | 
580 |         // Assert that no intermediate value overflows:
581 |         // The naive implementation of lcm(a,b) would be (a*b)/gcd(a,b)
582 |         assertEquals((1<<20)*15, MathUtils.lcm((1<<20)*3, (1<<20)*5));
583 | 
584 |         // Special case
585 |         assertEquals(0, MathUtils.lcm(0, 0));
586 | 
587 |         try {
588 |             // lcm == abs(MIN_VALUE) cannot be represented as a nonnegative int
589 |             MathUtils.lcm(Integer.MIN_VALUE, 1);
590 |             fail("Expecting ArithmeticException");
591 |         } catch (ArithmeticException ex) {
592 |             // expected
593 |         }
594 |         
595 |         try {
596 |             // lcm == abs(MIN_VALUE) cannot be represented as a nonnegative int
597 |             MathUtils.lcm(Integer.MIN_VALUE, 1<<20);
598 |             fail("Expecting ArithmeticException");
599 |         } catch (ArithmeticException ex) {
600 |             // expected
601 |         }
602 | 
603 |         try {
604 |             MathUtils.lcm(Integer.MAX_VALUE, Integer.MAX_VALUE - 1);
605 |             fail("Expecting ArithmeticException");
606 |         } catch (ArithmeticException ex) {
607 |             // expected
608 |         }
609 |     }
```
