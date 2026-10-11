# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.ArrayUtilsAddTest.testJira567()
Resolved declaration: org.apache.commons.lang3.ArrayUtilsAddTest.testJira567()
Source: src/test/org/apache/commons/lang3/ArrayUtilsAddTest.java

```java
32 |     public void testJira567(){
33 |         Number[] n;
34 |         // Valid array construction
35 |         n = ArrayUtils.addAll(new Number[]{Integer.valueOf(1)}, new Long[]{Long.valueOf(2)});
36 |         assertEquals(2,n.length);
37 |         assertEquals(Number.class,n.getClass().getComponentType());
38 |         try {
39 |             // Invalid - can't store Long in Integer array
40 |                n = ArrayUtils.addAll(new Integer[]{Integer.valueOf(1)}, new Long[]{Long.valueOf(2)});
41 |                fail("Should have generated IllegalArgumentException");
42 |         } catch (IllegalArgumentException expected) {
43 |         }
44 |     }
```
