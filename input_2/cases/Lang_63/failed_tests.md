# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.time.DurationFormatUtilsTest.testJiraLang281()
Resolved declaration: org.apache.commons.lang.time.DurationFormatUtilsTest.testJiraLang281()
Source: src/test/org/apache/commons/lang/time/DurationFormatUtilsTest.java

```java
415 |     public void testJiraLang281() {
416 |         Calendar cal = Calendar.getInstance();
417 |         cal.set(Calendar.MONTH, Calendar.DECEMBER);
418 |         cal.set(Calendar.DAY_OF_MONTH, 31);
419 |         cal.set(Calendar.YEAR, 2005);
420 |         cal.set(Calendar.HOUR_OF_DAY, 0);
421 |         cal.set(Calendar.MINUTE, 0);
422 |         cal.set(Calendar.SECOND, 0);
423 |         cal.set(Calendar.MILLISECOND, 0);
424 | 
425 |         Calendar cal2 = Calendar.getInstance();
426 |         cal2.set(Calendar.MONTH, Calendar.OCTOBER);
427 |         cal2.set(Calendar.DAY_OF_MONTH, 6);
428 |         cal2.set(Calendar.YEAR, 2006);
429 |         cal2.set(Calendar.HOUR_OF_DAY, 0);
430 |         cal2.set(Calendar.MINUTE, 0);
431 |         cal2.set(Calendar.SECOND, 0);
432 |         cal2.set(Calendar.MILLISECOND, 0);
433 |         String result = DurationFormatUtils.formatPeriod(cal.getTime().getTime(), cal2.getTime().getTime(), "MM");
434 |         assertEquals("09", result);
435 |     }
```
