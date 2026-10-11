# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.stubbing.defaultanswers.ReturnsEmptyValuesTest.should_return_empty_iterable()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsEmptyValuesTest.should_return_empty_iterable()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsEmptyValuesTest.java

```java
55 |     @Test
56 |     public void should_return_empty_iterable() throws Exception {
57 |         assertFalse(((Iterable) values.returnValueFor(Iterable.class)).iterator().hasNext());
58 |     }
```
