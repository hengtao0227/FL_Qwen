# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.StringEscapeUtilsTest.testLang720()
Resolved declaration: org.apache.commons.lang3.StringEscapeUtilsTest.testLang720()
Source: src/test/java/org/apache/commons/lang3/StringEscapeUtilsTest.java

```java
428 |     public void testLang720() {
429 |         String input = new StringBuilder("\ud842\udfb7").append("A").toString();
430 |         String escaped = StringEscapeUtils.escapeXml(input);
431 |         assertEquals(input, escaped);
432 |     }
```
