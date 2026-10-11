# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testIssue284()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testIssue284()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
1766 |   public void testIssue284() {
1767 |     CompilerOptions options = createCompilerOptions();
1768 |     options.smartNameRemoval = true;
1769 |     test(options,
1770 |         "var goog = {};" +
1771 |         "goog.inherits = function(x, y) {};" +
1772 |         "var ns = {};" +
1773 |         "/** @constructor */" +
1774 |         "ns.PageSelectionModel = function() {};" +
1775 |         "/** @constructor */" +
1776 |         "ns.PageSelectionModel.FooEvent = function() {};" +
1777 |         "/** @constructor */" +
1778 |         "ns.PageSelectionModel.SelectEvent = function() {};" +
1779 |         "goog.inherits(ns.PageSelectionModel.ChangeEvent," +
1780 |         "    ns.PageSelectionModel.FooEvent);",
1781 |         "");
1782 |   }
```

## com.google.javascript.jscomp.NameAnalyzerTest.testIssue284()
Resolved declaration: com.google.javascript.jscomp.NameAnalyzerTest.testIssue284()
Source: test/com/google/javascript/jscomp/NameAnalyzerTest.java

```java
1643 |   public void testIssue284() {
1644 |     test(
1645 |         "var goog = {};" +
1646 |         "goog.inherits = function(x, y) {};" +
1647 |         "var ns = {};" +
1648 |         "/** @constructor */" +
1649 |         "ns.PageSelectionModel = function() {};" +
1650 |         "/** @constructor */" +
1651 |         "ns.PageSelectionModel.FooEvent = function() {};" +
1652 |         "/** @constructor */" +
1653 |         "ns.PageSelectionModel.SelectEvent = function() {};" +
1654 |         "goog.inherits(ns.PageSelectionModel.ChangeEvent," +
1655 |         "    ns.PageSelectionModel.FooEvent);",
1656 |         "");
1657 |   }
```
