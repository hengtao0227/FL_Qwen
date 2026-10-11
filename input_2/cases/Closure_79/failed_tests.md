# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.NormalizeTest.testIssue()
Resolved declaration: com.google.javascript.jscomp.NormalizeTest.testIssue()
Source: test/com/google/javascript/jscomp/NormalizeTest.java

```java
384 |   public void testIssue() {
385 |     super.allowExternsChanges(true);
386 |     test("var a,b,c; var a,b", "a(), b()", "a(), b()", null, null);
387 |   }
```

## com.google.javascript.jscomp.VarCheckTest.testPropReferenceInExterns1()
Resolved declaration: com.google.javascript.jscomp.VarCheckTest.testPropReferenceInExterns1()
Source: test/com/google/javascript/jscomp/VarCheckTest.java

```java
140 |   public void testPropReferenceInExterns1() {
141 |     testSame("asdf.foo;", "var asdf;",
142 |         VarCheck.UNDEFINED_EXTERN_VAR_ERROR);
143 |   }
```

## com.google.javascript.jscomp.VarCheckTest.testPropReferenceInExterns3()
Resolved declaration: com.google.javascript.jscomp.VarCheckTest.testPropReferenceInExterns3()
Source: test/com/google/javascript/jscomp/VarCheckTest.java

```java
150 |   public void testPropReferenceInExterns3() {
151 |     testSame("asdf.foo;", "var asdf;",
152 |         VarCheck.UNDEFINED_EXTERN_VAR_ERROR);
153 | 
154 |     externValidationErrorLevel = CheckLevel.ERROR;
155 |     test(
156 |         "asdf.foo;", "var asdf;", "",
157 |          VarCheck.UNDEFINED_EXTERN_VAR_ERROR, null);
158 | 
159 |     externValidationErrorLevel = CheckLevel.OFF;
160 |     test("asdf.foo;", "var asdf;", "var asdf;", null, null);
161 |   }
```

## com.google.javascript.jscomp.VarCheckTest.testVarReferenceInExterns()
Resolved declaration: com.google.javascript.jscomp.VarCheckTest.testVarReferenceInExterns()
Source: test/com/google/javascript/jscomp/VarCheckTest.java

```java
130 |   public void testVarReferenceInExterns() {
131 |     testSame("asdf;", "var asdf;",
132 |         VarCheck.NAME_REFERENCE_IN_EXTERNS_ERROR);
133 |   }
```

## com.google.javascript.jscomp.VarCheckTest.testCallInExterns()
Resolved declaration: com.google.javascript.jscomp.VarCheckTest.testCallInExterns()
Source: test/com/google/javascript/jscomp/VarCheckTest.java

```java
135 |   public void testCallInExterns() {
136 |     testSame("yz();", "function yz() {}",
137 |         VarCheck.NAME_REFERENCE_IN_EXTERNS_ERROR);
138 |   }
```
