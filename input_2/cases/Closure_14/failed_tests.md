# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckMissingReturnTest.testIssue779()
Resolved declaration: com.google.javascript.jscomp.CheckMissingReturnTest.testIssue779()
Source: test/com/google/javascript/jscomp/CheckMissingReturnTest.java

```java
194 |   public void testIssue779() {
195 |     testNotMissing(
196 |         "var a = f(); try { alert(); if (a > 0) return 1; }" +
197 |         "finally { a = 5; } return 2;");
198 |   }
```

## com.google.javascript.jscomp.ControlFlowAnalysisTest.testDeepNestedFinally()
Resolved declaration: com.google.javascript.jscomp.ControlFlowAnalysisTest.testDeepNestedFinally()
Source: test/com/google/javascript/jscomp/ControlFlowAnalysisTest.java

```java
1112 |   public void testDeepNestedFinally() {
1113 |     String src = "try{try{try{throw 1}" +
1114 |         "finally{1;var a}}finally{2;if(a);}}finally{3;a()}";
1115 |     ControlFlowGraph<Node> cfg = createCfg(src);
1116 |     assertCrossEdge(cfg, Token.THROW, Token.BLOCK, Branch.ON_EX);
1117 |     assertCrossEdge(cfg, Token.VAR, Token.BLOCK, Branch.UNCOND);
1118 |     assertCrossEdge(cfg, Token.IF, Token.BLOCK, Branch.ON_EX);
1119 |   }
```

## com.google.javascript.jscomp.ControlFlowAnalysisTest.testDeepNestedBreakwithFinally()
Resolved declaration: com.google.javascript.jscomp.ControlFlowAnalysisTest.testDeepNestedBreakwithFinally()
Source: test/com/google/javascript/jscomp/ControlFlowAnalysisTest.java

```java
1097 |   public void testDeepNestedBreakwithFinally() {
1098 |     String src = "X:while(1){try{while(2){try{var a;break X;}" +
1099 |         "finally{}}}finally{}}";
1100 |     ControlFlowGraph<Node> cfg = createCfg(src);
1101 |     assertDownEdge(cfg, Token.WHILE, Token.BLOCK, Branch.ON_TRUE);
1102 |     assertDownEdge(cfg, Token.BLOCK, Token.TRY, Branch.UNCOND);
1103 |     assertDownEdge(cfg, Token.BLOCK, Token.VAR, Branch.UNCOND);
1104 |     // BREAK to FINALLY.
1105 |     assertCrossEdge(cfg, Token.BREAK, Token.BLOCK, Branch.UNCOND);
1106 |     // FINALLY to FINALLY.
1107 |     assertCrossEdge(cfg, Token.BLOCK, Token.BLOCK, Branch.ON_EX);
1108 |     assertCrossEdge(cfg, Token.WHILE, Token.BLOCK, Branch.ON_FALSE);
1109 |     assertReturnEdge(cfg, Token.BLOCK);
1110 |   }
```
