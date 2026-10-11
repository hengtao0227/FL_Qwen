# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest.testSupplementaryUnescaping()
Resolved declaration: org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest.testSupplementaryUnescaping()
Source: src/test/java/org/apache/commons/lang3/text/translate/NumericEntityUnescaperTest.java

```java
27 |     public void testSupplementaryUnescaping() {
28 |         NumericEntityUnescaper neu = new NumericEntityUnescaper();
29 |         String input = "&#68642;";
30 |         String expected = "\uD803\uDC22";
31 | 
32 |         String result = neu.translate(input);
33 |         assertEquals("Failed to unescape numeric entities supplementary characters", expected, result);
34 |     }
```
