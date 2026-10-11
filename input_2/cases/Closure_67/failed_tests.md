# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.RemoveUnusedPrototypePropertiesTest.testAliasing7()
Resolved declaration: com.google.javascript.jscomp.RemoveUnusedPrototypePropertiesTest.testAliasing7()
Source: test/com/google/javascript/jscomp/RemoveUnusedPrototypePropertiesTest.java

```java
186 |   public void testAliasing7() {
187 |     // An exported alias must preserved any referenced values in the
188 |     // referenced function.
189 |     testSame("function e(){}" +
190 |            "e.prototype['alias1'] = e.prototype.method1 = " +
191 |                "function(){this.method2()};" +
192 |            "e.prototype.method2 = function(){};");
193 |   }
```
