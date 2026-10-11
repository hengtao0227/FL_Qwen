# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.stubbing.defaultanswers.ReturnsSmartNullsTest.shouldPrintTheParametersOnSmartNullPointerExceptionMessage()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsSmartNullsTest.shouldPrintTheParametersOnSmartNullPointerExceptionMessage()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsSmartNullsTest.java

```java
60 |     @Test
61 | 	public void shouldPrintTheParametersOnSmartNullPointerExceptionMessage() throws Throwable {
62 |     	Answer<Object> answer = new ReturnsSmartNulls();
63 | 
64 |         Foo smartNull = (Foo) answer.answer(invocationOf(Foo.class, "withArgs", "oompa", "lumpa"));
65 | 
66 |         try {
67 |             smartNull.get();
68 |             fail();
69 |         } catch (SmartNullPointerException ex) {
70 |         	String message = ex.getMessage();
71 |         	assertTrue("Exception message should include oompa and lumpa, but was: " + message,
72 |         			message.contains("oompa, lumpa"));
73 |         }
74 | 	}
```
