# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.invocation.InvocationMatcherTest.should_capture_varargs_as_vararg()
Resolved declaration: org.mockito.internal.invocation.InvocationMatcherTest.should_capture_varargs_as_vararg()
Source: test/org/mockito/internal/invocation/InvocationMatcherTest.java

```java
142 |     @Test
143 |     public void should_capture_varargs_as_vararg() throws Exception {
144 |         //given
145 |         mock.mixedVarargs(1, "a", "b");
146 |         Invocation invocation = getLastInvocation();
147 |         CapturingMatcher m = new CapturingMatcher();
148 |         InvocationMatcher invocationMatcher = new InvocationMatcher(invocation, (List) asList(new Equals(1), new LocalizedMatcher(m)));
149 | 
150 |         //when
151 |         invocationMatcher.captureArgumentsFrom(invocation);
152 | 
153 |         //then
154 |         Assertions.assertThat(m.getAllValues()).containsExactly("a", "b");
155 |     }
```

## org.mockitousage.bugs.varargs.VarargsAndAnyObjectPicksUpExtraInvocationsTest.shouldVerifyCorrectlyNumberOfInvocationsWithVarargs()
Resolved declaration: org.mockitousage.bugs.varargs.VarargsAndAnyObjectPicksUpExtraInvocationsTest.shouldVerifyCorrectlyNumberOfInvocationsWithVarargs()
Source: test/org/mockitousage/bugs/varargs/VarargsAndAnyObjectPicksUpExtraInvocationsTest.java

```java
43 |     @Test
44 |     public void shouldVerifyCorrectlyNumberOfInvocationsWithVarargs() {
45 |         //when
46 |         table.newRow("qux", "foo", "bar", "baz");
47 |         table.newRow("abc", "def");
48 |         
49 |         //then
50 |         verify(table).newRow(anyString(), eq("foo"), anyString(), anyString());
51 |         verify(table).newRow(anyString(), anyString());
52 |     }
```

## org.mockitousage.bugs.varargs.VarargsNotPlayingWithAnyObjectTest.shouldMatchAnyVararg()
Resolved declaration: org.mockitousage.bugs.varargs.VarargsNotPlayingWithAnyObjectTest.shouldMatchAnyVararg()
Source: test/org/mockitousage/bugs/varargs/VarargsNotPlayingWithAnyObjectTest.java

```java
24 |     @Test
25 |     public void shouldMatchAnyVararg() {
26 |         mock.run("a", "b");
27 | 
28 |         verify(mock).run(anyString(), anyString());
29 |         verify(mock).run((String) anyObject(), (String) anyObject());
30 | 
31 |         verify(mock).run((String[]) anyVararg());
32 |         
33 |         verify(mock, never()).run();
34 |         verify(mock, never()).run(anyString(), eq("f"));
35 |     }
```

## org.mockitousage.matchers.CapturingArgumentsTest.should_capture_all_vararg()
Resolved declaration: org.mockitousage.matchers.CapturingArgumentsTest.should_capture_all_vararg()
Source: test/org/mockitousage/matchers/CapturingArgumentsTest.java

```java
266 |     @Test
267 |     public void should_capture_all_vararg() throws Exception {
268 |         // given
269 |         ArgumentCaptor<String> argumentCaptor = ArgumentCaptor.forClass(String.class);
270 | 
271 |         // when
272 |         mock.mixedVarargs(42, "a", "b", "c");
273 |         mock.mixedVarargs(42, "again ?!");
274 | 
275 |         // then
276 |         verify(mock, times(2)).mixedVarargs(any(), argumentCaptor.capture());
277 | 
278 |         Assertions.assertThat(argumentCaptor.getAllValues()).containsExactly("a", "b", "c", "again ?!");
279 |     }
```

## org.mockitousage.matchers.CapturingArgumentsTest.captures_correctly_when_captor_used_multiple_times()
Resolved declaration: org.mockitousage.matchers.CapturingArgumentsTest.captures_correctly_when_captor_used_multiple_times()
Source: test/org/mockitousage/matchers/CapturingArgumentsTest.java

