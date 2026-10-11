# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.matchers.AnyXMatchersAcceptNullsTest.shouldNotAcceptNullInAllAnyPrimitiveWrapperMatchers()
Resolved declaration: org.mockitousage.matchers.AnyXMatchersAcceptNullsTest.shouldNotAcceptNullInAllAnyPrimitiveWrapperMatchers()
Source: test/org/mockitousage/matchers/AnyXMatchersAcceptNullsTest.java

```java
43 |     @Test
44 |     public void shouldNotAcceptNullInAllAnyPrimitiveWrapperMatchers() {
45 |         when(mock.forInteger(anyInt())).thenReturn("0");
46 |         when(mock.forCharacter(anyChar())).thenReturn("1");
47 |         when(mock.forShort(anyShort())).thenReturn("2");
48 |         when(mock.forByte(anyByte())).thenReturn("3");
49 |         when(mock.forBoolean(anyBoolean())).thenReturn("4");
50 |         when(mock.forLong(anyLong())).thenReturn("5");
51 |         when(mock.forFloat(anyFloat())).thenReturn("6");
52 |         when(mock.forDouble(anyDouble())).thenReturn("7");
53 |         
54 |         assertEquals(null, mock.forInteger(null));
55 |         assertEquals(null, mock.forCharacter(null));
56 |         assertEquals(null, mock.forShort(null));
57 |         assertEquals(null, mock.forByte(null));
58 |         assertEquals(null, mock.forBoolean(null));
59 |         assertEquals(null, mock.forLong(null));
60 |         assertEquals(null, mock.forFloat(null));
61 |         assertEquals(null, mock.forDouble(null));
62 |     }
```

## org.mockitousage.matchers.AnyXMatchersAcceptNullsTest.shouldNotAcceptNullInAnyXMatchers()
Resolved declaration: org.mockitousage.matchers.AnyXMatchersAcceptNullsTest.shouldNotAcceptNullInAnyXMatchers()
Source: test/org/mockitousage/matchers/AnyXMatchersAcceptNullsTest.java

```java
26 |     @Test
27 |     public void shouldNotAcceptNullInAnyXMatchers() {
28 |         when(mock.oneArg(anyObject())).thenReturn("0");
29 |         when(mock.oneArg(anyString())).thenReturn("1");
30 |         when(mock.forList(anyList())).thenReturn("2");
31 |         when(mock.forMap(anyMap())).thenReturn("3");
32 |         when(mock.forCollection(anyCollection())).thenReturn("4");
33 |         when(mock.forSet(anySet())).thenReturn("5");
34 |         
35 |         assertEquals(null, mock.oneArg((Object) null));
36 |         assertEquals(null, mock.oneArg((String) null));
37 |         assertEquals(null, mock.forList(null));
38 |         assertEquals(null, mock.forMap(null));
39 |         assertEquals(null, mock.forCollection(null));
40 |         assertEquals(null, mock.forSet(null));
41 |     }
```

## org.mockitousage.matchers.MatchersTest.anyStringMatcher()
Resolved declaration: org.mockitousage.matchers.MatchersTest.anyStringMatcher()
Source: test/org/mockitousage/matchers/MatchersTest.java

```java
226 |     @Test
227 |     public void anyStringMatcher() {
228 |         when(mock.oneArg(anyString())).thenReturn("matched");
229 |         
230 |         assertEquals("matched", mock.oneArg(""));
231 |         assertEquals("matched", mock.oneArg("any string"));
232 |         assertEquals(null, mock.oneArg((String) null));
233 |     }
```

## org.mockitousage.matchers.NewMatchersTest.shouldAllowAnyCollection()
Resolved declaration: org.mockitousage.matchers.NewMatchersTest.shouldAllowAnyCollection()
Source: test/org/mockitousage/matchers/NewMatchersTest.java

```java
40 |     @Test
41 |     public void shouldAllowAnyCollection() {
42 |         when(mock.forCollection(anyCollection())).thenReturn("matched");
43 |         
44 |         assertEquals("matched", mock.forCollection(Arrays.asList("x", "y")));
45 |         assertEquals(null, mock.forCollection(null));
46 | 
47 |         verify(mock, times(1)).forCollection(anyCollection());
48 |     }
```

## org.mockitousage.matchers.NewMatchersTest.shouldAllowAnyList()
Resolved declaration: org.mockitousage.matchers.NewMatchersTest.shouldAllowAnyList()
Source: test/org/mockitousage/matchers/NewMatchersTest.java

```java
30 |     @Test
31 |     public void shouldAllowAnyList() {
32 |         when(mock.forList(anyList())).thenReturn("matched");
33 |         
34 |         assertEquals("matched", mock.forList(Arrays.asList("x", "y")));
35 |         assertEquals(null, mock.forList(null));
36 | 
37 |         verify(mock, times(1)).forList(anyList());
38 |     }
```

## org.mockitousage.matchers.NewMatchersTest.shouldAllowAnyMap()
Resolved declaration: org.mockitousage.matchers.NewMatchersTest.shouldAllowAnyMap()
Source: test/org/mockitousage/matchers/NewMatchersTest.java

```java
50 |     @Test
51 |     public void shouldAllowAnyMap() {
52 |         when(mock.forMap(anyMap())).thenReturn("matched");
53 |         
54 |         assertEquals("matched", mock.forMap(new HashMap<String, String>()));
55 |         assertEquals(null, mock.forMap(null));
56 | 
57 |         verify(mock, times(1)).forMap(anyMap());
58 |     }
```

## org.mockitousage.matchers.NewMatchersTest.shouldAllowAnySet()
Resolved declaration: org.mockitousage.matchers.NewMatchersTest.shouldAllowAnySet()
Source: test/org/mockitousage/matchers/NewMatchersTest.java

```java
60 |     @Test
61 |     public void shouldAllowAnySet() {
62 |         when(mock.forSet(anySet())).thenReturn("matched");
63 |         
64 |         assertEquals("matched", mock.forSet(new HashSet<String>()));
65 |         assertEquals(null, mock.forSet(null));
66 | 
67 |         verify(mock, times(1)).forSet(anySet());
68 |     }
```
