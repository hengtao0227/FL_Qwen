# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.ClassUtilsTest.testToClass_object()
Resolved declaration: org.apache.commons.lang3.ClassUtilsTest.testToClass_object()
Source: src/test/java/org/apache/commons/lang3/ClassUtilsTest.java

```java
902 |     public void testToClass_object() {
903 |         assertNull(ClassUtils.toClass(null));
904 | 
905 |         assertSame(ArrayUtils.EMPTY_CLASS_ARRAY, ClassUtils.toClass(ArrayUtils.EMPTY_OBJECT_ARRAY));
906 | 
907 |         assertTrue(Arrays.equals(new Class[] { String.class, Integer.class, Double.class },
908 |                 ClassUtils.toClass(new Object[] { "Test", 1, 99d })));
909 | 
910 |         assertTrue(Arrays.equals(new Class[] { String.class, null, Double.class },
911 |                 ClassUtils.toClass(new Object[] { "Test", null, 99d })));
912 |     }
```
