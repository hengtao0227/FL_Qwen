# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testDependencySorting()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testDependencySorting()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
2102 |   public void testDependencySorting() throws Exception {
2103 |     CompilerOptions options = createCompilerOptions();
2104 |     options.setDependencyOptions(
2105 |         new DependencyOptions()
2106 |         .setDependencySorting(true));
2107 |     test(
2108 |         options,
2109 |         new String[] {
2110 |           "goog.require('x');",
2111 |           "goog.provide('x');",
2112 |         },
2113 |         new String[] {
2114 |           "goog.provide('x');",
2115 |           "goog.require('x');",
2116 | 
2117 |           // For complicated reasons involving modules,
2118 |           // the compiler creates a synthetic source file.
2119 |           "",
2120 |         });
2121 |   }
```
