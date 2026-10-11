# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineObjectLiteralsTest.testObject10()
Resolved declaration: com.google.javascript.jscomp.InlineObjectLiteralsTest.testObject10()
Source: test/com/google/javascript/jscomp/InlineObjectLiteralsTest.java

```java
167 |   public void testObject10() {
168 |     testLocal("var x; var b = f(); x = {a:a, b:b}; if(x.a) g(x.b);",
169 |          "var JSCompiler_object_inline_a_0;" +
170 |          "var JSCompiler_object_inline_b_1;" +
171 |          "var b = f();" +
172 |          "JSCompiler_object_inline_a_0=a,JSCompiler_object_inline_b_1=b,true;" +
173 |          "if(JSCompiler_object_inline_a_0) g(JSCompiler_object_inline_b_1)");
174 |     testLocal("var x = {}; var b = f(); x = {a:a, b:b}; if(x.a) g(x.b) + x.c",
175 |          "var x = {}; var b = f(); x = {a:a, b:b}; if(x.a) g(x.b) + x.c");
176 |     testLocal("var x; var b = f(); x = {a:a, b:b}; x.c = c; if(x.a) g(x.b) + x.c",
177 |          "var JSCompiler_object_inline_a_0;" +
178 |          "var JSCompiler_object_inline_b_1;" +
179 |          "var JSCompiler_object_inline_c_2;" +
180 |          "var b = f();" +
181 |          "JSCompiler_object_inline_a_0 = a,JSCompiler_object_inline_b_1 = b, " +
182 |          "  JSCompiler_object_inline_c_2=void 0,true;" +
183 |          "JSCompiler_object_inline_c_2 = c;" +
184 |          "if (JSCompiler_object_inline_a_0)" +
185 |          "  g(JSCompiler_object_inline_b_1) + JSCompiler_object_inline_c_2;");
186 |     testLocal("var x = {a:a}; if (b) x={b:b}; f(x.a||x.b);",
187 |          "var JSCompiler_object_inline_a_0 = a;" +
188 |          "var JSCompiler_object_inline_b_1;" +
189 |          "if(b) JSCompiler_object_inline_b_1 = b," +
190 |          "      JSCompiler_object_inline_a_0 = void 0," +
191 |          "      true;" +
192 |          "f(JSCompiler_object_inline_a_0 || JSCompiler_object_inline_b_1)");
193 |     testLocal("var x; var y = 5; x = {a:a, b:b, c:c}; if (b) x={b:b}; f(x.a||x.b);",
194 |          "var JSCompiler_object_inline_a_0;" +
195 |          "var JSCompiler_object_inline_b_1;" +
196 |          "var JSCompiler_object_inline_c_2;" +
197 |          "var y=5;" +
198 |          "JSCompiler_object_inline_a_0=a," +
199 |          "JSCompiler_object_inline_b_1=b," +
200 |          "JSCompiler_object_inline_c_2=c," +
201 |          "true;" +
202 |          "if (b) JSCompiler_object_inline_b_1=b," +
203 |          "       JSCompiler_object_inline_a_0=void 0," +
204 |          "       JSCompiler_object_inline_c_2=void 0," +
205 |          "       true;" +
206 |          "f(JSCompiler_object_inline_a_0||JSCompiler_object_inline_b_1)");
207 |   }
```

## com.google.javascript.jscomp.InlineObjectLiteralsTest.testObject12()
Resolved declaration: com.google.javascript.jscomp.InlineObjectLiteralsTest.testObject12()
Source: test/com/google/javascript/jscomp/InlineObjectLiteralsTest.java

```java
214 |   public void testObject12() {
215 |     testLocal("var a; a = {x:1, y:2}; f(a.x, a.y2);",
216 |         "var a; a = {x:1, y:2}; f(a.x, a.y2);");
217 |   }
```

## com.google.javascript.jscomp.InlineObjectLiteralsTest.testObject22()
Resolved declaration: com.google.javascript.jscomp.InlineObjectLiteralsTest.testObject22()
Source: test/com/google/javascript/jscomp/InlineObjectLiteralsTest.java

```java
279 |   public void testObject22() {
280 |     testLocal("while(1) { var a = {y:1}; if (b) a.x = 2; f(a.y, a.x);}",
281 |       "for(;1;){" +
282 |       " var JSCompiler_object_inline_y_0=1;" +
283 |       " var JSCompiler_object_inline_x_1;" +
284 |       " if(b) JSCompiler_object_inline_x_1=2;" +
285 |       " f(JSCompiler_object_inline_y_0,JSCompiler_object_inline_x_1)" +
286 |       "}");
287 | 
288 |     testLocal("var a; while (1) { f(a.x, a.y); a = {x:1, y:1};}",
289 |         "var a; while (1) { f(a.x, a.y); a = {x:1, y:1};}");
290 |   }
```

## com.google.javascript.jscomp.InlineObjectLiteralsTest.testIssue724()
Resolved declaration: com.google.javascript.jscomp.InlineObjectLiteralsTest.testIssue724()
Source: test/com/google/javascript/jscomp/InlineObjectLiteralsTest.java

```java
343 |   public void testIssue724() {
344 |     testSameLocal(
345 |         "var getType; getType = {};" +
346 |         "return functionToCheck && " +
347 |         "   getType.toString.apply(functionToCheck) === " +
348 |         "   '[object Function]';");
349 |   }
```

## com.google.javascript.jscomp.IntegrationTest.testIssue724()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIssue724()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
1672 |   public void testIssue724() {
1673 |     CompilerOptions options = createCompilerOptions();
1674 |     CompilationLevel.ADVANCED_OPTIMIZATIONS
1675 |         .setOptionsForCompilationLevel(options);
1676 |     String code =
1677 |         "isFunction = function(functionToCheck) {" +
1678 |         "  var getType = {};" +
1679 |         "  return functionToCheck && " +
1680 |         "      getType.toString.apply(functionToCheck) === " +
1681 |         "     '[object Function]';" +
1682 |         "};";
1683 |     String result =
1684 |         "isFunction=function(a){var b={};" +
1685 |         "return a&&\"[object Function]\"===b.b.a(a)}";
1686 | 
1687 |     test(options, code, result);
1688 |   }
```
