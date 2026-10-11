# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue688()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue688()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
5905 |   public void testIssue688() throws Exception {
5906 |     testTypes(
5907 |         "/** @const */ var SOME_DEFAULT =\n" +
5908 |         "    /** @type {TwoNumbers} */ ({first: 1, second: 2});\n" +
5909 |         "/**\n" +
5910 |         "* Class defining an interface with two numbers.\n" +
5911 |         "* @interface\n" +
5912 |         "*/\n" +
5913 |         "function TwoNumbers() {}\n" +
5914 |         "/** @type number */\n" +
5915 |         "TwoNumbers.prototype.first;\n" +
5916 |         "/** @type number */\n" +
5917 |         "TwoNumbers.prototype.second;\n" +
5918 |         "/** @return {number} */ function f() { return SOME_DEFAULT; }",
5919 |         "inconsistent return type\n" +
5920 |         "found   : (TwoNumbers|null)\n" +
5921 |         "required: number");
5922 |   }
```
