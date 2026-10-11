# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testIssue477()
Resolved declaration: com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testIssue477()
Source: test/com/google/javascript/jscomp/parsing/JsDocInfoParserTest.java

```java
508 |   public void testIssue477() throws Exception {
509 |     parse("@type function */",
510 |         "Bad type annotation. missing opening (");
511 |   }
```
