# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions31()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions31()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
386 |   public void testInlineFunctions31() {
387 |     // Don't introduce a duplicate label in the same scope
388 |     test("function foo(){ lab:{4;} }" +
389 |         "lab:{foo();}",
390 |         "lab:{{JSCompiler_inline_label_0:{4}}}");
391 |   }
```
