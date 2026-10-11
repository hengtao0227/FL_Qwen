# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.time.junit.WeekTests.testConstructor()
Resolved declaration: org.jfree.data.time.junit.WeekTests.testConstructor()
Source: tests/org/jfree/data/time/junit/WeekTests.java

```java
500 |     public void testConstructor() {
501 |         Locale savedLocale = Locale.getDefault();
502 |         TimeZone savedZone = TimeZone.getDefault();
503 |         Locale.setDefault(new Locale("da", "DK"));
504 |         TimeZone.setDefault(TimeZone.getTimeZone("Europe/Copenhagen"));
505 |         GregorianCalendar cal = (GregorianCalendar) Calendar.getInstance(
506 |                 TimeZone.getDefault(), Locale.getDefault());
507 | 
508 |         // first day of week is monday
509 |         assertEquals(Calendar.MONDAY, cal.getFirstDayOfWeek());
510 |         cal.set(2007, Calendar.AUGUST, 26, 1, 0, 0);
511 |         cal.set(Calendar.MILLISECOND, 0);
512 |         Date t = cal.getTime();
513 |         Week w = new Week(t, TimeZone.getTimeZone("Europe/Copenhagen"));
514 |         assertEquals(34, w.getWeek());
515 | 
516 |         Locale.setDefault(Locale.US);
517 |         TimeZone.setDefault(TimeZone.getTimeZone("US/Detroit"));
518 |         cal = (GregorianCalendar) Calendar.getInstance(TimeZone.getDefault());
519 |         // first day of week is Sunday
520 |         assertEquals(Calendar.SUNDAY, cal.getFirstDayOfWeek());
521 |         cal.set(2007, Calendar.AUGUST, 26, 1, 0, 0);
522 |         cal.set(Calendar.MILLISECOND, 0);
523 | 
524 |         t = cal.getTime();
525 |         w = new Week(t, TimeZone.getTimeZone("Europe/Copenhagen"));
526 |         assertEquals(35, w.getWeek());
527 |         w = new Week(t, TimeZone.getTimeZone("Europe/Copenhagen"),
528 |                 new Locale("da", "DK"));
529 |         assertEquals(34, w.getWeek());
530 | 
531 |         Locale.setDefault(savedLocale);
532 |         TimeZone.setDefault(savedZone);
533 |     }
```
