# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.progress.HandyReturnValuesTest.should_default_values_for_primitive()
Resolved declaration: org.mockito.internal.progress.HandyReturnValuesTest.should_default_values_for_primitive()
Source: test/org/mockito/internal/progress/HandyReturnValuesTest.java

```java
42 |     @Test public void should_default_values_for_primitive() {
43 |         assertThat(h.returnFor(boolean.class)).isFalse();
44 |         assertThat(h.returnFor(char.class)).isEqualTo('\u0000');
45 |         assertThat(h.returnFor(byte.class)).isEqualTo((byte) 0);
46 |         assertThat(h.returnFor(short.class)).isEqualTo((short) 0);
47 |         assertThat(h.returnFor(int.class)).isEqualTo(0);
48 |         assertThat(h.returnFor(long.class)).isEqualTo(0L);
49 |         assertThat(h.returnFor(float.class)).isEqualTo(0.0F);
50 |         assertThat(h.returnFor(double.class)).isEqualTo(0.0D);
51 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsEmptyValuesTest.should_return_primitive()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsEmptyValuesTest.should_return_primitive()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsEmptyValuesTest.java

```java
43 |     @Test public void should_return_primitive() {
44 |         assertEquals(false, values.returnValueFor(Boolean.TYPE));
45 |         assertEquals((char) 0, values.returnValueFor(Character.TYPE));
46 |         assertEquals((byte) 0, values.returnValueFor(Byte.TYPE));
47 |         assertEquals((short) 0, values.returnValueFor(Short.TYPE));
48 |         assertEquals(0, values.returnValueFor(Integer.TYPE));
49 |         assertEquals(0L, values.returnValueFor(Long.TYPE));
50 |         assertEquals(0F, values.returnValueFor(Float.TYPE));
51 |         assertEquals(0D, values.returnValueFor(Double.TYPE));
52 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsMocksTest.should_return_the_usual_default_values_for_primitives()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsMocksTest.should_return_the_usual_default_values_for_primitives()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsMocksTest.java

```java
41 |     @Test
42 |     public void should_return_the_usual_default_values_for_primitives() throws Throwable {
43 |         ReturnsMocks answer = new ReturnsMocks();
44 |         assertEquals(false, answer.answer(invocationOf(HasPrimitiveMethods.class, "booleanMethod")));
45 |         assertEquals((char) 0, answer.answer(invocationOf(HasPrimitiveMethods.class, "charMethod")));
46 |         assertEquals((byte) 0, answer.answer(invocationOf(HasPrimitiveMethods.class, "byteMethod")));
47 |         assertEquals((short) 0, answer.answer(invocationOf(HasPrimitiveMethods.class, "shortMethod")));
48 |         assertEquals(0, answer.answer(invocationOf(HasPrimitiveMethods.class, "intMethod")));
49 |         assertEquals(0L, answer.answer(invocationOf(HasPrimitiveMethods.class, "longMethod")));
50 |         assertEquals(0f, answer.answer(invocationOf(HasPrimitiveMethods.class, "floatMethod")));
51 |         assertEquals(0d, answer.answer(invocationOf(HasPrimitiveMethods.class, "doubleMethod")));
52 |     }
```

## org.mockito.internal.stubbing.defaultanswers.ReturnsSmartNullsTest.should_return_the_usual_default_values_for_primitives()
Resolved declaration: org.mockito.internal.stubbing.defaultanswers.ReturnsSmartNullsTest.should_return_the_usual_default_values_for_primitives()
Source: test/org/mockito/internal/stubbing/defaultanswers/ReturnsSmartNullsTest.java

```java
14 |     @Test
15 |     public void should_return_the_usual_default_values_for_primitives() throws Throwable {
16 |         Answer<Object> answer = new ReturnsSmartNulls();
17 |         assertEquals(false  ,   answer.answer(invocationOf(HasPrimitiveMethods.class, "booleanMethod")));
18 |         assertEquals((char) 0,  answer.answer(invocationOf(HasPrimitiveMethods.class, "charMethod")));
19 |         assertEquals((byte) 0,  answer.answer(invocationOf(HasPrimitiveMethods.class, "byteMethod")));
20 |         assertEquals((short) 0, answer.answer(invocationOf(HasPrimitiveMethods.class, "shortMethod")));
21 |         assertEquals(0,         answer.answer(invocationOf(HasPrimitiveMethods.class, "intMethod")));
22 |         assertEquals(0L,        answer.answer(invocationOf(HasPrimitiveMethods.class, "longMethod")));
23 |         assertEquals(0f,        answer.answer(invocationOf(HasPrimitiveMethods.class, "floatMethod")));
24 |         assertEquals(0d,        answer.answer(invocationOf(HasPrimitiveMethods.class, "doubleMethod")));
25 |     }
```
