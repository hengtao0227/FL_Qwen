# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Source: src/test/java/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
176 |     public void testCreateNumber() {
177 |         // a lot of things can go wrong
178 |         assertEquals("createNumber(String) 1 failed", new Float("1234.5"), NumberUtils.createNumber("1234.5"));
179 |         assertEquals("createNumber(String) 2 failed", new Integer("12345"), NumberUtils.createNumber("12345"));
180 |         assertEquals("createNumber(String) 3 failed", new Double("1234.5"), NumberUtils.createNumber("1234.5D"));
181 |         assertEquals("createNumber(String) 3 failed", new Double("1234.5"), NumberUtils.createNumber("1234.5d"));
182 |         assertEquals("createNumber(String) 4 failed", new Float("1234.5"), NumberUtils.createNumber("1234.5F"));
183 |         assertEquals("createNumber(String) 4 failed", new Float("1234.5"), NumberUtils.createNumber("1234.5f"));
184 |         assertEquals("createNumber(String) 5 failed", new Long(Integer.MAX_VALUE + 1L), NumberUtils.createNumber(""
185 |             + (Integer.MAX_VALUE + 1L)));
186 |         assertEquals("createNumber(String) 6 failed", new Long(12345), NumberUtils.createNumber("12345L"));
187 |         assertEquals("createNumber(String) 6 failed", new Long(12345), NumberUtils.createNumber("12345l"));
188 |         assertEquals("createNumber(String) 7 failed", new Float("-1234.5"), NumberUtils.createNumber("-1234.5"));
189 |         assertEquals("createNumber(String) 8 failed", new Integer("-12345"), NumberUtils.createNumber("-12345"));
190 |         assertTrue("createNumber(String) 9 failed", 0xFADE == NumberUtils.createNumber("0xFADE").intValue());
191 |         assertTrue("createNumber(String) 10 failed", -0xFADE == NumberUtils.createNumber("-0xFADE").intValue());
192 |         assertEquals("createNumber(String) 11 failed", new Double("1.1E200"), NumberUtils.createNumber("1.1E200"));
193 |         assertEquals("createNumber(String) 12 failed", new Float("1.1E20"), NumberUtils.createNumber("1.1E20"));
194 |         assertEquals("createNumber(String) 13 failed", new Double("-1.1E200"), NumberUtils.createNumber("-1.1E200"));
195 |         assertEquals("createNumber(String) 14 failed", new Double("1.1E-200"), NumberUtils.createNumber("1.1E-200"));
196 |         assertEquals("createNumber(null) failed", null, NumberUtils.createNumber(null));
197 |         assertEquals("createNumber(String) failed", new BigInteger("12345678901234567890"), NumberUtils
198 |                 .createNumber("12345678901234567890L"));
199 | 
200 |         // jdk 1.2 doesn't support this. unsure about jdk 1.2.2
201 |         if (SystemUtils.isJavaVersionAtLeast(1.3f)) {
202 |             assertEquals("createNumber(String) 15 failed", new BigDecimal("1.1E-700"), NumberUtils
203 |                     .createNumber("1.1E-700F"));
204 |         }
205 |         assertEquals("createNumber(String) 16 failed", new Long("10" + Integer.MAX_VALUE), NumberUtils
206 |                 .createNumber("10" + Integer.MAX_VALUE + "L"));
207 |         assertEquals("createNumber(String) 17 failed", new Long("10" + Integer.MAX_VALUE), NumberUtils
208 |                 .createNumber("10" + Integer.MAX_VALUE));
209 |         assertEquals("createNumber(String) 18 failed", new BigInteger("10" + Long.MAX_VALUE), NumberUtils
210 |                 .createNumber("10" + Long.MAX_VALUE));
211 | 
212 |         // LANG-521
213 |         assertEquals("createNumber(String) LANG-521 failed", new Float("2."), NumberUtils.createNumber("2."));
214 | 
215 |         // LANG-638
216 |         assertFalse("createNumber(String) succeeded", checkCreateNumber("1eE"));
217 |     }
```
