# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.fraction.FractionFormatTest.testParseProperInvalidMinus()
Resolved declaration: org.apache.commons.math.fraction.FractionFormatTest.testParseProperInvalidMinus()
Source: src/test/org/apache/commons/math/fraction/FractionFormatTest.java

```java
232 |     public void testParseProperInvalidMinus() {
233 |         String source = "2 -2 / 3";
234 |         try {
235 |             Fraction c = properFormat.parse(source);
236 |             fail("invalid minus in improper fraction.");
237 |         } catch (ParseException ex) {
238 |             // expected
239 |         }
240 |         source = "2 2 / -3";
241 |         try {
242 |             Fraction c = properFormat.parse(source);
243 |             fail("invalid minus in improper fraction.");
244 |         } catch (ParseException ex) {
245 |             // expected
246 |         }
247 |     }
```
