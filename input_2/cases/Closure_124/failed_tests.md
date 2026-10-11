# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ExploitAssignsTest.testIssue1017()
Resolved declaration: com.google.javascript.jscomp.ExploitAssignsTest.testIssue1017()
Source: test/com/google/javascript/jscomp/ExploitAssignsTest.java

```java
160 |   public void testIssue1017() {
161 |     testSame("x = x.parentNode.parentNode; x = x.parentNode.parentNode;");
162 |   }
```
