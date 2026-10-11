# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeInferenceTest.testNoThisInference()
Resolved declaration: com.google.javascript.jscomp.TypeInferenceTest.testNoThisInference()
Source: test/com/google/javascript/jscomp/TypeInferenceTest.java

```java
1000 |   public void testNoThisInference() {
1001 |     JSType thisType = createNullableType(OBJECT_TYPE);
1002 |     assumingThisType(thisType);
1003 |     inFunction("var out = 3; if (goog.isNull(this)) out = this;");
1004 |     verify("out", createUnionType(OBJECT_TYPE, NUMBER_TYPE));
1005 |   }
```
