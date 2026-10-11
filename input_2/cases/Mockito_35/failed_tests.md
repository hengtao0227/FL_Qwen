# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntPassed()
Resolved declaration: org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntPassed()
Source: test/org/mockitousage/bugs/NPEWithCertainMatchersTest.java

```java
34 |     @Test
35 |     public void shouldNotThrowNPEWhenIntPassed() {
36 |         mock.intArgumentMethod(100);
37 |         
38 |         verify(mock).intArgumentMethod(isA(Integer.class));
39 |     }
```

## org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntegerPassed()
Resolved declaration: org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntegerPassed()
Source: test/org/mockitousage/bugs/NPEWithCertainMatchersTest.java

```java
27 |     @Test
28 |     public void shouldNotThrowNPEWhenIntegerPassed() {
29 |         mock.intArgumentMethod(100);
30 | 
31 |         verify(mock).intArgumentMethod(isA(Integer.class));
32 |     }
```

## org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntegerPassedToEq()
Resolved declaration: org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntegerPassedToEq()
Source: test/org/mockitousage/bugs/NPEWithCertainMatchersTest.java

```java
41 |     @Test
42 |     public void shouldNotThrowNPEWhenIntegerPassedToEq() {
43 |         mock.intArgumentMethod(100);
44 |         
45 |         verify(mock).intArgumentMethod(eq(new Integer(100)));
46 |     }
```

## org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntegerPassedToSame()
Resolved declaration: org.mockitousage.bugs.NPEWithCertainMatchersTest.shouldNotThrowNPEWhenIntegerPassedToSame()
Source: test/org/mockitousage/bugs/NPEWithCertainMatchersTest.java

```java
48 |     @Test
49 |     public void shouldNotThrowNPEWhenIntegerPassedToSame() {
50 |         mock.intArgumentMethod(100);
51 | 
52 |         verify(mock, never()).intArgumentMethod(same(new Integer(100)));
53 |     }
```
