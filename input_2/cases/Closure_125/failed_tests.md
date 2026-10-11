# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue1002()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue1002()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
6740 |   public void testIssue1002() throws Exception {
6741 |     testTypes(
6742 |         "/** @interface */" +
6743 |         "var I = function() {};" +
6744 |         "/** @constructor @implements {I} */" +
6745 |         "var A = function() {};" +
6746 |         "/** @constructor @implements {I} */" +
6747 |         "var B = function() {};" +
6748 |         "var f = function() {" +
6749 |         "  if (A === B) {" +
6750 |         "    new B();" +
6751 |         "  }" +
6752 |         "};");
6753 |   }
```
