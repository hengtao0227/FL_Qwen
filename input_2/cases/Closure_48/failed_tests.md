# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue586()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue586()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
5442 |   public void testIssue586() throws Exception {
5443 |     testTypes(
5444 |         "/** @constructor */" +
5445 |         "var MyClass = function() {};" +
5446 |         "/** @param {boolean} success */" +
5447 |         "MyClass.prototype.fn = function(success) {};" +
5448 |         "MyClass.prototype.test = function() {" +
5449 |         "  this.fn();" +
5450 |         "  this.fn = function() {};" +
5451 |         "};",
5452 |         "Function MyClass.prototype.fn: called with 0 argument(s). " +
5453 |         "Function requires at least 1 argument(s) " +
5454 |         "and no more than 1 argument(s).");
5455 |   }
```
