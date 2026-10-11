# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.format.TestISOPeriodFormat.testFormatStandard_negative()
Resolved declaration: org.joda.time.format.TestISOPeriodFormat.testFormatStandard_negative()
Source: src/test/java/org/joda/time/format/TestISOPeriodFormat.java

```java
118 |     public void testFormatStandard_negative() {
119 |         Period p = new Period(-1, -2, -3, -4, -5, -6, -7, -8);
120 |         assertEquals("P-1Y-2M-3W-4DT-5H-6M-7.008S", ISOPeriodFormat.standard().print(p));
121 |         
122 |         p = Period.years(-54);
123 |         assertEquals("P-54Y", ISOPeriodFormat.standard().print(p));
124 |         
125 |         p = Period.seconds(4).withMillis(-8);
126 |         assertEquals("PT3.992S", ISOPeriodFormat.standard().print(p));
127 |         
128 |         p = Period.seconds(-4).withMillis(8);
129 |         assertEquals("PT-3.992S", ISOPeriodFormat.standard().print(p));
130 |         
131 |         p = Period.seconds(-23);
132 |         assertEquals("PT-23S", ISOPeriodFormat.standard().print(p));
133 |         
134 |         p = Period.millis(-8);
135 |         assertEquals("PT-0.008S", ISOPeriodFormat.standard().print(p));
136 |     }
```
