# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.RandomStringUtilsTest.testExceptions()
Resolved declaration: org.apache.commons.lang3.RandomStringUtilsTest.testExceptions()
Source: src/test/java/org/apache/commons/lang3/RandomStringUtilsTest.java

```java
133 |     public void testExceptions() {
134 |         final char[] DUMMY = new char[]{'a'}; // valid char array
135 |         try {
136 |             RandomStringUtils.random(-1);
137 |             fail();
138 |         } catch (IllegalArgumentException ex) {}
139 |         try {
140 |             RandomStringUtils.random(-1, true, true);
141 |             fail();
142 |         } catch (IllegalArgumentException ex) {}
143 |         try {
144 |             RandomStringUtils.random(-1, DUMMY);
145 |             fail();
146 |         } catch (IllegalArgumentException ex) {}
147 |         try {
148 |             RandomStringUtils.random(1, new char[0]); // must not provide empty array => IAE
149 |             fail();
150 |         } catch (IllegalArgumentException ex) {}
151 |         try {
152 |             RandomStringUtils.random(-1, "");
153 |             fail();
154 |         } catch (IllegalArgumentException ex) {}
155 |         try {
156 |             RandomStringUtils.random(-1, (String)null);
157 |             fail();
158 |         } catch (IllegalArgumentException ex) {}
159 |         try {
160 |             RandomStringUtils.random(-1, 'a', 'z', false, false);
161 |             fail();
162 |         } catch (IllegalArgumentException ex) {}
163 |         try {
164 |             RandomStringUtils.random(-1, 'a', 'z', false, false, DUMMY);
165 |             fail();
166 |         } catch (IllegalArgumentException ex) {}
167 |         try {
168 |             RandomStringUtils.random(-1, 'a', 'z', false, false, DUMMY, new Random());
169 |             fail();
170 |         } catch (IllegalArgumentException ex) {}
171 |     }
```

## org.apache.commons.lang3.RandomStringUtilsTest.testLANG805()
Resolved declaration: org.apache.commons.lang3.RandomStringUtilsTest.testLANG805()
Source: src/test/java/org/apache/commons/lang3/RandomStringUtilsTest.java

```java
128 |     public void testLANG805() {
129 |         long seed = System.currentTimeMillis();
130 |         assertEquals("aaa", RandomStringUtils.random(3,0,0,false,false,new char[]{'a'},new Random(seed)));
131 |     }
```
