# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testIssue620()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testIssue620()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1282 |   public void testIssue620() {
1283 |     assertPrint("alert(/ / / / /);", "alert(/ // / /)");
1284 |     assertPrint("alert(/ // / /);", "alert(/ // / /)");
1285 |   }
```
