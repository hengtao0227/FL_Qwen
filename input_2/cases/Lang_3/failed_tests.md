# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.NumberUtilsTest.testStringCreateNumberEnsureNoPrecisionLoss()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.testStringCreateNumberEnsureNoPrecisionLoss()
Source: src/test/java/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
122 |     @Test
123 |     public void testStringCreateNumberEnsureNoPrecisionLoss(){
124 |         String shouldBeFloat = "1.23";
125 |         String shouldBeDouble = "3.40282354e+38";
126 |         String shouldBeBigDecimal = "1.797693134862315759e+308";
127 |         
128 |         assertTrue(NumberUtils.createNumber(shouldBeFloat) instanceof Float);
129 |         assertTrue(NumberUtils.createNumber(shouldBeDouble) instanceof Double);
130 |         assertTrue(NumberUtils.createNumber(shouldBeBigDecimal) instanceof BigDecimal);
131 |     }
```
