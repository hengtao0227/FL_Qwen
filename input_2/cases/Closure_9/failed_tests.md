# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ProcessCommonJSModulesTest.testGuessModuleName()
Resolved declaration: com.google.javascript.jscomp.ProcessCommonJSModulesTest.testGuessModuleName()
Source: test/com/google/javascript/jscomp/ProcessCommonJSModulesTest.java

```java
128 |   public void testGuessModuleName() {
129 |     ProcessCommonJSModules pass = new ProcessCommonJSModules(null, "foo");
130 |     assertEquals("module$baz",
131 |         pass.guessCJSModuleName("foo/baz.js"));
132 |     assertEquals("module$baz",
133 |         pass.guessCJSModuleName("foo\\baz.js"));
134 |     assertEquals("module$bar$baz",
135 |         pass.guessCJSModuleName("foo\\bar\\baz.js"));
136 |   }
```
