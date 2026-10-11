# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.invocation.InvocationTest.shouldScreamWhenCallingRealMethodOnInterface()
Resolved declaration: org.mockito.internal.invocation.InvocationTest.shouldScreamWhenCallingRealMethodOnInterface()
Source: test/org/mockito/internal/invocation/InvocationTest.java

```java
168 |     @Test
169 |     public void shouldScreamWhenCallingRealMethodOnInterface() throws Throwable {
170 |         //given
171 |         Invocation invocationOnInterface = new InvocationBuilder().toInvocation();
172 | 
173 |         try {
174 |             //when
175 |             invocationOnInterface.callRealMethod();
176 |             //then
177 |             fail();
178 |         } catch(MockitoException e) {}
179 |     }
```

## org.mockitousage.spies.SpyingOnInterfacesTest.shouldFailInRuntimeWhenCallingRealMethodOnInterface()
Resolved declaration: org.mockitousage.spies.SpyingOnInterfacesTest.shouldFailInRuntimeWhenCallingRealMethodOnInterface()
Source: test/org/mockitousage/spies/SpyingOnInterfacesTest.java

```java
31 |     @Test
32 |     public void shouldFailInRuntimeWhenCallingRealMethodOnInterface() throws Exception {
33 |         //given
34 |         List list = mock(List.class);
35 |         when(list.get(0)).thenAnswer(
36 |             new Answer() {
37 |                 public Object answer(InvocationOnMock invocation) throws Throwable {
38 |                     return invocation.callRealMethod();
39 |                 }
40 |             }
41 |         );
42 |         try {
43 |             //when
44 |             list.get(0);            
45 |             //then
46 |             fail();
47 |         } catch (MockitoException e) {}
48 |     }
```
