# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.text.ExtendedMessageFormatTest.testEscapedQuote_LANG_477()
Resolved declaration: org.apache.commons.lang.text.ExtendedMessageFormatTest.testEscapedQuote_LANG_477()
Source: src/test/org/apache/commons/lang/text/ExtendedMessageFormatTest.java

```java
98 |     public void testEscapedQuote_LANG_477() {
99 |         String pattern = "it''s a {0,lower} 'test'!";
100 |         ExtendedMessageFormat emf = new ExtendedMessageFormat(pattern, registry);
101 |         assertEquals("it's a dummy test!", emf.format(new Object[] {"DUMMY"}));
102 |     }
```
