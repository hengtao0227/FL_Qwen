# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testParseSourceMetaMap()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testParseSourceMetaMap()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
422 |   public void testParseSourceMetaMap() throws Exception {
423 |     final String INPUT1 = "file1";
424 |     final String INPUT2 = "file2";
425 |     LinkedHashMap<String, String> inputs = Maps.newLinkedHashMap();
426 |     inputs.put(INPUT1, "var __FOO__ = 1;");
427 |     inputs.put(INPUT2, "var __BAR__ = 2;");
428 |     RunResult result1 = compile(inputs.get(INPUT1), INPUT1);
429 |     RunResult result2 = compile(inputs.get(INPUT2), INPUT2);
430 | 
431 |     final String MAP1 = "map1";
432 |     final String MAP2 = "map2";
433 |     final LinkedHashMap<String, String> maps = Maps.newLinkedHashMap();
434 |     maps.put(MAP1, result1.sourceMapFileContent);
435 |     maps.put(MAP2, result2.sourceMapFileContent);
436 | 
437 |     List<SourceMapSection> sections = Lists.newArrayList();
438 | 
439 |     StringBuilder output = new StringBuilder();
440 |     FilePosition offset = appendAndCount(output, result1.generatedSource);
441 |     sections.add(SourceMapSection.forURL(MAP1, 0, 0));
442 |     output.append(result2.generatedSource);
443 |     sections.add(
444 |         SourceMapSection.forURL(MAP2, offset.getLine(), offset.getColumn()));
445 | 
446 |     SourceMapGeneratorV3 generator = new SourceMapGeneratorV3();
447 |     StringBuilder mapContents = new StringBuilder();
448 |     generator.appendIndexMapTo(mapContents, "out.js", sections);
449 | 
450 |     check(inputs, output.toString(), mapContents.toString(),
451 |       new SourceMapSupplier() {
452 |         @Override
453 |         public String getSourceMap(String url){
454 |           return maps.get(url);
455 |       }});
456 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput0a()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput0a()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
132 |   public void testGoldenOutput0a() throws Exception {
133 |     // Empty source map test
134 |     checkSourceMap("a;",
135 | 
136 |                    "{\n" +
137 |                    "\"version\":3,\n" +
138 |                    "\"file\":\"testcode\",\n" +
139 |                    "\"lineCount\":1,\n" +
140 |                    "\"mappings\":\"AAAAA;\",\n" +
141 |                    "\"sources\":[\"testcode\"],\n" +
142 |                    "\"names\":[\"a\"]\n" +
143 |                    "}\n");
144 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testMultilineMapping()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testMultilineMapping()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
92 |   public void testMultilineMapping() throws Exception {
93 |     compileAndCheck("function __BASIC__(__PARAM1__, __PARAM2__) {\n" +
94 |                     "var __VAR__ = '__STR__';\n" +
95 |                     "var __ANO__ = \"__STR2__\";\n" +
96 |                     "}");
97 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testMultiFunctionMapping()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testMultiFunctionMapping()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
106 |   public void testMultiFunctionMapping() throws Exception {
107 |     compileAndCheck("function __BASIC__(__PARAM1__, __PARAM2__) {\n" +
108 |                     "var __VAR__ = '__STR__';\n" +
109 |                     "var __ANO__ = \"__STR2__\";\n" +
110 |                     "}\n" +
111 | 
112 |                     "function __BASIC2__(__PARAM3__, __PARAM4__) {\n" +
113 |                     "var __VAR2__ = '__STR2__';\n" +
114 |                     "var __ANO2__ = \"__STR3__\";\n" +
115 |                     "}\n");
116 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testLiteralMappingsGoldenOutput()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testLiteralMappingsGoldenOutput()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
75 |   public void testLiteralMappingsGoldenOutput() throws Exception {
76 |     // Empty source map test
77 |     checkSourceMap("function __BASIC__(__PARAM1__, __PARAM2__) { " +
78 |                    "var __VAR__ = '__STR__'; }",
79 | 
80 |                    "{\n" +
81 |                    "\"version\":3,\n" +
82 |                    "\"file\":\"testcode\",\n" +
83 |                    "\"lineCount\":1,\n" +
84 |                    "\"mappings\":\"AAAAA,QAASA,UAAS,CAACC,UAAD,CAAaC,UAAb," +
85 |                        "CAAyB,CAAE,IAAIC,QAAU,SAAhB;\",\n" +
86 |                    "\"sources\":[\"testcode\"],\n" +
87 |                    "\"names\":[\"__BASIC__\",\"__PARAM1__\",\"__PARAM2__\"," +
88 |                        "\"__VAR__\"]\n" +
89 |                    "}\n");
90 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testMultilineMapping2()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testMultilineMapping2()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
99 |   public void testMultilineMapping2() throws Exception {
100 |     compileAndCheck("function __BASIC__(__PARAM1__, __PARAM2__) {\n" +
101 |                     "var __VAR__ = 1;\n" +
102 |                     "var __ANO__ = 2;\n" +
103 |                     "}");
104 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testBasicMappingGoldenOutput()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testBasicMappingGoldenOutput()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
52 |   public void testBasicMappingGoldenOutput() throws Exception {
53 |     // Empty source map test
54 |     checkSourceMap("function __BASIC__() { }",
55 | 
56 |                    "{\n" +
57 |                    "\"version\":3,\n" +
58 |                    "\"file\":\"testcode\",\n" +
59 |                    "\"lineCount\":1,\n" +
60 |                    "\"mappings\":\"AAAAA,QAASA,UAAS,EAAG;\",\n" +
61 |                    "\"sources\":[\"testcode\"],\n" +
62 |                    "\"names\":[\"__BASIC__\"]\n" +
63 |                    "}\n");
64 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testSourceMapMerging()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testSourceMapMerging()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
458 |   public void testSourceMapMerging() throws Exception {
459 |     final String INPUT1 = "file1";
460 |     final String INPUT2 = "file2";
461 |     LinkedHashMap<String, String> inputs = Maps.newLinkedHashMap();
462 |     inputs.put(INPUT1, "var __FOO__ = 1;");
463 |     inputs.put(INPUT2, "var __BAR__ = 2;");
464 |     RunResult result1 = compile(inputs.get(INPUT1), INPUT1);
465 |     RunResult result2 = compile(inputs.get(INPUT2), INPUT2);
466 | 
467 |     StringBuilder output = new StringBuilder();
468 |     FilePosition offset = appendAndCount(output, result1.generatedSource);
469 |     output.append(result2.generatedSource);
470 | 
471 |     SourceMapGeneratorV3 generator = new SourceMapGeneratorV3();
472 | 
473 |     generator.mergeMapSection(0, 0, result1.sourceMapFileContent);
474 |     generator.mergeMapSection(offset.getLine(), offset.getColumn(),
475 |         result2.sourceMapFileContent);
476 | 
477 |     StringBuilder mapContents = new StringBuilder();
478 |     generator.appendTo(mapContents, "out.js");
479 | 
480 |     check(inputs, output.toString(), mapContents.toString());
481 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testLiteralMappings()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testLiteralMappings()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
70 |   public void testLiteralMappings() throws Exception {
71 |     compileAndCheck("function __BASIC__(__PARAM1__, __PARAM2__) { " +
72 |                     "var __VAR__ = '__STR__'; }");
73 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testBasicMapping1()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testBasicMapping1()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
48 |   public void testBasicMapping1() throws Exception {
49 |     compileAndCheck("function __BASIC__() { }");
50 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testBasicMapping2()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testBasicMapping2()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
66 |   public void testBasicMapping2() throws Exception {
67 |     compileAndCheck("function __BASIC__(__PARAM1__) {}");
68 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput1()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput1()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
146 |   public void testGoldenOutput1() throws Exception {
147 |     detailLevel = SourceMap.DetailLevel.ALL;
148 | 
149 |     checkSourceMap("function f(foo, bar) { foo = foo + bar + 2; return foo; }",
150 | 
151 |                    "{\n" +
152 |                    "\"version\":3,\n" +
153 |                    "\"file\":\"testcode\",\n" +
154 |                    "\"lineCount\":1,\n" +
155 |                    "\"mappings\":\"AAAAA,QAASA,EAAC,CAACC,GAAD,CAAMC,GAAN," +
156 |                        "CAAW,CAAED,GAAA,CAAMA,GAAN,CAAYC,GAAZ,CAAkB,CAAG," +
157 |                        "OAAOD,IAA9B;\",\n" +
158 |                    "\"sources\":[\"testcode\"],\n" +
159 |                    "\"names\":[\"f\",\"foo\",\"bar\"]\n" +
160 |                    "}\n");
161 | 
162 |     detailLevel = SourceMap.DetailLevel.SYMBOLS;
163 | 
164 |     checkSourceMap("function f(foo, bar) { foo = foo + bar + 2; return foo; }",
165 | 
166 |                    "{\n" +
167 |                    "\"version\":3,\n" +
168 |                    "\"file\":\"testcode\",\n" +
169 |                    "\"lineCount\":1,\n" +
170 |                    "\"mappings\":\"AAAAA,QAASA,EAATA,CAAWC,GAAXD,CAAgBE," +
171 |                        "GAAhBF,EAAuBC,GAAvBD,CAA6BC,GAA7BD,CAAmCE,GAAnCF," +
172 |                        "SAAmDC,IAAnDD;\",\n" +
173 |                    "\"sources\":[\"testcode\"],\n" +
174 |                    "\"names\":[\"f\",\"foo\",\"bar\"]\n" +
175 |                    "}\n");
176 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput2()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput2()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
178 |   public void testGoldenOutput2() throws Exception {
179 |     checkSourceMap("function f(foo, bar) {\r\n\n\n\nfoo = foo + bar + foo;" +
180 |                    "\nreturn foo;\n}",
181 | 
182 |                    "{\n" +
183 |                    "\"version\":3,\n" +
184 |                    "\"file\":\"testcode\",\n" +
185 |                    "\"lineCount\":1,\n" +
186 |                    "\"mappings\":\"AAAAA,QAASA,EAAC,CAACC,GAAD,CAAMC,GAAN," +
187 |                        "CAAW,CAIrBD,GAAA,CAAMA,GAAN,CAAYC,GAAZ,CAAkBD," +
188 |                        "GAClB,OAAOA,IALc;\",\n" +
189 |                    "\"sources\":[\"testcode\"],\n" +
190 |                    "\"names\":[\"f\",\"foo\",\"bar\"]\n" +
191 |                    "}\n");
192 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput3()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput3()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
194 |   public void testGoldenOutput3() throws Exception {
195 |     checkSourceMap("c:\\myfile.js",
196 |                    "foo;",
197 | 
198 |                    "{\n" +
199 |                    "\"version\":3,\n" +
200 |                    "\"file\":\"testcode\",\n" +
201 |                    "\"lineCount\":1,\n" +
202 |                    "\"mappings\":\"AAAAA;\",\n" +
203 |                    "\"sources\":[\"c:\\\\myfile.js\"],\n" +
204 |                    "\"names\":[\"foo\"]\n" +
205 |                    "}\n");
206 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput4()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput4()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
208 |   public void testGoldenOutput4() throws Exception {
209 |     checkSourceMap("c:\\myfile.js",
210 |                    "foo;   boo;   goo;",
211 | 
212 |                    "{\n" +
213 |                    "\"version\":3,\n" +
214 |                    "\"file\":\"testcode\",\n" +
215 |                    "\"lineCount\":1,\n" +
216 |                    "\"mappings\":\"AAAAA,GAAOC,IAAOC;\",\n" +
217 |                    "\"sources\":[\"c:\\\\myfile.js\"],\n" +
218 |                    "\"names\":[\"foo\",\"boo\",\"goo\"]\n" +
219 |                    "}\n");
220 |   }
```

## com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput5()
Resolved declaration: com.google.debugging.sourcemap.SourceMapGeneratorV3Test.testGoldenOutput5()
Source: test/com/google/debugging/sourcemap/SourceMapGeneratorV3Test.java

```java
222 |   public void testGoldenOutput5() throws Exception {
223 |     detailLevel = SourceMap.DetailLevel.ALL;
224 | 
225 |     checkSourceMap(
226 |         "c:\\myfile.js",
227 |         "/** @preserve\n" +
228 |         " * this is a test.\n" +
229 |         " */\n" +
230 |         "var foo=a + 'this is a really long line that will force the"
231 |         + " mapping to span multiple lines 123456789 123456789"
232 |         + " 123456789 123456789 123456789 123456789 123456789"
233 |         + " 123456789 123456789 123456789 123456789 123456789"
234 |         + " 123456789 123456789 123456789 123456789 123456789"
235 |         + " 123456789 123456789 123456789 123456789 123456789"
236 |         + " 123456789 123456789 123456789 123456789 123456789"
237 |         + " 123456789 123456789 123456789 123456789 123456789"
238 |         + " 123456789 123456789 123456789 123456789 123456789"
239 |         + " 123456789 123456789 123456789 123456789 123456789"
240 |         + " 123456789 123456789 123456789 123456789 123456789"
241 |         + " 123456789 123456789 123456789 123456789 123456789"
242 |         + " 123456789 123456789 123456789 123456789 123456789"
243 |         + " 123456789 123456789 123456789 123456789 123456789"
244 |         + " 123456789 123456789 123456789 123456789 123456789"
245 |         + " 123456789 123456789 123456789 123456789 123456789"
246 |         + " 123456789 123456789 123456789 123456789 123456789"
247 |         + " 123456789 123456789 123456789 123456789 123456789"
248 |         + " 123456789 123456789 123456789 123456789 123456789"
249 |         + " 123456789 123456789 123456789 123456789 123456789"
250 |         + " 123456789 123456789 123456789 123456789 123456789"
251 |         + " 123456789 123456789 123456789 123456789 123456789"
252 |         + " 123456789 123456789 123456789 123456789 123456789"
253 |         + " 123456789 123456789 123456789 123456789 123456789"
254 |         + " 123456789 123456789 123456789 123456789 123456789"
255 |         + " 123456789 123456789 123456789 123456789 123456789"
256 |         + "' + c + d + e;",
257 | 
258 |         "{\n" +
259 |         "\"version\":3,\n" +
260 |         "\"file\":\"testcode\",\n" +
261 |         "\"lineCount\":6,\n" +
262 |         "\"mappings\":\"A;;;;AAGA,IAAIA,IAAIC,CAAJD,CAAQ,mxCAARA;AAA8xCE," +
263 |             "CAA9xCF,CAAkyCG,CAAlyCH,CAAsyCI;\",\n" +
264 |         "\"sources\":[\"c:\\\\myfile.js\"],\n" +
265 |         "\"names\":[\"foo\",\"a\",\"c\",\"d\",\"e\"]\n" +
266 |         "}\n");
267 | 
268 |     detailLevel = SourceMap.DetailLevel.SYMBOLS;
269 | 
270 |     checkSourceMap("c:\\myfile.js",
271 |         "/** @preserve\n" +
272 |         " * this is a test.\n" +
273 |         " */\n" +
274 |         "var foo=a + 'this is a really long line that will force the"
275 |         + " mapping to span multiple lines 123456789 123456789"
276 |         + " 123456789 123456789 123456789 123456789 123456789"
277 |         + " 123456789 123456789 123456789 123456789 123456789"
278 |         + " 123456789 123456789 123456789 123456789 123456789"
279 |         + " 123456789 123456789 123456789 123456789 123456789"
280 |         + " 123456789 123456789 123456789 123456789 123456789"
281 |         + " 123456789 123456789 123456789 123456789 123456789"
282 |         + " 123456789 123456789 123456789 123456789 123456789"
283 |         + " 123456789 123456789 123456789 123456789 123456789"
284 |         + " 123456789 123456789 123456789 123456789 123456789"
285 |         + " 123456789 123456789 123456789 123456789 123456789"
286 |         + " 123456789 123456789 123456789 123456789 123456789"
287 |         + " 123456789 123456789 123456789 123456789 123456789"
288 |         + " 123456789 123456789 123456789 123456789 123456789"
289 |         + " 123456789 123456789 123456789 123456789 123456789"
290 |         + " 123456789 123456789 123456789 123456789 123456789"
291 |         + " 123456789 123456789 123456789 123456789 123456789"
292 |         + " 123456789 123456789 123456789 123456789 123456789"
293 |         + " 123456789 123456789 123456789 123456789 123456789"
294 |         + " 123456789 123456789 123456789 123456789 123456789"
295 |         + " 123456789 123456789 123456789 123456789 123456789"
296 |         + " 123456789 123456789 123456789 123456789 123456789"
297 |         + " 123456789 123456789 123456789 123456789 123456789"
298 |         + " 123456789 123456789 123456789 123456789 123456789"
299 |         + " 123456789 123456789 123456789 123456789 123456789"
300 |         + "' + c + d + e;",
301 | 
302 |         "{\n" +
303 |         "\"version\":3,\n" +
304 |         "\"file\":\"testcode\",\n" +
305 |         "\"lineCount\":6,\n" +
306 |         "\"mappings\":\"A;;;;IAGIA,IAAIC,CAAJD;AAA8xCE,CAA9xCF,CAAkyCG," +
307 |             "CAAlyCH,CAAsyCI;\",\n" +
308 |         "\"sources\":[\"c:\\\\myfile.js\"],\n" +
309 |         "\"names\":[\"foo\",\"a\",\"c\",\"d\",\"e\"]\n" +
310 |         "}\n");
311 |   }
```
