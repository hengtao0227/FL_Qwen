# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineObjectLiteralsTest.testNoInlineDeletedProperties()
Resolved declaration: com.google.javascript.jscomp.InlineObjectLiteralsTest.testNoInlineDeletedProperties()
Source: test/com/google/javascript/jscomp/InlineObjectLiteralsTest.java

```java
351 |   public void testNoInlineDeletedProperties() {
352 |     testSameLocal(
353 |         "var foo = {bar:1};" +
354 |         "delete foo.bar;" +
355 |         "return foo.bar;");
356 |   }
```
