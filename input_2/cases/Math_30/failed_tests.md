# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.stat.inference.MannWhitneyUTestTest.testBigDataSet()
Resolved declaration: org.apache.commons.math3.stat.inference.MannWhitneyUTestTest.testBigDataSet()
Source: src/test/java/org/apache/commons/math3/stat/inference/MannWhitneyUTestTest.java

```java
104 |     @Test
105 |     public void testBigDataSet() throws Exception {
106 |         double[] d1 = new double[1500];
107 |         double[] d2 = new double[1500];
108 |         for (int i = 0; i < 1500; i++) {
109 |             d1[i] = 2 * i;
110 |             d2[i] = 2 * i + 1;
111 |         }
112 |         double result = testStatistic.mannWhitneyUTest(d1, d2);
113 |         Assert.assertTrue(result > 0.1);
114 |     }
```
