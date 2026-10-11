# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineVariablesTest.testNoInlineAliasesInLoop()
Resolved declaration: com.google.javascript.jscomp.InlineVariablesTest.testNoInlineAliasesInLoop()
Source: test/com/google/javascript/jscomp/InlineVariablesTest.java

```java
616 |   public void testNoInlineAliasesInLoop() {
617 |     testSame(
618 |         "function f() { " +
619 |         "  for (var i = 0; i < 5; i++) {" +
620 |         "    var x = extern();" +
621 |         "    (function() {" +
622 |         "       var y = x; window.setTimeout(function() { extern(y); }, 0);" +
623 |         "     })();" +
624 |         "  }" +
625 |         "}");
626 |   }
```
