# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.util.MathUtilsTest.testBinomialCoefficientLarge()
Resolved declaration: org.apache.commons.math.util.MathUtilsTest.testBinomialCoefficientLarge()
Source: src/test/org/apache/commons/math/util/MathUtilsTest.java

```java
176 |     public void testBinomialCoefficientLarge() throws Exception {
177 |         // This tests all legal and illegal values for n <= 200.
178 |         for (int n = 0; n <= 200; n++) {
179 |             for (int k = 0; k <= n; k++) {
180 |                 long ourResult = -1;
181 |                 long exactResult = -1;
182 |                 boolean shouldThrow = false;
183 |                 boolean didThrow = false;
184 |                 try {
185 |                     ourResult = MathUtils.binomialCoefficient(n, k);
186 |                 } catch (ArithmeticException ex) {
187 |                     didThrow = true;
188 |                 }
189 |                 try {
190 |                     exactResult = binomialCoefficient(n, k);
191 |                 } catch (ArithmeticException ex) {
192 |                     shouldThrow = true;
193 |                 }
194 |                 assertEquals(n+","+k, shouldThrow, didThrow);
195 |                 assertEquals(n+","+k, exactResult, ourResult);
196 |                 assertTrue(n+","+k, (n > 66 || !didThrow));
197 |             }
198 |         }
199 | 
200 |         long ourResult = MathUtils.binomialCoefficient(300, 3);
201 |         long exactResult = binomialCoefficient(300, 3);
202 |         assertEquals(exactResult, ourResult);
203 | 
204 |         ourResult = MathUtils.binomialCoefficient(700, 697);
205 |         exactResult = binomialCoefficient(700, 697);
206 |         assertEquals(exactResult, ourResult);
207 | 
208 |         // This one should throw
209 |         try {
210 |             MathUtils.binomialCoefficient(700, 300);
211 |             fail("Expecting ArithmeticException");
212 |         } catch (ArithmeticException ex) {
213 |             // Expected
214 |         }
215 | 
216 |         // Larger values cannot be computed directly by our
217 |         // test implementation because of stack limitations,
218 |         // so we make little jumps to fill the cache.
219 |         for (int i = 2000; i <= 10000; i += 2000) {
220 |             ourResult = MathUtils.binomialCoefficient(i, 3);
221 |             exactResult = binomialCoefficient(i, 3);
222 |             assertEquals(exactResult, ourResult);
223 |         }
224 | 
225 |     }
```
