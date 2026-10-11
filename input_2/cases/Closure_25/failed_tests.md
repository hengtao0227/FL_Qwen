# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeInferenceTest.testBackwardsInferenceNew()
Resolved declaration: com.google.javascript.jscomp.TypeInferenceTest.testBackwardsInferenceNew()
Source: test/com/google/javascript/jscomp/TypeInferenceTest.java

```java
880 |   public void testBackwardsInferenceNew() {
881 |     inFunction(
882 |         "/**\n" +
883 |         " * @constructor\n" +
884 |         " * @param {{foo: (number|undefined)}} x\n" +
885 |         " */" +
886 |         "function F(x) {}" +
887 |         "var y = {};" +
888 |         "new F(y);");
889 | 
890 |     assertEquals("{foo: (number|undefined)}", getType("y").toString());
891 |   }
```
