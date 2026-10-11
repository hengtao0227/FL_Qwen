# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.invocation.InvocationMatcherTest.should_capture_arguments_when_args_count_does_NOT_match()
Resolved declaration: org.mockito.internal.invocation.InvocationMatcherTest.should_capture_arguments_when_args_count_does_NOT_match()
Source: test/org/mockito/internal/invocation/InvocationMatcherTest.java

```java
157 |     @Test  // like using several time the captor in the vararg
158 |     public void should_capture_arguments_when_args_count_does_NOT_match() throws Exception {
159 |         //given
160 |         mock.varargs();
161 |         Invocation invocation = getLastInvocation();
162 | 
163 |         //when
164 |         InvocationMatcher invocationMatcher = new InvocationMatcher(invocation, (List) asList(new LocalizedMatcher(AnyVararg.ANY_VARARG)));
165 | 
166 |         //then
167 |         invocationMatcher.captureArgumentsFrom(invocation);
168 |     }
```

## org.mockito.internal.util.reflection.FieldInitializerTest.can_instantiate_class_with_parameterized_constructor()
Resolved declaration: org.mockito.internal.util.reflection.FieldInitializerTest.can_instantiate_class_with_parameterized_constructor()
Source: test/org/mockito/internal/util/reflection/FieldInitializerTest.java

```java
157 |     @Test
158 |     public void can_instantiate_class_with_parameterized_constructor() throws Exception {
159 |         ConstructorArgumentResolver resolver = given(mock(ConstructorArgumentResolver.class).resolveTypeInstances(any(Class[].class)))
160 |                         .willReturn(new Object[]{null}).getMock();
161 | 
162 |         new FieldInitializer(this, field("noDefaultConstructor"), resolver).initialize();
163 | 
164 |         assertNotNull(noDefaultConstructor);
165 |     }
```

## org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_report_failure_if_constructor_throws_exception()
Resolved declaration: org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_report_failure_if_constructor_throws_exception()
Source: test/org/mockito/internal/util/reflection/ParameterizedConstructorInstantiatorTest.java

```java
96 |     @Test
97 |     public void should_report_failure_if_constructor_throws_exception() throws Exception {
98 |         given(resolver.resolveTypeInstances(Matchers.<Class<?>[]>anyVararg())).willReturn(new Object[]{ null });
99 | 
100 |         try {
101 |             new ParameterizedConstructorInstantiator(this, field("withThrowingConstructor"), resolver).instantiate();
102 |             fail();
103 |         } catch (MockitoException e) {
104 |             assertThat(e.getMessage()).contains("constructor").contains("raised an exception");
105 |         }
106 |     }
```

## org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_fail_if_an_argument_instance_type_do_not_match_wanted_type()
Resolved declaration: org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_fail_if_an_argument_instance_type_do_not_match_wanted_type()
Source: test/org/mockito/internal/util/reflection/ParameterizedConstructorInstantiatorTest.java

```java
82 |     @Test
83 |     public void should_fail_if_an_argument_instance_type_do_not_match_wanted_type() throws Exception {
84 |         Observer observer = mock(Observer.class);
85 |         Set wrongArg = mock(Set.class);
86 |         given(resolver.resolveTypeInstances(Matchers.<Class<?>[]>anyVararg())).willReturn(new Object[]{ observer, wrongArg });
87 | 
88 |         try {
89 |             new ParameterizedConstructorInstantiator(this, field("withMultipleConstructor"), resolver).instantiate();
90 |             fail();
91 |         } catch (MockitoException e) {
92 |             assertThat(e.getMessage()).contains("argResolver").contains("incorrect types");
93 |         }
94 |     }
```

## org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_instantiate_type_with_vararg_constructor()
Resolved declaration: org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_instantiate_type_with_vararg_constructor()
Source: test/org/mockito/internal/util/reflection/ParameterizedConstructorInstantiatorTest.java

```java
108 |     @Test
109 |     public void should_instantiate_type_with_vararg_constructor() throws Exception {
110 |         Observer[] vararg = new Observer[] {  };
111 |         given(resolver.resolveTypeInstances(Matchers.<Class<?>[]>anyVararg())).willReturn(new Object[]{ "", vararg});
112 | 
113 |         new ParameterizedConstructorInstantiator(this, field("withVarargConstructor"), resolver).instantiate();
114 | 
115 |         assertNotNull(withVarargConstructor);
116 |     }
```

