# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckSideEffectsTest.testJSDocComments()
Resolved declaration: com.google.javascript.jscomp.CheckSideEffectsTest.testJSDocComments()
Source: test/com/google/javascript/jscomp/CheckSideEffectsTest.java

```java
85 |   public void testJSDocComments() {
86 |     test("function A() { /** This is a jsdoc comment */ this.foo; }", ok);
87 |     test("function A() { /* This is a normal comment */ this.foo; }", e);
88 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testTwinReferenceCancelsChildCollapsing()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testTwinReferenceCancelsChildCollapsing()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
1110 |   public void testTwinReferenceCancelsChildCollapsing() {
1111 |     test("var a = {}; if (a.b = function() {}) { a.b.c = 3; a.b(a.b.c); }",
1112 |          "var a$b; if (a$b = function() {}) { a$b.c = 3; a$b(a$b.c); }");
1113 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testCrashInNestedAssign()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testCrashInNestedAssign()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
1105 |   public void testCrashInNestedAssign() {
1106 |     test("var a = {}; if (a.b = function() {}) a.b();",
1107 |          "var a$b; if (a$b=function() {}) { a$b(); }");
1108 |   }
```

## com.google.javascript.jscomp.CollapsePropertiesTest.testCrashInCommaOperator()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testCrashInCommaOperator()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
1100 |   public void testCrashInCommaOperator() {
1101 |     test("var a = {}; a.b = function() {},a.b();",
1102 |          "var a$b; a$b=function() {},a$b();");
1103 |   }
```
