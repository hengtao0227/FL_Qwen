# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue1058()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue1058()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
12159 |   public void testIssue1058() throws Exception {
12160 |     testTypes(
12161 |         "/**\n" +
12162 |         "  * @constructor\n" +
12163 |         "  * @template CLASS\n" +
12164 |         "  */\n" +
12165 |         "var Class = function() {};\n" +
12166 |         "\n" +
12167 |         "/**\n" +
12168 |         "  * @param {function(CLASS):CLASS} a\n" +
12169 |         "  * @template T\n" +
12170 |         "  */\n" +
12171 |         "Class.prototype.foo = function(a) {\n" +
12172 |         "  return 'string';\n" +
12173 |         "};\n" +
12174 |         "\n" +
12175 |         "/** @param {number} a\n" +
12176 |         "  * @return {string} */\n" +
12177 |         "var a = function(a) { return '' };\n" +
12178 |         "\n" +
12179 |         "new Class().foo(a);");
12180 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testTemplatized11()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testTemplatized11()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
12140 |   public void testTemplatized11() throws Exception {
12141 |     testTypes(
12142 |         "/** \n" +
12143 |         " * @template T\n" +
12144 |         " * @constructor\n" +
12145 |         " */\n" +
12146 |         "function C() {}\n" +
12147 |         "\n" +
12148 |         "/**\n" +
12149 |         " * @param {T|K} a\n" +
12150 |         " * @return {T}\n" +
12151 |         " * @template K\n" +
12152 |         " */\n" +
12153 |         "C.prototype.method = function (a) {};\n" +
12154 |         "\n" +
12155 |         // method returns "?"
12156 |         "/** @type {void} */ var x = new C().method(1);");
12157 |   }
```
