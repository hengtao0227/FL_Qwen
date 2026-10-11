# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.util.reflection.GenericMetadataSupportTest.typeVariable_of_self_type()
Resolved declaration: org.mockito.internal.util.reflection.GenericMetadataSupportTest.typeVariable_of_self_type()
Source: test/org/mockito/internal/util/reflection/GenericMetadataSupportTest.java

```java
50 |     @Test
51 |     public void typeVariable_of_self_type() {
52 |         GenericMetadataSupport genericMetadata = inferFrom(GenericsSelfReference.class).resolveGenericReturnType(firstNamedMethod("self", GenericsSelfReference.class));
53 | 
54 |         assertThat(genericMetadata.rawType()).isEqualTo(GenericsSelfReference.class);
55 |     }
```
