# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.LooseTypeCheckTest.testTypeRedefinition()
Resolved declaration: com.google.javascript.jscomp.LooseTypeCheckTest.testTypeRedefinition()
Source: test/com/google/javascript/jscomp/LooseTypeCheckTest.java

```java
2120 |   public void testTypeRedefinition() throws Exception {
2121 |     testClosureTypesMultipleWarnings(
2122 |         "a={};/**@enum {string}*/ a.A = {ZOR:'b'};"
2123 |         + "/** @constructor */ a.A = function() {}",
2124 |         Lists.newArrayList(
2125 |             "variable a.A redefined with type function (new:a.A): undefined, " +
2126 |             "original definition at [testcode]:1 with type enum{a.A}",
2127 |             "assignment to property A of a\n" +
2128 |             "found   : function (new:a.A): undefined\n" +
2129 |             "required: enum{a.A}"));
2130 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testIssue635b()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue635b()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
6341 |   public void testIssue635b() throws Exception {
6342 |     testTypes(
6343 |         "/** @constructor */" +
6344 |         "function F() {}" +
6345 |         "/** @constructor */" +
6346 |         "function G() {}" +
6347 |         "/** @type {function(new:G)} */ var x = F;",
6348 |         "initializing variable\n" +
6349 |         "found   : function (new:F): undefined\n" +
6350 |         "required: function (new:G): ?");
6351 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testTypeRedefinition()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testTypeRedefinition()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
2515 |   public void testTypeRedefinition() throws Exception {
2516 |     testClosureTypesMultipleWarnings("a={};/**@enum {string}*/ a.A = {ZOR:'b'};"
2517 |         + "/** @constructor */ a.A = function() {}",
2518 |         Lists.newArrayList(
2519 |             "variable a.A redefined with type function (new:a.A): undefined, " +
2520 |             "original definition at [testcode]:1 with type enum{a.A}",
2521 |             "assignment to property A of a\n" +
2522 |             "found   : function (new:a.A): undefined\n" +
2523 |             "required: enum{a.A}"));
2524 |   }
```
