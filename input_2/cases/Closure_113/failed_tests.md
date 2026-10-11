# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.VarCheckTest.testNoUndeclaredVarWhenUsingClosurePass()
Resolved declaration: com.google.javascript.jscomp.VarCheckTest.testNoUndeclaredVarWhenUsingClosurePass()
Source: test/com/google/javascript/jscomp/VarCheckTest.java

```java
368 |   public void testNoUndeclaredVarWhenUsingClosurePass() {
369 |     enableClosurePass();
370 |     // We don't want to get goog as an undeclared var here.
371 |     test("goog.require('namespace.Class1');\n", null,
372 |         ProcessClosurePrimitives.MISSING_PROVIDE_ERROR);
373 |   }
```
