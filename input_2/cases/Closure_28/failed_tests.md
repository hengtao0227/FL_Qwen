# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.InlineCostEstimatorTest.testCost()
Resolved declaration: com.google.javascript.jscomp.InlineCostEstimatorTest.testCost()
Source: test/com/google/javascript/jscomp/InlineCostEstimatorTest.java

```java
47 |   public void testCost() {
48 |     checkCost("1", "1");
49 |     checkCost("true", "1");
50 |     checkCost("false", "1");
51 |     checkCost("a", "xx");
52 |     checkCost("a + b", "xx+xx");
53 |     checkCost("foo()", "xx()");
54 |     checkCost("foo(a,b)", "xx(xx,xx)");
55 |     checkCost("10 + foo(a,b)", "0+xx(xx,xx)");
56 |     checkCost("1 + foo(a,b)", "1+xx(xx,xx)");
57 |     checkCost("a ? 1 : 0", "xx?1:0");
58 |     checkCost("a.b", "xx.xx");
59 |     checkCost("new Obj()", "new xx");
60 |     checkCost("function a() {return \"monkey\"}",
61 |               "function xx(){return\"monkey\"}");
62 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testIssue728()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testIssue728()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2167 |   public void testIssue728() {
2168 |     String f = "var f = function() { return false; };";
2169 |     StringBuilder calls = new StringBuilder();
2170 |     StringBuilder folded = new StringBuilder();
2171 |     for (int i = 0; i < 30; i++) {
2172 |       calls.append("if (!f()) alert('x');");
2173 |       folded.append("if (!false) alert('x');");
2174 |     }
2175 | 
2176 |     test(f + calls, folded.toString());
2177 |   }
```
