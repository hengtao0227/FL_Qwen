# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testSimpleModeLeavesUnusedParams()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testSimpleModeLeavesUnusedParams()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
154 |   public void testSimpleModeLeavesUnusedParams() {
155 |     args.add("--compilation_level=SIMPLE_OPTIMIZATIONS");
156 |     testSame("window.f = function(a) {};");
157 |   }
```

## com.google.javascript.jscomp.CommandLineRunnerTest.testForwardDeclareDroppedTypes()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testForwardDeclareDroppedTypes()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
750 |   public void testForwardDeclareDroppedTypes() {
751 |     args.add("--manage_closure_dependencies=true");
752 | 
753 |     args.add("--warning_level=VERBOSE");
754 |     test(new String[] {
755 |           "goog.require('beer');",
756 |           "goog.provide('beer'); /** @param {Scotch} x */ function f(x) {}",
757 |           "goog.provide('Scotch'); var x = 3;"
758 |          },
759 |          new String[] {
760 |            "var beer = {}; function f(a) {}",
761 |            ""
762 |          });
763 | 
764 |     test(new String[] {
765 |           "goog.require('beer');",
766 |           "goog.provide('beer'); /** @param {Scotch} x */ function f(x) {}"
767 |          },
768 |          new String[] {
769 |            "var beer = {}; function f(a) {}",
770 |            ""
771 |          },
772 |          RhinoErrorReporter.TYPE_PARSE_ERROR);
773 |   }
```

## com.google.javascript.jscomp.CommandLineRunnerTest.testDebugFlag1()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testDebugFlag1()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
473 |   public void testDebugFlag1() {
474 |     args.add("--compilation_level=SIMPLE_OPTIMIZATIONS");
475 |     args.add("--debug=false");
476 |     test("function foo(a) {}",
477 |          "function foo(a) {}");
478 |   }
```

## com.google.javascript.jscomp.IntegrationTest.testIssue787()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIssue787()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
2326 |   public void testIssue787() {
2327 |     CompilerOptions options = createCompilerOptions();
2328 |     CompilationLevel level = CompilationLevel.SIMPLE_OPTIMIZATIONS;
2329 |     level.setOptionsForCompilationLevel(options);
2330 |     WarningLevel warnings = WarningLevel.DEFAULT;
2331 |     warnings.setOptionsForWarningLevel(options);
2332 | 
2333 |     String code = "" +
2334 |         "function some_function() {\n" +
2335 |         "  var fn1;\n" +
2336 |         "  var fn2;\n" +
2337 |         "\n" +
2338 |         "  if (any_expression) {\n" +
2339 |         "    fn2 = external_ref;\n" +
2340 |         "    fn1 = function (content) {\n" +
2341 |         "      return fn2();\n" +
2342 |         "    }\n" +
2343 |         "  }\n" +
2344 |         "\n" +
2345 |         "  return {\n" +
2346 |         "    method1: function () {\n" +
2347 |         "      if (fn1) fn1();\n" +
2348 |         "      return true;\n" +
2349 |         "    },\n" +
2350 |         "    method2: function () {\n" +
2351 |         "      return false;\n" +
2352 |         "    }\n" +
2353 |         "  }\n" +
2354 |         "}";
2355 | 
2356 |     String result = "" +
2357 |         "function some_function() {\n" +
2358 |         "  var a, b;\n" +
2359 |         "  any_expression && (b = external_ref, a = function(a) {\n" +
2360 |         "    return b()\n" +
2361 |         "  });\n" +
2362 |         "  return{method1:function() {\n" +
2363 |         "    a && a();\n" +
2364 |         "    return !0\n" +
2365 |         "  }, method2:function() {\n" +
2366 |         "    return !1\n" +
2367 |         "  }}\n" +
2368 |         "}\n" +
2369 |         "";
2370 | 
2371 |     test(options, code, result);
2372 |   }
```

## com.google.javascript.jscomp.RemoveUnusedVarsTest.testRemoveGlobal1()
Resolved declaration: com.google.javascript.jscomp.RemoveUnusedVarsTest.testRemoveGlobal1()
Source: test/com/google/javascript/jscomp/RemoveUnusedVarsTest.java

```java
244 |   public void testRemoveGlobal1() {
245 |     removeGlobal = false;
246 |     testSame("var x=1");
247 |     test("var y=function(x){var z;}", "var y=function(x){}");
248 |   }
```

## com.google.javascript.jscomp.RemoveUnusedVarsTest.testRemoveGlobal2()
Resolved declaration: com.google.javascript.jscomp.RemoveUnusedVarsTest.testRemoveGlobal2()
Source: test/com/google/javascript/jscomp/RemoveUnusedVarsTest.java

```java
250 |   public void testRemoveGlobal2() {
251 |     removeGlobal = false;
252 |     testSame("var x=1");
253 |     test("function y(x){var z;}", "function y(x){}");
254 |   }
```

## com.google.javascript.jscomp.RemoveUnusedVarsTest.testRemoveGlobal3()
Resolved declaration: com.google.javascript.jscomp.RemoveUnusedVarsTest.testRemoveGlobal3()
Source: test/com/google/javascript/jscomp/RemoveUnusedVarsTest.java

```java
256 |   public void testRemoveGlobal3() {
257 |     removeGlobal = false;
258 |     testSame("var x=1");
259 |     test("function x(){function y(x){var z;}y()}",
260 |          "function x(){function y(x){}y()}");
261 |   }
```

## com.google.javascript.jscomp.RemoveUnusedVarsTest.testIssue168b()
Resolved declaration: com.google.javascript.jscomp.RemoveUnusedVarsTest.testIssue168b()
Source: test/com/google/javascript/jscomp/RemoveUnusedVarsTest.java

```java
281 |   public void testIssue168b() {
282 |     removeGlobal = false;
283 |     test("function a(){" +
284 |          "  (function(x){ b(); })(1);" +
285 |          "}" +
286 |          "function b(){" +
287 |          "  a();" +
288 |          "}",
289 |          "function a(){(function(x){b()})(1)}" +
290 |          "function b(){a()}");
291 |   }
```
