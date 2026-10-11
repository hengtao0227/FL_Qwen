# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.fraction.BigFractionTest.testDigitLimitConstructor()
Resolved declaration: org.apache.commons.math3.fraction.BigFractionTest.testDigitLimitConstructor()
Source: src/test/java/org/apache/commons/math3/fraction/BigFractionTest.java

```java
147 |     @Test
148 |     public void testDigitLimitConstructor() throws ConvergenceException {
149 |         assertFraction(2, 5, new BigFraction(0.4, 9));
150 |         assertFraction(2, 5, new BigFraction(0.4, 99));
151 |         assertFraction(2, 5, new BigFraction(0.4, 999));
152 | 
153 |         assertFraction(3, 5, new BigFraction(0.6152, 9));
154 |         assertFraction(8, 13, new BigFraction(0.6152, 99));
155 |         assertFraction(510, 829, new BigFraction(0.6152, 999));
156 |         assertFraction(769, 1250, new BigFraction(0.6152, 9999));
157 |         
158 |         // MATH-996
159 |         assertFraction(1, 2, new BigFraction(0.5000000001, 10));
160 |     }
```

## org.apache.commons.math3.fraction.FractionTest.testDigitLimitConstructor()
Resolved declaration: org.apache.commons.math3.fraction.FractionTest.testDigitLimitConstructor()
Source: src/test/java/org/apache/commons/math3/fraction/FractionTest.java

```java
122 |     @Test
123 |     public void testDigitLimitConstructor() throws ConvergenceException  {
124 |         assertFraction(2, 5, new Fraction(0.4,   9));
125 |         assertFraction(2, 5, new Fraction(0.4,  99));
126 |         assertFraction(2, 5, new Fraction(0.4, 999));
127 | 
128 |         assertFraction(3, 5,      new Fraction(0.6152,    9));
129 |         assertFraction(8, 13,     new Fraction(0.6152,   99));
130 |         assertFraction(510, 829,  new Fraction(0.6152,  999));
131 |         assertFraction(769, 1250, new Fraction(0.6152, 9999));
132 | 
133 |         // MATH-996
134 |         assertFraction(1, 2, new Fraction(0.5000000001, 10));
135 |     }
```
