# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.parsing.ParserTest.testForEach()
Resolved declaration: com.google.javascript.jscomp.parsing.ParserTest.testForEach()
Source: test/com/google/javascript/jscomp/parsing/ParserTest.java

```java
961 |   public void testForEach() {
962 |     parseError(
963 |         "function f(stamp, status) {\n" +
964 |         "  for each ( var curTiming in this.timeLog.timings ) {\n" +
965 |         "    if ( curTiming.callId == stamp ) {\n" +
966 |         "      curTiming.flag = status;\n" +
967 |         "      break;\n" +
968 |         "    }\n" +
969 |         "  }\n" +
970 |         "};",
971 |         "unsupported language extension: for each");
972 |   }
```
