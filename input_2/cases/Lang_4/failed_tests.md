# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.text.translate.LookupTranslatorTest.testLang882()
Resolved declaration: org.apache.commons.lang3.text.translate.LookupTranslatorTest.testLang882()
Source: src/test/java/org/apache/commons/lang3/text/translate/LookupTranslatorTest.java

```java
43 |     @Test
44 |     public void testLang882() throws IOException {
45 |         final LookupTranslator lt = new LookupTranslator(new CharSequence[][] { { new StringBuffer("one"), new StringBuffer("two") } });
46 |         final StringWriter out = new StringWriter();
47 |         final int result = lt.translate(new StringBuffer("one"), 0, out);
48 |         assertEquals("Incorrect codepoint consumption", 3, result);
49 |         assertEquals("Incorrect value", "two", out.toString());
50 |     }
```
