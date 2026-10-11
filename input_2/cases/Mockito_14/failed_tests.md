# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.VerifyingWithAnExtraCallToADifferentMockTest.shouldAllowVerifyingWhenOtherMockCallIsInTheSameLine()
Resolved declaration: org.mockitousage.bugs.VerifyingWithAnExtraCallToADifferentMockTest.shouldAllowVerifyingWhenOtherMockCallIsInTheSameLine()
Source: test/org/mockitousage/bugs/VerifyingWithAnExtraCallToADifferentMockTest.java

```java
20 |     @Test 
21 |     public void shouldAllowVerifyingWhenOtherMockCallIsInTheSameLine() {
22 |         //given
23 |         when(mock.otherMethod()).thenReturn("foo");
24 |         
25 |         //when
26 |         mockTwo.simpleMethod("foo");
27 |         
28 |         //then
29 |         verify(mockTwo).simpleMethod(mock.otherMethod());
30 |     }
```
