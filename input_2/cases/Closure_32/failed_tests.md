# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testIssue701()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIssue701()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
1660 |   public void testIssue701() {
1661 |     // Check ASCII art in license comments.
1662 |     String ascii = "/**\n" +
1663 |         " * @preserve\n" +
1664 |         "   This\n" +
1665 |         "     is\n" +
1666 |         "       ASCII    ART\n" +
1667 |         "*/";
1668 |     String result = "/*\n\n" +
1669 |         "   This\n" +
1670 |         "     is\n" +
1671 |         "       ASCII    ART\n" +
1672 |         "*/\n";
1673 |     testSame(createCompilerOptions(), ascii);
1674 |     assertEquals(result, lastCompiler.toSource());
1675 |   }
```

## com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testParseLicense()
Resolved declaration: com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testParseLicense()
Source: test/com/google/javascript/jscomp/parsing/JsDocInfoParserTest.java

```java
1281 |   public void testParseLicense() throws Exception {
1282 |     Node node = new Node(1);
1283 |     this.fileLevelJsDocBuilder = node.getJsDocBuilderForNode();
1284 |     String comment = "@license Foo\nBar\n\nBaz*/";
1285 |     parse(comment);
1286 |     assertEquals(" Foo\nBar\n\nBaz", node.getJSDocInfo().getLicense());
1287 |   }
```

## com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testParsePreserve()
Resolved declaration: com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testParsePreserve()
Source: test/com/google/javascript/jscomp/parsing/JsDocInfoParserTest.java

```java
1273 |   public void testParsePreserve() throws Exception {
1274 |     Node node = new Node(1);
1275 |     this.fileLevelJsDocBuilder = node.getJsDocBuilderForNode();
1276 |     String comment = "@preserve Foo\nBar\n\nBaz*/";
1277 |     parse(comment);
1278 |     assertEquals(" Foo\nBar\n\nBaz", node.getJSDocInfo().getLicense());
1279 |   }
```

## com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testParseLicenseAscii()
Resolved declaration: com.google.javascript.jscomp.parsing.JsDocInfoParserTest.testParseLicenseAscii()
Source: test/com/google/javascript/jscomp/parsing/JsDocInfoParserTest.java

```java
1289 |   public void testParseLicenseAscii() throws Exception {
1290 |     Node node = new Node(1);
1291 |     this.fileLevelJsDocBuilder = node.getJsDocBuilderForNode();
1292 |     String comment = "@license Foo\n *   Bar\n\n  Baz*/";
1293 |     parse(comment);
1294 |     assertEquals(" Foo\n   Bar\n\n  Baz", node.getJSDocInfo().getLicense());
1295 |   }
```
