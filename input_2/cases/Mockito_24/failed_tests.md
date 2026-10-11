# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.stubbing.defaultanswers.ReturnsEmptyValuesTest.should_return_zero_if_mock_is_compared_to_itself()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsEmptyValuesTest.should_return_zero_if_mock_is_compared_to_itself()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsEmptyValuesTest.java

```java
67 |     @Test public void should_return_zero_if_mock_is_compared_to_itself() {
68 |         //given
69 |         Date d = mock(Date.class);
70 |         d.compareTo(d);
71 |         Invocation compareTo = this.getLastInvocation();
72 | 
73 |         //when
74 |         Object result = values.answer(compareTo);
75 | 
76 |         //then
77 |         assertEquals(0, result);
78 |     }
```

## org.mockitousage.bugs.ShouldMocksCompareToBeConsistentWithEqualsTest.should_compare_to_be_consistent_with_equals_when_comparing_the_same_reference()
Resolved declaration: org.mockitousage.bugs.ShouldMocksCompareToBeConsistentWithEqualsTest.should_compare_to_be_consistent_with_equals_when_comparing_the_same_reference()
Source: test/org/mockitousage/bugs/ShouldMocksCompareToBeConsistentWithEqualsTest.java

```java
37 |     @Test
38 |     public void should_compare_to_be_consistent_with_equals_when_comparing_the_same_reference() {
39 |         //given
40 |         Date today    = mock(Date.class);
41 | 
42 |         //when
43 |         Set<Date> set = new TreeSet<Date>();
44 |         set.add(today);
45 |         set.add(today);
46 | 
47 |         //then
48 |         assertEquals(1, set.size());
49 |     }
```
