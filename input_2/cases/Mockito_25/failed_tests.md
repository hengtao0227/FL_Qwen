# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.will_return_default_value_on_non_mockable_nested_generic()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.will_return_default_value_on_non_mockable_nested_generic()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsGenericDeepStubsTest.java

```java
92 |     @Test
93 |     public void will_return_default_value_on_non_mockable_nested_generic() throws Exception {
94 |         GenericsNest<?> genericsNest = mock(GenericsNest.class, RETURNS_DEEP_STUBS);
95 |         ListOfInteger listOfInteger = mock(ListOfInteger.class, RETURNS_DEEP_STUBS);
96 | 
97 |         assertThat(genericsNest.returningNonMockableNestedGeneric().keySet().iterator().next()).isNull();
98 |         assertThat(listOfInteger.get(25)).isEqualTo(0);
99 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_multiple_type_variable_bounds_when_return_type_of_parameterized_method_is_a_typevar_that_is_referencing_a_typevar_on_class()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_multiple_type_variable_bounds_when_return_type_of_parameterized_method_is_a_typevar_that_is_referencing_a_typevar_on_class()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsGenericDeepStubsTest.java

```java
67 |     @Test
68 |     public void can_create_mock_from_multiple_type_variable_bounds_when_return_type_of_parameterized_method_is_a_typevar_that_is_referencing_a_typevar_on_class() throws Exception {
69 |         GenericsNest<?> mock = mock(GenericsNest.class, RETURNS_DEEP_STUBS);
70 | 
71 |         Cloneable cloneable_bound_of_typevar_K_referenced_by_typevar_O = (Cloneable) mock.typeVarWithTypeParams();
72 |         Comparable<?> comparable_bound_of_typevar_K_referenced_by_typevar_O = (Comparable) mock.typeVarWithTypeParams();
73 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_return_types_declared_with_a_bounded_wildcard()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_return_types_declared_with_a_bounded_wildcard()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsGenericDeepStubsTest.java

```java
75 |     @Test
76 |     public void can_create_mock_from_return_types_declared_with_a_bounded_wildcard() throws Exception {
77 |         GenericsNest<?> mock = mock(GenericsNest.class, RETURNS_DEEP_STUBS);
78 | 
79 |         List<? super Integer> objects = mock.returningWildcard();
80 |         Number type_that_is_the_upper_bound_of_the_wildcard = (Number) mock.returningWildcard().get(45);
81 |         type_that_is_the_upper_bound_of_the_wildcard.floatValue();
82 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_multiple_type_variable_bounds_when_return_type_of_parameterized_method_is_a_parameterizedtype_that_is_referencing_a_typevar_on_class()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_multiple_type_variable_bounds_when_return_type_of_parameterized_method_is_a_parameterizedtype_that_is_referencing_a_typevar_on_class()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsGenericDeepStubsTest.java

```java
49 |     @Test
50 |     public void can_create_mock_from_multiple_type_variable_bounds_when_return_type_of_parameterized_method_is_a_parameterizedtype_that_is_referencing_a_typevar_on_class() throws Exception {
51 |         GenericsNest<?> mock = mock(GenericsNest.class, RETURNS_DEEP_STUBS);
52 | 
53 |         Cloneable cloneable_bound_that_is_declared_on_typevar_K_in_the_class_which_is_referenced_by_typevar_O_declared_on_the_method =
54 |                 mock.paramTypeWithTypeParams().get(0);
55 |         Comparable<?> comparable_bound_that_is_declared_on_typevar_K_in_the_class_which_is_referenced_by_typevar_O_declared_on_the_method =
56 |                 mock.paramTypeWithTypeParams().get(0);
57 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.generic_deep_mock_frenzy__look_at_these_chained_calls()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.generic_deep_mock_frenzy__look_at_these_chained_calls()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsGenericDeepStubsTest.java

```java
33 |     @Test
34 |     public void generic_deep_mock_frenzy__look_at_these_chained_calls() throws Exception {
35 |         GenericsNest<?> mock = mock(GenericsNest.class, RETURNS_DEEP_STUBS);
36 | 
37 |         Set<? extends Map.Entry<? extends Cloneable, Set<Number>>> entries = mock.entrySet();
38 |         Iterator<? extends Map.Entry<? extends Cloneable,Set<Number>>> entriesIterator = mock.entrySet().iterator();
39 |         Map.Entry<? extends Cloneable, Set<Number>> nextEntry = mock.entrySet().iterator().next();
40 | 
41 |         Cloneable cloneableKey = mock.entrySet().iterator().next().getKey();
42 |         Comparable<?> comparableKey = mock.entrySet().iterator().next().getKey();
43 | 
44 |         Set<Number> value = mock.entrySet().iterator().next().getValue();
45 |         Iterator<Number> numbersIterator = mock.entrySet().iterator().next().getValue().iterator();
46 |         Number number = mock.entrySet().iterator().next().getValue().iterator().next();
47 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_multiple_type_variable_bounds_when_method_return_type_is_referencing_a_typevar_on_class()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsGenericDeepStubsTest.can_create_mock_from_multiple_type_variable_bounds_when_method_return_type_is_referencing_a_typevar_on_class()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsGenericDeepStubsTest.java

```java
59 |     @Test
60 |     public void can_create_mock_from_multiple_type_variable_bounds_when_method_return_type_is_referencing_a_typevar_on_class() throws Exception {
61 |         GenericsNest<?> mock = mock(GenericsNest.class, RETURNS_DEEP_STUBS);
62 | 
63 |         Cloneable cloneable_bound_of_typevar_K = mock.returningK();
64 |         Comparable<?> comparable_bound_of_typevar_K = mock.returningK();
65 |     }
```
