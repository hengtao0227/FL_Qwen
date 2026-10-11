# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldArithmetic()
Resolved declaration: com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldArithmetic()
Source: test/com/google/javascript/jscomp/PeepholeFoldConstantsTest.java

```java
552 |   public void testFoldArithmetic() {
553 |     fold("x = 10 + 20", "x = 30");
554 |     fold("x = 2 / 4", "x = 0.5");
555 |     fold("x = 2.25 * 3", "x = 6.75");
556 |     fold("z = x * y", "z = x * y");
557 |     fold("x = y * 5", "x = y * 5");
558 |     fold("x = 1 / 0", "x = 1 / 0");
559 |     fold("x = 3 % 2", "x = 1");
560 |     fold("x = 3 % -2", "x = 1");
561 |     fold("x = -1 % 3", "x = -1");
562 |     fold("x = 1 % 0", "x = 1 % 0");
563 |   }
```
