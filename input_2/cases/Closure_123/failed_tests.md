# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testPrintInOperatorInForLoop()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testPrintInOperatorInForLoop()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
439 |   public void testPrintInOperatorInForLoop() {
440 |     // Check for in expression in for's init expression.
441 |     // Check alone, with + (higher precedence), with ?: (lower precedence),
442 |     // and with conditional.
443 |     assertPrint("var a={}; for (var i = (\"length\" in a); i;) {}",
444 |         "var a={};for(var i=(\"length\"in a);i;);");
445 |     assertPrint("var a={}; for (var i = (\"length\" in a) ? 0 : 1; i;) {}",
446 |         "var a={};for(var i=(\"length\"in a)?0:1;i;);");
447 |     assertPrint("var a={}; for (var i = (\"length\" in a) + 1; i;) {}",
448 |         "var a={};for(var i=(\"length\"in a)+1;i;);");
449 |     assertPrint("var a={};for (var i = (\"length\" in a|| \"size\" in a);;);",
450 |         "var a={};for(var i=(\"length\"in a)||(\"size\"in a);;);");
451 |     assertPrint("var a={};for (var i = a || a || (\"size\" in a);;);",
452 |         "var a={};for(var i=a||a||(\"size\"in a);;);");
453 | 
454 |     // Test works with unary operators and calls.
455 |     assertPrint("var a={}; for (var i = -(\"length\" in a); i;) {}",
456 |         "var a={};for(var i=-(\"length\"in a);i;);");
457 |     assertPrint("var a={};function b_(p){ return p;};" +
458 |         "for(var i=1,j=b_(\"length\" in a);;) {}",
459 |         "var a={};function b_(p){return p}" +
460 |             "for(var i=1,j=b_(\"length\"in a);;);");
461 | 
462 |     // Test we correctly handle an in operator in the test clause.
463 |     assertPrint("var a={}; for (;(\"length\" in a);) {}",
464 |         "var a={};for(;\"length\"in a;);");
465 | 
466 |     // Test we correctly handle an in operator inside a comma.
467 |     assertPrintSame("for(x,(y in z);;)foo()");
468 |     assertPrintSame("for(var x,w=(y in z);;)foo()");
469 | 
470 |     // And in operator inside a hook.
471 |     assertPrintSame("for(a=c?0:(0 in d);;)foo()");
472 |   }
```
