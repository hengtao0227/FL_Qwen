# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.SerializationUtilsTest.testPrimitiveTypeClassSerialization()
Resolved declaration: org.apache.commons.lang3.SerializationUtilsTest.testPrimitiveTypeClassSerialization()
Source: src/test/java/org/apache/commons/lang3/SerializationUtilsTest.java

```java
368 |     public void testPrimitiveTypeClassSerialization() {
369 |         Class<?>[] primitiveTypes = { byte.class, short.class, int.class, long.class, float.class, double.class,
370 |                 boolean.class, char.class, void.class };
371 | 
372 |         for (Class<?> primitiveType : primitiveTypes) {
373 |             Class<?> clone = SerializationUtils.clone(primitiveType);
374 |             assertEquals(primitiveType, clone);
375 |         }
376 |     }
```
