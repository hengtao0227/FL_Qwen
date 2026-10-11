# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.parsing.ParserTest.testDestructuringAssignForbidden4()
Resolved declaration: com.google.javascript.jscomp.parsing.ParserTest.testDestructuringAssignForbidden4()
Source: test/com/google/javascript/jscomp/parsing/ParserTest.java

```java
624 |   public void testDestructuringAssignForbidden4() {
625 |     parseError("[x, y] = foo();",
626 |         "destructuring assignment forbidden",
627 |         "invalid assignment target");
628 |   }
```
