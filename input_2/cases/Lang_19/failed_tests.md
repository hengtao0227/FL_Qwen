# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest.testUnfinishedEntity()
Resolved declaration: org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest.testUnfinishedEntity()
Source: src/test/java/org/apache/commons/lang3/text/translate/NumericEntityUnescaperTest.java

```java
46 |     public void testUnfinishedEntity() {
47 |         NumericEntityUnescaper neu = new NumericEntityUnescaper();
48 |         String input = "Test &#x30 not test";
49 |         String expected = "Test \u0030 not test";
50 | 
51 |         String result = neu.translate(input);
52 |         assertEquals("Failed to support unfinished entities (i.e. missing semi-colon", expected, result);
53 |     }
```

## org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest.testOutOfBounds()
Resolved declaration: org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest.testOutOfBounds()
Source: src/test/java/org/apache/commons/lang3/text/translate/NumericEntityUnescaperTest.java

```java
37 |     public void testOutOfBounds() {
38 |         NumericEntityUnescaper neu = new NumericEntityUnescaper();
39 | 
40 |         assertEquals("Failed to ignore when last character is &", "Test &", neu.translate("Test &"));
41 |         assertEquals("Failed to ignore when last character is &", "Test &#", neu.translate("Test &#"));
42 |         assertEquals("Failed to ignore when last character is &", "Test &#x", neu.translate("Test &#x"));
43 |         assertEquals("Failed to ignore when last character is &", "Test &#X", neu.translate("Test &#X"));
44 |     }
```
