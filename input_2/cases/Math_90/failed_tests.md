# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.FrequencyTest.testAddNonComparable()
Resolved declaration: org.apache.commons.math.stat.FrequencyTest.testAddNonComparable()
Source: src/test/org/apache/commons/math/stat/FrequencyTest.java

```java
193 |     public void testAddNonComparable(){
194 |         try {
195 |             f.addValue(new Object()); // This was OK
196 |             fail("Expected ClassCastException");
197 |         } catch (ClassCastException expected) {
198 |         }
199 |         f.clear();
200 |         f.addValue(1);
201 |         try {
202 |             f.addValue(new Object());
203 |             fail("Expected ClassCastException"); // Previously would have been IllegalArgument
204 |         } catch (ClassCastException expected) {
205 |         }
206 |     }
```
