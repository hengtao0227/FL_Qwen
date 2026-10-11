# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue669()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue669()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
5620 |   public void testIssue669() throws Exception {
5621 |     testTypes(
5622 |         "/** @return {{prop1: (Object|undefined)}} */" +
5623 |          "function f(a) {" +
5624 |          "  var results;" +
5625 |          "  if (a) {" +
5626 |          "    results = {};" +
5627 |          "    results.prop1 = {a: 3};" +
5628 |          "  } else {" +
5629 |          "    results = {prop2: 3};" +
5630 |          "  }" +
5631 |          "  return results;" +
5632 |          "}");
5633 |   }
```
