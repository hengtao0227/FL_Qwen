# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testQualifiedNameInference5()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testQualifiedNameInference5()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
4760 |   public void testQualifiedNameInference5() throws Exception {
4761 |     testTypes(
4762 |         "var ns = {}; " +
4763 |         "(function() { " +
4764 |         "    /** @param {number} x */ ns.foo = function(x) {}; })();" +
4765 |         "(function() { ns.foo(true); })();",
4766 |         "actual parameter 1 of ns.foo does not match formal parameter\n" +
4767 |         "found   : boolean\n" +
4768 |         "required: number");
4769 |   }
```

## com.google.javascript.jscomp.TypedScopeCreatorTest.testGlobalQualifiedNameInLocalScope()
Resolved declaration: com.google.javascript.jscomp.TypedScopeCreatorTest.testGlobalQualifiedNameInLocalScope()
Source: test/com/google/javascript/jscomp/TypedScopeCreatorTest.java

```java
775 |   public void testGlobalQualifiedNameInLocalScope() {
776 |     testSame(
777 |         "var ns = {}; " +
778 |         "(function() { " +
779 |         "    /** @param {number} x */ ns.foo = function(x) {}; })();" +
780 |         "(function() { ns.foo(3); })();");
781 |     assertNotNull(globalScope.getVar("ns.foo"));
782 |     assertEquals(
783 |         "function (number): undefined",
784 |         globalScope.getVar("ns.foo").getType().toString());
785 |   }
```
