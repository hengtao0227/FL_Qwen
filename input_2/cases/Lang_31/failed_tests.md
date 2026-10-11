# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAnyCharArrayWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAnyCharArrayWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
687 | 	public void testContainsAnyCharArrayWithSupplementaryChars() {
688 | 		assertEquals(true, StringUtils.containsAny(CharU20000 + CharU20001, CharU20000.toCharArray()));
689 | 		assertEquals(true, StringUtils.containsAny(CharU20000 + CharU20001, CharU20001.toCharArray()));
690 | 		assertEquals(true, StringUtils.containsAny(CharU20000, CharU20000.toCharArray()));
691 | 		// Sanity check:
692 | 		assertEquals(-1, CharU20000.indexOf(CharU20001));
693 | 		assertEquals(0, CharU20000.indexOf(CharU20001.charAt(0)));
694 | 		assertEquals(-1, CharU20000.indexOf(CharU20001.charAt(1)));
695 | 		// Test:
696 | 		assertEquals(false, StringUtils.containsAny(CharU20000, CharU20001.toCharArray()));
697 | 		assertEquals(false, StringUtils.containsAny(CharU20001, CharU20000.toCharArray()));
698 | 	}
```

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAnyStringWithSupplementaryChars()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testContainsAnyStringWithSupplementaryChars()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
671 | 	public void testContainsAnyStringWithSupplementaryChars() {
672 | 		assertEquals(true, StringUtils.containsAny(CharU20000 + CharU20001, CharU20000));
673 | 		assertEquals(true, StringUtils.containsAny(CharU20000 + CharU20001, CharU20001));
674 | 		assertEquals(true, StringUtils.containsAny(CharU20000, CharU20000));
675 | 		// Sanity check:
676 | 		assertEquals(-1, CharU20000.indexOf(CharU20001));
677 | 		assertEquals(0, CharU20000.indexOf(CharU20001.charAt(0)));
678 | 		assertEquals(-1, CharU20000.indexOf(CharU20001.charAt(1)));
679 | 		// Test:
680 | 		assertEquals(false, StringUtils.containsAny(CharU20000, CharU20001));
681 | 		assertEquals(false, StringUtils.containsAny(CharU20001, CharU20000));
682 | 	}
```
