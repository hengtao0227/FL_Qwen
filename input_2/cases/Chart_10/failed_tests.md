# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.imagemap.junit.StandardToolTipTagFragmentGeneratorTests.testGenerateURLFragment()
Resolved declaration: org.jfree.chart.imagemap.junit.StandardToolTipTagFragmentGeneratorTests.testGenerateURLFragment()
Source: tests/org/jfree/chart/imagemap/junit/StandardToolTipTagFragmentGeneratorTests.java

```java
75 |     public void testGenerateURLFragment() {
76 |         StandardToolTipTagFragmentGenerator g
77 |                 = new StandardToolTipTagFragmentGenerator();
78 |         assertEquals(" title=\"abc\" alt=\"\"",
79 |                 g.generateToolTipFragment("abc"));
80 |         assertEquals(" title=\"Series &quot;A&quot;, 100.0\" alt=\"\"",
81 |                 g.generateToolTipFragment("Series \"A\", 100.0"));
82 |     }
```
