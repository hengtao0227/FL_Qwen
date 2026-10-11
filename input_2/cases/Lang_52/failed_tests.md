# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.StringEscapeUtilsTest.testEscapeJavaScript()
Resolved declaration: org.apache.commons.lang.StringEscapeUtilsTest.testEscapeJavaScript()
Source: src/test/org/apache/commons/lang/StringEscapeUtilsTest.java

```java
169 |     public void testEscapeJavaScript() {
170 |         assertEquals(null, StringEscapeUtils.escapeJavaScript(null));
171 |         try {
172 |             StringEscapeUtils.escapeJavaScript(null, null);
173 |             fail();
174 |         } catch (IOException ex) {
175 |             fail();
176 |         } catch (IllegalArgumentException ex) {
177 |         }
178 |         try {
179 |             StringEscapeUtils.escapeJavaScript(null, "");
180 |             fail();
181 |         } catch (IOException ex) {
182 |             fail();
183 |         } catch (IllegalArgumentException ex) {
184 |         }
185 |         
186 |         assertEquals("He didn\\'t say, \\\"stop!\\\"", StringEscapeUtils.escapeJavaScript("He didn't say, \"stop!\""));
187 |         assertEquals("document.getElementById(\\\"test\\\").value = \\'<script>alert(\\'aaa\\');<\\/script>\\';", 
188 |                 StringEscapeUtils.escapeJavaScript("document.getElementById(\"test\").value = '<script>alert('aaa');</script>';"));
189 |     }
```
