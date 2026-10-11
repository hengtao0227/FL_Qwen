# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.time.FastDateFormat_ParserTest.testLANG_832()
Resolved declaration: org.apache.commons.lang3.time.FastDateParserTest.testLANG_832()
Source: src/test/java/org/apache/commons/lang3/time/FastDateParserTest.java

```java
336 |     @Test
337 |     public void testLANG_832() throws Exception {
338 |         testSdfAndFdp("'d'd" ,"d3", false); // OK
339 |         testSdfAndFdp("'d'd'","d3", true); // should fail (unterminated quote)
340 |     }
```

## org.apache.commons.lang3.time.FastDateParserTest.testLANG_832()
Resolved declaration: org.apache.commons.lang3.time.FastDateParserTest.testLANG_832()
Source: src/test/java/org/apache/commons/lang3/time/FastDateParserTest.java

```java
336 |     @Test
337 |     public void testLANG_832() throws Exception {
338 |         testSdfAndFdp("'d'd" ,"d3", false); // OK
339 |         testSdfAndFdp("'d'd'","d3", true); // should fail (unterminated quote)
340 |     }
```
