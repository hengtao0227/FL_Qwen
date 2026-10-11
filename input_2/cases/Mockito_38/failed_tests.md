# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.verification.argumentmatching.ArgumentMatchingToolTest.shouldWorkFineWhenGivenArgIsNull()
Resolved declaration: org.mockito.internal.verification.argumentmatching.ArgumentMatchingToolTest.shouldWorkFineWhenGivenArgIsNull()
Source: test/org/mockito/internal/verification/argumentmatching/ArgumentMatchingToolTest.java

```java
79 |     @Test
80 |     public void shouldWorkFineWhenGivenArgIsNull() {
81 |         //when
82 |         Integer[] suspicious = tool.getSuspiciouslyNotMatchingArgsIndexes((List) Arrays.asList(new Equals(20)), new Object[] {null});
83 |         
84 |         //then
85 |         assertEquals(0, suspicious.length);
86 |     }
```

## org.mockitousage.bugs.ActualInvocationHasNullArgumentNPEBugTest.shouldAllowPassingNullArgument()
Resolved declaration: org.mockitousage.bugs.ActualInvocationHasNullArgumentNPEBugTest.shouldAllowPassingNullArgument()
Source: test/org/mockitousage/bugs/ActualInvocationHasNullArgumentNPEBugTest.java

```java
19 |     @Test
20 |     public void shouldAllowPassingNullArgument() {
21 |         //given
22 |         Fun mockFun = mock(Fun.class);
23 |         when(mockFun.doFun((String) anyObject())).thenReturn("value");
24 | 
25 |         //when
26 |         mockFun.doFun(null);
27 | 
28 |         //then
29 |         try {
30 |             verify(mockFun).doFun("hello");
31 |         } catch(AssertionError r) {
32 |             //it's ok, we just want to reproduce the bug
33 |         }
34 |     }
```
