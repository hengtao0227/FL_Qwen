# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.time.FastDateFormatTest.test_changeDefault_Locale_DateInstance()
Resolved declaration: org.apache.commons.lang.time.FastDateFormatTest.test_changeDefault_Locale_DateInstance()
Source: src/test/org/apache/commons/lang/time/FastDateFormatTest.java

```java
135 |     public void test_changeDefault_Locale_DateInstance() {
136 |         Locale realDefaultLocale = Locale.getDefault();
137 |         try {
138 |             Locale.setDefault(Locale.US);
139 |             FastDateFormat format1 = FastDateFormat.getDateInstance(FastDateFormat.FULL, Locale.GERMANY);
140 |             FastDateFormat format2 = FastDateFormat.getDateInstance(FastDateFormat.FULL);
141 |             Locale.setDefault(Locale.GERMANY);
142 |             FastDateFormat format3 = FastDateFormat.getDateInstance(FastDateFormat.FULL);
143 | 
144 |             assertSame(Locale.GERMANY, format1.getLocale());
145 |             assertSame(Locale.US, format2.getLocale());
146 |             assertSame(Locale.GERMANY, format3.getLocale());
147 |             assertTrue(format1 != format2); // -- junit 3.8 version -- assertFalse(format1 == format2);
148 |             assertTrue(format2 != format3);
149 | 
150 |         } finally {
151 |             Locale.setDefault(realDefaultLocale);
152 |         }
153 |     }
```

## org.apache.commons.lang.time.FastDateFormatTest.test_changeDefault_Locale_DateTimeInstance()
Resolved declaration: org.apache.commons.lang.time.FastDateFormatTest.test_changeDefault_Locale_DateTimeInstance()
Source: src/test/org/apache/commons/lang/time/FastDateFormatTest.java

```java
155 |     public void test_changeDefault_Locale_DateTimeInstance() {
156 |         Locale realDefaultLocale = Locale.getDefault();
157 |         try {
158 |             Locale.setDefault(Locale.US);
159 |             FastDateFormat format1 = FastDateFormat.getDateTimeInstance(FastDateFormat.FULL, FastDateFormat.FULL, Locale.GERMANY);
160 |             FastDateFormat format2 = FastDateFormat.getDateTimeInstance(FastDateFormat.FULL, FastDateFormat.FULL);
161 |             Locale.setDefault(Locale.GERMANY);
162 |             FastDateFormat format3 = FastDateFormat.getDateTimeInstance(FastDateFormat.FULL, FastDateFormat.FULL);
163 | 
164 |             assertSame(Locale.GERMANY, format1.getLocale());
165 |             assertSame(Locale.US, format2.getLocale());
166 |             assertSame(Locale.GERMANY, format3.getLocale());
167 |             assertTrue(format1 != format2); // -- junit 3.8 version -- assertFalse(format1 == format2);
168 |             assertTrue(format2 != format3);
169 | 
170 |         } finally {
171 |             Locale.setDefault(realDefaultLocale);
172 |         }
173 |     }
```
