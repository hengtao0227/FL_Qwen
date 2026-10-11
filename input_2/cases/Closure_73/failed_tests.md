# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testUnicode()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testUnicode()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1212 |   public void testUnicode() {
1213 |     assertPrint("var x ='\\x0f';", "var x=\"\\u000f\"");
1214 |     assertPrint("var x ='\\x68';", "var x=\"h\"");
1215 |     assertPrint("var x ='\\x7f';", "var x=\"\\u007f\"");
1216 |   }
```
