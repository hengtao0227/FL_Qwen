# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.JSCompilerSourceExcerptProviderTest.testExceptNoNewLine()
Resolved declaration: com.google.javascript.jscomp.JSCompilerSourceExcerptProviderTest.testExceptNoNewLine()
Source: test/com/google/javascript/jscomp/JSCompilerSourceExcerptProviderTest.java

```java
64 |   public void testExceptNoNewLine() throws Exception {
65 |     assertEquals("foo2:first line", provider.getSourceLine("foo2", 1));
66 |     assertEquals("foo2:second line", provider.getSourceLine("foo2", 2));
67 |     assertEquals("foo2:third line", provider.getSourceLine("foo2", 3));
68 |     assertEquals(null, provider.getSourceLine("foo2", 4));
69 |   }
```

## com.google.javascript.jscomp.JsMessageExtractorTest.testSyntaxError1()
Resolved declaration: com.google.javascript.jscomp.JsMessageExtractorTest.testSyntaxError1()
Source: test/com/google/javascript/jscomp/JsMessageExtractorTest.java

```java
54 |   public void testSyntaxError1() {
55 |     try {
56 |       extractMessage("if (true) {}}");
57 |       fail("Expected exception");
58 |     } catch (RuntimeException e) {
59 |       assertTrue(e.getMessage().contains("JSCompiler errors\n"));
60 |       assertTrue(e.getMessage().contains(
61 |           "testcode:1: ERROR - Parse error. syntax error\n"));
62 |       assertTrue(e.getMessage().contains("if (true) {}}\n"));
63 |     }
64 |   }
```

## com.google.javascript.jscomp.JsMessageExtractorTest.testSyntaxError2()
Resolved declaration: com.google.javascript.jscomp.JsMessageExtractorTest.testSyntaxError2()
Source: test/com/google/javascript/jscomp/JsMessageExtractorTest.java

```java
66 |   public void testSyntaxError2() {
67 |     try {
68 |       extractMessage("", "if (true) {}}");
69 |       fail("Expected exception");
70 |     } catch (RuntimeException e) {
71 |       assertTrue(e.getMessage().contains("JSCompiler errors\n"));
72 |       assertTrue(e.getMessage().contains(
73 |           "testcode:2: ERROR - Parse error. syntax error\n"));
74 |       assertTrue(e.getMessage().contains("if (true) {}}\n"));
75 |     }
76 |   }
```
