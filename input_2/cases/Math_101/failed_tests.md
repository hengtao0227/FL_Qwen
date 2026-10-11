# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.complex.ComplexFormatTest.testForgottenImaginaryCharacter()
Resolved declaration: org.apache.commons.math.complex.ComplexFormatAbstractTest.testForgottenImaginaryCharacter()
Source: src/test/org/apache/commons/math/complex/ComplexFormatAbstractTest.java

```java
353 |     public void testForgottenImaginaryCharacter() {
354 |         ParsePosition pos = new ParsePosition(0);
355 |         assertNull(new ComplexFormat().parse("1 + 1", pos));
356 |         assertEquals(5, pos.getErrorIndex());
357 |     }
```

## org.apache.commons.math.complex.FrenchComplexFormatTest.testForgottenImaginaryCharacter()
Resolved declaration: org.apache.commons.math.complex.ComplexFormatAbstractTest.testForgottenImaginaryCharacter()
Source: src/test/org/apache/commons/math/complex/ComplexFormatAbstractTest.java

```java
353 |     public void testForgottenImaginaryCharacter() {
354 |         ParsePosition pos = new ParsePosition(0);
355 |         assertNull(new ComplexFormat().parse("1 + 1", pos));
356 |         assertEquals(5, pos.getErrorIndex());
357 |     }
```
