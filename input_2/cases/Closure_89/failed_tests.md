# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToChildOfUncollapsibleFunctionInLocalScope()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToChildOfUncollapsibleFunctionInLocalScope()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
609 |   public void testAddPropertyToChildOfUncollapsibleFunctionInLocalScope() {
610 |     testSame(
611 |         "function a() {} a.b = {x: 0}; var c = a;" +
612 |         "(function() {a.b.y = 0;})(); a.b.y;");
613 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth1_1()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth1_1()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
278 |   public void testAliasCreatedForFunctionDepth1_1() {
279 |     testSame("var a = function(){}; a.b = 1; var c = a; c.b = 2; a.b != c.b;");
280 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth1_2()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth1_2()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
294 |   public void testAliasCreatedForFunctionDepth1_2() {
295 |     testSame("var a = function(){}; a.b = 1; f(a); a.b;");
296 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth1_3()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth1_3()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
303 |   public void testAliasCreatedForFunctionDepth1_3() {
304 |     testSame("var a = function(){}; a.b = 1; new f(a); a.b;");
305 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToUncollapsibleNamedCtorInLocalScopeDepth1()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToUncollapsibleNamedCtorInLocalScopeDepth1()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
547 |   public void testAddPropertyToUncollapsibleNamedCtorInLocalScopeDepth1() {
548 |     // This technically should be collapsed, according to the rules.
549 |     // We don't collapse named constructors for legacy reasons
550 |     // (this pass has been around too long, and we don't know who's
551 |     // depending on this behavior).
552 |     testSame(
553 |           "/** @constructor */ function a() {} var c = a; " +
554 |           "(function() {a.b = 0;})(); a.b;");
555 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToUncollapsibleFunctionInLocalScopeDepth1()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToUncollapsibleFunctionInLocalScopeDepth1()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
543 |   public void testAddPropertyToUncollapsibleFunctionInLocalScopeDepth1() {
544 |     testSame("function a() {} var c = a; (function() {a.b = 0;})(); a.b;");
545 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToUncollapsibleFunctionInLocalScopeDepth2()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAddPropertyToUncollapsibleFunctionInLocalScopeDepth2()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
571 |   public void testAddPropertyToUncollapsibleFunctionInLocalScopeDepth2() {
572 |     test("var a = {}; a.b = function (){}; var d = a.b;" +
573 |          "(function() {a.b.c = 0;})(); a.b.c;",
574 |          "var a$b = function (){}; var d = a$b;" +
575 |          "(function() {a$b.c = 0;})(); a$b.c;");
576 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth2()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testAliasCreatedForFunctionDepth2()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
312 |   public void testAliasCreatedForFunctionDepth2() {
313 |     test(
314 |         "var a = {}; a.b = function() {}; a.b.c = 1; var d = a.b;" +
315 |         "a.b.c != d.c;",
316 |         "var a$b = function() {}; a$b.c = 1; var d = a$b;" +
317 |         "a$b.c != d.c;");
318 |   }
```
