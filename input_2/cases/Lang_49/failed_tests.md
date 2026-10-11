# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.math.FractionTest.testReduce()
Resolved declaration: org.apache.commons.lang.math.FractionTest.testReduce()
Source: src/test/org/apache/commons/lang/math/FractionTest.java

```java
616 |     public void testReduce() {
617 |         Fraction f = null;
618 |         
619 |         f = Fraction.getFraction(50, 75);
620 |         Fraction result = f.reduce();
621 |         assertEquals(2, result.getNumerator());
622 |         assertEquals(3, result.getDenominator());
623 | 
624 |         f = Fraction.getFraction(-2, -3);
625 |         result = f.reduce();
626 |         assertEquals(2, result.getNumerator());
627 |         assertEquals(3, result.getDenominator());
628 | 
629 |         f = Fraction.getFraction(2, -3);
630 |         result = f.reduce();
631 |         assertEquals(-2, result.getNumerator());
632 |         assertEquals(3, result.getDenominator());
633 | 
634 |         f = Fraction.getFraction(-2, 3);
635 |         result = f.reduce();
636 |         assertEquals(-2, result.getNumerator());
637 |         assertEquals(3, result.getDenominator());
638 |         assertSame(f, result);
639 | 
640 |         f = Fraction.getFraction(2, 3);
641 |         result = f.reduce();
642 |         assertEquals(2, result.getNumerator());
643 |         assertEquals(3, result.getDenominator());
644 |         assertSame(f, result);
645 | 
646 |         f = Fraction.getFraction(0, 1);
647 |         result = f.reduce();
648 |         assertEquals(0, result.getNumerator());
649 |         assertEquals(1, result.getDenominator());
650 |         assertSame(f, result);
651 | 
652 |         f = Fraction.getFraction(0, 100);
653 |         result = f.reduce();
654 |         assertEquals(0, result.getNumerator());
655 |         assertEquals(1, result.getDenominator());
656 |         assertSame(result, Fraction.ZERO);
657 |     }
```
