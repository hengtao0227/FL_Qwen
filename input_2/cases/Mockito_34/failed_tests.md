# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.invocation.InvocationMatcherTest.shouldMatchCaptureArgumentsWhenArgsCountDoesNOTMatch()
Resolved declaration: org.mockito.internal.invocation.InvocationMatcherTest.shouldMatchCaptureArgumentsWhenArgsCountDoesNOTMatch()
Source: test/org/mockito/internal/invocation/InvocationMatcherTest.java

```java
142 |     @Test
143 |     public void shouldMatchCaptureArgumentsWhenArgsCountDoesNOTMatch() throws Exception {
144 |         //given
145 |         mock.varargs();
146 |         Invocation invocation = getLastInvocation();
147 | 
148 |         //when
149 |         InvocationMatcher invocationMatcher = new InvocationMatcher(invocation, (List) asList(new LocalizedMatcher(AnyVararg.ANY_VARARG)));
150 | 
151 |         //then
152 |         invocationMatcher.captureArgumentsFrom(invocation);
153 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldMatchEasilyEmptyVararg()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldMatchEasilyEmptyVararg()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
168 |     @Test
169 |     //See bug #157
170 |     public void shouldMatchEasilyEmptyVararg() throws Exception {
171 |         //when
172 |         when(mock.foo(anyVararg())).thenReturn(-1);
173 | 
174 |         //then
175 |         assertEquals(-1, mock.foo());
176 |     } 
```
