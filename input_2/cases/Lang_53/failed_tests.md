# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.time.DateUtilsTest.testRoundLang346()
Resolved declaration: org.apache.commons.lang.time.DateUtilsTest.testRoundLang346()
Source: src/test/org/apache/commons/lang/time/DateUtilsTest.java

```java
699 |     public void testRoundLang346() throws Exception
700 |     {
701 |         TimeZone.setDefault(defaultZone);
702 |         dateTimeParser.setTimeZone(defaultZone);
703 |         Calendar testCalendar = Calendar.getInstance();
704 |         testCalendar.set(2007, 6, 2, 8, 8, 50);
705 |         Date date = testCalendar.getTime();
706 |         assertEquals("Minute Round Up Failed",
707 |                      dateTimeParser.parse("July 2, 2007 08:09:00.000"),
708 |                      DateUtils.round(date, Calendar.MINUTE));
709 | 
710 |         testCalendar.set(2007, 6, 2, 8, 8, 20);
711 |         date = testCalendar.getTime();
712 |         assertEquals("Minute No Round Failed",
713 |                      dateTimeParser.parse("July 2, 2007 08:08:00.000"),
714 |                      DateUtils.round(date, Calendar.MINUTE));
715 | 
716 |         testCalendar.set(2007, 6, 2, 8, 8, 50);
717 |         testCalendar.set(Calendar.MILLISECOND, 600);
718 |         date = testCalendar.getTime();
719 | 
720 |         assertEquals("Second Round Up with 600 Milli Seconds Failed",
721 |                      dateTimeParser.parse("July 2, 2007 08:08:51.000"),
722 |                      DateUtils.round(date, Calendar.SECOND));
723 | 
724 |         testCalendar.set(2007, 6, 2, 8, 8, 50);
725 |         testCalendar.set(Calendar.MILLISECOND, 200);
726 |         date = testCalendar.getTime();
727 |         assertEquals("Second Round Down with 200 Milli Seconds Failed",
728 |                      dateTimeParser.parse("July 2, 2007 08:08:50.000"),
729 |                      DateUtils.round(date, Calendar.SECOND));
730 | 
731 |         testCalendar.set(2007, 6, 2, 8, 8, 20);
732 |         testCalendar.set(Calendar.MILLISECOND, 600);
733 |         date = testCalendar.getTime();
734 |         assertEquals("Second Round Up with 200 Milli Seconds Failed",
735 |                      dateTimeParser.parse("July 2, 2007 08:08:21.000"),
736 |                      DateUtils.round(date, Calendar.SECOND));
737 | 
738 |         testCalendar.set(2007, 6, 2, 8, 8, 20);
739 |         testCalendar.set(Calendar.MILLISECOND, 200);
740 |         date = testCalendar.getTime();
741 |         assertEquals("Second Round Down with 200 Milli Seconds Failed",
742 |                      dateTimeParser.parse("July 2, 2007 08:08:20.000"),
743 |                      DateUtils.round(date, Calendar.SECOND));
744 | 
745 |         testCalendar.set(2007, 6, 2, 8, 8, 50);
746 |         date = testCalendar.getTime();
747 |         assertEquals("Hour Round Down Failed",
748 |                      dateTimeParser.parse("July 2, 2007 08:00:00.000"),
749 |                      DateUtils.round(date, Calendar.HOUR));
750 | 
751 |         testCalendar.set(2007, 6, 2, 8, 31, 50);
752 |         date = testCalendar.getTime();
753 |         assertEquals("Hour Round Up Failed",
754 |                      dateTimeParser.parse("July 2, 2007 09:00:00.000"),
755 |                      DateUtils.round(date, Calendar.HOUR));
756 |     }
```
