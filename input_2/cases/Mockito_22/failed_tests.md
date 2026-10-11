# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.matchers.EqualityTest.shouldKnowIfObjectsAreEqual()
Resolved declaration: org.mockito.internal.matchers.EqualityTest.shouldKnowIfObjectsAreEqual()
Source: test/org/mockito/internal/matchers/EqualityTest.java

```java
13 |     @Test
14 |     public void shouldKnowIfObjectsAreEqual() throws Exception {
15 |         int[] arr = new int[] {1, 2};
16 |         assertTrue(areEqual(arr, arr));
17 |         assertTrue(areEqual(new int[] {1, 2}, new int[] {1, 2}));
18 |         assertTrue(areEqual(new Double[] {1.0}, new Double[] {1.0}));
19 |         assertTrue(areEqual(new String[0], new String[0]));
20 |         assertTrue(areEqual(new Object[10], new Object[10]));
21 |         assertTrue(areEqual(new int[] {1}, new Integer[] {1}));
22 |         assertTrue(areEqual(new Object[] {"1"}, new String[] {"1"}));
23 | 	Object badequals=new BadEquals();
24 | 	assertTrue(areEqual(badequals,badequals));
25 | 
26 |         assertFalse(areEqual(new Object[9], new Object[10]));
27 |         assertFalse(areEqual(new int[] {1, 2}, new int[] {1}));
28 |         assertFalse(areEqual(new int[] {1}, new double[] {1.0}));
29 |     }
```
