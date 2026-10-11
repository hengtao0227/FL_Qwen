# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.basicapi.MocksSerializationTest.shouldBeSerializeAndHaveExtraInterfaces()
Resolved declaration: org.mockitousage.basicapi.MocksSerializationTest.shouldBeSerializeAndHaveExtraInterfaces()
Source: test/org/mockitousage/basicapi/MocksSerializationTest.java

```java
299 |     @Test
300 |     public void shouldBeSerializeAndHaveExtraInterfaces() throws Exception {
301 |         //when
302 |         IMethods mock = mock(IMethods.class, withSettings().serializable().extraInterfaces(List.class));
303 |         IMethods mockTwo = mock(IMethods.class, withSettings().extraInterfaces(List.class).serializable());
304 | 
305 |         //then
306 |         serializeAndBack((List) mock);
307 |         serializeAndBack((List) mockTwo);
308 |     }
```
