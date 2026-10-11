# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckGlobalThisTest.testPropertyOfMethod()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testPropertyOfMethod()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
157 |   public void testPropertyOfMethod() {
158 |     testFailure("a.protoype.b = {}; " +
159 |         "a.prototype.b.c = function() { this.foo = 3; };");
160 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testMethod4()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testMethod4()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
153 |   public void testMethod4() {
154 |     testSame("a.prototype['x' + 'y'] =  function() { this.foo = 3; };");
155 |   }
```

## com.google.javascript.jscomp.CheckGlobalThisTest.testInterface1()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testInterface1()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
111 |   public void testInterface1() {
112 |     testSame(
113 |         "/** @interface */function A() { /** @type {string} */ this.m2; }");
114 |   }
```
