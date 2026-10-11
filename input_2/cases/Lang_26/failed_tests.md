# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.time.FastDateFormatTest.testLang645()
Resolved declaration: org.apache.commons.lang3.time.FastDateFormatTest.testLang645()
Source: src/test/java/org/apache/commons/lang3/time/FastDateFormatTest.java

```java
326 |     public void testLang645() {
327 |         Locale locale = new Locale("sv", "SE");
328 | 
329 |         Calendar cal = Calendar.getInstance();
330 |         cal.set(2010, 0, 1, 12, 0, 0);
331 |         Date d = cal.getTime();
332 | 
333 |         FastDateFormat fdf = FastDateFormat.getInstance("EEEE', week 'ww", locale);
334 | 
335 |         assertEquals("fredag, week 53", fdf.format(d));
336 |     }
```
