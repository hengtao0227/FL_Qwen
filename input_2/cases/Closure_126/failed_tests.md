# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.MinimizeExitPointsTest.testDontRemoveBreakInTryFinally()
Resolved declaration: com.google.javascript.jscomp.MinimizeExitPointsTest.testDontRemoveBreakInTryFinally()
Source: test/com/google/javascript/jscomp/MinimizeExitPointsTest.java

```java
275 |   public void testDontRemoveBreakInTryFinally() throws Exception {
276 |     foldSame("function f() {b:try{throw 9} finally {break b} return 1;}");
277 |   }
```

## com.google.javascript.jscomp.MinimizeExitPointsTest.testFunctionReturnOptimization()
Resolved declaration: com.google.javascript.jscomp.MinimizeExitPointsTest.testFunctionReturnOptimization()
Source: test/com/google/javascript/jscomp/MinimizeExitPointsTest.java

```java
91 |   public void testFunctionReturnOptimization() throws Exception {
92 |     fold("function f(){if(a()){b();if(c())return;}}",
93 |          "function f(){if(a()){b();if(c());}}");
94 |     fold("function f(){if(x)return; x=3; return; }",
95 |          "function f(){if(x); else x=3}");
96 |     fold("function f(){if(true){a();return;}else;b();}",
97 |          "function f(){if(true){a();}else{b();}}");
98 |     fold("function f(){if(false){a();return;}else;b();return;}",
99 |          "function f(){if(false){a();}else{b();}}");
100 |     fold("function f(){if(a()){b();return;}else;c();}",
101 |          "function f(){if(a()){b();}else{c();}}");
102 |     fold("function f(){if(a()){b()}else{c();return;}}",
103 |          "function f(){if(a()){b()}else{c();}}");
104 |     fold("function f(){if(a()){b();return;}else;}",
105 |          "function f(){if(a()){b();}else;}");
106 |     fold("function f(){if(a()){return;}else{return;} return;}",
107 |          "function f(){if(a()){}else{}}");
108 |     fold("function f(){if(a()){return;}else{return;} b();}",
109 |          "function f(){if(a()){}else{return;b()}}");
110 |     fold("function f(){ if (x) return; if (y) return; if (z) return; w(); }",
111 |         " function f() {" +
112 |         "   if (x) {} else { if (y) {} else { if (z) {} else w(); }}" +
113 |         " }");
114 | 
115 |     fold("function f(){while(a())return;}",
116 |          "function f(){while(a())return}");
117 |     foldSame("function f(){for(x in a())return}");
118 | 
119 |     fold("function f(){while(a())break;}",
120 |          "function f(){while(a())break}");
121 |     foldSame("function f(){for(x in a())break}");
122 | 
123 |     fold("function f(){try{return;}catch(e){throw 9;}finally{return}}",
124 |          "function f(){try{}catch(e){throw 9;}finally{return}}");
125 |     foldSame("function f(){try{throw 9;}finally{return;}}");
126 | 
127 |     fold("function f(){try{return;}catch(e){return;}}",
128 |          "function f(){try{}catch(e){}}");
129 |     fold("function f(){try{if(a()){return;}else{return;} return;}catch(e){}}",
130 |          "function f(){try{if(a()){}else{}}catch(e){}}");
131 | 
132 |     fold("function f(){g:return}",
133 |          "function f(){}");
134 |     fold("function f(){g:if(a()){return;}else{return;} return;}",
135 |          "function f(){g:if(a()){}else{}}");
136 |     fold("function f(){try{g:if(a()){throw 9;} return;}finally{return}}",
137 |          "function f(){try{g:if(a()){throw 9;}}finally{return}}");
138 |   }
```
