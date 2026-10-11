# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.exceptions.ReporterTest.can_use_print_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_no_more_interaction_wanted_in_order()
Resolved declaration: org.mockito.exceptions.ReporterTest.can_use_print_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_no_more_interaction_wanted_in_order()
Source: test/org/mockito/exceptions/ReporterTest.java

```java
44 |     @Test(expected = VerificationInOrderFailure.class)
45 |     public void can_use_print_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_no_more_interaction_wanted_in_order() throws Exception {
46 |         Invocation invocation_with_bogus_default_answer = new InvocationBuilder().mock(mock(IMethods.class, new Returns(false))).toInvocation();
47 |         new Reporter().noMoreInteractionsWantedInOrder(invocation_with_bogus_default_answer);
48 |     }
```

## org.mockito.exceptions.ReporterTest.can_use_print_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_injection_failure()
Resolved declaration: org.mockito.exceptions.ReporterTest.can_use_print_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_injection_failure()
Source: test/org/mockito/exceptions/ReporterTest.java

```java
76 |     @Test(expected = MockitoException.class)
77 |     public void can_use_print_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_injection_failure() throws Exception {
78 |         IMethods mock_with_bogus_default_answer = mock(IMethods.class, new Returns(false));
79 |         new Reporter().cannotInjectDependency(someField(), mock_with_bogus_default_answer, new Exception());
80 |     }
```

## org.mockito.exceptions.ReporterTest.can_use_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_no_more_interaction_wanted()
Resolved declaration: org.mockito.exceptions.ReporterTest.can_use_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_no_more_interaction_wanted()
Source: test/org/mockito/exceptions/ReporterTest.java

```java
38 |     @Test(expected = NoInteractionsWanted.class)
39 |     public void can_use_mock_name_even_when_mock_bogus_default_answer_and_when_reporting_no_more_interaction_wanted() throws Exception {
40 |         Invocation invocation_with_bogus_default_answer = new InvocationBuilder().mock(mock(IMethods.class, new Returns(false))).toInvocation();
41 |         new Reporter().noMoreInteractionsWanted(invocation_with_bogus_default_answer, Collections.<VerificationAwareInvocation>emptyList());
42 |     }
```

## org.mockitousage.bugs.ClassCastExOnVerifyZeroInteractionsTest.should_not_throw_a_ClassCastException()
Resolved declaration: org.mockitousage.bugs.ClassCastExOnVerifyZeroInteractionsTest.should_not_throw_a_ClassCastException()
Source: test/org/mockitousage/bugs/ClassCastExOnVerifyZeroInteractionsTest.java

```java
16 |     @Test(expected = NoInteractionsWanted.class)
17 |     public void should_not_throw_a_ClassCastException() {
18 |         TestMock test = mock(TestMock.class, new Answer() {
19 |             public Object answer(InvocationOnMock invocation) throws Throwable {
20 |                 return false;
21 |             }
22 |         });
23 |         test.m1();
24 |         verifyZeroInteractions(test);
25 |     }
```
