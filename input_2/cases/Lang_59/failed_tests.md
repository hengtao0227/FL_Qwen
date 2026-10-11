# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.text.StrBuilderAppendInsertTest.testLang299()
Resolved declaration: org.apache.commons.lang.text.StrBuilderAppendInsertTest.testLang299()
Source: src/test/org/apache/commons/lang/text/StrBuilderAppendInsertTest.java

```java
600 |     public void testLang299() {
601 |         StrBuilder sb = new StrBuilder(1);
602 |         sb.appendFixedWidthPadRight("foo", 1, '-');
603 |         assertEquals("f", sb.toString());
604 |     }
```