## org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_instantiate_type_if_resolver_provide_matching_types()
Resolved declaration: org.mockito.internal.util.reflection.ParameterizedConstructorInstantiatorTest.should_instantiate_type_if_resolver_provide_matching_types()
Source: test/org/mockito/internal/util/reflection/ParameterizedConstructorInstantiatorTest.java

```java
69 |     @Test
70 |     public void should_instantiate_type_if_resolver_provide_matching_types() throws Exception {
71 |         Observer observer = mock(Observer.class);
72 |         Map map = mock(Map.class);
73 |         given(resolver.resolveTypeInstances(Matchers.<Class<?>[]>anyVararg())).willReturn(new Object[]{ observer, map });
74 | 
75 |         new ParameterizedConstructorInstantiator(this, field("withMultipleConstructor"), resolver).instantiate();
76 | 
77 |         assertNotNull(withMultipleConstructor);
78 |         assertNotNull(withMultipleConstructor.observer);
79 |         assertNotNull(withMultipleConstructor.map);
80 |     }
```

## org.mockitousage.basicapi.ResetTest.shouldRemoveAllStubbing()
Resolved declaration: org.mockitousage.basicapi.ResetTest.shouldRemoveAllStubbing()
Source: test/org/mockitousage/basicapi/ResetTest.java

