# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.stubbing.answers.AnswersValidatorTest.shouldFailWhenCallingRealMethodOnIterface()
Resolved declaration: org.mockito.internal.stubbing.answers.AnswersValidatorTest.shouldFailWhenCallingRealMethodOnIterface()
Source: test/org/mockito/internal/stubbing/answers/AnswersValidatorTest.java

```java
91 |     @Test
92 |     public void shouldFailWhenCallingRealMethodOnIterface() throws Throwable {
93 |         //given
94 |         Invocation inovcationOnIterface = new InvocationBuilder().method("simpleMethod").toInvocation();
95 |         try {
96 |             //when
97 |             validator.validate(new CallsRealMethods(), inovcationOnIterface);
98 |             //then
99 |             fail();
100 |         } catch (MockitoException e) {}
101 |     }
```

## org.mockitousage.spies.SpyingOnInterfacesTest.shouldFailFastWhenCallingRealMethodOnInterface()
Resolved declaration: org.mockitousage.spies.SpyingOnInterfacesTest.shouldFailFastWhenCallingRealMethodOnInterface()
Source: test/org/mockitousage/spies/SpyingOnInterfacesTest.java

```java
21 |     @Test
22 |     public void shouldFailFastWhenCallingRealMethodOnInterface() throws Exception {
23 |         List list = mock(List.class);
24 |         try {
25 |             //when
26 |             when(list.get(0)).thenCallRealMethod();
27 |             //then
28 |             fail();
29 |         } catch (MockitoException e) {}
30 |     }
```
