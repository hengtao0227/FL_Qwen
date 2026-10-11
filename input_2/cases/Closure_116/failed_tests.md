# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FunctionInjectorTest.testIssue1101a()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testIssue1101a()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
1346 |   public void testIssue1101a() {
1347 |     helperCanInlineReferenceToFunction(CanInlineResult.NO,
1348 |         "function foo(a){return modifiyX() + a;} foo(x);", "foo",
1349 |         INLINE_DIRECT);
1350 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testIssue1101b()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testIssue1101b()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
1352 |   public void testIssue1101b() {
1353 |     helperCanInlineReferenceToFunction(CanInlineResult.NO,
1354 |         "function foo(a){return (x.prop = 2),a;} foo(x.prop);", "foo",
1355 |         INLINE_DIRECT);
1356 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testBug4944818()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testBug4944818()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2062 |   public void testBug4944818() {
2063 |     test(
2064 |         "var getDomServices_ = function(self) {\n" +
2065 |         "  if (!self.domServices_) {\n" +
2066 |         "    self.domServices_ = goog$component$DomServices.get(" +
2067 |         "        self.appContext_);\n" +
2068 |         "  }\n" +
2069 |         "\n" +
2070 |         "  return self.domServices_;\n" +
2071 |         "};\n" +
2072 |         "\n" +
2073 |         "var getOwnerWin_ = function(self) {\n" +
2074 |         "  return getDomServices_(self).getDomHelper().getWindow();\n" +
2075 |         "};\n" +
2076 |         "\n" +
2077 |         "HangoutStarter.prototype.launchHangout = function() {\n" +
2078 |         "  var self = a.b;\n" +
2079 |         "  var myUrl = new goog.Uri(getOwnerWin_(self).location.href);\n" +
2080 |         "};",
2081 |         "HangoutStarter.prototype.launchHangout=function(){" +
2082 |         "  var self$$2=a.b;" +
2083 |         "  var JSCompiler_temp_const$$0=goog.Uri;" +
2084 |         "  var JSCompiler_inline_result$$1;" +
2085 |         "  {" +
2086 |         "    var JSCompiler_inline_result$$0;" +
2087 |         "    {" +
2088 |         "      var self$$inline_1=self$$2;" +
2089 |         "      if(!self$$inline_1.domServices_) {" +
2090 |         "        self$$inline_1.domServices_=goog$component$DomServices.get(self$$inline_1.appContext_);" +
2091 |         "      }" +
2092 |         "      JSCompiler_inline_result$$0=self$$inline_1.domServices_;" +
2093 |         "    }" +
2094 |         "    JSCompiler_inline_result$$1=JSCompiler_inline_result$$0.getDomHelper().getWindow();" +
2095 |         "  }" +
2096 |         "  var myUrl=new JSCompiler_temp_const$$0(JSCompiler_inline_result$$1.location.href)" +
2097 |         "}");
2098 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testDoubleInlining2()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testDoubleInlining2()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1108 |   public void testDoubleInlining2() {
1109 |     test("var foo = function(a) { return getWindow(a); };" +
1110 |          "var bar = function(b) { return b; };" +
1111 |          "foo(bar(x));",
1112 |          "{getWindow(x)}");
1113 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testIssue1101()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testIssue1101()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2370 |   public void testIssue1101() {
2371 |     test(
2372 |         "var x = (function (saved) {" +
2373 |         "    return foo(obj) + saved;" +
2374 |         "  })(obj[\"prop\"]);",
2375 |         "var x;" +
2376 |         "{" +
2377 |         "  var saved$$inline_0=obj[\"prop\"];x=foo(obj)+saved$$inline_0" +
2378 |         "}");
2379 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineIfParametersModified8()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineIfParametersModified8()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
599 |   public void testInlineIfParametersModified8() {
600 |     // OK, object parameter modified.
601 |     test("function f(a){return a.x=2}f(o)", "{o.x=2}");
602 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineIfParametersModified9()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineIfParametersModified9()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
604 |   public void testInlineIfParametersModified9() {
605 |     // OK, array parameter modified.
606 |     test("function f(a){return a[2]=2}f(o)", "{o[2]=2}");
607 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions6()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions6()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
155 |   public void testInlineFunctions6() {
156 |     // more complex inlines
157 |     test("function BAR_FN(x, y, z) { return z(nochg(x + y)) }" +
158 |          "alert(BAR_FN(1, 2, baz))",
159 | 
160 |          "var JSCompiler_temp_const$$0=alert;" +
161 |          "var JSCompiler_inline_result$$1;" +
162 |          "{JSCompiler_inline_result$$1=baz(nochg(1+2));}" +
163 |          "JSCompiler_temp_const$$0(JSCompiler_inline_result$$1)");
164 |   }
```
