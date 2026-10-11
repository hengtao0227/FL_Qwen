# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testGetMsgWiringNoWarnings()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testGetMsgWiringNoWarnings()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
393 |   public void testGetMsgWiringNoWarnings() throws Exception {
394 |     args.add("--compilation_level=ADVANCED_OPTIMIZATIONS");
395 |     test("/** @desc A bad foo. */ var MSG_FOO = 1;", "");
396 |   }
```
