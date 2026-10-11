# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.StringUtilsTest.testEscapeSurrogatePairs()
Resolved declaration: org.apache.commons.lang3.StringUtilsTest.testEscapeSurrogatePairs()
Source: src/test/java/org/apache/commons/lang3/StringUtilsTest.java

```java
2185 |     @Test
2186 |     public void testEscapeSurrogatePairs() throws Exception {
2187 |         assertEquals("\uD83D\uDE30", StringEscapeUtils.escapeCsv("\uD83D\uDE30"));
2188 |         // Examples from https://en.wikipedia.org/wiki/UTF-16
2189 |         assertEquals("\uD800\uDC00", StringEscapeUtils.escapeCsv("\uD800\uDC00"));
2190 |         assertEquals("\uD834\uDD1E", StringEscapeUtils.escapeCsv("\uD834\uDD1E"));
2191 |         assertEquals("\uDBFF\uDFFD", StringEscapeUtils.escapeCsv("\uDBFF\uDFFD"));
2192 |         
2193 |     }
```
