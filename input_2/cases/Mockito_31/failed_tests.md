# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.stubbing.defaultanswers.ReturnsSmartNullsTest.shouldPrintTheParametersWhenCallingAMethodWithArgs()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsSmartNullsTest.shouldPrintTheParametersWhenCallingAMethodWithArgs()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsSmartNullsTest.java

```java
51 |     @Test
52 |     public void shouldPrintTheParametersWhenCallingAMethodWithArgs() throws Throwable {
53 |     	Answer<Object> answer = new ReturnsSmartNulls();
54 | 
55 |     	Foo smartNull = (Foo) answer.answer(invocationOf(Foo.class, "withArgs", "oompa", "lumpa"));
56 | 
57 |     	assertEquals("SmartNull returned by unstubbed withArgs(oompa, lumpa) method on mock", smartNull + "");
58 |     }
```
