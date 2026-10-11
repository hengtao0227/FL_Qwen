# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.builder.HashCodeBuilderTest.testReflectionObjectCycle()
Resolved declaration: org.apache.commons.lang3.builder.HashCodeBuilderTest.testReflectionObjectCycle()
Source: src/test/java/org/apache/commons/lang3/builder/HashCodeBuilderTest.java

```java
500 |     public void testReflectionObjectCycle() {
501 |         ReflectionTestCycleA a = new ReflectionTestCycleA();
502 |         ReflectionTestCycleB b = new ReflectionTestCycleB();
503 |         a.b = b;
504 |         b.a = a;
505 |         
506 |         // Used to caused:
507 |         // java.lang.StackOverflowError
508 |         // at java.lang.ClassLoader.getCallerClassLoader(Native Method)
509 |         // at java.lang.Class.getDeclaredFields(Class.java:992)
510 |         // at org.apache.commons.lang.builder.HashCodeBuilder.reflectionAppend(HashCodeBuilder.java:373)
511 |         // at org.apache.commons.lang.builder.HashCodeBuilder.reflectionHashCode(HashCodeBuilder.java:349)
512 |         // at org.apache.commons.lang.builder.HashCodeBuilder.reflectionHashCode(HashCodeBuilder.java:155)
513 |         // at
514 |         // org.apache.commons.lang.builder.HashCodeBuilderTest$ReflectionTestCycleB.hashCode(HashCodeBuilderTest.java:53)
515 |         // at org.apache.commons.lang.builder.HashCodeBuilder.append(HashCodeBuilder.java:422)
516 |         // at org.apache.commons.lang.builder.HashCodeBuilder.reflectionAppend(HashCodeBuilder.java:383)
517 |         // at org.apache.commons.lang.builder.HashCodeBuilder.reflectionHashCode(HashCodeBuilder.java:349)
518 |         // at org.apache.commons.lang.builder.HashCodeBuilder.reflectionHashCode(HashCodeBuilder.java:155)
519 |         // at
520 |         // org.apache.commons.lang.builder.HashCodeBuilderTest$ReflectionTestCycleA.hashCode(HashCodeBuilderTest.java:42)
521 |         // at org.apache.commons.lang.builder.HashCodeBuilder.append(HashCodeBuilder.java:422)
522 | 
523 |         a.hashCode();
524 |         assertNull(HashCodeBuilder.getRegistry());
525 |         b.hashCode();
526 |         assertNull(HashCodeBuilder.getRegistry());
527 |     }
```
