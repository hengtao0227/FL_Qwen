# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ScopedAliasesTest.testHoistedFunctionDeclaration()
Resolved declaration: com.google.javascript.jscomp.ScopedAliasesTest.testHoistedFunctionDeclaration()
Source: test/com/google/javascript/jscomp/ScopedAliasesTest.java

```java
521 |   public void testHoistedFunctionDeclaration() {
522 |     testScoped(" g(f); function f() {} ",
523 |                SCOPE_NAMESPACE +
524 |                " $jscomp.scope.f = function () {}; " +
525 |                "g($jscomp.scope.f); ");
526 |   }
```

## com.google.javascript.jscomp.ScopedAliasesTest.testFunctionDeclaration()
Resolved declaration: com.google.javascript.jscomp.ScopedAliasesTest.testFunctionDeclaration()
Source: test/com/google/javascript/jscomp/ScopedAliasesTest.java

```java
514 |   public void testFunctionDeclaration() {
515 |     testScoped("if (x) { function f() {} } g(f)",
516 |                SCOPE_NAMESPACE +
517 |                "if (x) { $jscomp.scope.f = function () {}; } " +
518 |                "g($jscomp.scope.f); ");
519 |   }
```
