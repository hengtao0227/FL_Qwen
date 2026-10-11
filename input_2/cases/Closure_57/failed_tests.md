# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ClosureCodingConventionTest.testRequire()
Resolved declaration: com.google.javascript.jscomp.ClosureCodingConventionTest.testRequire()
Source: test/com/google/javascript/jscomp/ClosureCodingConventionTest.java

```java
194 |   public void testRequire() {
195 |     assertRequire("goog.require('foo')");
196 |     assertNotRequire("goog.require(foo)");
197 |     assertNotRequire("goog.require()");
198 |     assertNotRequire("foo()");
199 |   }
```
