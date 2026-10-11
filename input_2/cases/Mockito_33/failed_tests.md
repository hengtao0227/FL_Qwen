# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.InheritedGenericsPolimorphicCallTest.shouldStubbingWork()
Resolved declaration: org.mockitousage.bugs.InheritedGenericsPolimorphicCallTest.shouldStubbingWork()
Source: test/org/mockitousage/bugs/InheritedGenericsPolimorphicCallTest.java

```java
36 |     @Test
37 |     public void shouldStubbingWork() {
38 |         Mockito.when(iterable.iterator()).thenReturn(myIterator);
39 |         Assert.assertNotNull(((Iterable) iterable).iterator());
40 |         Assert.assertNotNull(iterable.iterator());
41 |     }
```

## org.mockitousage.bugs.InheritedGenericsPolimorphicCallTest.shouldVerificationWorks()
Resolved declaration: org.mockitousage.bugs.InheritedGenericsPolimorphicCallTest.shouldVerificationWorks()
Source: test/org/mockitousage/bugs/InheritedGenericsPolimorphicCallTest.java

```java
43 |     @Test
44 |     public void shouldVerificationWorks() {
45 |         iterable.iterator();
46 |         
47 |         verify(iterable).iterator();
48 |         verify((Iterable) iterable).iterator();
49 |     }
```
