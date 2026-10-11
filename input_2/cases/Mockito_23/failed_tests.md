# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.stubbing.DeepStubsSerializableTest.should_serialize_and_deserialize_mock_created_by_deep_stubs()
Resolved declaration: org.mockitousage.stubbing.DeepStubsSerializableTest.should_serialize_and_deserialize_mock_created_by_deep_stubs()
Source: test/org/mockitousage/stubbing/DeepStubsSerializableTest.java

```java
17 |     @Test
18 |     public void should_serialize_and_deserialize_mock_created_by_deep_stubs() throws Exception {
19 |         // given
20 |         SampleClass sampleClass = mock(SampleClass.class, withSettings().defaultAnswer(Mockito.RETURNS_DEEP_STUBS).serializable());
21 |         when(sampleClass.getSample().isSth()).thenReturn(STUBBED_BOOLEAN_VALUE);
22 |         when(sampleClass.getSample().getNumber()).thenReturn(STUBBED_INTEGER_VALUE);
23 | 
24 |         // when
25 |         Object o = SimpleSerializationUtil.serializeAndBack(sampleClass);
26 | 
27 |         // then
28 |         assertThat(o).isInstanceOf(SampleClass.class);
29 |         SampleClass deserializedSample = (SampleClass) o;
30 |         assertThat(deserializedSample.getSample().isSth()).isEqualTo(STUBBED_BOOLEAN_VALUE);
31 |         assertThat(deserializedSample.getSample().getNumber()).isEqualTo(STUBBED_INTEGER_VALUE);
32 |     }
```
