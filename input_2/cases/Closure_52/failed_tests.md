# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testNumericKeys()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testNumericKeys()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1257 |   public void testNumericKeys() {
1258 |     assertPrint("var x = {010: 1};", "var x={8:1}");
1259 |     assertPrint("var x = {'010': 1};", "var x={\"010\":1}");
1260 | 
1261 |     assertPrint("var x = {0x10: 1};", "var x={16:1}");
1262 |     assertPrint("var x = {'0x10': 1};", "var x={\"0x10\":1}");
1263 | 
1264 |     // I was surprised at this result too.
1265 |     assertPrint("var x = {.2: 1};", "var x={\"0.2\":1}");
1266 |     assertPrint("var x = {'.2': 1};", "var x={\".2\":1}");
1267 | 
1268 |     assertPrint("var x = {0.2: 1};", "var x={\"0.2\":1}");
1269 |     assertPrint("var x = {'0.2': 1};", "var x={\"0.2\":1}");
1270 |   }
```
