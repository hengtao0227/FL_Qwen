# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Source: src/test/java/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
181 |     @Test
182 |     public void testCreateNumber() {
183 |         // a lot of things can go wrong
184 |         assertEquals("createNumber(String) 1 failed", Float.valueOf("1234.5"), NumberUtils.createNumber("1234.5"));
185 |         assertEquals("createNumber(String) 2 failed", Integer.valueOf("12345"), NumberUtils.createNumber("12345"));
186 |         assertEquals("createNumber(String) 3 failed", Double.valueOf("1234.5"), NumberUtils.createNumber("1234.5D"));
187 |         assertEquals("createNumber(String) 3 failed", Double.valueOf("1234.5"), NumberUtils.createNumber("1234.5d"));
188 |         assertEquals("createNumber(String) 4 failed", Float.valueOf("1234.5"), NumberUtils.createNumber("1234.5F"));
189 |         assertEquals("createNumber(String) 4 failed", Float.valueOf("1234.5"), NumberUtils.createNumber("1234.5f"));
190 |         assertEquals("createNumber(String) 5 failed", Long.valueOf(Integer.MAX_VALUE + 1L), NumberUtils.createNumber(""
191 |             + (Integer.MAX_VALUE + 1L)));
192 |         assertEquals("createNumber(String) 6 failed", Long.valueOf(12345), NumberUtils.createNumber("12345L"));
193 |         assertEquals("createNumber(String) 6 failed", Long.valueOf(12345), NumberUtils.createNumber("12345l"));
194 |         assertEquals("createNumber(String) 7 failed", Float.valueOf("-1234.5"), NumberUtils.createNumber("-1234.5"));
195 |         assertEquals("createNumber(String) 8 failed", Integer.valueOf("-12345"), NumberUtils.createNumber("-12345"));
196 |         assertTrue("createNumber(String) 9a failed", 0xFADE == NumberUtils.createNumber("0xFADE").intValue());
197 |         assertTrue("createNumber(String) 9b failed", 0xFADE == NumberUtils.createNumber("0Xfade").intValue());
198 |         assertTrue("createNumber(String) 10a failed", -0xFADE == NumberUtils.createNumber("-0xFADE").intValue());
199 |         assertTrue("createNumber(String) 10b failed", -0xFADE == NumberUtils.createNumber("-0Xfade").intValue());
200 |         assertEquals("createNumber(String) 11 failed", Double.valueOf("1.1E200"), NumberUtils.createNumber("1.1E200"));
201 |         assertEquals("createNumber(String) 12 failed", Float.valueOf("1.1E20"), NumberUtils.createNumber("1.1E20"));
202 |         assertEquals("createNumber(String) 13 failed", Double.valueOf("-1.1E200"), NumberUtils.createNumber("-1.1E200"));
203 |         assertEquals("createNumber(String) 14 failed", Double.valueOf("1.1E-200"), NumberUtils.createNumber("1.1E-200"));
204 |         assertEquals("createNumber(null) failed", null, NumberUtils.createNumber(null));
205 |         assertEquals("createNumber(String) failed", new BigInteger("12345678901234567890"), NumberUtils
206 |                 .createNumber("12345678901234567890L"));
207 | 
208 |         // jdk 1.2 doesn't support this. unsure about jdk 1.2.2
209 |         if (SystemUtils.isJavaVersionAtLeast(JAVA_1_3)) {
210 |             assertEquals("createNumber(String) 15 failed", new BigDecimal("1.1E-700"), NumberUtils
211 |                     .createNumber("1.1E-700F"));
212 |         }
213 |         assertEquals("createNumber(String) 16 failed", Long.valueOf("10" + Integer.MAX_VALUE), NumberUtils
214 |                 .createNumber("10" + Integer.MAX_VALUE + "L"));
215 |         assertEquals("createNumber(String) 17 failed", Long.valueOf("10" + Integer.MAX_VALUE), NumberUtils
216 |                 .createNumber("10" + Integer.MAX_VALUE));
217 |         assertEquals("createNumber(String) 18 failed", new BigInteger("10" + Long.MAX_VALUE), NumberUtils
218 |                 .createNumber("10" + Long.MAX_VALUE));
219 | 
220 |         // LANG-521
221 |         assertEquals("createNumber(String) LANG-521 failed", Float.valueOf("2."), NumberUtils.createNumber("2."));
222 | 
223 |         // LANG-638
224 |         assertFalse("createNumber(String) succeeded", checkCreateNumber("1eE"));
225 | 
226 |         // LANG-693
227 |         assertEquals("createNumber(String) LANG-693 failed", Double.valueOf(Double.MAX_VALUE), NumberUtils
228 |                     .createNumber("" + Double.MAX_VALUE));
229 |     }
```
