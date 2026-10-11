# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testZero()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testZero()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1178 |   public void testZero() {
1179 |     assertPrint("var x ='\\0';", "var x=\"\\0\"");
1180 |     assertPrint("var x ='\\x00';", "var x=\"\\0\"");
1181 |     assertPrint("var x ='\\u0000';", "var x=\"\\0\"");
1182 |   }
```
