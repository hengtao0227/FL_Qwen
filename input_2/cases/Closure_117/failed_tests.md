# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue1047()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue1047()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
6851 |   public void testIssue1047() throws Exception {
6852 |     testTypes(
6853 |         "/**\n" +
6854 |         " * @constructor\n" +
6855 |         " */\n" +
6856 |         "function C2() {}\n" +
6857 |         "\n" +
6858 |         "/**\n" +
6859 |         " * @constructor\n" +
6860 |         " */\n" +
6861 |         "function C3(c2) {\n" +
6862 |         "  /**\n" +
6863 |         "   * @type {C2} \n" +
6864 |         "   * @private\n" +
6865 |         "   */\n" +
6866 |         "  this.c2_;\n" +
6867 |         "\n" +
6868 |         "  var x = this.c2_.prop;\n" +
6869 |         "}",
6870 |         "Property prop never defined on C2");
6871 |   }
```
