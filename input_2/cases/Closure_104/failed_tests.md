# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.rhino.jstype.UnionTypeTest.testGreatestSubtypeUnionTypes5()
Resolved declaration: com.google.javascript.rhino.jstype.UnionTypeTest.testGreatestSubtypeUnionTypes5()
Source: test/com/google/javascript/rhino/jstype/UnionTypeTest.java

```java
157 |   public void testGreatestSubtypeUnionTypes5() throws Exception {
158 |     JSType errUnion = createUnionType(EVAL_ERROR_TYPE, URI_ERROR_TYPE);
159 |     assertEquals(NO_OBJECT_TYPE,
160 |         errUnion.getGreatestSubtype(STRING_OBJECT_TYPE));
161 |   }
```
