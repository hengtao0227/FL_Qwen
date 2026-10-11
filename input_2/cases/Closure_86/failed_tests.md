# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.NodeUtilTest.testLocalValue1()
Resolved declaration: com.google.javascript.jscomp.NodeUtilTest.testLocalValue1()
Source: test/com/google/javascript/jscomp/NodeUtilTest.java

```java
1014 |   public void testLocalValue1() throws Exception {
1015 |     // Names are not known to be local.
1016 |     assertFalse(testLocalValue("x"));
1017 |     assertFalse(testLocalValue("x()"));
1018 |     assertFalse(testLocalValue("this"));
1019 |     assertFalse(testLocalValue("arguments"));
1020 | 
1021 |     // We can't know if new objects are local unless we know
1022 |     // that they don't alias themselves.
1023 |     assertFalse(testLocalValue("new x()"));
1024 | 
1025 |     // property references are assume to be non-local
1026 |     assertFalse(testLocalValue("(new x()).y"));
1027 |     assertFalse(testLocalValue("(new x())['y']"));
1028 | 
1029 |     // Primitive values are local
1030 |     assertTrue(testLocalValue("null"));
1031 |     assertTrue(testLocalValue("undefined"));
1032 |     assertTrue(testLocalValue("Infinity"));
1033 |     assertTrue(testLocalValue("NaN"));
1034 |     assertTrue(testLocalValue("1"));
1035 |     assertTrue(testLocalValue("'a'"));
1036 |     assertTrue(testLocalValue("true"));
1037 |     assertTrue(testLocalValue("false"));
1038 |     assertTrue(testLocalValue("[]"));
1039 |     assertTrue(testLocalValue("{}"));
1040 | 
1041 |     // The contents of arrays and objects don't matter
1042 |     assertTrue(testLocalValue("[x]"));
1043 |     assertTrue(testLocalValue("{'a':x}"));
1044 | 
1045 |     // Pre-increment results in primitive number
1046 |     assertTrue(testLocalValue("++x"));
1047 |     assertTrue(testLocalValue("--x"));
1048 | 
1049 |     // Post-increment, the previous value matters.
1050 |     assertFalse(testLocalValue("x++"));
1051 |     assertFalse(testLocalValue("x--"));
1052 | 
1053 |     // The left side of an only assign matters if it is an alias or mutable.
1054 |     assertTrue(testLocalValue("x=1"));
1055 |     assertFalse(testLocalValue("x=[]"));
1056 |     assertFalse(testLocalValue("x=y"));
1057 |     // The right hand side of assignment opts don't matter, as they force
1058 |     // a local result.
1059 |     assertTrue(testLocalValue("x+=y"));
1060 |     assertTrue(testLocalValue("x*=y"));
1061 |     // Comparisons always result in locals, as they force a local boolean
1062 |     // result.
1063 |     assertTrue(testLocalValue("x==y"));
1064 |     assertTrue(testLocalValue("x!=y"));
1065 |     assertTrue(testLocalValue("x>y"));
1066 |     // Only the right side of a comma matters
1067 |     assertTrue(testLocalValue("(1,2)"));
1068 |     assertTrue(testLocalValue("(x,1)"));
1069 |     assertFalse(testLocalValue("(x,y)"));
1070 | 
1071 |     // Both the operands of OR matter
1072 |     assertTrue(testLocalValue("1||2"));
1073 |     assertFalse(testLocalValue("x||1"));
1074 |     assertFalse(testLocalValue("x||y"));
1075 |     assertFalse(testLocalValue("1||y"));
1076 | 
1077 |     // Both the operands of AND matter
1078 |     assertTrue(testLocalValue("1&&2"));
1079 |     assertFalse(testLocalValue("x&&1"));
1080 |     assertFalse(testLocalValue("x&&y"));
1081 |     assertFalse(testLocalValue("1&&y"));
1082 | 
1083 |     // Only the results of HOOK matter
1084 |     assertTrue(testLocalValue("x?1:2"));
1085 |     assertFalse(testLocalValue("x?x:2"));
1086 |     assertFalse(testLocalValue("x?1:x"));
1087 |     assertFalse(testLocalValue("x?x:y"));
1088 | 
1089 |     // Results of ops are local values
1090 |     assertTrue(testLocalValue("!y"));
1091 |     assertTrue(testLocalValue("~y"));
1092 |     assertTrue(testLocalValue("y + 1"));
1093 |     assertTrue(testLocalValue("y + z"));
1094 |     assertTrue(testLocalValue("y * z"));
1095 | 
1096 |     assertTrue(testLocalValue("'a' in x"));
1097 |     assertTrue(testLocalValue("typeof x"));
1098 |     assertTrue(testLocalValue("x instanceof y"));
1099 | 
1100 |     assertTrue(testLocalValue("void x"));
1101 |     assertTrue(testLocalValue("void 0"));
1102 | 
1103 |     assertFalse(testLocalValue("{}.x"));
1104 | 
1105 |     assertTrue(testLocalValue("{}.toString()"));
1106 |     assertTrue(testLocalValue("o.toString()"));
1107 | 
1108 |     assertFalse(testLocalValue("o.valueOf()"));
1109 |   }
```

