# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testZero()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testZero()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1230 |   public void testZero() {
1231 |     assertPrint("var x ='\\0';", "var x=\"\\000\"");
1232 |     assertPrint("var x ='\\x00';", "var x=\"\\000\"");
1233 |     assertPrint("var x ='\\u0000';", "var x=\"\\000\"");
1234 |     assertPrint("var x ='\\u00003';", "var x=\"\\0003\"");
1235 |   }
```
