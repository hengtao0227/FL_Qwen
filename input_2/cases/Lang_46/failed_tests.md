# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.StringEscapeUtilsTest.testEscapeJavaWithSlash()
Resolved declaration: org.apache.commons.lang.StringEscapeUtilsTest.testEscapeJavaWithSlash()
Source: src/test/org/apache/commons/lang/StringEscapeUtilsTest.java

```java
103 |     public void testEscapeJavaWithSlash() {
104 |         final String input = "String with a slash (/) in it";
105 | 
106 |         final String expected = input;
107 |         final String actual = StringEscapeUtils.escapeJava(input);
108 | 
109 |         /**
110 |          * In 2.4 StringEscapeUtils.escapeJava(String) escapes '/' characters, which are not a valid character to escape
111 |          * in a Java string.
112 |          */
113 |         assertEquals(expected, actual);
114 |     }
```
