# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.ListenersLostOnResetMockTest.listener()
Resolved declaration: org.mockitousage.bugs.ListenersLostOnResetMockTest.listener()
Source: test/org/mockitousage/bugs/ListenersLostOnResetMockTest.java

```java
14 |     @Test
15 |     public void listener() throws Exception {
16 |         InvocationListener invocationListener = mock(InvocationListener.class);
17 | 
18 |         List mockedList = mock(List.class, withSettings().invocationListeners(invocationListener));
19 |         reset(mockedList);
20 | 
21 |         mockedList.clear();
22 | 
23 |         verify(invocationListener).reportInvocation(any(MethodInvocationReport.class));
24 |     }
```
