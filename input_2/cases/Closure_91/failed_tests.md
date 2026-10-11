# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckGlobalThisTest.testLendsAnnotation3()
Resolved declaration: com.google.javascript.jscomp.CheckGlobalThisTest.testLendsAnnotation3()
Source: test/com/google/javascript/jscomp/CheckGlobalThisTest.java

```java
235 |   public void testLendsAnnotation3() {
236 |     testSame("/** @constructor */ function F() {}" +
237 |         "dojo.declare(F, /** @lends {F.prototype} */ (" +
238 |         "    {foo: function() { return this.foo; }}));");
239 |   }
```