## com.google.javascript.jscomp.PureFunctionIdentifierTest.testLocalizedSideEffects8()
Resolved declaration: com.google.javascript.jscomp.PureFunctionIdentifierTest.testLocalizedSideEffects8()
Source: test/com/google/javascript/jscomp/PureFunctionIdentifierTest.java

```java
769 |   public void testLocalizedSideEffects8() throws Exception {
770 |     // Returning a local object that has been modified
771 |     // is not a global side-effect.
772 |     checkMarkedCalls("/** @constructor A */ function A() {};" +
773 |                      "function f() {" +
774 |                      "  var a = new A; a.foo = 1; return a;" +
775 |                      "}" +
776 |                      "f()",
777 |                      BROKEN_NEW ?
778 |                          ImmutableList.<String>of("A") :
779 |                          ImmutableList.<String>of("A", "f"));
780 |   }
```

## com.google.javascript.jscomp.PureFunctionIdentifierTest.testLocalizedSideEffects9()
Resolved declaration: com.google.javascript.jscomp.PureFunctionIdentifierTest.testLocalizedSideEffects9()
Source: test/com/google/javascript/jscomp/PureFunctionIdentifierTest.java

```java
782 |   public void testLocalizedSideEffects9() throws Exception {
783 |     // Returning a local object that has been modified
784 |     // is not a global side-effect.
785 |     checkMarkedCalls("/** @constructor A */ function A() {this.x = 1};" +
786 |                      "function f() {" +
787 |                      "  var a = new A; a.foo = 1; return a;" +
788 |                      "}" +
789 |                      "f()",
790 |                      BROKEN_NEW ?
791 |                          ImmutableList.<String>of("A") :
792 |                          ImmutableList.<String>of("A", "f"));
793 |   }
```

## com.google.javascript.jscomp.PureFunctionIdentifierTest.testAnnotationInExterns_new4()
Resolved declaration: com.google.javascript.jscomp.PureFunctionIdentifierTest.testAnnotationInExterns_new4()
Source: test/com/google/javascript/jscomp/PureFunctionIdentifierTest.java

```java
237 |   public void testAnnotationInExterns_new4() throws Exception {
238 |     // The entire expression containing "externObjSEThisMethod" is considered
239 |     // side-effect free in this context.
240 | 
241 |     checkMarkedCalls("new externObjSEThis().externObjSEThisMethod('')",
242 |         BROKEN_NEW ?
243 |             ImmutableList.<String>of(
244 |                "externObjSEThis") :
245 |             ImmutableList.<String>of(
246 |                "externObjSEThis", "NEW STRING externObjSEThisMethod"));
247 |   }
```

## com.google.javascript.jscomp.PureFunctionIdentifierTest.testAnnotationInExterns_new6()
Resolved declaration: com.google.javascript.jscomp.PureFunctionIdentifierTest.testAnnotationInExterns_new6()
Source: test/com/google/javascript/jscomp/PureFunctionIdentifierTest.java

```java
256 |   public void testAnnotationInExterns_new6() throws Exception {
257 |     // While "externObjSEThisMethod" has modifies "this"
258 |     // it does not have global side-effects with "this" is
259 |     // a known local value.
260 |     checkMarkedCalls(
261 |         "function f() {" +
262 |         "  new externObjSEThis().externObjSEThisMethod('') " +
263 |         "};" +
264 |         "f();",
265 |         BROKEN_NEW ?
266 |             ImmutableList.<String>of(
267 |                 "externObjSEThis") :
268 |            ImmutableList.<String>of(
269 |                "externObjSEThis", "NEW STRING externObjSEThisMethod", "f"));
270 |   }
```

## com.google.javascript.jscomp.PureFunctionIdentifierTest.testIssue303b()
Resolved declaration: com.google.javascript.jscomp.PureFunctionIdentifierTest.testIssue303b()
Source: test/com/google/javascript/jscomp/PureFunctionIdentifierTest.java

```java
205 |   public void testIssue303b() throws Exception {
206 |     checkMarkedCalls(
207 |         "/** @constructor */ function F() {" +
208 |         "  var self = this;" +
209 |         "  window.setTimeout(function() {" +
210 |         "    window.location = self.location;" +
211 |         "  }, 0);" +
212 |         "}" +
213 |         "F.prototype.setLocation = function(x) {" +
214 |         "  this.location = x;" +
215 |         "};" +
216 |         "function x() {" +
217 |         "  (new F()).setLocation('http://www.google.com/');" +
218 |         "} window['x'] = x;",
219 |         ImmutableList.<String>of());
220 |   }
```

## com.google.javascript.jscomp.PureFunctionIdentifierTest.testIssue303()
Resolved declaration: com.google.javascript.jscomp.PureFunctionIdentifierTest.testIssue303()
Source: test/com/google/javascript/jscomp/PureFunctionIdentifierTest.java

```java
190 |   public void testIssue303() throws Exception {
191 |     checkMarkedCalls(
192 |         "/** @constructor */ function F() {" +
193 |         "  var self = this;" +
194 |         "  window.setTimeout(function() {" +
195 |         "    window.location = self.location;" +
196 |         "  }, 0);" +
197 |         "}" +
198 |         "F.prototype.setLocation = function(x) {" +
199 |         "  this.location = x;" +
200 |         "};" +
201 |         "(new F()).setLocation('http://www.google.com/');",
202 |         ImmutableList.<String>of());
203 |   }
```
