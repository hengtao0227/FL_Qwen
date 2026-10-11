# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testCascadedRemovalOfUnlessUnconditonalJumps()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testCascadedRemovalOfUnlessUnconditonalJumps()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
234 |   public void testCascadedRemovalOfUnlessUnconditonalJumps() {
235 |     test("switch (a) { case 'a': break; case 'b': break; case 'c': break }",
236 |          "switch (a) { case 'a': break; case 'b': case 'c': }");
237 |     // Only one break removed per pass.
238 |     test("switch (a) { case 'a': break; case 'b': case 'c': }",
239 |          "switch (a) { case 'a': case 'b': case 'c': }");
240 | 
241 |     test("function foo() {" +
242 |       "  switch (a) { case 'a':return; case 'b':return; case 'c':return }}",
243 |       "function foo() { switch (a) { case 'a':return; case 'b': case 'c': }}");
244 |     test("function foo() {" +
245 |       "  switch (a) { case 'a':return; case 'b': case 'c': }}",
246 |       "function foo() { switch (a) { case 'a': case 'b': case 'c': }}");
247 | 
248 |     testSame("function foo() {" +
249 |              "switch (a) { case 'a':return 2; case 'b':return 1}}");
250 |   }
```

## com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue311()
Resolved declaration: com.google.javascript.jscomp.UnreachableCodeEliminationTest.testIssue311()
Source: test/com/google/javascript/jscomp/UnreachableCodeEliminationTest.java

```java
252 |   public void testIssue311() {
253 |     test("function a(b) {\n" +
254 |          "  switch (b.v) {\n" +
255 |          "    case 'SWITCH':\n" +
256 |          "      if (b.i >= 0) {\n" +
257 |          "        return b.o;\n" +
258 |          "      } else {\n" +
259 |          "        return;\n" +
260 |          "      }\n" +
261 |          "      break;\n" +
262 |          "  }\n" +
263 |          "}",
264 |          "function a(b) {\n" +
265 |          "  switch (b.v) {\n" +
266 |          "    case 'SWITCH':\n" +
267 |          "      if (b.i >= 0) {\n" +
268 |          "        return b.o;\n" +
269 |          "      } else {\n" +
270 |          "      }\n" +
271 |          "  }\n" +
272 |          "}");
273 |   }
```
