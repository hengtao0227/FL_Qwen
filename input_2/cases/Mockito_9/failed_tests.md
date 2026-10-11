# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.abstractMethodStubbed()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.abstractMethodStubbed()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
116 |     @Test
117 |     public void abstractMethodStubbed() {
118 |     	AbstractThing thing = spy(AbstractThing.class);
119 |     	when(thing.name()).thenReturn("me");
120 |     	assertEquals("abstract me", thing.fullName());
121 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.testCallsRealInterfaceMethod()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.testCallsRealInterfaceMethod()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
123 |     @Test
124 |     public void testCallsRealInterfaceMethod() {
125 |     	List<String> list = mock(List.class, withSettings().defaultAnswer(CALLS_REAL_METHODS));
126 |     	assertNull(list.get(1));
127 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.abstractMethodReturnsDefault()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.abstractMethodReturnsDefault()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
110 |     @Test
111 |     public void abstractMethodReturnsDefault() {
112 |     	AbstractThing thing = spy(AbstractThing.class);
113 |     	assertEquals("abstract null", thing.fullName());
114 |     }
```
