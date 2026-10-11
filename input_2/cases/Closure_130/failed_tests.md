# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CollapsePropertiesTest.testIssue931()
Resolved declaration: com.google.javascript.jscomp.CollapsePropertiesTest.testIssue931()
Source: test/com/google/javascript/jscomp/CollapsePropertiesTest.java

```java
1099 |   public void testIssue931() {
1100 |     collapsePropertiesOnExternTypes = true;
1101 |     testSame(
1102 |       "function f() {\n" +
1103 |       "  return function () {\n" +
1104 |       "    var args = arguments;\n" +
1105 |       "    setTimeout(function() { alert(args); }, 0);\n" +
1106 |       "  }\n" +
1107 |       "};\n");
1108 |   }
```
