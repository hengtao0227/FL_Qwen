# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.SystemUtilsTest.testJavaVersionAsInt()
Resolved declaration: org.apache.commons.lang3.SystemUtilsTest.testJavaVersionAsInt()
Source: src/test/java/org/apache/commons/lang3/SystemUtilsTest.java

```java
209 |     public void testJavaVersionAsInt() {
210 |         assertEquals(0, SystemUtils.toJavaVersionInt(null));
211 |         assertEquals(0, SystemUtils.toJavaVersionInt(""));
212 |         assertEquals(0, SystemUtils.toJavaVersionInt("0"));
213 |         assertEquals(110, SystemUtils.toJavaVersionInt("1.1"));
214 |         assertEquals(120, SystemUtils.toJavaVersionInt("1.2"));
215 |         assertEquals(130, SystemUtils.toJavaVersionInt("1.3.0"));
216 |         assertEquals(131, SystemUtils.toJavaVersionInt("1.3.1"));
217 |         assertEquals(140, SystemUtils.toJavaVersionInt("1.4.0"));
218 |         assertEquals(141, SystemUtils.toJavaVersionInt("1.4.1"));
219 |         assertEquals(142, SystemUtils.toJavaVersionInt("1.4.2"));
220 |         assertEquals(150, SystemUtils.toJavaVersionInt("1.5.0"));
221 |         assertEquals(160, SystemUtils.toJavaVersionInt("1.6.0"));
222 |         assertEquals(131, SystemUtils.toJavaVersionInt("JavaVM-1.3.1"));
223 |         assertEquals(131, SystemUtils.toJavaVersionInt("1.3.1 subset"));
224 |         // This used to return 0f in [lang] version 2.5:
225 |         assertEquals(130, SystemUtils.toJavaVersionInt("XXX-1.3.x"));
226 |     }
```