```java
45 |     @Test
46 |     public void shouldRemoveAllStubbing() throws Exception {
47 |         when(mock.objectReturningMethod(isA(Integer.class))).thenReturn(100);
48 |         when(mock.objectReturningMethod(200)).thenReturn(200);
49 |         reset(mock);
50 |         assertNull(mock.objectReturningMethod(200));
51 |         assertEquals("default behavior should return null", null, mock.objectReturningMethod("blah"));
52 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyWithNullVarArgArray()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyWithNullVarArgArray()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
125 |     @Test
126 |     public void shouldVerifyWithNullVarArgArray() {
127 |         Foo foo = Mockito.mock(Foo.class);
128 |         foo.varArgs((String[]) null);    
129 |         Mockito.verify(foo).varArgs((String[]) Mockito.anyObject());
130 |         Mockito.verify(foo).varArgs((String[]) null);
131 |     }  
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyWithAnyObject()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyWithAnyObject()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
117 |     @Test
118 |     public void shouldVerifyWithAnyObject() {
119 |         Foo foo = Mockito.mock(Foo.class);
120 |         foo.varArgs("");        
121 |         Mockito.verify(foo).varArgs((String[]) Mockito.anyObject());
122 |         Mockito.verify(foo).varArgs((String) Mockito.anyObject());
123 |     }   
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldStubBooleanVarargs()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldStubBooleanVarargs()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
60 |     @Test
61 |     public void shouldStubBooleanVarargs() {
62 |         when(mock.withBooleanVarargs(1)).thenReturn(true);
63 |         when(mock.withBooleanVarargs(1, true, false)).thenReturn(true);
64 |         
65 |         assertEquals(true, mock.withBooleanVarargs(1));
66 |         assertEquals(false, mock.withBooleanVarargs(9999));
67 |         
68 |         assertEquals(true, mock.withBooleanVarargs(1, true, false));
69 |         assertEquals(false, mock.withBooleanVarargs(1, true, false, true));
70 |         assertEquals(false, mock.withBooleanVarargs(2, true, false));
71 |         assertEquals(false, mock.withBooleanVarargs(1, true));
72 |         assertEquals(false, mock.withBooleanVarargs(1, false, false));
73 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldMatchEasilyEmptyVararg()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldMatchEasilyEmptyVararg()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
167 |     @Test
168 |     //See bug #157
169 |     public void shouldMatchEasilyEmptyVararg() throws Exception {
170 |         //when
171 |         when(mock.foo(anyVararg())).thenReturn(-1);
172 | 
173 |         //then
174 |         assertEquals(-1, mock.foo());
175 |     } 
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyBooleanVarargs()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyBooleanVarargs()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
103 |     @Test
104 |     public void shouldVerifyBooleanVarargs() {
105 |         mock.withBooleanVarargs(1);
106 |         mock.withBooleanVarargs(2, true, false, true);
107 |         mock.withBooleanVarargs(3, true, true, true);
108 | 
109 |         verify(mock).withBooleanVarargs(1);
110 |         verify(mock).withBooleanVarargs(2, true, false, true);
111 |         try {
112 |             verify(mock).withBooleanVarargs(3, true, true, true, true);
113 |             fail();
114 |         } catch (ArgumentsAreDifferent e) {}
115 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldStubCorrectlyWhenMixedVarargsUsed()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldStubCorrectlyWhenMixedVarargsUsed()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
142 |     @SuppressWarnings("all")
143 |     @Test
144 |     //See bug #31
145 |     public void shouldStubCorrectlyWhenMixedVarargsUsed() {
146 |         MixedVarargs mixedVarargs = mock(MixedVarargs.class);
147 |         when(mixedVarargs.doSomething("hello", (String[])null)).thenReturn("hello");
148 |         when(mixedVarargs.doSomething("goodbye", (String[])null)).thenReturn("goodbye");
149 | 
150 |         String result = mixedVarargs.doSomething("hello",(String[]) null);
151 |         assertEquals("hello", result);
152 |         
153 |         verify(mixedVarargs).doSomething("hello", (String[])null);
154 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldStubStringVarargs()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldStubStringVarargs()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
32 |     @SuppressWarnings("deprecation")
33 |     @Test
34 |     public void shouldStubStringVarargs() {
35 |         when(mock.withStringVarargsReturningString(1)).thenReturn("1");
36 |         when(mock.withStringVarargsReturningString(2, "1", "2", "3")).thenReturn("2");
37 |         
38 |         RuntimeException expected = new RuntimeException();
39 |         stubVoid(mock).toThrow(expected).on().withStringVarargs(3, "1", "2", "3", "4");
40 | 
41 |         assertEquals("1", mock.withStringVarargsReturningString(1));
42 |         assertEquals(null, mock.withStringVarargsReturningString(2));
43 |         
44 |         assertEquals("2", mock.withStringVarargsReturningString(2, "1", "2", "3"));
45 |         assertEquals(null, mock.withStringVarargsReturningString(2, "1", "2"));
46 |         assertEquals(null, mock.withStringVarargsReturningString(2, "1", "2", "3", "4"));
47 |         assertEquals(null, mock.withStringVarargsReturningString(2, "1", "2", "9999"));
48 |         
49 |         mock.withStringVarargs(3, "1", "2", "3", "9999");
50 |         mock.withStringVarargs(9999, "1", "2", "3", "4");
51 |         
52 |         try {
53 |             mock.withStringVarargs(3, "1", "2", "3", "4");
54 |             fail();
55 |         } catch (Exception e) {
56 |             assertEquals(expected, e);
57 |         }
58 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldStubCorrectlyWhenDoubleStringAndMixedVarargsUsed()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldStubCorrectlyWhenDoubleStringAndMixedVarargsUsed()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
156 |     @SuppressWarnings("all")
157 |     @Test
158 |     public void shouldStubCorrectlyWhenDoubleStringAndMixedVarargsUsed() {
159 |         MixedVarargs mixedVarargs = mock(MixedVarargs.class);
160 |         when(mixedVarargs.doSomething("one", "two", (String[])null)).thenReturn("hello");
161 |         when(mixedVarargs.doSomething("1", "2", (String[])null)).thenReturn("goodbye");
162 | 
163 |         String result = mixedVarargs.doSomething("one", "two", (String[])null);
164 |         assertEquals("hello", result);
165 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyStringVarargs()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyStringVarargs()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
75 |     @Test
76 |     public void shouldVerifyStringVarargs() {
77 |         mock.withStringVarargs(1);
78 |         mock.withStringVarargs(2, "1", "2", "3");
79 |         mock.withStringVarargs(3, "1", "2", "3", "4");
80 | 
81 |         verify(mock).withStringVarargs(1);
82 |         verify(mock).withStringVarargs(2, "1", "2", "3");
83 |         try {
84 |             verify(mock).withStringVarargs(2, "1", "2", "79", "4");
85 |             fail();
86 |         } catch (ArgumentsAreDifferent e) {}
87 |     }
```

## org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyObjectVarargs()
Resolved declaration: org.mockitousage.basicapi.UsingVarargsTest.shouldVerifyObjectVarargs()
Source: test/org/mockitousage/basicapi/UsingVarargsTest.java

```java
89 |     @Test
90 |     public void shouldVerifyObjectVarargs() {
91 |         mock.withObjectVarargs(1);
92 |         mock.withObjectVarargs(2, "1", new ArrayList<Object>(), new Integer(1));
93 |         mock.withObjectVarargs(3, new Integer(1));
94 | 
95 |         verify(mock).withObjectVarargs(1);
96 |         verify(mock).withObjectVarargs(2, "1", new ArrayList<Object>(), new Integer(1));
97 |         try {
98 |             verifyNoMoreInteractions(mock);
99 |             fail();
100 |         } catch (NoInteractionsWanted e) {}
101 |     }
```

