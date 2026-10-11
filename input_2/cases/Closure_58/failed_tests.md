# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.LiveVariableAnalysisTest.testExpressionInForIn()
Resolved declaration: com.google.javascript.jscomp.LiveVariableAnalysisTest.testExpressionInForIn()
Source: test/com/google/javascript/jscomp/LiveVariableAnalysisTest.java

```java
209 |   public void testExpressionInForIn() {
210 |     assertLiveBeforeX("var a = [0]; X:for (a[1] in foo) { }", "a");
211 |   }
```
