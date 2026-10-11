# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testGetprop4()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testGetprop4()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
3926 |   public void testGetprop4() throws Exception {
3927 |     testTypes("var x = null; x.prop = 3;",
3928 |         "No properties on this expression\n" +
3929 |         "found   : null\n" +
3930 |         "required: Object");
3931 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testIssue810()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue810()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
6185 |   public void testIssue810() throws Exception {
6186 |     testTypes(
6187 |         "/** @constructor */" +
6188 |         "var Type = function () {" +
6189 |         "};" +
6190 |         "Type.prototype.doIt = function(obj) {" +
6191 |         "  this.prop = obj.unknownProp;" +
6192 |         "};",
6193 |         "Property unknownProp never defined on obj");
6194 |   }
```
