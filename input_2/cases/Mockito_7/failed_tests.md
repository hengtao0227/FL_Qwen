# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.deepstubs.DeepStubFailingWhenGenricNestedAsRawTypeTest.discoverDeepMockingOfGenerics()
Resolved declaration: org.mockitousage.bugs.deepstubs.DeepStubFailingWhenGenricNestedAsRawTypeTest.discoverDeepMockingOfGenerics()
Source: test/org/mockitousage/bugs/deepstubs/DeepStubFailingWhenGenricNestedAsRawTypeTest.java

```java
23 |   @Test
24 |   public void discoverDeepMockingOfGenerics() {
25 |     MyClass1 myMock1 = mock(MyClass1.class, RETURNS_DEEP_STUBS);
26 |     when(myMock1.getNested().getNested().returnSomething()).thenReturn("Hello World.");
27 |   }
```
