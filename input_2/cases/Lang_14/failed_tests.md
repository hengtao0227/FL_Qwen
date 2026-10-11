# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testEquals()
Resolved declaration: org.apache.commons.lang3.StringUtilsEqualsIndexOfTest.testEquals()
Source: src/test/java/org/apache/commons/lang3/StringUtilsEqualsIndexOfTest.java

```java
486 |     public void testEquals() {
487 |         final CharSequence fooCs = FOO, barCs = BAR, foobarCs = FOOBAR;
488 |         assertTrue(StringUtils.equals(null, null));
489 |         assertTrue(StringUtils.equals(fooCs, fooCs));
490 |         assertTrue(StringUtils.equals(fooCs, (CharSequence) new StringBuilder(FOO)));
491 |         assertTrue(StringUtils.equals(fooCs, (CharSequence) new String(new char[] { 'f', 'o', 'o' })));
492 |         assertTrue(StringUtils.equals(fooCs, (CharSequence) new CustomCharSequence(FOO)));
493 |         assertTrue(StringUtils.equals((CharSequence) new CustomCharSequence(FOO), fooCs));
494 |         assertFalse(StringUtils.equals(fooCs, (CharSequence) new String(new char[] { 'f', 'O', 'O' })));
495 |         assertFalse(StringUtils.equals(fooCs, barCs));
496 |         assertFalse(StringUtils.equals(fooCs, null));
497 |         assertFalse(StringUtils.equals(null, fooCs));
498 |         assertFalse(StringUtils.equals(fooCs, foobarCs));
499 |         assertFalse(StringUtils.equals(foobarCs, fooCs));
500 |     }
```
