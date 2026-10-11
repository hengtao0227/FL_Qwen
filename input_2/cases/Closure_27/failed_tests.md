# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.rhino.IRTest.testIssue727_1()
Resolved declaration: com.google.javascript.rhino.IRTest.testIssue727_1()
Source: test/com/google/javascript/rhino/IRTest.java

```java
47 |   public void testIssue727_1() {
48 |     testIR(
49 |         IR.tryFinally(
50 |             IR.block(),
51 |             IR.block()),
52 |         "TRY\n" +
53 |         "    BLOCK\n" +
54 |         "    BLOCK\n" +
55 |         "    BLOCK\n");
56 |   }
```

## com.google.javascript.rhino.IRTest.testIssue727_2()
Resolved declaration: com.google.javascript.rhino.IRTest.testIssue727_2()
Source: test/com/google/javascript/rhino/IRTest.java

```java
58 |   public void testIssue727_2() {
59 |     testIR(
60 |         IR.tryCatch(
61 |             IR.block(),
62 |             IR.catchNode(
63 |                 IR.name("e"),
64 |                 IR.block())),
65 |         "TRY\n" +
66 |         "    BLOCK\n" +
67 |         "    BLOCK\n" +
68 |         "        CATCH\n" +
69 |         "            NAME e\n" +
70 |         "            BLOCK\n");
71 |   }
```

## com.google.javascript.rhino.IRTest.testIssue727_3()
Resolved declaration: com.google.javascript.rhino.IRTest.testIssue727_3()
Source: test/com/google/javascript/rhino/IRTest.java

```java
73 |   public void testIssue727_3() {
74 |     testIR(
75 |         IR.tryCatchFinally(
76 |             IR.block(),
77 |             IR.catchNode(IR.name("e"), IR.block()),
78 |             IR.block()),
79 |         "TRY\n" +
80 |         "    BLOCK\n" +
81 |         "    BLOCK\n" +
82 |         "        CATCH\n" +
83 |         "            NAME e\n" +
84 |         "            BLOCK\n" +
85 |         "    BLOCK\n");
86 |   }
```
