# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CheckAccessControlsTest.testNoPrivateAccessForProperties6()
Resolved declaration: com.google.javascript.jscomp.CheckAccessControlsTest.testNoPrivateAccessForProperties6()
Source: test/com/google/javascript/jscomp/CheckAccessControlsTest.java

```java
399 |   public void testNoPrivateAccessForProperties6() {
400 |     // Overriding a private property with a non-private property
401 |     // in a different file causes problems.
402 |     test(new String[] {
403 |       "/** @constructor */ function Foo() {} " +
404 |       "/** @private */ Foo.prototype.bar_ = function() {};",
405 |       "/** @constructor \n * @extends {Foo} */ " +
406 |       "function SubFoo() {};" +
407 |       "SubFoo.prototype.bar_ = function() {};"
408 |     }, null, BAD_PRIVATE_PROPERTY_ACCESS);
409 |   }
```

## com.google.javascript.jscomp.CheckAccessControlsTest.testNoPrivateAccessForProperties8()
Resolved declaration: com.google.javascript.jscomp.CheckAccessControlsTest.testNoPrivateAccessForProperties8()
Source: test/com/google/javascript/jscomp/CheckAccessControlsTest.java

```java
424 |   public void testNoPrivateAccessForProperties8() {
425 |     test(new String[] {
426 |       "/** @constructor */ function Foo() { /** @private */ this.bar_ = 3; }",
427 |       "/** @constructor \n * @extends {Foo} */ " +
428 |       "function SubFoo() { /** @private */ this.bar_ = 3; };"
429 |     }, null, PRIVATE_OVERRIDE);
430 |   }
```
