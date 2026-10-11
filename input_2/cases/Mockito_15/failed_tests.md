# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.InjectMocksShouldTryPropertySettersFirstBeforeFieldAccessTest.shouldInjectUsingPropertySetterIfAvailable()
Resolved declaration: org.mockitousage.bugs.InjectMocksShouldTryPropertySettersFirstBeforeFieldAccessTest.shouldInjectUsingPropertySetterIfAvailable()
Source: test/org/mockitousage/bugs/InjectMocksShouldTryPropertySettersFirstBeforeFieldAccessTest.java

```java
23 |     @Test
24 |     public void shouldInjectUsingPropertySetterIfAvailable() {
25 |         assertTrue(awaitingInjection.propertySetterUsed);
26 |     }
```
