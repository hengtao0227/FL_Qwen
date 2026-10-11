# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.LooseTypeCheckTest.testDuplicateLocalVarDecl()
Resolved declaration: com.google.javascript.jscomp.LooseTypeCheckTest.testDuplicateLocalVarDecl()
Source: test/com/google/javascript/jscomp/LooseTypeCheckTest.java

```java
1969 |   public void testDuplicateLocalVarDecl() throws Exception {
1970 |     testClosureTypesMultipleWarnings(
1971 |         "/** @param {number} x */\n" +
1972 |         "function f(x) { /** @type {string} */ var x = ''; }",
1973 |         Lists.newArrayList(
1974 |             "variable x redefined with type string, original definition" +
1975 |             " at  [testcode] :2 with type number",
1976 |             "initializing variable\n" +
1977 |             "found   : string\n" +
1978 |             "required: number"));
1979 |   }
```

## com.google.javascript.jscomp.LooseTypeCheckTest.testFunctionArguments13()
Resolved declaration: com.google.javascript.jscomp.LooseTypeCheckTest.testFunctionArguments13()
Source: test/com/google/javascript/jscomp/LooseTypeCheckTest.java

```java
1344 |   public void testFunctionArguments13() throws Exception {
1345 |     // verifying that the argument type have non-inferrable types
1346 |     testTypes(
1347 |         "/** @return {boolean} */ function u() { return true; }" +
1348 |         "/** @param {boolean} b\n@return {?boolean} */" +
1349 |         "function f(b) { if (u()) { b = null; } return b; }",
1350 |         "assignment\n" +
1351 |         "found   : null\n" +
1352 |         "required: boolean");
1353 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testScoping12()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testScoping12()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
1420 |   public void testScoping12() throws Exception {
1421 |     testTypes(
1422 |         "/** @constructor */ function F() {}" +
1423 |         "/** @type {number} */ F.prototype.bar = 3;" +
1424 |         "/** @param {!F} f */ function g(f) {" +
1425 |         "  /** @return {string} */" +
1426 |         "  function h() {" +
1427 |         "    return f.bar;" +
1428 |         "  }" +
1429 |         "}",
1430 |         "inconsistent return type\n" +
1431 |         "found   : number\n" +
1432 |         "required: string");
1433 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testDuplicateLocalVarDecl()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testDuplicateLocalVarDecl()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
2146 |   public void testDuplicateLocalVarDecl() throws Exception {
2147 |     testClosureTypesMultipleWarnings(
2148 |         "/** @param {number} x */\n" +
2149 |         "function f(x) { /** @type {string} */ var x = ''; }",
2150 |         Lists.newArrayList(
2151 |             "variable x redefined with type string, original definition" +
2152 |             " at  [testcode] :2 with type number",
2153 |             "initializing variable\n" +
2154 |             "found   : string\n" +
2155 |             "required: number"));
2156 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testFunctionArguments13()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testFunctionArguments13()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
1512 |   public void testFunctionArguments13() throws Exception {
1513 |     // verifying that the argument type have non-inferrable types
1514 |     testTypes(
1515 |         "/** @return {boolean} */ function u() { return true; }" +
1516 |         "/** @param {boolean} b\n@return {?boolean} */" +
1517 |         "function f(b) { if (u()) { b = null; } return b; }",
1518 |         "assignment\n" +
1519 |         "found   : null\n" +
1520 |         "required: boolean");
1521 |   }
```
