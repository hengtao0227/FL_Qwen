# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.util.MathUtilsTest.testArrayEquals()
Resolved declaration: org.apache.commons.math.util.MathUtilsTest.testArrayEquals()
Source: src/test/java/org/apache/commons/math/util/MathUtilsTest.java

```java
442 |     public void testArrayEquals() {
443 |         assertFalse(MathUtils.equals(new double[] { 1d }, null));
444 |         assertFalse(MathUtils.equals(null, new double[] { 1d }));
445 |         assertTrue(MathUtils.equals((double[]) null, (double[]) null));
446 | 
447 |         assertFalse(MathUtils.equals(new double[] { 1d }, new double[0]));
448 |         assertTrue(MathUtils.equals(new double[] { 1d }, new double[] { 1d }));
449 |         assertTrue(MathUtils.equals(new double[] {
450 |                                       Double.POSITIVE_INFINITY,
451 |                                       Double.NEGATIVE_INFINITY, 1d, 0d
452 |                                     }, new double[] {
453 |                                       Double.POSITIVE_INFINITY,
454 |                                       Double.NEGATIVE_INFINITY, 1d, 0d
455 |                                     }));
456 |         assertFalse(MathUtils.equals(new double[] { Double.NaN },
457 |                                      new double[] { Double.NaN }));
458 |         assertFalse(MathUtils.equals(new double[] { Double.POSITIVE_INFINITY },
459 |                                      new double[] { Double.NEGATIVE_INFINITY }));
460 |         assertFalse(MathUtils.equals(new double[] { 1d },
461 |                                      new double[] { FastMath.nextAfter(FastMath.nextAfter(1d, 2d), 2d) }));
462 | 
463 |     }
```
