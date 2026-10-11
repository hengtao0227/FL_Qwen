# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.StringEscapeUtilsTest.testEscapeHtmlHighUnicode()
Resolved declaration: org.apache.commons.lang.StringEscapeUtilsTest.testEscapeHtmlHighUnicode()
Source: src/test/org/apache/commons/lang/StringEscapeUtilsTest.java

```java
420 |     public void testEscapeHtmlHighUnicode() throws java.io.UnsupportedEncodingException {
421 |         // this is the utf8 representation of the character:
422 |         // COUNTING ROD UNIT DIGIT THREE
423 |         // in unicode
424 |         // codepoint: U+1D362
425 |         byte[] data = new byte[] { (byte)0xF0, (byte)0x9D, (byte)0x8D, (byte)0xA2 };
426 | 
427 |         String escaped = StringEscapeUtils.escapeHtml( new String(data, "UTF8") );
428 |         String unescaped = StringEscapeUtils.unescapeHtml( escaped );
429 | 
430 |         assertEquals( "High unicode was not escaped correctly", "&#119650;", escaped);
431 |     }
```
