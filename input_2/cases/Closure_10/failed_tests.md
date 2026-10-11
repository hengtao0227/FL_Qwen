# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeFoldConstantsTest.testIssue821()
Resolved declaration: com.google.javascript.jscomp.PeepholeFoldConstantsTest.testIssue821()
Source: test/com/google/javascript/jscomp/PeepholeFoldConstantsTest.java

```java
580 |   public void testIssue821() {
581 |     foldSame("var a =(Math.random()>0.5? '1' : 2 ) + 3 + 4;");
582 |     foldSame("var a = ((Math.random() ? 0 : 1) ||" +
583 |              "(Math.random()>0.5? '1' : 2 )) + 3 + 4;");
584 |   }
```
