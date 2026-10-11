# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testInlineAcrossSideEffect1()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testInlineAcrossSideEffect1()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
324 |   public void testInlineAcrossSideEffect1() {
325 |     // This can't be inlined because print() has side-effects and might change
326 |     // the definition of noSFX.
327 |     //
328 |     // noSFX must be both const and pure in order to inline it.
329 |     noInline("var y; var x = noSFX(y); print(x)");
330 |     //inline("var y; var x = noSFX(y); print(x)", "var y;var x;print(noSFX(y))");
331 |   }
```

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testCanInlineAcrossNoSideEffect()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testCanInlineAcrossNoSideEffect()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
359 |   public void testCanInlineAcrossNoSideEffect() {
360 |     // This can't be inlined because print() has side-effects and might change
361 |     // the definition of noSFX. We should be able to mark noSFX as const
362 |     // in some way.
363 |     noInline(
364 |         "var y; var x = noSFX(y), z = noSFX(); noSFX(); noSFX(), print(x)");
365 |     //inline(
366 |     //    "var y; var x = noSFX(y), z = noSFX(); noSFX(); noSFX(), print(x)",
367 |     //    "var y; var x, z = noSFX(); noSFX(); noSFX(), print(noSFX(y))");
368 |   }
```

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testIssue698()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testIssue698()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
419 |   public void testIssue698() {
420 |     // Most of the flow algorithms operate on Vars. We want to make
421 |     // sure the algorithm bails out appropriately if it sees
422 |     // a var that it doesn't know about.
423 |     inline(
424 |         "var x = ''; "
425 |         + "unknown.length < 2 && (unknown='0' + unknown);"
426 |         + "x = x + unknown; "
427 |         + "unknown.length < 3 && (unknown='0' + unknown);"
428 |         + "x = x + unknown; "
429 |         + "return x;",
430 |         "var x; "
431 |         + "unknown.length < 2 && (unknown='0' + unknown);"
432 |         + "x = '' + unknown; "
433 |         + "unknown.length < 3 && (unknown='0' + unknown);"
434 |         + "x = x + unknown; "
435 |         + "return x;");
436 |   }
```
