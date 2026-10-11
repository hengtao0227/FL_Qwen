# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.parsing.ParserTest.testSuspiciousBlockCommentWarning3()
Resolved declaration: com.google.javascript.jscomp.parsing.ParserTest.testSuspiciousBlockCommentWarning3()
Source: test/com/google/javascript/jscomp/parsing/ParserTest.java

```java
694 |   public void testSuspiciousBlockCommentWarning3() {
695 |     parse("/* \n *@type {number} */ var x = 3;", SUSPICIOUS_COMMENT_WARNING);
696 |   }
```

## com.google.javascript.jscomp.parsing.ParserTest.testSuspiciousBlockCommentWarning4()
Resolved declaration: com.google.javascript.jscomp.parsing.ParserTest.testSuspiciousBlockCommentWarning4()
Source: test/com/google/javascript/jscomp/parsing/ParserTest.java

```java
698 |   public void testSuspiciousBlockCommentWarning4() {
699 |     parse(
700 |         "  /*\n" +
701 |         "   * @type {number}\n" +
702 |         "   */\n" +
703 |         "  var x = 3;",
704 |         SUSPICIOUS_COMMENT_WARNING);
705 |   }
```

## com.google.javascript.jscomp.parsing.ParserTest.testSuspiciousBlockCommentWarning5()
Resolved declaration: com.google.javascript.jscomp.parsing.ParserTest.testSuspiciousBlockCommentWarning5()
Source: test/com/google/javascript/jscomp/parsing/ParserTest.java

```java
707 |   public void testSuspiciousBlockCommentWarning5() {
708 |     parse(
709 |         "  /*\n" +
710 |         "   * some random text here\n" +
711 |         "   * @type {number}\n" +
712 |         "   */\n" +
713 |         "  var x = 3;",
714 |         SUSPICIOUS_COMMENT_WARNING);
715 |   }
```
