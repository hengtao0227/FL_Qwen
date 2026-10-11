# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeSubstituteAlternateSyntaxTest.testIssue925()
Resolved declaration: com.google.javascript.jscomp.PeepholeSubstituteAlternateSyntaxTest.testIssue925()
Source: test/com/google/javascript/jscomp/PeepholeSubstituteAlternateSyntaxTest.java

```java
966 |   public void testIssue925() {
967 |     test(
968 |         "if (x[--y] === 1) {\n" +
969 |         "    x[y] = 0;\n" +
970 |         "} else {\n" +
971 |         "    x[y] = 1;\n" +
972 |         "}",
973 |         "(x[--y] === 1) ? x[y] = 0 : x[y] = 1;");
974 | 
975 |     test(
976 |         "if (x[--y]) {\n" +
977 |         "    a = 0;\n" +
978 |         "} else {\n" +
979 |         "    a = 1;\n" +
980 |         "}",
981 |         "a = (x[--y]) ? 0 : 1;");
982 | 
983 |     test("if (x++) { x += 2 } else { x += 3 }",
984 |          "x++ ? x += 2 : x += 3");
985 | 
986 |     test("if (x++) { x = x + 2 } else { x = x + 3 }",
987 |         "x = x++ ? x + 2 : x + 3");
988 |   }
```
