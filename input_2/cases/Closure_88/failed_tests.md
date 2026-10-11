# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testIssue297()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testIssue297()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
250 |   public void testIssue297() {
251 |     args.add("--compilation_level=SIMPLE_OPTIMIZATIONS");
252 |     test("function f(p) {" +
253 |          " var x;" +
254 |          " return ((x=p.id) && (x=parseInt(x.substr(1))) && x>0);" +
255 |          "}",
256 |          "function f(b) {" +
257 |          " var a;" +
258 |          " return ((a=b.id) && (a=parseInt(a.substr(1))) && a>0);" +
259 |          "}");
260 |   }  
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297a()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297a()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
367 |   public void testIssue297a() {
368 |     testSame("function f(p) {" +
369 |          " var x;" +
370 |          " return ((x=p.id) && (x=parseInt(x.substr(1))) && x>0);" +
371 |          "}; f('');");
372 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297b()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297b()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
374 |   public void testIssue297b() {
375 |     test("function f() {" +
376 |          " var x;" +
377 |          " return (x='') && (x = x.substr(1));" +
378 |          "};",
379 |          "function f() {" +
380 |          " var x;" +
381 |          " return (x='') && (x.substr(1));" +
382 |          "};");
383 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297c()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297c()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
385 |   public void testIssue297c() {
386 |     test("function f() {" +
387 |          " var x;" +
388 |          " return (x=1) && (x = f(x));" +
389 |          "};",
390 |          "function f() {" +
391 |          " var x;" +
392 |          " return (x=1) && f(x);" +
393 |          "};");
394 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297d()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297d()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
396 |   public void testIssue297d() {
397 |     test("function f(a) {" +
398 |          " return (a=1) && (a = f(a));" +
399 |          "};",
400 |          "function f(a) {" +
401 |          " return (a=1) && (f(a));" +
402 |          "};");
403 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297e()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297e()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
405 |   public void testIssue297e() {
406 |     test("function f(a) {" +
407 |          " return (a=1) - (a = g(a));" +
408 |          "};",
409 |          "function f(a) {" +
410 |          " return (a=1) - (g(a));" +
411 |          "};");
412 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297f()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue297f()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
414 |   public void testIssue297f() {
415 |     test("function f(a) {" +
416 |          " h((a=1) - (a = g(a)));" +
417 |          "};",
418 |          "function f(a) {" +
419 |          " h((a=1) - (g(a)));" +
420 |          "};");
421 |   }
```
