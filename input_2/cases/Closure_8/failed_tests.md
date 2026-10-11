# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CollapseVariableDeclarationsTest.testIssue820()
Resolved declaration: com.google.javascript.jscomp.CollapseVariableDeclarationsTest.testIssue820()
Source: test/com/google/javascript/jscomp/CollapseVariableDeclarationsTest.java

```java
45 |   public void testIssue820() throws Exception {
46 |     // Don't redeclare function parameters, this is incompatible with
47 |     // strict mode.
48 |     testSame("function f(a){ var b=1; a=2; var c; }");
49 |   }
```
