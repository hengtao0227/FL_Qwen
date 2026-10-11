# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testVersionFlag2()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testVersionFlag2()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
600 |   public void testVersionFlag2() {
601 |     lastArg = "--version";
602 |     testSame("");
603 |     assertEquals(
604 |         0,
605 |         new String(errReader.toByteArray()).indexOf(
606 |             "Closure Compiler (http://code.google.com/closure/compiler)\n" +
607 |             "Version: "));
608 |   }
```
