# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CompilerRunnerTest.testIssue115()
Resolved declaration: com.google.javascript.jscomp.CompilerRunnerTest.testIssue115()
Source: test/com/google/javascript/jscomp/CompilerRunnerTest.java

```java
175 |   public void testIssue115() {
176 |     CompilerRunner.FLAG_compilation_level.setForTest(
177 |         CompilationLevel.SIMPLE_OPTIMIZATIONS);
178 |     CompilerRunner.FLAG_warning_level.setForTest(
179 |         WarningLevel.VERBOSE);
180 |     test("function f() { " +
181 |          "  var arguments = Array.prototype.slice.call(arguments, 0);" +
182 |          "  return arguments[0]; " +
183 |          "}",
184 |          "function f() { " +
185 |          "  arguments = Array.prototype.slice.call(arguments, 0);" +
186 |          "  return arguments[0]; " +
187 |          "}");
188 |   }
```
