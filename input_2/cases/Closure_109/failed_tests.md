# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testStructuralConstructor2()
Resolved declaration: com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testStructuralConstructor2()
Source: test/com/google/javascript/jscomp/parsing/JsDocInfoParserTest.java

```java
584 |   public void testStructuralConstructor2() throws Exception {
585 |     JSType type = testParseType(
586 |         "function (new:?)",
587 |         // toString skips unknowns, but isConstructor reveals the truth.
588 |         "function (): ?");
589 |     assertTrue(type.isConstructor());
590 |     assertFalse(type.isNominalConstructor());
591 |   }
```

## com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testStructuralConstructor3()
Resolved declaration: com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testStructuralConstructor3()
Source: test/com/google/javascript/jscomp/parsing/JsDocInfoParserTest.java

```java
593 |   public void testStructuralConstructor3() throws Exception {
594 |     resolve(parse("@type {function (new:*)} */").getType(),
595 |         "constructed type must be an object type");
596 |   }
```
