# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testLends10()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testLends10()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
8780 |   public void testLends10() throws Exception {
8781 |     testTypes(
8782 |         "function defineClass(x) { return function() {}; } " +
8783 |         "/** @constructor */" +
8784 |         "var Foo = defineClass(" +
8785 |         "    /** @lends {Foo.prototype} */ ({/** @type {number} */ bar: 1}));" +
8786 |         "/** @return {string} */ function f() { return (new Foo()).bar; }",
8787 |         "inconsistent return type\n" +
8788 |         "found   : number\n" +
8789 |         "required: string");
8790 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testLends11()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testLends11()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
8792 |   public void testLends11() throws Exception {
8793 |     testTypes(
8794 |         "function defineClass(x, y) { return function() {}; } " +
8795 |         "/** @constructor */" +
8796 |         "var Foo = function() {};" +
8797 |         "/** @return {*} */ Foo.prototype.bar = function() { return 3; };" +
8798 |         "/**\n" +
8799 |         " * @constructor\n" +
8800 |         " * @extends {Foo}\n" +
8801 |         " */\n" +
8802 |         "var SubFoo = defineClass(Foo, " +
8803 |         "    /** @lends {SubFoo.prototype} */ ({\n" +
8804 |         "      /** @return {number} */ bar: function() { return 3; }}));" +
8805 |         "/** @return {string} */ function f() { return (new SubFoo()).bar(); }",
8806 |         "inconsistent return type\n" +
8807 |         "found   : number\n" +
8808 |         "required: string");
8809 |   }
```
