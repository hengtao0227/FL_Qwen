# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineObjectLiteralsTest.testBug545()
Resolved declaration: com.google.javascript.jscomp.InlineObjectLiteralsTest.testBug545()
Source: test/com/google/javascript/jscomp/InlineObjectLiteralsTest.java

```java
359 |   public void testBug545() {
360 |     testLocal("var a = {}", "");
361 |     testLocal("var a; a = {}", "true");
362 |   }
```
