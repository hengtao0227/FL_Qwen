# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.time.FastDateFormatTest.testFormat()
Resolved declaration: org.apache.commons.lang3.time.FastDateFormatTest.testFormat()
Source: src/test/java/org/apache/commons/lang3/time/FastDateFormatTest.java

```java
173 |     public void testFormat() {
174 |         Locale realDefaultLocale = Locale.getDefault();
175 |         TimeZone realDefaultZone = TimeZone.getDefault();
176 |         try {
177 |             Locale.setDefault(Locale.US);
178 |             TimeZone.setDefault(TimeZone.getTimeZone("America/New_York"));
179 | 
180 |             GregorianCalendar cal1 = new GregorianCalendar(2003, 0, 10, 15, 33, 20);
181 |             GregorianCalendar cal2 = new GregorianCalendar(2003, 6, 10, 9, 00, 00);
182 |             Date date1 = cal1.getTime();
183 |             Date date2 = cal2.getTime();
184 |             long millis1 = date1.getTime();
185 |             long millis2 = date2.getTime();
186 | 
187 |             FastDateFormat fdf = FastDateFormat.getInstance("yyyy-MM-dd'T'HH:mm:ss");
188 |             SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
189 |             assertEquals(sdf.format(date1), fdf.format(date1));
190 |             assertEquals("2003-01-10T15:33:20", fdf.format(date1));
191 |             assertEquals("2003-01-10T15:33:20", fdf.format(cal1));
192 |             assertEquals("2003-01-10T15:33:20", fdf.format(millis1));
193 |             assertEquals("2003-07-10T09:00:00", fdf.format(date2));
194 |             assertEquals("2003-07-10T09:00:00", fdf.format(cal2));
195 |             assertEquals("2003-07-10T09:00:00", fdf.format(millis2));
196 | 
197 |             fdf = FastDateFormat.getInstance("Z");
198 |             assertEquals("-0500", fdf.format(date1));
199 |             assertEquals("-0500", fdf.format(cal1));
200 |             assertEquals("-0500", fdf.format(millis1));
201 | 
202 |             assertEquals("-0400", fdf.format(date2));
203 |             assertEquals("-0400", fdf.format(cal2));
204 |             assertEquals("-0400", fdf.format(millis2));
205 | 
206 |             fdf = FastDateFormat.getInstance("ZZ");
207 |             assertEquals("-05:00", fdf.format(date1));
208 |             assertEquals("-05:00", fdf.format(cal1));
209 |             assertEquals("-05:00", fdf.format(millis1));
210 | 
211 |             assertEquals("-04:00", fdf.format(date2));
212 |             assertEquals("-04:00", fdf.format(cal2));
213 |             assertEquals("-04:00", fdf.format(millis2));
214 | 
215 |             String pattern = "GGGG GGG GG G yyyy yyy yy y MMMM MMM MM M" +
216 |                 " dddd ddd dd d DDDD DDD DD D EEEE EEE EE E aaaa aaa aa a zzzz zzz zz z";
217 |             fdf = FastDateFormat.getInstance(pattern);
218 |             sdf = new SimpleDateFormat(pattern);
219 |             // SDF bug fix starting with Java 7
220 |             assertEquals(sdf.format(date1).replaceAll("2003 03 03 03", "2003 2003 03 2003"), fdf.format(date1));
221 |             assertEquals(sdf.format(date2).replaceAll("2003 03 03 03", "2003 2003 03 2003"), fdf.format(date2));
222 |         } finally {
223 |             Locale.setDefault(realDefaultLocale);
224 |             TimeZone.setDefault(realDefaultZone);
225 |         }
226 |     }
```
