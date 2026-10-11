# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ClosureReverseAbstractInterpreterTest.testGoogIsFunction2()
Resolved declaration: com.google.javascript.jscomp.ClosureReverseAbstractInterpreterTest.testGoogIsFunction2()
Source: test/com/google/javascript/jscomp/ClosureReverseAbstractInterpreterTest.java

```java
120 |   public void testGoogIsFunction2() throws Exception {
121 |     testClosureFunction("goog.isFunction",
122 |         OBJECT_NUMBER_STRING_BOOLEAN,
123 |         U2U_CONSTRUCTOR_TYPE,
124 |         OBJECT_NUMBER_STRING_BOOLEAN);
125 |   }
```

## com.google.javascript.jscomp.SemanticReverseAbstractInterpreterTest.testTypeof3()
Resolved declaration: com.google.javascript.jscomp.SemanticReverseAbstractInterpreterTest.testTypeof3()
Source: test/com/google/javascript/jscomp/SemanticReverseAbstractInterpreterTest.java

```java
462 |   @SuppressWarnings("unchecked")
463 |   public void testTypeof3() {
464 |     FlowScope blind = newScope();
465 |     testBinop(blind,
466 |         Token.EQ,
467 |         new Node(Token.TYPEOF, createVar(
468 |             blind, "a", OBJECT_NUMBER_STRING_BOOLEAN)),
469 |         Node.newString("function"),
470 |         Sets.newHashSet(
471 |             new TypedName("a", U2U_CONSTRUCTOR_TYPE)),
472 |         Sets.newHashSet(
473 |             new TypedName("a", OBJECT_NUMBER_STRING_BOOLEAN)));
474 |   }
```
