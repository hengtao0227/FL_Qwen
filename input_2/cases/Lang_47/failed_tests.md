# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.text.StrBuilderTest.testLang412Left()
Resolved declaration: org.apache.commons.lang.text.StrBuilderTest.testLang412Left()
Source: src/test/org/apache/commons/lang/text/StrBuilderTest.java

```java
1759 |     public void testLang412Left() {
1760 |         StrBuilder sb = new StrBuilder();
1761 |         sb.appendFixedWidthPadLeft(null, 10, '*');
1762 |         assertEquals( "Failed to invoke appendFixedWidthPadLeft correctly", "**********", sb.toString());
1763 |     }
```

## org.apache.commons.lang.text.StrBuilderTest.testLang412Right()
Resolved declaration: org.apache.commons.lang.text.StrBuilderTest.testLang412Right()
Source: src/test/org/apache/commons/lang/text/StrBuilderTest.java

```java
1753 |     public void testLang412Right() {
1754 |         StrBuilder sb = new StrBuilder();
1755 |         sb.appendFixedWidthPadRight(null, 10, '*');
1756 |         assertEquals( "Failed to invoke appendFixedWidthPadRight correctly", "**********", sb.toString());
1757 |     }
```