```java
294 |     @Test
295 |     public void captures_correctly_when_captor_used_multiple_times() throws Exception {
296 |         // given
297 |         ArgumentCaptor<String> argumentCaptor = ArgumentCaptor.forClass(String.class);
298 | 
299 |         // when
300 |         mock.mixedVarargs(42, "a", "b", "c");
301 | 
302 |         // then
303 |         // this is only for backwards compatibility. It does not make sense in real to do so.
304 |         verify(mock).mixedVarargs(any(), argumentCaptor.capture(), argumentCaptor.capture(), argumentCaptor.capture());
305 |         Assertions.assertThat(argumentCaptor.getAllValues()).containsExactly("a", "b", "c");
306 |     }
```

## org.mockitousage.matchers.CapturingArgumentsTest.should_capture_vararg()
Resolved declaration: org.mockitousage.matchers.CapturingArgumentsTest.should_capture_vararg()
Source: test/org/mockitousage/matchers/CapturingArgumentsTest.java

```java
253 |     @Test
254 |     public void should_capture_vararg() throws Exception {
255 |         // given
256 |         ArgumentCaptor<String> argumentCaptor = ArgumentCaptor.forClass(String.class);
257 | 
258 |         // when
259 |         mock.mixedVarargs(42, "a", "b", "c");
260 | 
261 |         // then
262 |         verify(mock).mixedVarargs(any(), argumentCaptor.capture());
263 |         Assertions.assertThat(argumentCaptor.getAllValues()).containsExactly("a", "b", "c");
264 |     }
```

## org.mockitousage.matchers.CapturingArgumentsTest.captures_correctly_when_captor_used_on_pure_vararg_method()
Resolved declaration: org.mockitousage.matchers.CapturingArgumentsTest.captures_correctly_when_captor_used_on_pure_vararg_method()
Source: test/org/mockitousage/matchers/CapturingArgumentsTest.java

```java
308 |     @Test
309 |     public void captures_correctly_when_captor_used_on_pure_vararg_method() throws Exception {
310 |         // given
311 |         ArgumentCaptor<String> argumentCaptor = ArgumentCaptor.forClass(String.class);
312 | 
313 |         // when
314 |         mock.varargs(42, "capturedValue");
315 | 
316 |         // then
317 |         verify(mock).varargs(eq(42), argumentCaptor.capture());
318 |         Assertions.assertThat(argumentCaptor.getValue()).contains("capturedValue");
319 |     }
```

## org.mockitousage.matchers.CapturingArgumentsTest.should_capture_byte_vararg_by_creating_captor_with_primitive_wrapper()
Resolved declaration: org.mockitousage.matchers.CapturingArgumentsTest.should_capture_byte_vararg_by_creating_captor_with_primitive_wrapper()
Source: test/org/mockitousage/matchers/CapturingArgumentsTest.java

```java
239 |     @Test
240 |     public void should_capture_byte_vararg_by_creating_captor_with_primitive_wrapper() throws Exception {
241 |         // given
242 |         ArgumentCaptor<Byte> argumentCaptor = ArgumentCaptor.forClass(Byte.class);
243 | 
244 |         // when
245 |         mock.varargsbyte((byte) 1, (byte) 2);
246 | 
247 |         // then
248 |         verify(mock).varargsbyte(argumentCaptor.capture());
249 |         assertEquals((byte) 2, (byte) argumentCaptor.getValue());
250 |         Assertions.assertThat(argumentCaptor.getAllValues()).containsExactly((byte) 1, (byte) 2);
251 |     }
```

## org.mockitousage.matchers.CapturingArgumentsTest.should_capture_byte_vararg_by_creating_captor_with_primitive()
Resolved declaration: org.mockitousage.matchers.CapturingArgumentsTest.should_capture_byte_vararg_by_creating_captor_with_primitive()
Source: test/org/mockitousage/matchers/CapturingArgumentsTest.java

```java
225 |     @Test
226 |     public void should_capture_byte_vararg_by_creating_captor_with_primitive() throws Exception {
227 |         // given
228 |         ArgumentCaptor<Byte> argumentCaptor = ArgumentCaptor.forClass(byte.class);
229 | 
230 |         // when
231 |         mock.varargsbyte((byte) 1, (byte) 2);
232 | 
233 |         // then
234 |         verify(mock).varargsbyte(argumentCaptor.capture());
235 |         assertEquals((byte) 2, (byte) argumentCaptor.getValue());
236 |         Assertions.assertThat(argumentCaptor.getAllValues()).containsExactly((byte) 1, (byte) 2);
237 |     }
```
