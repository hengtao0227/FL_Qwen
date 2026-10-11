# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckGlobalThisTest.testStaticFunction6()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testStaticFunction6()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
87 |   public void testStaticFunction6() {
88 |     testSame("function a() { return function() { this = 8; } }");
89 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testStaticFunction7()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testStaticFunction7()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
91 |   public void testStaticFunction7() {
92 |     testSame("var a = function() { return function() { this = 8; } }");
93 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testStaticFunction8()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testStaticFunction8()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
95 |   public void testStaticFunction8() {
96 |     testFailure("var a = function() { return this.foo; };");
97 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testGlobalThis7()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testGlobalThis7()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
63 |   public void testGlobalThis7() {
64 |     testFailure("var a = this.foo;");
65 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testStaticMethod2()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testStaticMethod2()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
147 |   public void testStaticMethod2() {
148 |     testSame("a.b = function() { return function() { this.m2 = 5; } }");
149 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testStaticMethod3()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testStaticMethod3()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
151 |   public void testStaticMethod3() {
152 |     testSame("a.b.c = function() { return function() { this.m2 = 5; } }");
153 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testInnerFunction1()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testInnerFunction1()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
170 |   public void testInnerFunction1() {
171 |     testFailure("function f() { function g() { return this.x; } }");
172 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testInnerFunction2()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testInnerFunction2()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
174 |   public void testInnerFunction2() {
175 |     testFailure("function f() { var g = function() { return this.x; } }");
176 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testInnerFunction3()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testInnerFunction3()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
178 |   public void testInnerFunction3() {
179 |     testFailure(
180 |         "function f() { var x = {}; x.y = function() { return this.x; } }");
181 |   }
```
