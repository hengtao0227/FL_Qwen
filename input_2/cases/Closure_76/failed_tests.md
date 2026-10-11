# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testInExpression2()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testInExpression2()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
456 |   public void testInExpression2() {
457 |     // This can be improved.  "a = 1" is dead but "a" is read in the following
458 |     // expression.
459 |     inFunction(
460 |         "var a; a = 1; if ((a = 2) || (a = 3) || (a)) {}",
461 |         "var a; a = 1; if ((    2) || (a = 3) || (a)) {}");
462 | 
463 |     inFunction(
464 |         "var a; (a = 1) || (a = 2)",
465 |         "var a; 1 || 2");
466 | 
467 |     inFunction("var a; (a = 1) || (a = 2); return a");
468 | 
469 |     inFunction(
470 |         "var a; a = 1; a ? a = 2 : a;",
471 |         "var a; a = 1; a ?     2 : a;");
472 | 
473 |     inFunction("var a; a = 1; a ? a = 2 : a; return a");
474 | 
475 |     inFunction(
476 |         "var a; a = 1; a ? a : a = 2;",
477 |         "var a; a = 1; a ? a : 2;");
478 | 
479 |     inFunction("var a; a = 1; a ? a : a =2; return a");
480 | 
481 |     inFunction(
482 |         "var a; (a = 1) ? a = 2 : a = 3;",
483 |         "var a;      1  ?     2 :     3;");
484 | 
485 |     // This can be improved.  "a = 1" is dead but "a" is read in the following
486 |     // expression.
487 |     inFunction("var a; (a = 1) ? a = 2 : a = 3; return a");
488 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue384b()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue384b()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
500 |   public void testIssue384b() {
501 |     inFunction(
502 |             " var a, b;\n" +
503 |             " (f(b = true) || f(b = false)) ? (a = b) : (a = null);\n" +
504 |             " return a;");
505 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue384c()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue384c()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
507 |   public void testIssue384c() {
508 |     inFunction(
509 |             " var a, b;\n" +
510 |             " (a ? f(b = true) : f(b = false)) && (a = b);\n" +
511 |             " return a;");
512 |   }
```

## com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue384d()
Resolved declaration: com.google.javascript.jscomp.DeadAssignmentsEliminationTest.testIssue384d()
Source: test/com/google/javascript/jscomp/DeadAssignmentsEliminationTest.java

```java
514 |   public void testIssue384d() {
515 |     inFunction(
516 |             " var a, b;\n" +
517 |             " (f(b = true) || f(b = false)) && (a = b);\n" +
518 |             " return a;");
519 |   }
```
