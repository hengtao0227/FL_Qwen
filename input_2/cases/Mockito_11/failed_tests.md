# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.creation.DelegatingMethodTest.equals_should_return_true_when_equal()
Resolved declaration: org.mockito.internal.creation.DelegatingMethodTest.equals_should_return_true_when_equal()
Source: test/org/mockito/internal/creation/DelegatingMethodTest.java

```java
27 |     @Test
28 |     public void equals_should_return_true_when_equal() throws Exception {
29 |         DelegatingMethod equal = new DelegatingMethod(someMethod);
30 |         assertTrue(delegatingMethod.equals(equal));
31 |     }
```

## org.mockito.internal.creation.DelegatingMethodTest.equals_should_return_true_when_self()
Resolved declaration: org.mockito.internal.creation.DelegatingMethodTest.equals_should_return_true_when_self()
Source: test/org/mockito/internal/creation/DelegatingMethodTest.java

```java
33 |     @Test
34 |     public void equals_should_return_true_when_self() throws Exception {
35 |         assertTrue(delegatingMethod.equals(delegatingMethod));
36 |     }
```
