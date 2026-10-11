# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testThisTypeOfFunction2()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testThisTypeOfFunction2()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
4552 |   public void testThisTypeOfFunction2() throws Exception {
4553 |     testTypes(
4554 |         "/** @constructor */ function F() {}" +
4555 |         "/** @type {function(this:F)} */ function f() {}" +
4556 |         "f();",
4557 |         "\"function (this:F): ?\" must be called with a \"this\" type");
4558 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testThisTypeOfFunction3()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testThisTypeOfFunction3()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
4560 |   public void testThisTypeOfFunction3() throws Exception {
4561 |     testTypes(
4562 |         "/** @constructor */ function F() {}" +
4563 |         "F.prototype.bar = function() {};" +
4564 |         "var f = (new F()).bar; f();",
4565 |         "\"function (this:F): undefined\" must be called with a \"this\" type");
4566 |   }
```

## com.google.javascript.jscomp.TypeCheckTest.testThisTypeOfFunction4()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testThisTypeOfFunction4()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
4568 |   public void testThisTypeOfFunction4() throws Exception {
4569 |     testTypes(
4570 |         "/** @constructor */ function F() {}" +
4571 |         "F.prototype.moveTo = function(x, y) {};" +
4572 |         "F.prototype.lineTo = function(x, y) {};" +
4573 |         "function demo() {" +
4574 |         "  var path = new F();" +
4575 |         "  var points = [[1,1], [2,2]];" +
4576 |         "  for (var i = 0; i < points.length; i++) {" +
4577 |         "    (i == 0 ? path.moveTo : path.lineTo)(" +
4578 |         "       points[i][0], points[i][1]);" +
4579 |         "  }" +
4580 |         "}",
4581 |         "\"function (this:F, ?, ?): undefined\" " +
4582 |         "must be called with a \"this\" type");
4583 |   }
```
