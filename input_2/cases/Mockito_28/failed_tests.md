# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.InjectionByTypeShouldFirstLookForExactTypeThenAncestorTest.mock_should_be_injected_once_and_in_the_best_matching_type()
Resolved declaration: org.mockitousage.bugs.InjectionByTypeShouldFirstLookForExactTypeThenAncestorTest.mock_should_be_injected_once_and_in_the_best_matching_type()
Source: test/org/mockitousage/bugs/InjectionByTypeShouldFirstLookForExactTypeThenAncestorTest.java

```java
31 |     @Test
32 |     public void mock_should_be_injected_once_and_in_the_best_matching_type() {
33 |         assertSame(REFERENCE, illegalInjectionExample.mockShouldNotGoInHere);
34 |         assertSame(mockedBean, illegalInjectionExample.mockShouldGoInHere);
35 |     }
```
