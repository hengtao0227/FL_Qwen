# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.text.StrBuilderTest.testIndexOfLang294()
Resolved declaration: org.apache.commons.lang.text.StrBuilderTest.testIndexOfLang294()
Source: src/test/org/apache/commons/lang/text/StrBuilderTest.java

```java
1738 |     public void testIndexOfLang294() {
1739 |         StrBuilder sb = new StrBuilder("onetwothree");
1740 |         sb.deleteFirst("three");
1741 |         assertEquals(-1, sb.indexOf("three"));
1742 |     }
```

## org.apache.commons.lang.text.StrBuilderTest.testLang294()
Resolved declaration: org.apache.commons.lang.text.StrBuilderTest.testLang294()
Source: src/test/org/apache/commons/lang/text/StrBuilderTest.java

```java
1732 |     public void testLang294() {
1733 |         StrBuilder sb = new StrBuilder("\n%BLAH%\nDo more stuff\neven more stuff\n%BLAH%\n");
1734 |         sb.deleteAll("\n%BLAH%");
1735 |         assertEquals("\nDo more stuff\neven more stuff\n", sb.toString()); 
1736 |     }
```
