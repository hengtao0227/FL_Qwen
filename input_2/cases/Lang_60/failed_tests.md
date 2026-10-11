# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.text.StrBuilderTest.testLang295()
Resolved declaration: org.apache.commons.lang.text.StrBuilderTest.testLang295()
Source: src/test/org/apache/commons/lang/text/StrBuilderTest.java

```java
1745 |     public void testLang295() {
1746 |         StrBuilder sb = new StrBuilder("onetwothree");
1747 |         sb.deleteFirst("three");
1748 |         assertFalse( "The contains(char) method is looking beyond the end of the string", sb.contains('h'));
1749 |         assertEquals( "The indexOf(char) method is looking beyond the end of the string", -1, sb.indexOf('h'));
1750 |     }
```