## org.mockitousage.bugs.VarargsErrorWhenCallingRealMethodTest.shouldNotThrowAnyException()
Resolved declaration: org.mockitousage.bugs.VarargsErrorWhenCallingRealMethodTest.shouldNotThrowAnyException()
Source: test/org/mockitousage/bugs/VarargsErrorWhenCallingRealMethodTest.java

```java
20 |     @Test
21 |     public void shouldNotThrowAnyException() throws Exception {
22 |         Foo foo = mock(Foo.class);
23 | 
24 |         when(foo.blah(anyString(), anyString())).thenCallRealMethod();
25 | 
26 |         assertEquals(1, foo.blah("foo", "bar"));
27 |     }
```

## org.mockitousage.bugs.varargs.VarargsAndAnyObjectPicksUpExtraInvocationsTest.shouldVerifyCorrectlyWithAnyVarargs()
Resolved declaration: org.mockitousage.bugs.varargs.VarargsAndAnyObjectPicksUpExtraInvocationsTest.shouldVerifyCorrectlyWithAnyVarargs()
Source: test/org/mockitousage/bugs/varargs/VarargsAndAnyObjectPicksUpExtraInvocationsTest.java

```java
23 |     @Test
24 |     public void shouldVerifyCorrectlyWithAnyVarargs() {
25 |         //when
26 |         table.newRow("qux", "foo", "bar", "baz");
27 |         table.newRow("abc", "def");
28 |         
29 |         //then
30 |         verify(table, times(2)).newRow(anyString(), (String[]) anyVararg());
31 |     }
```

## org.mockitousage.bugs.varargs.VarargsAndAnyObjectPicksUpExtraInvocationsTest.shouldVerifyCorrectlyNumberOfInvocationsUsingAnyVarargAndEqualArgument()
Resolved declaration: org.mockitousage.bugs.varargs.VarargsAndAnyObjectPicksUpExtraInvocationsTest.shouldVerifyCorrectlyNumberOfInvocationsUsingAnyVarargAndEqualArgument()
Source: test/org/mockitousage/bugs/varargs/VarargsAndAnyObjectPicksUpExtraInvocationsTest.java

```java
33 |     @Test
34 |     public void shouldVerifyCorrectlyNumberOfInvocationsUsingAnyVarargAndEqualArgument() {
35 |         //when
36 |         table.newRow("x", "foo", "bar", "baz");
37 |         table.newRow("x", "def");
38 | 
39 |         //then
40 |         verify(table, times(2)).newRow(eq("x"), (String[]) anyVararg());
41 |     }
```

## org.mockitousage.bugs.varargs.VarargsNotPlayingWithAnyObjectTest.shouldStubUsingAnyVarargs()
Resolved declaration: org.mockitousage.bugs.varargs.VarargsNotPlayingWithAnyObjectTest.shouldStubUsingAnyVarargs()
Source: test/org/mockitousage/bugs/varargs/VarargsNotPlayingWithAnyObjectTest.java

```java
49 |     @Test
50 |     public void shouldStubUsingAnyVarargs() {
51 |         when(mock.run((String[]) anyVararg())).thenReturn("foo");
52 |         
53 |         assertEquals("foo", mock.run("a", "b"));
54 |     }
```

## org.mockitousage.matchers.VerificationAndStubbingUsingMatchersTest.shouldVerifyUsingMatchers()
Resolved declaration: org.mockitousage.matchers.VerificationAndStubbingUsingMatchersTest.shouldVerifyUsingMatchers()
Source: test/org/mockitousage/matchers/VerificationAndStubbingUsingMatchersTest.java

```java
50 |     @SuppressWarnings("deprecation")
51 |     @Test
52 |     public void shouldVerifyUsingMatchers() {
53 |         stubVoid(one).toThrow(new RuntimeException()).on().oneArg(true);
54 |         when(three.varargsObject(5, "first arg", "second arg")).thenReturn("stubbed");
55 | 
56 |         try {
57 |             one.oneArg(true);
58 |             fail();
59 |         } catch (RuntimeException e) {}
60 | 
61 |         one.simpleMethod(100);
62 |         two.simpleMethod("test Mockito");
63 |         three.varargsObject(10, "first arg", "second arg");
64 |         
65 |         assertEquals("stubbed", three.varargsObject(5, "first arg", "second arg"));
66 | 
67 |         verify(one).oneArg(eq(true));
68 |         verify(one).simpleMethod(anyInt());
69 |         verify(two).simpleMethod(startsWith("test"));
70 |         verify(three).varargsObject(5, "first arg", "second arg");
71 |         verify(three).varargsObject(eq(10), eq("first arg"), startsWith("second"));
72 |         
73 |         verifyNoMoreInteractions(one, two, three);
74 |         
75 |         try {
76 |             verify(three).varargsObject(eq(10), eq("first arg"), startsWith("third"));
77 |             fail();
78 |         } catch (WantedButNotInvoked e) {}
79 |     }
```

