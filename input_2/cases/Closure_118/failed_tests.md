# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.DisambiguatePropertiesTest.testOneType4()
Resolved declaration: com.google.javascript.jscomp.DisambiguatePropertiesTest.testOneType4()
Source: test/com/google/javascript/jscomp/DisambiguatePropertiesTest.java

```java
120 |   public void testOneType4() {
121 |     String js = ""
122 |         + "/** @constructor */ function Foo() {}\n"
123 |         + "Foo.prototype = {'a': 0};\n"
124 |         + "/** @type Foo */\n"
125 |         + "var F = new Foo;\n"
126 |         + "F['a'] = 0;";
127 |     String expected = "{}";
128 |     testSets(false, js, js, expected);
129 |     testSets(true, js, js, expected);
130 |   }
```

## com.google.javascript.jscomp.DisambiguatePropertiesTest.testTwoTypes4()
Resolved declaration: com.google.javascript.jscomp.DisambiguatePropertiesTest.testTwoTypes4()
Source: test/com/google/javascript/jscomp/DisambiguatePropertiesTest.java

```java
235 |   public void testTwoTypes4() {
236 |     String js = ""
237 |         + "/** @constructor */ function Foo() {}\n"
238 |         + "Foo.prototype = {a: 0};"
239 |         + "/** @type Foo */\n"
240 |         + "var F = new Foo;\n"
241 |         + "F.a = 0;"
242 |         + "/** @constructor */ function Bar() {}\n"
243 |         + "Bar.prototype = {'a': 0};"
244 |         + "/** @type Bar */\n"
245 |         + "var B = new Bar;\n"
246 |         + "B['a'] = 0;";
247 | 
248 |     String output = ""
249 |         + "function Foo(){}"
250 |         + "Foo.prototype = {a: 0};"
251 |         + "var F=new Foo;"
252 |         + "F.a=0;"
253 |         + "function Bar(){}"
254 |         + "Bar.prototype = {'a': 0};"
255 |         + "var B=new Bar;"
256 |         + "B['a']=0";
257 | 
258 |     testSets(false, js, output, "{a=[[Foo.prototype]]}");
259 |     testSets(true, js, output, "{a=[[Foo.prototype]]}");
260 |   }
```
