# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testProcessClosurePrimitives()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testProcessClosurePrimitives()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
154 |   public void testProcessClosurePrimitives() {
155 |     test("var goog = {}; goog.provide('goog.dom');",
156 |          "var goog = {}; goog.dom = {};");
157 |     args.add("--process_closure_primitives=false");
158 |     testSame("var goog = {}; goog.provide('goog.dom');");
159 |   }
```
