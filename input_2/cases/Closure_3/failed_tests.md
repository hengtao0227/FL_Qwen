# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testDoNotInlineCatchExpression1a()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testDoNotInlineCatchExpression1a()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
156 |   public void testDoNotInlineCatchExpression1a() {
157 |     noInline(
158 |         "var a;\n" +
159 |         "try {\n" +
160 |         "  throw Error(\"\");\n" +
161 |         "}catch(err) {" +
162 |         "   a = err + 1;\n" +
163 |         "}\n" +
164 |         "return a.stack\n");
165 |   }
```

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testDoNotInlineCatchExpression1()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testDoNotInlineCatchExpression1()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
145 |   public void testDoNotInlineCatchExpression1() {
146 |     noInline(
147 |         "var a;\n" +
148 |         "try {\n" +
149 |         "  throw Error(\"\");\n" +
150 |         "}catch(err) {" +
151 |         "   a = err;\n" +
152 |         "}\n" +
153 |         "return a.stack\n");
154 |   }
```

## com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testDoNotInlineCatchExpression3()
Resolved declaration: com.google.javascript.jscomp.FlowSensitiveInlineVariablesTest.testDoNotInlineCatchExpression3()
Source: test/com/google/javascript/jscomp/FlowSensitiveInlineVariablesTest.java

```java
178 |   public void testDoNotInlineCatchExpression3() {
179 |     noInline(
180 |         "var a;\n" +
181 |         "try {\n" +
182 |         "  throw Error(\"\");\n" +
183 |         "} catch(err) {" +
184 |         "  err = x;\n" +
185 |         "  a = err;\n" +
186 |         "}\n" +
187 |         "return a.stack\n");
188 |   }
```
