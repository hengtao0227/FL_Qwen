# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.util.MultidimensionalCounterTest.testIterationConsistency()
Resolved declaration: org.apache.commons.math.util.MultidimensionalCounterTest.testIterationConsistency()
Source: src/test/java/org/apache/commons/math/util/MultidimensionalCounterTest.java

```java
122 |     @Test
123 |     public void testIterationConsistency() {
124 |         final MultidimensionalCounter c = new MultidimensionalCounter(2, 3, 4);
125 |         final int[][] expected = new int[][] {
126 |             { 0, 0, 0 },
127 |             { 0, 0, 1 },
128 |             { 0, 0, 2 },
129 |             { 0, 0, 3 },
130 |             { 0, 1, 0 },
131 |             { 0, 1, 1 },
132 |             { 0, 1, 2 },
133 |             { 0, 1, 3 },
134 |             { 0, 2, 0 },
135 |             { 0, 2, 1 },
136 |             { 0, 2, 2 },
137 |             { 0, 2, 3 },
138 |             { 1, 0, 0 },
139 |             { 1, 0, 1 },
140 |             { 1, 0, 2 },
141 |             { 1, 0, 3 },
142 |             { 1, 1, 0 },
143 |             { 1, 1, 1 },
144 |             { 1, 1, 2 },
145 |             { 1, 1, 3 },
146 |             { 1, 2, 0 },
147 |             { 1, 2, 1 },
148 |             { 1, 2, 2 },
149 |             { 1, 2, 3 }
150 |         };
151 | 
152 |         final int totalSize = c.getSize();
153 |         final int nDim = c.getDimension();
154 |         final MultidimensionalCounter.Iterator iter = c.iterator();
155 |         for (int i = 0; i < totalSize; i++) {
156 |             if (!iter.hasNext()) {
157 |                 Assert.fail("Too short");
158 |             }
159 |             final int uniDimIndex = iter.next();
160 |             Assert.assertEquals("Wrong iteration at " + i, i, uniDimIndex);
161 | 
162 |             for (int dimIndex = 0; dimIndex < nDim; dimIndex++) {
163 |                 Assert.assertEquals("Wrong multidimensional index for [" + i + "][" + dimIndex + "]",
164 |                                     expected[i][dimIndex], iter.getCount(dimIndex));
165 |             }
166 | 
167 |             Assert.assertEquals("Wrong unidimensional index for [" + i + "]",
168 |                                 c.getCount(expected[i]), uniDimIndex);
169 | 
170 |             final int[] indices = c.getCounts(uniDimIndex);
171 |             for (int dimIndex = 0; dimIndex < nDim; dimIndex++) {
172 |                 Assert.assertEquals("Wrong multidimensional index for [" + i + "][" + dimIndex + "]",
173 |                                     expected[i][dimIndex], indices[dimIndex]);
174 |             }
175 |         }
176 | 
177 |         if (iter.hasNext()) {
178 |             Assert.fail("Too long");
179 |         }
180 |     }
```
