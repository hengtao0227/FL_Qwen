# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeSubstituteAlternateSyntaxTest.testSimpleFunctionCall()
Resolved declaration: com.google.javascript.jscomp.PeepholeSubstituteAlternateSyntaxTest.testSimpleFunctionCall()
Source: test/com/google/javascript/jscomp/PeepholeSubstituteAlternateSyntaxTest.java

```java
1028 |   public void testSimpleFunctionCall() {
1029 |     test("var a = String(23)", "var a = '' + 23");
1030 |     test("var a = String('hello')", "var a = '' + 'hello'");
1031 |     testSame("var a = String('hello', bar());");
1032 |     testSame("var a = String({valueOf: function() { return 1; }});");
1033 |   }
```
