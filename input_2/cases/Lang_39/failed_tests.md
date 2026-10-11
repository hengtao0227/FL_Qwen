# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.StringUtilsTest.testReplace_StringStringArrayStringArray()
Resolved declaration: org.apache.commons.lang3.StringUtilsTest.testReplace_StringStringArrayStringArray()
Source: src/test/org/apache/commons/lang3/StringUtilsTest.java

```java
1009 |     public void testReplace_StringStringArrayStringArray() {
1010 | 
1011 |         
1012 |         //JAVADOC TESTS START
1013 |         assertNull(StringUtils.replaceEach(null, new String[]{"a"}, new String[]{"b"}));
1014 |         assertEquals(StringUtils.replaceEach("", new String[]{"a"}, new String[]{"b"}),"");
1015 |         assertEquals(StringUtils.replaceEach("aba", null, null),"aba");
1016 |         assertEquals(StringUtils.replaceEach("aba", new String[0], null),"aba");
1017 |         assertEquals(StringUtils.replaceEach("aba", null, new String[0]),"aba");
1018 |         assertEquals(StringUtils.replaceEach("aba", new String[]{"a"}, null),"aba");
1019 | 
1020 |         assertEquals(StringUtils.replaceEach("aba", new String[]{"a"}, new String[]{""}),"b");
1021 |         assertEquals(StringUtils.replaceEach("aba", new String[]{null}, new String[]{"a"}),"aba");
1022 |         assertEquals(StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"w", "t"}),"wcte");
1023 |         assertEquals(StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"d", "t"}),"dcte");
1024 |         //JAVADOC TESTS END
1025 | 
1026 |         assertEquals("bcc", StringUtils.replaceEach("abc", new String[]{"a", "b"}, new String[]{"b", "c"}));
1027 |         assertEquals("q651.506bera", StringUtils.replaceEach("d216.102oren",
1028 |             new String[]{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
1029 |                 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", 
1030 |                 "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
1031 |                 "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
1032 |             new String[]{"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", 
1033 |                 "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "N", "O", "P", "Q", 
1034 |                 "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", 
1035 |                 "H", "I", "J", "K", "L", "M", "5", "6", "7", "8", "9", "1", "2", "3", "4"}));
1036 | 
1037 |         // Test null safety inside arrays - LANG-552
1038 |         assertEquals(StringUtils.replaceEach("aba", new String[]{"a"}, new String[]{null}),"aba");
1039 |         assertEquals(StringUtils.replaceEach("aba", new String[]{"a", "b"}, new String[]{"c", null}),"cbc");
1040 |     }
```
