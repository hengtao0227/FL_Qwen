# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeSubstituteAlternateSyntaxTest.testIssue291()
Resolved declaration: com.google.javascript.jscomp.PeepholeSubstituteAlternateSyntaxTest.testIssue291()
Source: test/com/google/javascript/jscomp/PeepholeSubstituteAlternateSyntaxTest.java

```java
566 |   public void testIssue291() {
567 |     fold("if (true) { f.onchange(); }", "if (1) f.onchange();");
568 |     foldSame("if (f) { f.onchange(); }");
569 |     foldSame("if (f) { f.bar(); } else { f.onchange(); }");
570 |     fold("if (f) { f.bonchange(); }", "f && f.bonchange();");
571 |     foldSame("if (f) { f['x'](); }");
572 |   }
```
