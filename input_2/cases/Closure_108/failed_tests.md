# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ScopedAliasesTest.testIssue1144()
Resolved declaration: com.google.javascript.jscomp.ScopedAliasesTest.testIssue1144()
Source: test/com/google/javascript/jscomp/ScopedAliasesTest.java

```java
569 |   public void testIssue1144() {
570 |     test("var ns = {};" +
571 |          "ns.sub = {};" +
572 |          "/** @constructor */ ns.sub.C = function () {};" +
573 |          "goog.scope(function () {" +
574 |          "  var sub = ns.sub;" +
575 |          "  /** @type {sub.C} */" +
576 |          "  var x = null;" +
577 |          "});",
578 |          SCOPE_NAMESPACE +
579 |          "var ns = {};" +
580 |          "ns.sub = {};" +
581 |          "/** @constructor */ ns.sub.C = function () {};" +
582 |          "$jscomp.scope.x = null;");
583 |   }
```
