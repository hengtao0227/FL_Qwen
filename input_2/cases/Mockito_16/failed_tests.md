# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.StubbingMocksThatAreConfiguredToReturnMocksTest.shouldAllowStubbingMocksConfiguredWithRETURNS_MOCKS()
Resolved declaration: org.mockitousage.bugs.StubbingMocksThatAreConfiguredToReturnMocksTest.shouldAllowStubbingMocksConfiguredWithRETURNS_MOCKS()
Source: test/org/mockitousage/bugs/StubbingMocksThatAreConfiguredToReturnMocksTest.java

```java
16 |     @Test
17 |     public void shouldAllowStubbingMocksConfiguredWithRETURNS_MOCKS() {
18 |         IMethods mock = mock(IMethods.class, RETURNS_MOCKS);
19 |         when(mock.objectReturningMethodNoArgs()).thenReturn(null);
20 |     }
```
