# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.LightweightMessageFormatterTest.testFormatErrorSpaceEndOfLine1()
Resolved declaration: com.google.javascript.jscomp.LightweightMessageFormatterTest.testFormatErrorSpaceEndOfLine1()
Source: test/com/google/javascript/jscomp/LightweightMessageFormatterTest.java

```java
87 |   public void testFormatErrorSpaceEndOfLine1() throws Exception {
88 |     JSError error = JSError.make("javascript/complex.js",
89 |         1, 10, FOO_TYPE);
90 |     LightweightMessageFormatter formatter = formatter("assert (1;");
91 |     assertEquals("javascript/complex.js:1: ERROR - error description here\n" +
92 |         "assert (1;\n" +
93 |         "          ^\n", formatter.formatError(error));
94 |   }
```

## com.google.javascript.jscomp.LightweightMessageFormatterTest.testFormatErrorSpaceEndOfLine2()
Resolved declaration: com.google.javascript.jscomp.LightweightMessageFormatterTest.testFormatErrorSpaceEndOfLine2()
Source: test/com/google/javascript/jscomp/LightweightMessageFormatterTest.java

```java
96 |   public void testFormatErrorSpaceEndOfLine2() throws Exception {
97 |     JSError error = JSError.make("javascript/complex.js",
98 |         6, 7, FOO_TYPE);
99 |     LightweightMessageFormatter formatter = formatter("if (foo");
100 |     assertEquals("javascript/complex.js:6: ERROR - error description here\n" +
101 |         "if (foo\n" +
102 |         "       ^\n", formatter.formatError(error));
103 |   }
```
