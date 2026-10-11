# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.correlation.PearsonsCorrelationTest.testPValueNearZero()
Resolved declaration: org.apache.commons.math.stat.correlation.PearsonsCorrelationTest.testPValueNearZero()
Source: src/test/java/org/apache/commons/math/stat/correlation/PearsonsCorrelationTest.java

```java
167 |     public void testPValueNearZero() throws Exception {
168 |         /*
169 |          * Create a dataset that has r -> 1, p -> 0 as dimension increases.
170 |          * Prior to the fix for MATH-371, p vanished for dimension >= 14.
171 |          * Post fix, p-values diminish smoothly, vanishing at dimension = 127.
172 |          * Tested value is ~1E-303.
173 |          */
174 |         int dimension = 120; 
175 |         double[][] data = new double[dimension][2];
176 |         for (int i = 0; i < dimension; i++) {
177 |             data[i][0] = i;
178 |             data[i][1] = i + 1/((double)i + 1);
179 |         }
180 |         PearsonsCorrelation corrInstance = new PearsonsCorrelation(data);
181 |         assertTrue(corrInstance.getCorrelationPValues().getEntry(0, 1) > 0);
182 |     }
```

## org.apache.commons.math.stat.correlation.SpearmansRankCorrelationTest.testPValueNearZero()
Resolved declaration: org.apache.commons.math.stat.correlation.PearsonsCorrelationTest.testPValueNearZero()
Source: src/test/java/org/apache/commons/math/stat/correlation/PearsonsCorrelationTest.java

```java
167 |     public void testPValueNearZero() throws Exception {
168 |         /*
169 |          * Create a dataset that has r -> 1, p -> 0 as dimension increases.
170 |          * Prior to the fix for MATH-371, p vanished for dimension >= 14.
171 |          * Post fix, p-values diminish smoothly, vanishing at dimension = 127.
172 |          * Tested value is ~1E-303.
173 |          */
174 |         int dimension = 120; 
175 |         double[][] data = new double[dimension][2];
176 |         for (int i = 0; i < dimension; i++) {
177 |             data[i][0] = i;
178 |             data[i][1] = i + 1/((double)i + 1);
179 |         }
180 |         PearsonsCorrelation corrInstance = new PearsonsCorrelation(data);
181 |         assertTrue(corrInstance.getCorrelationPValues().getEntry(0, 1) > 0);
182 |     }
```
