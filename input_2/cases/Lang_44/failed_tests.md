# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.NumberUtilsTest.testLang457()
Resolved declaration: org.apache.commons.lang.NumberUtilsTest.testLang457()
Source: src/test/org/apache/commons/lang/NumberUtilsTest.java

```java
524 |     public void testLang457() {
525 |         String[] badInputs = new String[] { "l", "L", "f", "F", "junk", "bobL"};
526 |         for(int i=0; i<badInputs.length; i++) {
527 |             try {
528 |                 NumberUtils.createNumber(badInputs[i]);
529 |                 fail("NumberFormatException was expected for " + badInputs[i]);
530 |             } catch (NumberFormatException e) {
531 |                 return; // expected
532 |             }
533 |         }
534 |     }
```
