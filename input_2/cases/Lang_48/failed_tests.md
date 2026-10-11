# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.builder.EqualsBuilderTest.testBigDecimal()
Resolved declaration: org.apache.commons.lang.builder.EqualsBuilderTest.testBigDecimal()
Source: src/test/org/apache/commons/lang/builder/EqualsBuilderTest.java

```java
381 |     public void testBigDecimal() {
382 |         BigDecimal o1 = new BigDecimal("2.0");
383 |         BigDecimal o2 = new BigDecimal("2.00");
384 |         assertTrue(new EqualsBuilder().append(o1, o1).isEquals());
385 |         assertTrue(new EqualsBuilder().append(o1, o2).isEquals());
386 |     }
```
