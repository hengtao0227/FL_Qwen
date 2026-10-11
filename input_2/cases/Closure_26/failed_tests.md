# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testTransformAMDAndProcessCJS()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testTransformAMDAndProcessCJS()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
1052 |   public void testTransformAMDAndProcessCJS() {
1053 |     args.add("--transform_amd_modules");
1054 |     args.add("--process_common_js_modules");
1055 |     args.add("--common_js_entry_module=foo/bar");
1056 |     setFilename(0, "foo/bar.js");
1057 |     test("define({foo: 1})",
1058 |         "var module$foo$bar={}, module$foo$bar={foo:1};");
1059 |   }
```

## com.google.javascript.jscomp.CommandLineRunnerTest.testProcessCJS()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testProcessCJS()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
1044 |   public void testProcessCJS() {
1045 |     args.add("--process_common_js_modules");
1046 |     args.add("--common_js_entry_module=foo/bar");
1047 |     setFilename(0, "foo/bar.js");
1048 |     test("exports.test = 1",
1049 |         "var module$foo$bar={test:1};");
1050 |   }
```

## com.google.javascript.jscomp.ProcessCommonJSModulesTest.testExports()
Resolved declaration: com.google.javascript.jscomp.ProcessCommonJSModulesTest.testExports()
Source: test/com/google/javascript/jscomp/ProcessCommonJSModulesTest.java

```java
58 |   public void testExports() {
59 |     setFilename("test");
60 |     test(
61 |         "var name = require('name');" +
62 |         "exports.foo = 1;",
63 |         "goog.provide('module$test');" +
64 |         "var module$test = {};" +
65 |         "goog.require('module$name');" +
66 |         "var name$$module$test = module$name;" +
67 |         "module$test.foo = 1;");
68 |     test(
69 |         "var name = require('name');" +
70 |         "module.exports = function() {};",
71 |         "goog.provide('module$test');" +
72 |         "var module$test = {};" +
73 |         "goog.require('module$name');" +
74 |         "var name$$module$test = module$name;" +
75 |         "module$test.module$exports = function() {};" +
76 |         "if(module$test.module$exports)" +
77 |         "module$test=module$test.module$exports");
78 |   }
```

## com.google.javascript.jscomp.ProcessCommonJSModulesTest.testModuleName()
Resolved declaration: com.google.javascript.jscomp.ProcessCommonJSModulesTest.testModuleName()
Source: test/com/google/javascript/jscomp/ProcessCommonJSModulesTest.java

```java
102 |   public void testModuleName() {
103 |     assertEquals("module$foo$baz",
104 |         ProcessCommonJSModules.toModuleName("./baz.js", "foo/bar.js"));
105 |     assertEquals("module$foo$baz_bar",
106 |         ProcessCommonJSModules.toModuleName("./baz-bar.js", "foo/bar.js"));
107 |     assertEquals("module$baz",
108 |         ProcessCommonJSModules.toModuleName("../baz.js", "foo/bar.js"));
109 |     assertEquals("module$baz",
110 |         ProcessCommonJSModules.toModuleName("../../baz.js", "foo/bar/abc.js"));
111 |     assertEquals("module$baz", ProcessCommonJSModules.toModuleName(
112 |         "../../../baz.js", "foo/bar/abc/xyz.js"));
113 |     setFilename("foo/bar");
114 |     test(
115 |         "var name = require('name');",
116 |         "goog.provide('module$foo$bar'); var module$foo$bar = {};" +
117 |         "goog.require('module$name');" +
118 |         "var name$$module$foo$bar = module$name;");
119 |     test(
120 |         "var name = require('./name');",
121 |         "goog.provide('module$foo$bar');" +
122 |         "var module$foo$bar = {};" +
123 |         "goog.require('module$foo$name');" +
124 |         "var name$$module$foo$bar = module$foo$name;");
125 | 
126 |   }
```

## com.google.javascript.jscomp.ProcessCommonJSModulesTest.testDash()
Resolved declaration: com.google.javascript.jscomp.ProcessCommonJSModulesTest.testDash()
Source: test/com/google/javascript/jscomp/ProcessCommonJSModulesTest.java

```java
91 |   public void testDash() {
92 |     setFilename("test-test");
93 |     test(
94 |         "var name = require('name'); exports.foo = 1;",
95 |         "goog.provide('module$test_test');" +
96 |         "var module$test_test = {};" +
97 |         "goog.require('module$name');" +
98 |         "var name$$module$test_test = module$name;" +
99 |         "module$test_test.foo = 1;");
100 |   }
```

## com.google.javascript.jscomp.ProcessCommonJSModulesTest.testVarRenaming()
Resolved declaration: com.google.javascript.jscomp.ProcessCommonJSModulesTest.testVarRenaming()
Source: test/com/google/javascript/jscomp/ProcessCommonJSModulesTest.java

```java
80 |   public void testVarRenaming() {
81 |     setFilename("test");
82 |     test(
83 |         "var a = 1, b = 2;" +
84 |         "(function() { var a; b = 4})()",
85 |         "goog.provide('module$test');" +
86 |         "var module$test = {};" +
87 |         "var a$$module$test = 1, b$$module$test = 2;" +
88 |         "(function() { var a; b$$module$test = 4})();");
89 |   }
```

## com.google.javascript.jscomp.ProcessCommonJSModulesTest.testWithoutExports()
Resolved declaration: com.google.javascript.jscomp.ProcessCommonJSModulesTest.testWithoutExports()
Source: test/com/google/javascript/jscomp/ProcessCommonJSModulesTest.java

```java
37 |   public void testWithoutExports() {
38 |     setFilename("test");
39 |     test(
40 |         "var name = require('name');" +
41 |         "name()",
42 |         "goog.provide('module$test');" +
43 |         "var module$test = {};" +
44 |         "goog.require('module$name');" +
45 |         "var name$$module$test = module$name;" +
46 |         "name$$module$test();");
47 |     setFilename("test/sub");
48 |     test(
49 |         "var name = require('mod/name');" +
50 |         "(function() { name(); })();",
51 |         "goog.provide('module$test$sub');" +
52 |         "var module$test$sub = {};" +
53 |         "goog.require('module$mod$name');" +
54 |         "var name$$module$test$sub = module$mod$name;" +
55 |         "(function() { name$$module$test$sub(); })();");
56 |   }
```
