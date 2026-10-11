# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428_return()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428_return()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
361 |   public void testIssue4177428_return() {
362 |     test(
363 |         "f = function() {\n" +
364 |         "  var action;\n" +
365 |         "  a: {\n" +
366 |         "    var proto = null;\n" +
367 |         "    try {\n" +
368 |         "      proto = new Proto\n" +
369 |         "    } finally {\n" +
370 |         "      action = proto;\n" +
371 |         "      return\n" +  // Keep this...
372 |         "    }\n" +
373 |         "  }\n" +
374 |         "  alert(action)\n" + // and remove this.
375 |         "};",
376 |         "f = function() {\n" +
377 |         "  var action;\n" +
378 |         "  a: {\n" +
379 |         "    var proto = null;\n" +
380 |         "    try {\n" +
381 |         "      proto = new Proto\n" +
382 |         "    } finally {\n" +
383 |         "      action = proto;\n" +
384 |         "      return\n" +
385 |         "    }\n" +
386 |         "  }\n" +
387 |         "};"
388 |         );
389 |   }
```

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testDontRemoveBreakInTryFinally()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testDontRemoveBreakInTryFinally()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
416 |   public void testDontRemoveBreakInTryFinally() throws Exception {
417 |     testSame("function f() {b:try{throw 9} finally {break b} return 1;}");
418 |   }
```

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428_continue()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428_continue()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
344 |   public void testIssue4177428_continue() {
345 |     testSame(
346 |         "f = function() {\n" +
347 |         "  var action;\n" +
348 |         "  a: do {\n" +
349 |         "    var proto = null;\n" +
350 |         "    try {\n" +
351 |         "      proto = new Proto\n" +
352 |         "    } finally {\n" +
353 |         "      action = proto;\n" +
354 |         "      continue a\n" +  // Keep this...
355 |         "    }\n" +
356 |         "  } while(false)\n" +
357 |         "  alert(action)\n" + // and this.
358 |         "};");
359 |   }
```

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testDontRemoveBreakInTryFinallySwitch()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testDontRemoveBreakInTryFinallySwitch()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
420 |   public void testDontRemoveBreakInTryFinallySwitch() throws Exception {
421 |     testSame("function f() {b:try{throw 9} finally {switch(x) {case 1: break b} } return 1;}");
422 |   }
```

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428a()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428a()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
287 |   public void testIssue4177428a() {
288 |     testSame(
289 |         "f = function() {\n" +
290 |         "  var action;\n" +
291 |         "  a: {\n" +
292 |         "    var proto = null;\n" +
293 |         "    try {\n" +
294 |         "      proto = new Proto\n" +
295 |         "    } finally {\n" +
296 |         "      action = proto;\n" +
297 |         "      break a\n" +  // Keep this...
298 |         "    }\n" +
299 |         "  }\n" +
300 |         "  alert(action)\n" + // and this.
301 |         "};");
302 |   }
```

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428c()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue4177428c()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
324 |   public void testIssue4177428c() {
325 |     testSame(
326 |         "f = function() {\n" +
327 |         "  var action;\n" +
328 |         "  a: {\n" +
329 |         "    var proto = null;\n" +
330 |         "    try {\n" +
331 |         "    } finally {\n" +
332 |         "    try {\n" +
333 |         "      proto = new Proto\n" +
334 |         "    } finally {\n" +
335 |         "      action = proto;\n" +
336 |         "      break a\n" +  // Keep this...
337 |         "    }\n" +
338 |         "    }\n" +
339 |         "  }\n" +
340 |         "  alert(action)\n" + // and this.
341 |         "};");
342 |   }
```
