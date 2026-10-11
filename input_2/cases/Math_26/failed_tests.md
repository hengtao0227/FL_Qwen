# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.fraction.FractionTest.testIntegerOverflow()
Resolved declaration: org.apache.commons.math3.fraction.FractionTest.testIntegerOverflow()
Source: src/test/java/org/apache/commons/math3/fraction/FractionTest.java

```java
134 |     @Test
135 |     public void testIntegerOverflow() {
136 |         checkIntegerOverflow(0.75000000001455192);
137 |         checkIntegerOverflow(1.0e10);
138 |         checkIntegerOverflow(-1.0e10);
139 |         checkIntegerOverflow(-43979.60679604749);
140 |     }
```
