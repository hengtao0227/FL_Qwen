# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Source: src/test/java/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
184 |     @Test
185 |     public void testCreateNumber() {
186 |         // a lot of things can go wrong
187 |         assertEquals("createNumber(String) 1 failed", Float.valueOf("1234.5"), NumberUtils.createNumber("1234.5"));
188 |         assertEquals("createNumber(String) 2 failed", Integer.valueOf("12345"), NumberUtils.createNumber("12345"));
189 |         assertEquals("createNumber(String) 3 failed", Double.valueOf("1234.5"), NumberUtils.createNumber("1234.5D"));
190 |         assertEquals("createNumber(String) 3 failed", Double.valueOf("1234.5"), NumberUtils.createNumber("1234.5d"));
191 |         assertEquals("createNumber(String) 4 failed", Float.valueOf("1234.5"), NumberUtils.createNumber("1234.5F"));
192 |         assertEquals("createNumber(String) 4 failed", Float.valueOf("1234.5"), NumberUtils.createNumber("1234.5f"));
193 |         assertEquals("createNumber(String) 5 failed", Long.valueOf(Integer.MAX_VALUE + 1L), NumberUtils.createNumber(""
194 |             + (Integer.MAX_VALUE + 1L)));
195 |         assertEquals("createNumber(String) 6 failed", Long.valueOf(12345), NumberUtils.createNumber("12345L"));
196 |         assertEquals("createNumber(String) 6 failed", Long.valueOf(12345), NumberUtils.createNumber("12345l"));
197 |         assertEquals("createNumber(String) 7 failed", Float.valueOf("-1234.5"), NumberUtils.createNumber("-1234.5"));
198 |         assertEquals("createNumber(String) 8 failed", Integer.valueOf("-12345"), NumberUtils.createNumber("-12345"));
199 |         assertTrue("createNumber(String) 9a failed", 0xFADE == NumberUtils.createNumber("0xFADE").intValue());
200 |         assertTrue("createNumber(String) 9b failed", 0xFADE == NumberUtils.createNumber("0Xfade").intValue());
201 |         assertTrue("createNumber(String) 10a failed", -0xFADE == NumberUtils.createNumber("-0xFADE").intValue());
202 |         assertTrue("createNumber(String) 10b failed", -0xFADE == NumberUtils.createNumber("-0Xfade").intValue());
203 |         assertEquals("createNumber(String) 11 failed", Double.valueOf("1.1E200"), NumberUtils.createNumber("1.1E200"));
204 |         assertEquals("createNumber(String) 12 failed", Float.valueOf("1.1E20"), NumberUtils.createNumber("1.1E20"));
205 |         assertEquals("createNumber(String) 13 failed", Double.valueOf("-1.1E200"), NumberUtils.createNumber("-1.1E200"));
206 |         assertEquals("createNumber(String) 14 failed", Double.valueOf("1.1E-200"), NumberUtils.createNumber("1.1E-200"));
207 |         assertEquals("createNumber(null) failed", null, NumberUtils.createNumber(null));
208 |         assertEquals("createNumber(String) failed", new BigInteger("12345678901234567890"), NumberUtils
209 |                 .createNumber("12345678901234567890L"));
210 | 
211 |         // jdk 1.2 doesn't support this. unsure about jdk 1.2.2
212 |         if (SystemUtils.isJavaVersionAtLeast(JAVA_1_3)) {
213 |             assertEquals("createNumber(String) 15 failed", new BigDecimal("1.1E-700"), NumberUtils
214 |                     .createNumber("1.1E-700F"));
215 |         }
216 |         assertEquals("createNumber(String) 16 failed", Long.valueOf("10" + Integer.MAX_VALUE), NumberUtils
217 |                 .createNumber("10" + Integer.MAX_VALUE + "L"));
218 |         assertEquals("createNumber(String) 17 failed", Long.valueOf("10" + Integer.MAX_VALUE), NumberUtils
219 |                 .createNumber("10" + Integer.MAX_VALUE));
220 |         assertEquals("createNumber(String) 18 failed", new BigInteger("10" + Long.MAX_VALUE), NumberUtils
221 |                 .createNumber("10" + Long.MAX_VALUE));
222 | 
223 |         // LANG-521
224 |         assertEquals("createNumber(String) LANG-521 failed", Float.valueOf("2."), NumberUtils.createNumber("2."));
225 | 
226 |         // LANG-638
227 |         assertFalse("createNumber(String) succeeded", checkCreateNumber("1eE"));
228 | 
229 |         // LANG-693
230 |         assertEquals("createNumber(String) LANG-693 failed", Double.valueOf(Double.MAX_VALUE), NumberUtils
231 |                     .createNumber("" + Double.MAX_VALUE));
232 |         
233 |         // LANG-822
234 |         // ensure that the underlying negative number would create a BigDecimal
235 |         final Number bigNum = NumberUtils.createNumber("-1.1E-700F");
236 |         assertEquals(BigDecimal.class,bigNum.getClass());
237 |         assertNotNull(bigNum);
238 | 
239 |         // Check that the code fails to create a valid number when preceeded by -- rather than -
240 |         try {
241 |             NumberUtils.createNumber("--1.1E-700F");
242 |             fail("Expected NumberFormatException");
243 |         } catch (NumberFormatException nfe) {
244 |             // expected
245 |         }
246 |     }
```
