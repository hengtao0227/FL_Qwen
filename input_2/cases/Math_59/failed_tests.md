# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.util.FastMathTest.testMinMaxFloat()
Resolved declaration: org.apache.commons.math.util.FastMathTest.testMinMaxFloat()
Source: src/test/java/org/apache/commons/math/util/FastMathTest.java

```java
77 |     @Test
78 |     public void testMinMaxFloat() {
79 |         float[][] pairs = {
80 |             { -50.0f, 50.0f },
81 |             {  Float.POSITIVE_INFINITY, 1.0f },
82 |             {  Float.NEGATIVE_INFINITY, 1.0f },
83 |             {  Float.NaN, 1.0f },
84 |             {  Float.POSITIVE_INFINITY, 0.0f },
85 |             {  Float.NEGATIVE_INFINITY, 0.0f },
86 |             {  Float.NaN, 0.0f },
87 |             {  Float.NaN, Float.NEGATIVE_INFINITY },
88 |             {  Float.NaN, Float.POSITIVE_INFINITY }
89 |         };
90 |         for (float[] pair : pairs) {
91 |             Assert.assertEquals("min(" + pair[0] + ", " + pair[1] + ")",
92 |                                 Math.min(pair[0], pair[1]),
93 |                                 FastMath.min(pair[0], pair[1]),
94 |                                 MathUtils.EPSILON);
95 |             Assert.assertEquals("min(" + pair[1] + ", " + pair[0] + ")",
96 |                                 Math.min(pair[1], pair[0]),
97 |                                 FastMath.min(pair[1], pair[0]),
98 |                                 MathUtils.EPSILON);
99 |             Assert.assertEquals("max(" + pair[0] + ", " + pair[1] + ")",
100 |                                 Math.max(pair[0], pair[1]),
101 |                                 FastMath.max(pair[0], pair[1]),
102 |                                 MathUtils.EPSILON);
103 |             Assert.assertEquals("max(" + pair[1] + ", " + pair[0] + ")",
104 |                                 Math.max(pair[1], pair[0]),
105 |                                 FastMath.max(pair[1], pair[0]),
106 |                                 MathUtils.EPSILON);
107 |         }
108 |     }
```
