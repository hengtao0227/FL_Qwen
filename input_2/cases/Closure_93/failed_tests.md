# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ProcessClosurePrimitivesTest.testProvideInIndependentModules4()
Resolved declaration: com.google.javascript.jscomp.ProcessClosurePrimitivesTest.testProvideInIndependentModules4()
Source: test/com/google/javascript/jscomp/ProcessClosurePrimitivesTest.java

```java
774 |   public void testProvideInIndependentModules4() {
775 |     // Regression test for bug 261:
776 |     // http://code.google.com/p/closure-compiler/issues/detail?id=261
777 |     test(
778 |         createModuleStar(
779 |             "goog.provide('apps');",
780 |             "goog.provide('apps.foo.bar.B');",
781 |             "goog.provide('apps.foo.bar.C');"),
782 |         new String[] {
783 |             "var apps = {};apps.foo = {};apps.foo.bar = {}",
784 |             "apps.foo.bar.B = {};",
785 |             "apps.foo.bar.C = {};",
786 |         });
787 |   }
```
