# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.util.junit.ShapeUtilitiesTests.testEqualGeneralPaths()
Resolved declaration: org.jfree.chart.util.junit.ShapeUtilitiesTests.testEqualGeneralPaths()
Source: tests/org/jfree/chart/util/junit/ShapeUtilitiesTests.java

```java
191 |     public void testEqualGeneralPaths() {
192 |         GeneralPath g1 = new GeneralPath();
193 |         g1.moveTo(1.0f, 2.0f);
194 |         g1.lineTo(3.0f, 4.0f);
195 |         g1.curveTo(5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f);
196 |         g1.quadTo(1.0f, 2.0f, 3.0f, 4.0f);
197 |         g1.closePath();
198 |         GeneralPath g2 = new GeneralPath();
199 |         g2.moveTo(1.0f, 2.0f);
200 |         g2.lineTo(3.0f, 4.0f);
201 |         g2.curveTo(5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f);
202 |         g2.quadTo(1.0f, 2.0f, 3.0f, 4.0f);
203 |         g2.closePath();
204 |         assertTrue(ShapeUtilities.equal(g1, g2));
205 | 
206 |         g2 = new GeneralPath();
207 |         g2.moveTo(11.0f, 22.0f);
208 |         g2.lineTo(3.0f, 4.0f);
209 |         g2.curveTo(5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f);
210 |         g2.quadTo(1.0f, 2.0f, 3.0f, 4.0f);
211 |         g2.closePath();
212 |         assertFalse(ShapeUtilities.equal(g1, g2));
213 | 
214 |         g2 = new GeneralPath();
215 |         g2.moveTo(1.0f, 2.0f);
216 |         g2.lineTo(33.0f, 44.0f);
217 |         g2.curveTo(5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f);
218 |         g2.quadTo(1.0f, 2.0f, 3.0f, 4.0f);
219 |         g2.closePath();
220 |         assertFalse(ShapeUtilities.equal(g1, g2));
221 | 
222 |         g2 = new GeneralPath();
223 |         g2.moveTo(1.0f, 2.0f);
224 |         g2.lineTo(3.0f, 4.0f);
225 |         g2.curveTo(55.0f, 66.0f, 77.0f, 88.0f, 99.0f, 100.0f);
226 |         g2.quadTo(1.0f, 2.0f, 3.0f, 4.0f);
227 |         g2.closePath();
228 |         assertFalse(ShapeUtilities.equal(g1, g2));
229 | 
230 |         g2 = new GeneralPath();
231 |         g2.moveTo(1.0f, 2.0f);
232 |         g2.lineTo(3.0f, 4.0f);
233 |         g2.curveTo(5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f);
234 |         g2.quadTo(11.0f, 22.0f, 33.0f, 44.0f);
235 |         g2.closePath();
236 |         assertFalse(ShapeUtilities.equal(g1, g2));
237 | 
238 |         g2 = new GeneralPath();
239 |         g2.moveTo(1.0f, 2.0f);
240 |         g2.lineTo(3.0f, 4.0f);
241 |         g2.curveTo(5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f);
242 |         g2.quadTo(1.0f, 2.0f, 3.0f, 4.0f);
243 |         g2.lineTo(3.0f, 4.0f);
244 |         g2.closePath();
245 |         assertFalse(ShapeUtilities.equal(g1, g2));
246 |     }
```
