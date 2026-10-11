# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.FrequencyTest.testPcts()
Resolved declaration: org.apache.commons.math.stat.FrequencyTest.testPcts()
Source: src/test/java/org/apache/commons/math/stat/FrequencyTest.java

```java
135 |     public void testPcts() {
136 |         f.addValue(oneL);
137 |         f.addValue(twoL);
138 |         f.addValue(oneI);
139 |         f.addValue(twoI);
140 |         f.addValue(threeL);
141 |         f.addValue(threeL);
142 |         f.addValue(3);
143 |         f.addValue(threeI);
144 |         assertEquals("one pct",0.25,f.getPct(1),tolerance);
145 |         assertEquals("two pct",0.25,f.getPct(Long.valueOf(2)),tolerance);
146 |         assertEquals("three pct",0.5,f.getPct(threeL),tolerance);
147 |         // MATH-329
148 |         assertEquals("three (Object) pct",0.5,f.getPct((Object) (Integer.valueOf(3))),tolerance);
149 |         assertEquals("five pct",0,f.getPct(5),tolerance);
150 |         assertEquals("foo pct",0,f.getPct("foo"),tolerance);
151 |         assertEquals("one cum pct",0.25,f.getCumPct(1),tolerance);
152 |         assertEquals("two cum pct",0.50,f.getCumPct(Long.valueOf(2)),tolerance);
153 |         assertEquals("Integer argument",0.50,f.getCumPct(Integer.valueOf(2)),tolerance);
154 |         assertEquals("three cum pct",1.0,f.getCumPct(threeL),tolerance);
155 |         assertEquals("five cum pct",1.0,f.getCumPct(5),tolerance);
156 |         assertEquals("zero cum pct",0.0,f.getCumPct(0),tolerance);
157 |         assertEquals("foo cum pct",0,f.getCumPct("foo"),tolerance);
158 |     }
```
