# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.util.FastMathTest.testMath905LargePositive()
Resolved declaration: org.apache.commons.math3.util.FastMathTest.testMath905LargePositive()
Source: src/test/java/org/apache/commons/math3/util/FastMathTest.java

```java
160 |     @Test
161 |     public void testMath905LargePositive() {
162 |         final double start = StrictMath.log(Double.MAX_VALUE);
163 |         final double endT = StrictMath.sqrt(2) * StrictMath.sqrt(Double.MAX_VALUE);
164 |         final double end = 2 * StrictMath.log(endT);
165 | 
166 |         double maxErr = 0;
167 |         for (double x = start; x < end; x += 1e-3) {
168 |             final double tst = FastMath.cosh(x);
169 |             final double ref = Math.cosh(x);
170 |             maxErr = FastMath.max(maxErr, FastMath.abs(ref - tst) / FastMath.ulp(ref));            
171 |         }
172 |         Assert.assertEquals(0, maxErr, 3);
173 | 
174 |         for (double x = start; x < end; x += 1e-3) {
175 |             final double tst = FastMath.sinh(x);
176 |             final double ref = Math.sinh(x);
177 |             maxErr = FastMath.max(maxErr, FastMath.abs(ref - tst) / FastMath.ulp(ref));            
178 |         }
179 |         Assert.assertEquals(0, maxErr, 3);
180 |     }
```

## org.apache.commons.math3.util.FastMathTest.testMath905LargeNegative()
Resolved declaration: org.apache.commons.math3.util.FastMathTest.testMath905LargeNegative()
Source: src/test/java/org/apache/commons/math3/util/FastMathTest.java

```java
182 |     @Test
183 |     public void testMath905LargeNegative() {
184 |         final double start = -StrictMath.log(Double.MAX_VALUE);
185 |         final double endT = StrictMath.sqrt(2) * StrictMath.sqrt(Double.MAX_VALUE);
186 |         final double end = -2 * StrictMath.log(endT);
187 | 
188 |         double maxErr = 0;
189 |         for (double x = start; x > end; x -= 1e-3) {
190 |             final double tst = FastMath.cosh(x);
191 |             final double ref = Math.cosh(x);
192 |             maxErr = FastMath.max(maxErr, FastMath.abs(ref - tst) / FastMath.ulp(ref));            
193 |         }
194 |         Assert.assertEquals(0, maxErr, 3);
195 | 
196 |         for (double x = start; x > end; x -= 1e-3) {
197 |             final double tst = FastMath.sinh(x);
198 |             final double ref = Math.sinh(x);
199 |             maxErr = FastMath.max(maxErr, FastMath.abs(ref - tst) / FastMath.ulp(ref));            
200 |         }
201 |         Assert.assertEquals(0, maxErr, 3);
202 |     }
```
