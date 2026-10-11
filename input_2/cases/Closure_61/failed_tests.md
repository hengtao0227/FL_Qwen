# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeRemoveDeadCodeTest.testCall1()
Resolved declaration: com.google.javascript.jscomp.PeepholeRemoveDeadCodeTest.testCall1()
Source: test/com/google/javascript/jscomp/PeepholeRemoveDeadCodeTest.java

```java
543 |   public void testCall1() {
544 |     test("Math.sin(0);", "");
545 |   }
```

## com.google.javascript.jscomp.PeepholeRemoveDeadCodeTest.testCall2()
Resolved declaration: com.google.javascript.jscomp.PeepholeRemoveDeadCodeTest.testCall2()
Source: test/com/google/javascript/jscomp/PeepholeRemoveDeadCodeTest.java

```java
547 |   public void testCall2() {
548 |     test("1 + Math.sin(0);", "");
549 |   }
```

## com.google.javascript.jscomp.PeepholeRemoveDeadCodeTest.testRemoveUselessOps()
Resolved declaration: com.google.javascript.jscomp.PeepholeRemoveDeadCodeTest.testRemoveUselessOps()
Source: test/com/google/javascript/jscomp/PeepholeRemoveDeadCodeTest.java

```java
222 |   public void testRemoveUselessOps() {
223 |     // There are four place where expression results are discarded:
224 |     //  - a top level expression EXPR_RESULT
225 |     //  - the LHS of a COMMA
226 |     //  - the FOR init expression
227 |     //  - the FOR increment expression
228 | 
229 | 
230 |     // Known side-effect free functions calls are removed.
231 |     fold("Math.random()", "");
232 |     fold("Math.random(f() + g())", "f(),g();");
233 |     fold("Math.random(f(),g(),h())", "f(),g(),h();");
234 | 
235 |     // Calls to functions with unknown side-effects are are left.
236 |     foldSame("f();");
237 |     foldSame("(function () {})();");
238 | 
239 |     // Uncalled function expressions are removed
240 |     fold("(function () {});", "");
241 |     fold("(function f() {});", "");
242 |     // ... including any code they contain.
243 |     fold("(function () {foo();});", "");
244 | 
245 |     // Useless operators are removed.
246 |     fold("+f()", "f()");
247 |     fold("a=(+f(),g())", "a=(f(),g())");
248 |     fold("a=(true,g())", "a=g()");
249 |     fold("f(),true", "f()");
250 |     fold("f() + g()", "f(),g()");
251 | 
252 |     fold("for(;;+f()){}", "for(;;f()){}");
253 |     fold("for(+f();;g()){}", "for(f();;g()){}");
254 |     fold("for(;;Math.random(f(),g(),h())){}", "for(;;f(),g(),h()){}");
255 | 
256 |     // The optimization cascades into conditional expressions:
257 |     fold("g() && +f()", "g() && f()");
258 |     fold("g() || +f()", "g() || f()");
259 |     fold("x ? g() : +f()", "x ? g() : f()");
260 | 
261 |     fold("+x()", "x()");
262 |     fold("+x() * 2", "x()");
263 |     fold("-(+x() * 2)", "x()");
264 |     fold("2 -(+x() * 2)", "x()");
265 |     fold("x().foo", "x()");
266 |     foldSame("x().foo()");
267 | 
268 |     foldSame("x++");
269 |     foldSame("++x");
270 |     foldSame("x--");
271 |     foldSame("--x");
272 |     foldSame("x = 2");
273 |     foldSame("x *= 2");
274 | 
275 |     // Sanity check, other expression are left alone.
276 |     foldSame("function f() {}");
277 |     foldSame("var x;");
278 |   }
```
