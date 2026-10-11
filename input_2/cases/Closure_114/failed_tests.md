# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.NameAnalyzerTest.testAssignWithCall()
Resolved declaration: com.google.javascript.jscomp.NameAnalyzerTest.testAssignWithCall()
Source: test/com/google/javascript/jscomp/NameAnalyzerTest.java

```java
1235 |   public void testAssignWithCall() {
1236 |     test("var fun, x; (fun = function(){ x; })();",
1237 |         "var x; (function(){ x; })();");
1238 |   }
```
