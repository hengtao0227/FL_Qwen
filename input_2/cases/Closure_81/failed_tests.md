# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.parsing.ParserTest.testUnnamedFunctionStatement()
Resolved declaration: com.google.javascript.jscomp.parsing.ParserTest.testUnnamedFunctionStatement()
Source: test/com/google/javascript/jscomp/parsing/ParserTest.java

```java
774 |   public void testUnnamedFunctionStatement() {
775 |     // Statements
776 |     parseError("function() {};", "unnamed function statement");
777 |     parseError("if (true) { function() {}; }", "unnamed function statement");
778 |     parse("function f() {};");
779 |     // Expressions
780 |     parse("(function f() {});");
781 |     parse("(function () {});");
782 |   }
```
