# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.EntitiesTest.testNumberOverflow()
Resolved declaration: org.apache.commons.lang.EntitiesTest.testNumberOverflow()
Source: src/test/org/apache/commons/lang/EntitiesTest.java

```java
200 |     public void testNumberOverflow() throws Exception {
201 |         doTestUnescapeEntity("&#12345678;", "&#12345678;");
202 |         doTestUnescapeEntity("x&#12345678;y", "x&#12345678;y");
203 |         doTestUnescapeEntity("&#x12345678;", "&#x12345678;");
204 |         doTestUnescapeEntity("x&#x12345678;y", "x&#x12345678;y");
205 |     }
```
