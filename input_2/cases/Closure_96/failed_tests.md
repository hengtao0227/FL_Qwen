# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testFunctionArguments16()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testFunctionArguments16()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
1361 |   public void testFunctionArguments16() throws Exception {
1362 |     testTypes(
1363 |         "/** @param {...number} var_args */" +
1364 |         "function g(var_args) {} g(1, true);",
1365 |         "actual parameter 2 of g does not match formal parameter\n" +
1366 |         "found   : boolean\n" +
1367 |         "required: (number|undefined)");
1368 |   }
```
