# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testIssue794b()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testIssue794b()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
512 |   public void testIssue794b() {
513 |     noInline(
514 |         "var x = 1; " +
515 |         "try { x = x + someFunction(); } catch (e) {}" +
516 |         "x = x + 1;" +
517 |         "try { x = x + someFunction(); } catch (e) {}" +
518 |         "return x;");
519 |   }
```
