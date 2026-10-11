# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.dfp.DfpTest.testIssue567()
Resolved declaration: org.apache.commons.math.dfp.DfpTest.testIssue567()
Source: src/test/java/org/apache/commons/math/dfp/DfpTest.java

```java
1509 |     @Test
1510 |     public void testIssue567() {
1511 |         DfpField field = new DfpField(100);
1512 |         Assert.assertEquals(0.0, field.getZero().toDouble(), MathUtils.SAFE_MIN);
1513 |         Assert.assertEquals(0.0, field.newDfp(0.0).toDouble(), MathUtils.SAFE_MIN);
1514 |         Assert.assertEquals(-1, FastMath.copySign(1, field.newDfp(-0.0).toDouble()), MathUtils.EPSILON);
1515 |         Assert.assertEquals(+1, FastMath.copySign(1, field.newDfp(+0.0).toDouble()), MathUtils.EPSILON);
1516 |     }
```
