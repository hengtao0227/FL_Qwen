# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testIssue582()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testIssue582()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1272 |   public void testIssue582() {
1273 |     assertPrint("var x = -0.0;", "var x=-0.0");
1274 |   }
```
