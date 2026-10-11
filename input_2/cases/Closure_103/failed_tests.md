# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckUnreachableCodeTest.testInstanceOfThrowsException()
Resolved declaration: com.google.javascript.jscomp.CheckUnreachableCodeTest.testInstanceOfThrowsException()
Source: test/com/google/javascript/jscomp/CheckUnreachableCodeTest.java

```java
139 |   public void testInstanceOfThrowsException() {
140 |     testSame("function f() {try { if (value instanceof type) return true; } " +
141 |              "catch (e) { }}");
142 |   }
```

## com.google.javascript.jscomp.ControlFlowAnalysisTest.testInstanceOf()
Resolved declaration: com.google.javascript.jscomp.ControlFlowAnalysisTest.testInstanceOf()
Source: test/com/google/javascript/jscomp/ControlFlowAnalysisTest.java

```java
1243 |   public void testInstanceOf() {
1244 |     String src = "try { x instanceof 'x' } catch (e) { }";
1245 |     ControlFlowGraph<Node> cfg = createCfg(src, true);
1246 |     assertCrossEdge(cfg, Token.EXPR_RESULT, Token.BLOCK, Branch.ON_EX);
1247 |   }
```

## com.google.javascript.jscomp.DisambiguatePropertiesTest.testSupertypeReferenceOfSubtypeProperty()
Resolved declaration: com.google.javascript.jscomp.DisambiguatePropertiesTest.testSupertypeReferenceOfSubtypeProperty()
Source: test/com/google/javascript/jscomp/DisambiguatePropertiesTest.java

```java
587 |   public void testSupertypeReferenceOfSubtypeProperty() {
588 |     String externs = ""
589 |         + "/** @constructor */ function Ext() {}"
590 |         + "Ext.prototype.a;";
591 |     String js = ""
592 |         + "/** @constructor */ function Foo() {}\n"
593 |         + "/** @constructor \n@extends Foo*/ function Bar() {}\n"
594 |         + "Bar.prototype.a;\n"
595 |         + "/** @param {Foo} foo */"
596 |         + "function foo(foo) {\n"
597 |         + "  var x = foo.a;\n"
598 |         + "}\n";
599 |     String result = ""
600 |         + "function Foo() {}\n"
601 |         + "function Bar() {}\n"
602 |         + "Bar.prototype.Bar_prototype$a;\n"
603 |         + "function foo(foo) {\n"
604 |         + "  var x = foo.Bar_prototype$a;\n"
605 |         + "}\n";
606 |     testSets(false, externs, js, result, "{a=[[Bar.prototype]]}");
607 |   }
```
