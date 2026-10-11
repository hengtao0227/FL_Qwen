# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ScopedAliasesTest.testNonAliasLocal()
Resolved declaration: com.google.javascript.jscomp.ScopedAliasesTest.testNonAliasLocal()
Source: test/com/google/javascript/jscomp/ScopedAliasesTest.java

```java
405 |   public void testNonAliasLocal() {
406 |     testScopedFailure("var x = 10", ScopedAliases.GOOG_SCOPE_NON_ALIAS_LOCAL);
407 |     testScopedFailure("var x = goog.dom + 10",
408 |         ScopedAliases.GOOG_SCOPE_NON_ALIAS_LOCAL);
409 |     testScopedFailure("var x = goog['dom']",
410 |         ScopedAliases.GOOG_SCOPE_NON_ALIAS_LOCAL);
411 |     testScopedFailure("var x = goog.dom, y = 10",
412 |         ScopedAliases.GOOG_SCOPE_NON_ALIAS_LOCAL);
413 |     testScopedFailure("function f() {}",
414 |         ScopedAliases.GOOG_SCOPE_NON_ALIAS_LOCAL);
415 |   }
```
