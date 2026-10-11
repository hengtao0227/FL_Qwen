# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testTextExtents()
Resolved declaration: com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testTextExtents()
Source: test/com/google/javascript/jscomp/parsing/JsDocInfoParserTest.java

```java
2755 |   public void testTextExtents() {
2756 |     parse("@return {@code foo} bar \n *    baz. */",
2757 |         true, "Bad type annotation. type not recognized due to syntax error");
2758 |   }
```
