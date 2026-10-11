# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.NodeUtilTest.testValidDefine()
Resolved declaration: com.google.javascript.jscomp.NodeUtilTest.testValidDefine()
Source: test/com/google/javascript/jscomp/NodeUtilTest.java

```java
1071 |   public void testValidDefine() {
1072 |     assertTrue(testValidDefineValue("1"));
1073 |     assertTrue(testValidDefineValue("-3"));
1074 |     assertTrue(testValidDefineValue("true"));
1075 |     assertTrue(testValidDefineValue("false"));
1076 |     assertTrue(testValidDefineValue("'foo'"));
1077 |     
1078 |     assertFalse(testValidDefineValue("x"));
1079 |     assertFalse(testValidDefineValue("null"));
1080 |     assertFalse(testValidDefineValue("undefined"));
1081 |     assertFalse(testValidDefineValue("NaN"));
1082 |     
1083 |     assertTrue(testValidDefineValue("!true"));
1084 |     assertTrue(testValidDefineValue("-true"));
1085 |     assertTrue(testValidDefineValue("1 & 8"));
1086 |     assertTrue(testValidDefineValue("1 + 8"));
1087 |     assertTrue(testValidDefineValue("'a' + 'b'"));
1088 | 
1089 |     assertFalse(testValidDefineValue("1 & foo"));
1090 |   }
```

## com.google.javascript.jscomp.ProcessDefinesTest.testOverridingString1()
Resolved declaration: com.google.javascript.jscomp.ProcessDefinesTest.testOverridingString1()
Source: test/com/google/javascript/jscomp/ProcessDefinesTest.java

```java
146 |   public void testOverridingString1() {
147 |     test(
148 |         "/** @define {string} */ var DEF_OVERRIDE_STRING = 'x' + 'y';",
149 |         "var DEF_OVERRIDE_STRING=\"x\" + \"y\"");
150 |   }  
```

## com.google.javascript.jscomp.ProcessDefinesTest.testOverridingString3()
Resolved declaration: com.google.javascript.jscomp.ProcessDefinesTest.testOverridingString3()
Source: test/com/google/javascript/jscomp/ProcessDefinesTest.java

```java
159 |   public void testOverridingString3() {
160 |     overrides.put("DEF_OVERRIDE_STRING", Node.newString("foo"));
161 |     test(
162 |         "/** @define {string} */ var DEF_OVERRIDE_STRING = 'x' + 'y';",
163 |         "var DEF_OVERRIDE_STRING=\"foo\"");
164 |   }
```
