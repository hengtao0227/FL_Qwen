# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testCheckGlobalThisOff()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testCheckGlobalThisOff()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
157 |   public void testCheckGlobalThisOff() {
158 |     args.add("--warning_level=VERBOSE");
159 |     args.add("--jscomp_off=globalThis");
160 |     testSame("function f() { this.a = 3; }");
161 |   }
```
