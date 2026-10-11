# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testIssue504()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testIssue504()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
363 |   public void testIssue504() {
364 |     args.add("--compilation_level=ADVANCED_OPTIMIZATIONS");
365 |     test("void function() { alert('hi'); }();",
366 |          "alert('hi');", CheckSideEffects.USELESS_CODE_ERROR);
367 |   }
```

## com.google.javascript.jscomp.NodeUtilTest.testGetBooleanValue()
Resolved declaration: com.google.javascript.jscomp.NodeUtilTest.testGetBooleanValue()
Source: test/com/google/javascript/jscomp/NodeUtilTest.java

```java
91 |   public void testGetBooleanValue() {
92 |     assertPureBooleanTrue("true");
93 |     assertPureBooleanTrue("10");
94 |     assertPureBooleanTrue("'0'");
95 |     assertPureBooleanTrue("/a/");
96 |     assertPureBooleanTrue("{}");
97 |     assertPureBooleanTrue("[]");
98 |     assertPureBooleanFalse("false");
99 |     assertPureBooleanFalse("null");
100 |     assertPureBooleanFalse("0");
101 |     assertPureBooleanFalse("''");
102 |     assertPureBooleanFalse("undefined");
103 |     assertPureBooleanFalse("void 0");
104 |     assertPureBooleanUnknown("void foo()");
105 |     assertPureBooleanUnknown("b");
106 |     assertPureBooleanUnknown("-'0.0'");
107 | 
108 |     // Known but getBooleanValue return false for expressions with side-effects
109 |     assertPureBooleanUnknown("{a:foo()}");
110 |     assertPureBooleanUnknown("[foo()]");
111 |   }
```
