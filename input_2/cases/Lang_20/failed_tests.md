# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.StringUtilsTest.testJoin_ArrayChar()
Resolved declaration: org.apache.commons.lang3.StringUtilsTest.testJoin_ArrayChar()
Source: src/test/java/org/apache/commons/lang3/StringUtilsTest.java

```java
200 |     public void testJoin_ArrayChar() {
201 |         assertEquals(null, StringUtils.join((Object[]) null, ','));
202 |         assertEquals(TEXT_LIST_CHAR, StringUtils.join(ARRAY_LIST, SEPARATOR_CHAR));
203 |         assertEquals("", StringUtils.join(EMPTY_ARRAY_LIST, SEPARATOR_CHAR));
204 |         assertEquals(";;foo", StringUtils.join(MIXED_ARRAY_LIST, SEPARATOR_CHAR));
205 |         assertEquals("foo;2", StringUtils.join(MIXED_TYPE_LIST, SEPARATOR_CHAR));
206 | 
207 |         assertEquals("/", StringUtils.join(MIXED_ARRAY_LIST, '/', 0, MIXED_ARRAY_LIST.length-1));
208 |         assertEquals("foo", StringUtils.join(MIXED_TYPE_LIST, '/', 0, 1));
209 |         assertEquals("null", StringUtils.join(NULL_TO_STRING_LIST,'/', 0, 1));
210 |         assertEquals("foo/2", StringUtils.join(MIXED_TYPE_LIST, '/', 0, 2));
211 |         assertEquals("2", StringUtils.join(MIXED_TYPE_LIST, '/', 1, 2));
212 |         assertEquals("", StringUtils.join(MIXED_TYPE_LIST, '/', 2, 1));
213 |     }
```

## org.apache.commons.lang3.StringUtilsTest.testJoin_Objectarray()
Resolved declaration: org.apache.commons.lang3.StringUtilsTest.testJoin_Objectarray()
Source: src/test/java/org/apache/commons/lang3/StringUtilsTest.java

```java
184 |     public void testJoin_Objectarray() {
185 | //        assertEquals(null, StringUtils.join(null)); // generates warning
186 |         assertEquals(null, StringUtils.join((Object[]) null)); // equivalent explicit cast
187 |         // test additional varargs calls
188 |         assertEquals("", StringUtils.join()); // empty array
189 |         assertEquals("", StringUtils.join((Object) null)); // => new Object[]{null}
190 | 
191 |         assertEquals("", StringUtils.join(EMPTY_ARRAY_LIST));
192 |         assertEquals("", StringUtils.join(NULL_ARRAY_LIST));
193 |         assertEquals("null", StringUtils.join(NULL_TO_STRING_LIST));
194 |         assertEquals("abc", StringUtils.join(new String[] {"a", "b", "c"}));
195 |         assertEquals("a", StringUtils.join(new String[] {null, "a", ""}));
196 |         assertEquals("foo", StringUtils.join(MIXED_ARRAY_LIST));
197 |         assertEquals("foo2", StringUtils.join(MIXED_TYPE_LIST));
198 |     }
```
