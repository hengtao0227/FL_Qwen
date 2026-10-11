# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineVariablesTest.testExternalIssue1053()
Resolved declaration: com.google.javascript.jscomp.InlineVariablesTest.testExternalIssue1053()
Source: test/com/google/javascript/jscomp/InlineVariablesTest.java

```java
1068 |   public void testExternalIssue1053() {
1069 |     testSame(
1070 |         "var u; function f() { u = Random(); var x = u; f(); alert(x===u)}");
1071 |   }
```
