# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckSideEffectsTest.testUselessCode()
Resolved declaration: com.google.javascript.jscomp.CheckSideEffectsTest.testUselessCode()
Source: test/com/google/javascript/jscomp/CheckSideEffectsTest.java

```java
49 |   public void testUselessCode() {
50 |     test("function f(x) { if(x) return; }", ok);
51 |     test("function f(x) { if(x); }", "function f(x) { if(x); }", e);
52 | 
53 |     test("if(x) x = y;", ok);
54 |     test("if(x) x == bar();", "if(x) JSCOMPILER_PRESERVE(x == bar());", e);
55 | 
56 |     test("x = 3;", ok);
57 |     test("x == 3;", "JSCOMPILER_PRESERVE(x == 3);", e);
58 | 
59 |     test("var x = 'test'", ok);
60 |     test("var x = 'test'\n'str'",
61 |          "var x = 'test'\nJSCOMPILER_PRESERVE('str')", e);
62 | 
63 |     test("", ok);
64 |     test("foo();;;;bar();;;;", ok);
65 | 
66 |     test("var a, b; a = 5, b = 6", ok);
67 |     test("var a, b; a = 5, b == 6",
68 |          "var a, b; a = 5, JSCOMPILER_PRESERVE(b == 6)", e);
69 |     test("var a, b; a = (5, 6)",
70 |          "var a, b; a = (JSCOMPILER_PRESERVE(5), 6)", e);
71 |     test("var a, b; a = (bar(), 6, 7)",
72 |          "var a, b; a = (bar(), JSCOMPILER_PRESERVE(6), 7)", e);
73 |     test("var a, b; a = (bar(), bar(), 7, 8)",
74 |          "var a, b; a = (bar(), bar(), JSCOMPILER_PRESERVE(7), 8)", e);
75 |     test("var a, b; a = (b = 7, 6)", ok);
76 |     test("function x(){}\nfunction f(a, b){}\nf(1,(x(), 2));", ok);
77 |     test("function x(){}\nfunction f(a, b){}\nf(1,(2, 3));",
78 |          "function x(){}\nfunction f(a, b){}\n" +
79 |          "f(1,(JSCOMPILER_PRESERVE(2), 3));", e);
80 |   }
```
