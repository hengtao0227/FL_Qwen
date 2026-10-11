# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.LooseTypeCheckTest.testMethodInference6()
Resolved declaration: com.google.javascript.jscomp.LooseTypeCheckTest.testMethodInference6()
Source: test/com/google/javascript/jscomp/LooseTypeCheckTest.java

```java
1771 |   public void testMethodInference6() throws Exception {
1772 |     testTypes(
1773 |         "/** @constructor */ function F() {}" +
1774 |         "/** @param {number} x */ F.prototype.foo = function(x) { };" +
1775 |         "/** @constructor \n * @extends {F} */ " +
1776 |         "function G() {}" +
1777 |         "/** @override */ G.prototype.foo = function() { };" +
1778 |         "(new G()).foo(1);");
1779 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testIssue368()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue368()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
5325 |   public void testIssue368() throws Exception {
5326 |     testTypes(
5327 |         "/** @constructor */ function Foo(){}" +
5328 |         "/**\n" +
5329 |         " * @param {number} one\n" +
5330 |         " * @param {string} two\n" +
5331 |         " */\n" +
5332 |         "Foo.prototype.add = function(one, two) {};" +
5333 |         "/**\n" +
5334 |         " * @constructor\n" +
5335 |         " * @extends {Foo}\n" +
5336 |         " */\n" +
5337 |         "function Bar(){}" +
5338 |         "/** @override */\n" +
5339 |         "Bar.prototype.add = function(ignored) {};" +
5340 |         "(new Bar()).add(1, 2);",
5341 |         "actual parameter 2 of Bar.prototype.add does not match formal parameter\n" +
5342 |         "found   : number\n" +
5343 |         "required: string");
5344 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testMethodInference6()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testMethodInference6()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
2026 |   public void testMethodInference6() throws Exception {
2027 |     testTypes(
2028 |         "/** @constructor */ function F() {}" +
2029 |         "/** @param {number} x */ F.prototype.foo = function(x) { };" +
2030 |         "/** @constructor \n * @extends {F} */ " +
2031 |         "function G() {}" +
2032 |         "/** @override */ G.prototype.foo = function() { };" +
2033 |         "(new G()).foo(1);");
2034 |   }
```
