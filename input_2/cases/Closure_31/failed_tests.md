# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CommandLineRunnerTest.testDependencySortingWhitespaceMode()
Resolved declaration: com.google.javascript.jscomp.CommandLineRunnerTest.testDependencySortingWhitespaceMode()
Source: test/com/google/javascript/jscomp/CommandLineRunnerTest.java

```java
624 |   public void testDependencySortingWhitespaceMode() {
625 |     args.add("--manage_closure_dependencies");
626 |     args.add("--compilation_level=WHITESPACE_ONLY");
627 |     test(new String[] {
628 |           "goog.require('beer');",
629 |           "goog.provide('beer');\ngoog.require('hops');",
630 |           "goog.provide('hops');",
631 |          },
632 |          new String[] {
633 |           "goog.provide('hops');",
634 |           "goog.provide('beer');\ngoog.require('hops');",
635 |           "goog.require('beer');"
636 |          });
637 |   }
```
