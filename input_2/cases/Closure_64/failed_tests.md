# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testES5StrictUseStrictMultipleInputs()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testES5StrictUseStrictMultipleInputs()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
797 |   public void testES5StrictUseStrictMultipleInputs() {
798 |     args.add("--language_in=ECMASCRIPT5_STRICT");
799 |     Compiler compiler = compile(new String[] {"var x = f.function",
800 |         "var y = f.function", "var z = f.function"});
801 |     String outputSource = compiler.toSource();
802 |     assertEquals("'use strict'", outputSource.substring(0, 12));
803 |     assertEquals(outputSource.substring(13).indexOf("'use strict'"), -1);
804 |   }
```
