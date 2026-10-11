# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testMinusNegativeZero()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testMinusNegativeZero()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1371 |   public void testMinusNegativeZero() {
1372 |     // Negative zero is weird, because we have to be able to distinguish
1373 |     // it from positive zero (there are some subtle differences in behavior).
1374 |     assertPrint("x- -0", "x- -0.0");
1375 |   }
```
