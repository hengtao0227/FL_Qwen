# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.general.MinpackTest.testMinpackJennrichSampson()
Resolved declaration: org.apache.commons.math.optimization.general.MinpackTest.testMinpackJennrichSampson()
Source: src/test/java/org/apache/commons/math/optimization/general/MinpackTest.java

```java
324 |   public void testMinpackJennrichSampson() {
325 |     minpackTest(new JennrichSampsonFunction(10, new double[] { 0.3, 0.4 },
326 |                                             64.5856498144943, 11.1517793413499,
327 |                                             new double[] {
328 |                                              0.2578330049, 0.257829976764542
329 |                                             }), false);
330 |   }
```

## org.apache.commons.math.optimization.general.MinpackTest.testMinpackFreudensteinRoth()
Resolved declaration: org.apache.commons.math.optimization.general.MinpackTest.testMinpackFreudensteinRoth()
Source: src/test/java/org/apache/commons/math/optimization/general/MinpackTest.java

```java
145 |   public void testMinpackFreudensteinRoth() {
146 |     minpackTest(new FreudensteinRothFunction(new double[] { 0.5, -2.0 },
147 |                                              20.0124960961895, 6.99887517584575,
148 |                                              new double[] {
149 |                                                11.4124844654993,
150 |                                                -0.896827913731509
151 |                                              }), false);
152 |     minpackTest(new FreudensteinRothFunction(new double[] { 5.0, -20.0 },
153 |                                              12432.833948863, 6.9988751744895,
154 |                                              new double[] {
155 |                                                11.4121122022341,
156 |                                                -0.8968550851268697
157 |                                              }), false);
158 |     minpackTest(new FreudensteinRothFunction(new double[] { 50.0, -200.0 },
159 |                                              11426454.595762, 6.99887517242903,
160 |                                              new double[] {
161 |                                                11.412069435091231,
162 |                                                -0.8968582807605691
163 |                                              }), false);
164 |   }
```
