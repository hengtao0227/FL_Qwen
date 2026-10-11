# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.fraction.FractionTest.testCompareTo()
Resolved declaration: org.apache.commons.math.fraction.FractionTest.testCompareTo()
Source: src/test/org/apache/commons/math/fraction/FractionTest.java

```java
163 |     public void testCompareTo() {
164 |         Fraction first = new Fraction(1, 2);
165 |         Fraction second = new Fraction(1, 3);
166 |         Fraction third = new Fraction(1, 2);
167 |         
168 |         assertEquals(0, first.compareTo(first));
169 |         assertEquals(0, first.compareTo(third));
170 |         assertEquals(1, first.compareTo(second));
171 |         assertEquals(-1, second.compareTo(first));
172 | 
173 |         // these two values are different approximations of PI
174 |         // the first  one is approximately PI - 3.07e-18
175 |         // the second one is approximately PI + 1.936e-17
176 |         Fraction pi1 = new Fraction(1068966896, 340262731);
177 |         Fraction pi2 = new Fraction( 411557987, 131002976);
178 |         assertEquals(-1, pi1.compareTo(pi2));
179 |         assertEquals( 1, pi2.compareTo(pi1));
180 |         assertEquals(0.0, pi1.doubleValue() - pi2.doubleValue(), 1.0e-20);
181 |     }
```
