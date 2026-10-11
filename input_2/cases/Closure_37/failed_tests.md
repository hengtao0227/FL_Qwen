# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testIncompleteFunction()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIncompleteFunction()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
1937 |   public void testIncompleteFunction() {
1938 |     CompilerOptions options = createCompilerOptions();
1939 |     options.ideMode = true;
1940 |     DiagnosticType[] warnings = new DiagnosticType[]{
1941 |         RhinoErrorReporter.PARSE_ERROR,
1942 |         RhinoErrorReporter.PARSE_ERROR,
1943 |         RhinoErrorReporter.PARSE_ERROR,
1944 |         RhinoErrorReporter.PARSE_ERROR};
1945 |     test(options,
1946 |         new String[] { "var foo = {bar: function(e) }" },
1947 |         new String[] { "var foo = {bar: function(e){}};" },
1948 |         warnings
1949 |     );
1950 |   }
```
