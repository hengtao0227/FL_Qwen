# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.SpyShouldHaveNiceNameTest.shouldPrintNiceName()
Resolved declaration: org.mockitousage.bugs.SpyShouldHaveNiceNameTest.shouldPrintNiceName()
Source: test/org/mockitousage/bugs/SpyShouldHaveNiceNameTest.java

```java
22 |     @Test
23 |     public void shouldPrintNiceName() {
24 |         //when
25 |         veryCoolSpy.add(1);
26 | 
27 |         try {
28 |             verify(veryCoolSpy).add(2);
29 |             fail();
30 |         } catch(AssertionError e) {
31 |             Assertions.assertThat(e.getMessage()).contains("veryCoolSpy");
32 |         }
33 |     }
```
