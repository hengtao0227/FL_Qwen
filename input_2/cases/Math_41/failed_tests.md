# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.descriptive.moment.VarianceTest.testEvaluateArraySegmentWeighted()
Resolved declaration: org.apache.commons.math.stat.descriptive.UnivariateStatisticAbstractTest.testEvaluateArraySegmentWeighted()
Source: src/test/java/org/apache/commons/math/stat/descriptive/UnivariateStatisticAbstractTest.java

```java
117 |     @Test
118 |     public void testEvaluateArraySegmentWeighted() {
119 |         // See if this statistic computes weighted statistics
120 |         // If not, skip this test
121 |         UnivariateStatistic statistic = getUnivariateStatistic();
122 |         if (!(statistic instanceof WeightedEvaluation)) {
123 |             return;
124 |         }
125 |         final WeightedEvaluation stat = (WeightedEvaluation) getUnivariateStatistic();
126 |         final double[] arrayZero = new double[5];
127 |         final double[] weightZero = new double[5];
128 |         System.arraycopy(testArray, 0, arrayZero, 0, 5);
129 |         System.arraycopy(testWeightsArray, 0, weightZero, 0, 5);
130 |         Assert.assertEquals(stat.evaluate(arrayZero, weightZero),
131 |                 stat.evaluate(testArray, testWeightsArray, 0, 5), 0);
132 |         final double[] arrayOne = new double[5];
133 |         final double[] weightOne = new double[5];
134 |         System.arraycopy(testArray, 5, arrayOne, 0, 5);
135 |         System.arraycopy(testWeightsArray, 5, weightOne, 0, 5);
136 |         Assert.assertEquals(stat.evaluate(arrayOne, weightOne),
137 |                 stat.evaluate(testArray, testWeightsArray, 5, 5), 0);
138 |         final double[] arrayEnd = new double[5];
139 |         final double[] weightEnd = new double[5];
140 |         System.arraycopy(testArray, testArray.length - 5, arrayEnd, 0, 5);
141 |         System.arraycopy(testWeightsArray, testArray.length - 5, weightEnd, 0, 5);
142 |         Assert.assertEquals(stat.evaluate(arrayEnd, weightEnd),
143 |                 stat.evaluate(testArray, testWeightsArray, testArray.length - 5, 5), 0);
144 |     }
```
