# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineFunctionsTest.testBug4944818()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testBug4944818()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2059 |   public void testBug4944818() {
2060 |     test(
2061 |         "var getDomServices_ = function(self) {\n" +
2062 |         "  if (!self.domServices_) {\n" +
2063 |         "    self.domServices_ = goog$component$DomServices.get(" +
2064 |         "        self.appContext_);\n" +
2065 |         "  }\n" +
2066 |         "\n" +
2067 |         "  return self.domServices_;\n" +
2068 |         "};\n" +
2069 |         "\n" +
2070 |         "var getOwnerWin_ = function(self) {\n" +
2071 |         "  return getDomServices_(self).getDomHelper().getWindow();\n" +
2072 |         "};\n" +
2073 |         "\n" +
2074 |         "HangoutStarter.prototype.launchHangout = function() {\n" +
2075 |         "  var self = a.b;\n" +
2076 |         "  var myUrl = new goog.Uri(getOwnerWin_(self).location.href);\n" +
2077 |         "};",
2078 |         "HangoutStarter.prototype.launchHangout = function() { " +
2079 |         "  var self$$2 = a.b;" +
2080 |         "  var JSCompiler_temp_const$$0 = goog.Uri;" +
2081 |         "  var JSCompiler_inline_result$$1;" +
2082 |         "  {" +
2083 |         "  var self$$inline_2 = self$$2;" +
2084 |         "  if (!self$$inline_2.domServices_) {" +
2085 |         "    self$$inline_2.domServices_ = goog$component$DomServices.get(" +
2086 |         "        self$$inline_2.appContext_);" +
2087 |         "  }" +
2088 |         "  JSCompiler_inline_result$$1=self$$inline_2.domServices_;" +
2089 |         "  }" +
2090 |         "  var myUrl = new JSCompiler_temp_const$$0(" +
2091 |         "      JSCompiler_inline_result$$1.getDomHelper()." +
2092 |         "          getWindow().location.href)" +
2093 |         "}");
2094 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testDoubleInlining1()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testDoubleInlining1()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1097 |   public void testDoubleInlining1() {
1098 |     allowBlockInlining = false;
1099 |     test("var foo = function(a) { return getWindow(a); };" +
1100 |          "var bar = function(b) { return b; };" +
1101 |          "foo(bar(x));",
1102 |          "getWindow(x)");
1103 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified8()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified8()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
596 |   public void testNoInlineIfParametersModified8() {
597 |     // OK, object parameter modified.
598 |     test("function f(a){return a.x=2}f(o)", "o.x=2");
599 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified9()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified9()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
601 |   public void testNoInlineIfParametersModified9() {
602 |     // OK, array parameter modified.
603 |     test("function f(a){return a[2]=2}f(o)", "o[2]=2");
604 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions6()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions6()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
150 |   public void testInlineFunctions6() {
151 |     // more complex inlines
152 |     test("function BAR_FN(x, y, z) { return z(foo(x + y)) }" +
153 |          "alert(BAR_FN(1, 2, baz))",
154 | 
155 |          "alert(baz(foo(1+2)))");
156 |   }
```
