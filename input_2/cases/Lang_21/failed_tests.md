# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.time.DateUtilsTest.testIsSameLocalTime_Cal()
Resolved declaration: org.apache.commons.lang3.time.DateUtilsTest.testIsSameLocalTime_Cal()
Source: src/test/java/org/apache/commons/lang3/time/DateUtilsTest.java

```java
222 |     public void testIsSameLocalTime_Cal() {
223 |         GregorianCalendar cal1 = new GregorianCalendar(TimeZone.getTimeZone("GMT+1"));
224 |         GregorianCalendar cal2 = new GregorianCalendar(TimeZone.getTimeZone("GMT-1"));
225 |         cal1.set(2004, 6, 9, 13, 45, 0);
226 |         cal1.set(Calendar.MILLISECOND, 0);
227 |         cal2.set(2004, 6, 9, 13, 45, 0);
228 |         cal2.set(Calendar.MILLISECOND, 0);
229 |         assertEquals(true, DateUtils.isSameLocalTime(cal1, cal2));
230 | 
231 |         Calendar cal3 = Calendar.getInstance();
232 |         Calendar cal4 = Calendar.getInstance();
233 |         cal3.set(2004, 6, 9, 4,  0, 0);
234 |         cal4.set(2004, 6, 9, 16, 0, 0);
235 |         cal3.set(Calendar.MILLISECOND, 0);
236 |         cal4.set(Calendar.MILLISECOND, 0);
237 |         assertFalse("LANG-677", DateUtils.isSameLocalTime(cal3, cal4));
238 |         
239 |         cal2.set(2004, 6, 9, 11, 45, 0);
240 |         assertEquals(false, DateUtils.isSameLocalTime(cal1, cal2));
241 |         try {
242 |             DateUtils.isSameLocalTime((Calendar) null, (Calendar) null);
243 |             fail();
244 |         } catch (IllegalArgumentException ex) {}
245 |     }
```
