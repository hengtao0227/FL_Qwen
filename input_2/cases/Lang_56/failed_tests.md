# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.time.FastDateFormatTest.testLang303()
Resolved declaration: org.apache.commons.lang.time.FastDateFormatTest.testLang303()
Source: src/test/org/apache/commons/lang/time/FastDateFormatTest.java

```java
284 |     public void testLang303() {
285 |         FastDateFormat format = FastDateFormat.getInstance("yyyy/MM/dd");
286 |         format = (FastDateFormat) SerializationUtils.deserialize( SerializationUtils.serialize( format ) );
287 |     }
```
