# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testBadInterfaceExtendsNonExistentInterfaces()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testBadInterfaceExtendsNonExistentInterfaces()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
3771 |   public void testBadInterfaceExtendsNonExistentInterfaces() throws Exception {
3772 |     String js = "/** @interface \n" +
3773 |         " * @extends {nonExistent1} \n" +
3774 |         " * @extends {nonExistent2} \n" +
3775 |         " */function A() {}";
3776 |     String[] expectedWarnings = {
3777 |       "Bad type annotation. Unknown type nonExistent1",
3778 |       "Bad type annotation. Unknown type nonExistent2"
3779 |     };
3780 |     testTypes(js, expectedWarnings);
3781 |   }
```
