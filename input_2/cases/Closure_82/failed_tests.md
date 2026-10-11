# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue301()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue301()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
4954 |   public void testIssue301() throws Exception {
4955 |     testTypes(
4956 |         "Array.indexOf = function() {};" +
4957 |         "var s = 'hello';" +
4958 |         "alert(s.toLowerCase.indexOf('1'));",
4959 |         "Property indexOf never defined on String.prototype.toLowerCase");
4960 |   }
```

## com.google.javascript.rhino.jstype.FunctionTypeTest.testEmptyFunctionTypes()
Resolved declaration: com.google.javascript.rhino.jstype.FunctionTypeTest.testEmptyFunctionTypes()
Source: test/com/google/javascript/rhino/jstype/FunctionTypeTest.java

```java
172 |   public void testEmptyFunctionTypes() {
173 |     assertTrue(LEAST_FUNCTION_TYPE.isEmptyType());
174 |     assertFalse(GREATEST_FUNCTION_TYPE.isEmptyType());
175 |   }
```
