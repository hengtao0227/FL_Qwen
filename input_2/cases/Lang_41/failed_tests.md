# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.ClassUtilsTest.test_getShortClassName_Class()
Resolved declaration: org.apache.commons.lang.ClassUtilsTest.test_getShortClassName_Class()
Source: src/test/org/apache/commons/lang/ClassUtilsTest.java

```java
91 |     public void test_getShortClassName_Class() {
92 |         assertEquals("ClassUtils", ClassUtils.getShortClassName(ClassUtils.class));
93 |         assertEquals("Map.Entry", ClassUtils.getShortClassName(Map.Entry.class));
94 |         assertEquals("", ClassUtils.getShortClassName((Class) null));
95 | 
96 |         // LANG-535
97 |         assertEquals("String[]", ClassUtils.getShortClassName(String[].class));
98 |         assertEquals("Map.Entry[]", ClassUtils.getShortClassName(Map.Entry[].class));
99 | 
100 |         // Primitives
101 |         assertEquals("boolean", ClassUtils.getShortClassName(boolean.class));
102 |         assertEquals("byte", ClassUtils.getShortClassName(byte.class));
103 |         assertEquals("char", ClassUtils.getShortClassName(char.class));
104 |         assertEquals("short", ClassUtils.getShortClassName(short.class));
105 |         assertEquals("int", ClassUtils.getShortClassName(int.class));
106 |         assertEquals("long", ClassUtils.getShortClassName(long.class));
107 |         assertEquals("float", ClassUtils.getShortClassName(float.class));
108 |         assertEquals("double", ClassUtils.getShortClassName(double.class));
109 | 
110 |         // Primitive Arrays
111 |         assertEquals("boolean[]", ClassUtils.getShortClassName(boolean[].class));
112 |         assertEquals("byte[]", ClassUtils.getShortClassName(byte[].class));
113 |         assertEquals("char[]", ClassUtils.getShortClassName(char[].class));
114 |         assertEquals("short[]", ClassUtils.getShortClassName(short[].class));
115 |         assertEquals("int[]", ClassUtils.getShortClassName(int[].class));
116 |         assertEquals("long[]", ClassUtils.getShortClassName(long[].class));
117 |         assertEquals("float[]", ClassUtils.getShortClassName(float[].class));
118 |         assertEquals("double[]", ClassUtils.getShortClassName(double[].class));
119 | 
120 |         // Arrays of arrays of ...
121 |         assertEquals("String[][]", ClassUtils.getShortClassName(String[][].class));
122 |         assertEquals("String[][][]", ClassUtils.getShortClassName(String[][][].class));
123 |         assertEquals("String[][][][]", ClassUtils.getShortClassName(String[][][][].class));
124 |     }
```

## org.apache.commons.lang.ClassUtilsTest.test_getPackageName_Class()
Resolved declaration: org.apache.commons.lang.ClassUtilsTest.test_getPackageName_Class()
Source: src/test/org/apache/commons/lang/ClassUtilsTest.java

```java
140 |     public void test_getPackageName_Class() {
141 |         assertEquals("java.lang", ClassUtils.getPackageName(String.class));
142 |         assertEquals("java.util", ClassUtils.getPackageName(Map.Entry.class));
143 |         assertEquals("", ClassUtils.getPackageName((Class)null));
144 | 
145 |         // LANG-535
146 |         assertEquals("java.lang", ClassUtils.getPackageName(String[].class));
147 | 
148 |         // Primitive Arrays
149 |         assertEquals("", ClassUtils.getPackageName(boolean[].class));
150 |         assertEquals("", ClassUtils.getPackageName(byte[].class));
151 |         assertEquals("", ClassUtils.getPackageName(char[].class));
152 |         assertEquals("", ClassUtils.getPackageName(short[].class));
153 |         assertEquals("", ClassUtils.getPackageName(int[].class));
154 |         assertEquals("", ClassUtils.getPackageName(long[].class));
155 |         assertEquals("", ClassUtils.getPackageName(float[].class));
156 |         assertEquals("", ClassUtils.getPackageName(double[].class));
157 | 
158 |         // Arrays of arrays of ...
159 |         assertEquals("java.lang", ClassUtils.getPackageName(String[][].class));
160 |         assertEquals("java.lang", ClassUtils.getPackageName(String[][][].class));
161 |         assertEquals("java.lang", ClassUtils.getPackageName(String[][][][].class));
162 |     }
```
