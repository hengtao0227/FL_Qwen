# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FunctionRewriterTest.testIssue538()
Resolved declaration: com.google.javascript.jscomp.FunctionRewriterTest.testIssue538()
Source: test/com/google/javascript/jscomp/FunctionRewriterTest.java

```java
165 |   public void testIssue538() {
166 |     checkCompilesToSame(      "/** @constructor */\n" +
167 |         "WebInspector.Setting = function() {}\n" +
168 |         "WebInspector.Setting.prototype = {\n" +
169 |         "    get name0(){return this._name;},\n" +
170 |         "    get name1(){return this._name;},\n" +
171 |         "    get name2(){return this._name;},\n" +
172 |         "    get name3(){return this._name;},\n" +
173 |         "    get name4(){return this._name;},\n" +
174 |         "    get name5(){return this._name;},\n" +
175 |         "    get name6(){return this._name;},\n" +
176 |         "    get name7(){return this._name;},\n" +
177 |         "    get name8(){return this._name;},\n" +
178 |         "    get name9(){return this._name;},\n" +
179 |         "}", 1);
180 |   }
```
