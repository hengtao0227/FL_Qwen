# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testImplementsExtendsLoop()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testImplementsExtendsLoop()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
9231 |   public void testImplementsExtendsLoop() throws Exception {
9232 |     testClosureTypesMultipleWarnings(
9233 |         suppressMissingProperty("foo") +
9234 |             "/** @constructor \n * @implements {F} */var G = function() {};" +
9235 |             "/** @constructor \n * @extends {G} */var F = function() {};" +
9236 |         "alert((new F).foo);",
9237 |         Lists.newArrayList(
9238 |             "Parse error. Cycle detected in inheritance chain of type F"));
9239 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testImplementsLoop()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testImplementsLoop()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
9222 |   public void testImplementsLoop() throws Exception {
9223 |     testClosureTypesMultipleWarnings(
9224 |         suppressMissingProperty("foo") +
9225 |         "/** @constructor \n * @implements {T} */var T = function() {};" +
9226 |         "alert((new T).foo);",
9227 |         Lists.newArrayList(
9228 |             "Parse error. Cycle detected in inheritance chain of type T"));
9229 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testConversionFromInterfaceToRecursiveConstructor()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testConversionFromInterfaceToRecursiveConstructor()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
9252 |   public void testConversionFromInterfaceToRecursiveConstructor()
9253 |       throws Exception {
9254 |     testClosureTypesMultipleWarnings(
9255 |         suppressMissingProperty("foo") +
9256 |             "/** @interface */ var OtherType = function() {}\n" +
9257 |             "/** @implements {MyType} \n * @constructor */\n" +
9258 |             "var MyType = function() {}\n" +
9259 |             "/** @type {MyType} */\n" +
9260 |             "var x = /** @type {!OtherType} */ (new Object());",
9261 |         Lists.newArrayList(
9262 |             "Parse error. Cycle detected in inheritance chain of type MyType",
9263 |             "initializing variable\n" +
9264 |             "found   : OtherType\n" +
9265 |             "required: (MyType|null)"));
9266 |   }
```
