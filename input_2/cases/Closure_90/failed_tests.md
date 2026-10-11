# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testBackwardsTypedefUse8()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testBackwardsTypedefUse8()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
2667 |   public void testBackwardsTypedefUse8() throws Exception {
2668 |     // Tehnically, this isn't quite right, because the JS runtime
2669 |     // will coerce null -> the global object. But we'll punt on that for now.
2670 |     testTypes(
2671 |         "/** @param {!Array} x */ function g(x) {}" +
2672 |         "/** @this {goog.MyTypedef} */ function f() { g(this); }" +
2673 |         "var goog = {};" +
2674 |         "/** @typedef {(Array|null|undefined)} */ goog.MyTypedef;");
2675 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testBackwardsTypedefUse9()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testBackwardsTypedefUse9()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
2677 |   public void testBackwardsTypedefUse9() throws Exception {
2678 |     testTypes(
2679 |         "/** @param {!Array} x */ function g(x) {}" +
2680 |         "/** @this {goog.MyTypedef} */ function f() { g(this); }" +
2681 |         "var goog = {};" +
2682 |         "/** @typedef {(Error|null|undefined)} */ goog.MyTypedef;",
2683 |         "actual parameter 1 of g does not match formal parameter\n" +
2684 |         "found   : Error\n" +
2685 |         "required: Array");
2686 |   }
```
