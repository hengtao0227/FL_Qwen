# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.RemoveUnusedVarsTest.testIssue618_1()
Resolved declaration: com.google.javascript.jscomp.RemoveUnusedVarsTest.testIssue618_1()
Source: test/com/google/javascript/jscomp/RemoveUnusedVarsTest.java

```java
739 |   public void testIssue618_1() {
740 |     this.removeGlobal = false;
741 |     testSame(
742 |         "function f() {\n" +
743 |         "  var a = [], b;\n" +
744 |         "  a.push(b = []);\n" +
745 |         "  b[0] = 1;\n" +
746 |         "  return a;\n" +
747 |         "}");
748 |   }
```
