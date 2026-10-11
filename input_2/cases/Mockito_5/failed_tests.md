# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitointegration.NoJUnitDependenciesTest.pure_mockito_should_not_depend_JUnit()
Resolved declaration: org.mockitointegration.NoJUnitDependenciesTest.pure_mockito_should_not_depend_JUnit()
Source: test/org/mockitointegration/NoJUnitDependenciesTest.java

```java
13 |     @Test
14 |     public void pure_mockito_should_not_depend_JUnit() throws Exception {
15 |         ClassLoader classLoader_without_JUnit = ClassLoaders.excludingClassLoader()
16 |                 .withCodeSourceUrlOf(
17 |                         Mockito.class,
18 |                         Matcher.class,
19 |                         Enhancer.class,
20 |                         Objenesis.class
21 |                 )
22 |                 .without("junit", "org.junit")
23 |                 .build();
24 | 
25 |         Set<String> pureMockitoAPIClasses = ClassLoaders.in(classLoader_without_JUnit).omit("runners", "junit", "JUnit").listOwnedClasses();
26 | 
27 |         for (String pureMockitoAPIClass : pureMockitoAPIClasses) {
28 |             checkDependency(classLoader_without_JUnit, pureMockitoAPIClass);
29 |         }
30 |     }
```
