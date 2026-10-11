# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue537a()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue537a()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
5263 |   public void testIssue537a() throws Exception {
5264 |     testTypes(
5265 |         "/** @constructor */ function Foo() {}" +
5266 |         "Foo.prototype = {method: function() {}};" +
5267 |         "/**\n" +
5268 |         " * @constructor\n" +
5269 |         " * @extends {Foo}\n" +
5270 |         " */\n" +
5271 |         "function Bar() {" +
5272 |         "  Foo.call(this);" +
5273 |         "  if (this.baz()) this.method(1);" +
5274 |         "}" +
5275 |         "Bar.prototype = {" +
5276 |         "  baz: function() {" +
5277 |         "    return true;" +
5278 |         "  }" +
5279 |         "};" +
5280 |         "Bar.prototype.__proto__ = Foo.prototype;",
5281 |         "Function Foo.prototype.method: called with 1 argument(s). " +
5282 |         "Function requires at least 0 argument(s) " +
5283 |         "and no more than 0 argument(s).");
5284 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testIssue537b()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue537b()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
5286 |   public void testIssue537b() throws Exception {
5287 |     testTypes(
5288 |         "/** @constructor */ function Foo() {}" +
5289 |         "Foo.prototype = {method: function() {}};" +
5290 |         "/**\n" +
5291 |         " * @constructor\n" +
5292 |         " * @extends {Foo}\n" +
5293 |         " */\n" +
5294 |         "function Bar() {" +
5295 |         "  Foo.call(this);" +
5296 |         "  if (this.baz(1)) this.method();" +
5297 |         "}" +
5298 |         "Bar.prototype = {" +
5299 |         "  baz: function() {" +
5300 |         "    return true;" +
5301 |         "  }" +
5302 |         "};" +
5303 |         "Bar.prototype.__proto__ = Foo.prototype;",
5304 |         "Function Bar.prototype.baz: called with 1 argument(s). " +
5305 |         "Function requires at least 0 argument(s) " +
5306 |         "and no more than 0 argument(s).");
5307 |   }
```

## com.google.javascript.jscomp.TypedScopeCreatorTest.testPropertyOnUnknownSuperClass2()
Resolved declaration: com.google.javascript.jscomp.TypedScopeCreatorTest.testPropertyOnUnknownSuperClass2()
Source: test/com/google/javascript/jscomp/TypedScopeCreatorTest.java

```java
365 |   public void testPropertyOnUnknownSuperClass2() {
366 |     testSame(
367 |         "var goog = this.foo();" +
368 |         "/** @constructor \n * @extends {goog.Unknown} */" +
369 |         "function Foo() {}" +
370 |         "Foo.prototype = {bar: 1};" +
371 |         "var x = new Foo();",
372 |         RhinoErrorReporter.TYPE_PARSE_ERROR);
373 |     ObjectType x = (ObjectType) findNameType("x", globalScope);
374 |     assertEquals("Foo", x.toString());
375 |     assertEquals("Foo.prototype", x.getImplicitPrototype().toString());
376 |     assertTrue(x.getImplicitPrototype().hasOwnProperty("bar"));
377 |     assertEquals("?", x.getPropertyType("bar").toString());
378 |     assertTrue(x.isPropertyTypeInferred("bar"));
379 |   }
```
