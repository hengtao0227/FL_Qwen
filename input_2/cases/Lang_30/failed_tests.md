# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_CharArrayWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_CharArrayWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
318 |     public void testContainsNone_CharArrayWithSupplementaryChars() {
319 |         assertEquals(false, StringUtils.containsNone(CharU20000 + CharU20001, CharU20000.toCharArray()));
320 |         assertEquals(false, StringUtils.containsNone(CharU20000 + CharU20001, CharU20001.toCharArray()));
321 |         assertEquals(false, StringUtils.containsNone(CharU20000, CharU20000.toCharArray()));
322 |         // Sanity check:
323 |         assertEquals(-1, CharU20000.indexOf(CharU20001));
324 |         assertEquals(0, CharU20000.indexOf(CharU20001.charAt(0)));
325 |         assertEquals(-1, CharU20000.indexOf(CharU20001.charAt(1)));
326 |         // Test:
327 |         assertEquals(true, StringUtils.containsNone(CharU20000, CharU20001.toCharArray()));
328 |         assertEquals(true, StringUtils.containsNone(CharU20001, CharU20000.toCharArray()));
329 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_StringWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_StringWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
372 |     public void testContainsNone_StringWithSupplementaryChars() {
373 |         assertEquals(false, StringUtils.containsNone(CharU20000 + CharU20001, CharU20000));
374 |         assertEquals(false, StringUtils.containsNone(CharU20000 + CharU20001, CharU20001));
375 |         assertEquals(false, StringUtils.containsNone(CharU20000, CharU20000));
376 |         // Sanity check:
377 |         assertEquals(-1, CharU20000.indexOf(CharU20001));
378 |         assertEquals(0, CharU20000.indexOf(CharU20001.charAt(0)));
379 |         assertEquals(-1, CharU20000.indexOf(CharU20001.charAt(1)));
380 |         // Test:
381 |         assertEquals(true, StringUtils.containsNone(CharU20000, CharU20001));
382 |         assertEquals(true, StringUtils.containsNone(CharU20001, CharU20000));
383 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAny_StringCharArrayWithBadSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAny_StringCharArrayWithBadSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
133 |     public void testContainsAny_StringCharArrayWithBadSupplementaryChars() {
134 |         // Test edge case: 1/2 of a (broken) supplementary char
135 |         assertEquals(false, StringUtils.containsAny(CharUSuppCharHigh, CharU20001.toCharArray()));
136 |         assertEquals(false, StringUtils.containsAny("abc" + CharUSuppCharHigh + "xyz", CharU20001.toCharArray()));
137 |         assertEquals(-1, CharUSuppCharLow.indexOf(CharU20001));
138 |         assertEquals(false, StringUtils.containsAny(CharUSuppCharLow, CharU20001.toCharArray()));
139 |         assertEquals(false, StringUtils.containsAny(CharU20001, CharUSuppCharHigh.toCharArray()));
140 |         assertEquals(0, CharU20001.indexOf(CharUSuppCharLow));
141 |         assertEquals(true, StringUtils.containsAny(CharU20001, CharUSuppCharLow.toCharArray()));
142 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAnyBut_StringStringWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAnyBut_StringStringWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
615 |     public void testIndexOfAnyBut_StringStringWithSupplementaryChars() {
616 |         assertEquals(2, StringUtils.indexOfAnyBut(CharU20000 + CharU20001, CharU20000));
617 |         assertEquals(0, StringUtils.indexOfAnyBut(CharU20000 + CharU20001, CharU20001));
618 |         assertEquals(-1, StringUtils.indexOfAnyBut(CharU20000, CharU20000));
619 |         assertEquals(0, StringUtils.indexOfAnyBut(CharU20000, CharU20001));        
620 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAny_StringWithBadSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAny_StringWithBadSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
182 |     public void testContainsAny_StringWithBadSupplementaryChars() {
183 |         // Test edge case: 1/2 of a (broken) supplementary char
184 |         assertEquals(false, StringUtils.containsAny(CharUSuppCharHigh, CharU20001));
185 |         assertEquals(-1, CharUSuppCharLow.indexOf(CharU20001));
186 |         assertEquals(false, StringUtils.containsAny(CharUSuppCharLow, CharU20001));
187 |         assertEquals(false, StringUtils.containsAny(CharU20001, CharUSuppCharHigh));
188 |         assertEquals(0, CharU20001.indexOf(CharUSuppCharLow));
189 |         assertEquals(true, StringUtils.containsAny(CharU20001, CharUSuppCharLow));
190 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAny_StringCharArrayWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAny_StringCharArrayWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
526 |     public void testIndexOfAny_StringCharArrayWithSupplementaryChars() {
527 |         assertEquals(0, StringUtils.indexOfAny(CharU20000 + CharU20001, CharU20000.toCharArray()));
528 |         assertEquals(2, StringUtils.indexOfAny(CharU20000 + CharU20001, CharU20001.toCharArray()));
529 |         assertEquals(0, StringUtils.indexOfAny(CharU20000, CharU20000.toCharArray()));
530 |         assertEquals(-1, StringUtils.indexOfAny(CharU20000, CharU20001.toCharArray()));    
531 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAnyBut_StringCharArrayWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAnyBut_StringCharArrayWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
592 |     public void testIndexOfAnyBut_StringCharArrayWithSupplementaryChars() {
593 |         assertEquals(2, StringUtils.indexOfAnyBut(CharU20000 + CharU20001, CharU20000.toCharArray()));
594 |         assertEquals(0, StringUtils.indexOfAnyBut(CharU20000 + CharU20001, CharU20001.toCharArray()));
595 |         assertEquals(-1, StringUtils.indexOfAnyBut(CharU20000, CharU20000.toCharArray()));
596 |         assertEquals(0, StringUtils.indexOfAnyBut(CharU20000, CharU20001.toCharArray()));        
597 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_StringWithBadSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_StringWithBadSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
358 |     public void testContainsNone_StringWithBadSupplementaryChars() {
359 |         // Test edge case: 1/2 of a (broken) supplementary char
360 |         assertEquals(true, StringUtils.containsNone(CharUSuppCharHigh, CharU20001));
361 |         assertEquals(-1, CharUSuppCharLow.indexOf(CharU20001));
362 |         assertEquals(true, StringUtils.containsNone(CharUSuppCharLow, CharU20001));
363 |         assertEquals(-1, CharU20001.indexOf(CharUSuppCharHigh));
364 |         assertEquals(true, StringUtils.containsNone(CharU20001, CharUSuppCharHigh));
365 |         assertEquals(0, CharU20001.indexOf(CharUSuppCharLow));
366 |         assertEquals(false, StringUtils.containsNone(CharU20001, CharUSuppCharLow));        
367 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAny_StringStringWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testIndexOfAny_StringStringWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
569 |     public void testIndexOfAny_StringStringWithSupplementaryChars() {
570 |         assertEquals(0, StringUtils.indexOfAny(CharU20000 + CharU20001, CharU20000));
571 |         assertEquals(2, StringUtils.indexOfAny(CharU20000 + CharU20001, CharU20001));
572 |         assertEquals(0, StringUtils.indexOfAny(CharU20000, CharU20000));
573 |         assertEquals(-1, StringUtils.indexOfAny(CharU20000, CharU20001));    
574 |     }
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_CharArrayWithBadSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsNone_CharArrayWithBadSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
304 |     public void testContainsNone_CharArrayWithBadSupplementaryChars() {
305 |         // Test edge case: 1/2 of a (broken) supplementary char
306 |         assertEquals(true, StringUtils.containsNone(CharUSuppCharHigh, CharU20001.toCharArray()));
307 |         assertEquals(-1, CharUSuppCharLow.indexOf(CharU20001));
308 |         assertEquals(true, StringUtils.containsNone(CharUSuppCharLow, CharU20001.toCharArray()));
309 |         assertEquals(-1, CharU20001.indexOf(CharUSuppCharHigh));
310 |         assertEquals(true, StringUtils.containsNone(CharU20001, CharUSuppCharHigh.toCharArray()));
311 |         assertEquals(0, CharU20001.indexOf(CharUSuppCharLow));
312 |         assertEquals(false, StringUtils.containsNone(CharU20001, CharUSuppCharLow.toCharArray()));
313 |     }
```
