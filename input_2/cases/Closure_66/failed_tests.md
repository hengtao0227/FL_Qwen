# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testGetTypedPercent5()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testGetTypedPercent5()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
7782 |   public void testGetTypedPercent5() throws Exception {
7783 |     String js = "/** @enum {number} */ keys = {A: 1,B: 2,C: 3};";
7784 |     assertEquals(100.0, getTypedPercent(js), 0.1);
7785 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testGetTypedPercent6()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testGetTypedPercent6()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
7787 |   public void testGetTypedPercent6() throws Exception {
7788 |     String js = "a = {TRUE: 1, FALSE: 0};";
7789 |     assertEquals(100.0, getTypedPercent(js), 0.1);
7790 |   }
```
