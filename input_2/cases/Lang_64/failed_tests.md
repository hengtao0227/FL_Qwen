# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.enums.ValuedEnumTest.testCompareTo_otherEnumType()
Resolved declaration: org.apache.commons.lang.enums.ValuedEnumTest.testCompareTo_otherEnumType()
Source: src/test/org/apache/commons/lang/enums/ValuedEnumTest.java

```java
105 |     public void testCompareTo_otherEnumType() {
106 |         try {
107 |             ValuedColorEnum.BLUE.compareTo(ValuedLanguageEnum.ENGLISH);
108 |             fail();
109 |         } catch (ClassCastException ex) {
110 |             // expected
111 |         }
112 |     }
```
