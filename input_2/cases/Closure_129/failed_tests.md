# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testIssue937()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIssue937()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
2418 |   public void testIssue937() {
2419 |     CompilerOptions options = createCompilerOptions();
2420 |     CompilationLevel level = CompilationLevel.SIMPLE_OPTIMIZATIONS;
2421 |     level.setOptionsForCompilationLevel(options);
2422 |     WarningLevel warnings = WarningLevel.DEFAULT;
2423 |     warnings.setOptionsForWarningLevel(options);
2424 | 
2425 |     String code = "" +
2426 |         "console.log(" +
2427 |             "/** @type {function():!string} */ ((new x())['abc'])() );";
2428 |     String result = "" +
2429 |         "console.log((new x()).abc());";
2430 |     test(options, code, result);
2431 |   }
```
