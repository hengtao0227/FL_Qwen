# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.FrequencyTest.testAddNonComparable()
Resolved declaration: org.apache.commons.math.stat.FrequencyTest.testAddNonComparable()
Source: src/test/org/apache/commons/math/stat/FrequencyTest.java

```java
193 |     public void testAddNonComparable(){
194 |         try {
195 |             f.addValue(new Object()); // This was previously OK
196 |             fail("Expected IllegalArgumentException");
197 |         } catch (IllegalArgumentException expected) {
198 |         }
199 |         f.clear();
200 |         f.addValue(1);
201 |         try {
202 |             f.addValue(new Object());
203 |             fail("Expected IllegalArgumentException");
204 |         } catch (IllegalArgumentException expected) {
205 |         }
206 |     }
```
