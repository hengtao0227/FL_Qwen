# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckGlobalNamesTest.testGlobalCatch()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalNamesTest.testGlobalCatch()
Source: test/com/google/javascript/jscomp/CheckGlobalNamesTest.java

```java
340 |   public void testGlobalCatch() throws Exception {
341 |     testSame(
342 |         "try {" +
343 |         "  throw Error();" +
344 |         "} catch (e) {" +
345 |         "  console.log(e.name)" +
346 |         "}");
347 |   }
```
