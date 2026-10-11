# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.creation.instance.ConstructorInstantiatorTest.creates_instances_of_inner_classes()
Resolved declaration: org.mockito.internal.creation.instance.ConstructorInstantiatorTest.creates_instances_of_inner_classes()
Source: test/org/mockito/internal/creation/instance/ConstructorInstantiatorTest.java

```java
19 |     @Test public void creates_instances_of_inner_classes() {
20 |         assertEquals(new ConstructorInstantiator(this).newInstance(SomeInnerClass.class).getClass(), SomeInnerClass.class);
21 |         assertEquals(new ConstructorInstantiator(new ChildOfThis()).newInstance(SomeInnerClass.class).getClass(), SomeInnerClass.class);
22 |     }
```
