# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testIssue787()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIssue787()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
2217 |   public void testIssue787() {
2218 |     CompilerOptions options = createCompilerOptions();
2219 |     CompilationLevel level = CompilationLevel.SIMPLE_OPTIMIZATIONS;
2220 |     level.setOptionsForCompilationLevel(options);
2221 |     WarningLevel warnings = WarningLevel.DEFAULT;
2222 |     warnings.setOptionsForWarningLevel(options);
2223 | 
2224 |     String code = "" +
2225 |         "function some_function() {\n" +
2226 |         "  var fn1;\n" +
2227 |         "  var fn2;\n" +
2228 |         "\n" +
2229 |         "  if (any_expression) {\n" +
2230 |         "    fn2 = external_ref;\n" +
2231 |         "    fn1 = function (content) {\n" +
2232 |         "      return fn2();\n" +
2233 |         "    }\n" +
2234 |         "  }\n" +
2235 |         "\n" +
2236 |         "  return {\n" +
2237 |         "    method1: function () {\n" +
2238 |         "      if (fn1) fn1();\n" +
2239 |         "      return true;\n" +
2240 |         "    },\n" +
2241 |         "    method2: function () {\n" +
2242 |         "      return false;\n" +
2243 |         "    }\n" +
2244 |         "  }\n" +
2245 |         "}";
2246 | 
2247 |     String result = "" +
2248 |         "function some_function() {\n" +
2249 |         "  var a, b;\n" +
2250 |         "  any_expression && (b = external_ref, a = function() {\n" +
2251 |         "    return b()\n" +
2252 |         "  });\n" +
2253 |         "  return{method1:function() {\n" +
2254 |         "    a && a();\n" +
2255 |         "    return !0\n" +
2256 |         "  }, method2:function() {\n" +
2257 |         "    return !1\n" +
2258 |         "  }}\n" +
2259 |         "}\n" +
2260 |         "";
2261 | 
2262 |     test(options, code, result);
2263 |   }
```
