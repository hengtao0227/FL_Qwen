# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.VerifyingWithAnExtraCallToADifferentMockTest.shouldAllowVerifyingWhenOtherMockCallIsInTheSameLine()
Resolved declaration: org.mockitousage.bugs.VerifyingWithAnExtraCallToADifferentMockTest.shouldAllowVerifyingWhenOtherMockCallIsInTheSameLine()
Source: test/org/mockitousage/bugs/VerifyingWithAnExtraCallToADifferentMockTest.java

```java
21 |     @Test 
22 |     public void shouldAllowVerifyingWhenOtherMockCallIsInTheSameLine() {
23 |         //given
24 |         when(mock.otherMethod()).thenReturn("foo");
25 |         
26 |         //when
27 |         mockTwo.simpleMethod("foo");
28 |         
29 |         //then
30 |         verify(mockTwo).simpleMethod(mock.otherMethod());
31 |         try {
32 |             verify(mockTwo, never()).simpleMethod(mock.otherMethod());
33 |             fail();
34 |         } catch (NeverWantedButInvoked e) {}
35 |     }
```