## org.mockitousage.stubbing.BasicStubbingTest.test_stub_only_not_verifiable()
Resolved declaration: org.mockitousage.stubbing.BasicStubbingTest.test_stub_only_not_verifiable()
Source: test/org/mockitousage/stubbing/BasicStubbingTest.java

```java
99 |     @Test
100 |     public void test_stub_only_not_verifiable() throws Exception {
101 |         IMethods localMock = mock(IMethods.class, withSettings().stubOnly());
102 | 
103 |         when(localMock.objectReturningMethod(isA(Integer.class))).thenReturn(100);
104 |         when(localMock.objectReturningMethod(200)).thenReturn(200);
105 | 
106 |         assertEquals(200, localMock.objectReturningMethod(200));
107 |         assertEquals(100, localMock.objectReturningMethod(666));
108 |         assertEquals("default behavior should return null", null, localMock.objectReturningMethod("blah"));
109 | 
110 |         try {
111 |             verify(localMock, atLeastOnce()).objectReturningMethod(eq(200));
112 |             fail();
113 |         } catch (CannotVerifyStubOnlyMock e) {}
114 |     }
```

## org.mockitousage.stubbing.BasicStubbingTest.should_evaluate_latest_stubbing_first()
Resolved declaration: org.mockitousage.stubbing.BasicStubbingTest.should_evaluate_latest_stubbing_first()
Source: test/org/mockitousage/stubbing/BasicStubbingTest.java

```java
28 |     @Test
29 |     public void should_evaluate_latest_stubbing_first() throws Exception {
30 |         when(mock.objectReturningMethod(isA(Integer.class))).thenReturn(100);
31 |         when(mock.objectReturningMethod(200)).thenReturn(200);
32 |         
33 |         assertEquals(200, mock.objectReturningMethod(200));
34 |         assertEquals(100, mock.objectReturningMethod(666));
35 |         assertEquals("default behavior should return null", null, mock.objectReturningMethod("blah"));
36 |     }
```

## org.mockitousage.stubbing.DeprecatedStubbingTest.shouldEvaluateLatestStubbingFirst()
Resolved declaration: org.mockitousage.stubbing.DeprecatedStubbingTest.shouldEvaluateLatestStubbingFirst()
Source: test/org/mockitousage/stubbing/DeprecatedStubbingTest.java

```java
28 |     @Test
29 |     public void shouldEvaluateLatestStubbingFirst() throws Exception {
30 |         stub(mock.objectReturningMethod(isA(Integer.class))).toReturn(100);
31 |         stub(mock.objectReturningMethod(200)).toReturn(200);
32 |         
33 |         assertEquals(200, mock.objectReturningMethod(200));
34 |         assertEquals(100, mock.objectReturningMethod(666));
35 |         assertEquals("default behavior should return null", null, mock.objectReturningMethod("blah"));
36 |     }
```

## org.mockitousage.verification.VerificationInOrderMixedWithOrdiraryVerificationTest.shouldUseEqualsToVerifyMethodVarargs()
Resolved declaration: org.mockitousage.verification.VerificationInOrderMixedWithOrdiraryVerificationTest.shouldUseEqualsToVerifyMethodVarargs()
Source: test/org/mockitousage/verification/VerificationInOrderMixedWithOrdiraryVerificationTest.java

```java
145 |     @Test
146 |     public void shouldUseEqualsToVerifyMethodVarargs() {
147 |         mockOne = mock(IMethods.class);
148 |         
149 |         String textOne = "test";
150 |         String textTwo = new String(textOne);
151 |         
152 |         assertEquals(textOne, textTwo);
153 |         assertNotSame(textOne, textTwo);
154 |         
155 |         mockOne.varargsObject(1, textOne, textOne);
156 |         mockOne.varargsObject(1, textTwo, textTwo);
157 |         
158 |         verify(mockOne, times(2)).varargsObject(1, textOne, textOne);
159 |         
160 |         inOrder = inOrder(mockOne);
161 |         inOrder.verify(mockOne, times(2)).varargsObject(1, textOne, textOne);
162 |     } 
```
