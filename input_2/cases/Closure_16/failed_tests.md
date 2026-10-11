# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testIssue772()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIssue772()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
1864 |   public void testIssue772() throws Exception {
1865 |     CompilerOptions options = createCompilerOptions();
1866 |     options.closurePass = true;
1867 |     options.checkTypes = true;
1868 |     test(
1869 |         options,
1870 |         "/** @const */ var a = {};" +
1871 |         "/** @const */ a.b = {};" +
1872 |         "/** @const */ a.b.c = {};" +
1873 |         "goog.scope(function() {" +
1874 |         "  var b = a.b;" +
1875 |         "  var c = b.c;" +
1876 |         "  /** @typedef {string} */" +
1877 |         "  c.MyType;" +
1878 |         "  /** @param {c.MyType} x The variable. */" +
1879 |         "  c.myFunc = function(x) {};" +
1880 |         "});",
1881 |         "/** @const */ var a = {};" +
1882 |         "/** @const */ a.b = {};" +
1883 |         "/** @const */ a.b.c = {};" +
1884 |         "a.b.c.MyType;" +
1885 |         "a.b.c.myFunc = function(x) {};");
1886 |   }
```

## com.google.javascript.jscomp.ScopedAliasesTest.testIssue772()
Resolved declaration: com.google.javascript.jscomp.ScopedAliasesTest.testIssue772()
Source: test/com/google/javascript/jscomp/ScopedAliasesTest.java

```java
406 |   public void testIssue772() {
407 |     testTypes(
408 |         "var b = a.b;" +
409 |         "var c = b.c;",
410 |         "/** @param {c.MyType} x */ types.actual;" +
411 |         "/** @param {a.b.c.MyType} x */ types.expected;");
412 |   }
```
