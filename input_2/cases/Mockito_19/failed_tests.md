# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.annotation.MockInjectionUsingSetterOrPropertyTest.shouldInsertFieldWithCorrectNameWhenMultipleTypesAvailable()
Resolved declaration: org.mockitousage.annotation.MockInjectionUsingSetterOrPropertyTest.shouldInsertFieldWithCorrectNameWhenMultipleTypesAvailable()
Source: test/org/mockitousage/annotation/MockInjectionUsingSetterOrPropertyTest.java

```java
112 |     @Test
113 | 	public void shouldInsertFieldWithCorrectNameWhenMultipleTypesAvailable() {
114 | 		MockitoAnnotations.initMocks(this);
115 | 		assertNull(otherSuperUnderTesting.candidate1);
116 | 		assertNotNull(otherSuperUnderTesting.candidate2);
117 | 	}
```
