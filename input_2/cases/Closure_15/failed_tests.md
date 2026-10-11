# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testSimpleForIn()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testSimpleForIn()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
64 |   public void testSimpleForIn() {
65 |     inline("var a,b,x = a in b; x",
66 |            "var a,b,x; a in b");
67 |     noInline("var a, b; var x = a in b; print(1); x");
68 |     noInline("var a,b,x = a in b; delete a[b]; x");
69 |   }
```
