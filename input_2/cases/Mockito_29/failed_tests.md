# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenNullPassedToSame()
Resolved declaration: org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenNullPassedToSame()
Source: test/org/mockitousage/bugs/NPEWithCertainMatchersTest.java

```java
61 |     @Test(expected = AssertionError.class)
62 |     public void shouldNotThrowNPEWhenNullPassedToSame() {
63 |         mock.objectArgMethod("not null");
64 | 
65 |         verify(mock).objectArgMethod(same(null));
66 |     }
```
