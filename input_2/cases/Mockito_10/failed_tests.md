# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.DeepStubsWronglyReportsSerializationProblemsTest.should_not_raise_a_mockito_exception_about_serialization_when_accessing_deep_stub()
Resolved declaration: org.mockitousage.bugs.DeepStubsWronglyReportsSerializationProblemsTest.should_not_raise_a_mockito_exception_about_serialization_when_accessing_deep_stub()
Source: test/org/mockitousage/bugs/DeepStubsWronglyReportsSerializationProblemsTest.java

```java
14 |     @Test
15 |     public void should_not_raise_a_mockito_exception_about_serialization_when_accessing_deep_stub() {
16 |         NotSerializableShouldBeMocked the_deep_stub = mock(ToBeDeepStubbed.class, RETURNS_DEEP_STUBS).getSomething();
17 |         assertThat(the_deep_stub).isNotNull();
18 |     }
```
