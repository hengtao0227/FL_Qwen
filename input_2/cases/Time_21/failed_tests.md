# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZone.testGetName_berlin()
Resolved declaration: org.joda.time.TestDateTimeZone.testGetName_berlin()
Source: src/test/java/org/joda/time/TestDateTimeZone.java

```java
693 |     public void testGetName_berlin() {
694 |       DateTimeZone berlin = DateTimeZone.forID("Europe/Berlin");
695 |       assertEquals("Central European Time", berlin.getName(TEST_TIME_WINTER, Locale.ENGLISH));
696 |       assertEquals("Central European Summer Time", berlin.getName(TEST_TIME_SUMMER, Locale.ENGLISH));
697 |       if (JDK6) {
698 |         assertEquals("Mitteleurop\u00e4ische Zeit", berlin.getName(TEST_TIME_WINTER, Locale.GERMAN));
699 |         assertEquals("Mitteleurop\u00e4ische Sommerzeit", berlin.getName(TEST_TIME_SUMMER, Locale.GERMAN));
700 |       } else {
701 |         assertEquals("Zentraleurop\u00e4ische Zeit", berlin.getName(TEST_TIME_WINTER, Locale.GERMAN));
702 |         assertEquals("Zentraleurop\u00e4ische Sommerzeit", berlin.getName(TEST_TIME_SUMMER, Locale.GERMAN));
703 |       }
704 |   }
```

## org.joda.time.TestDateTimeZone.testGetShortName_berlin()
Resolved declaration: org.joda.time.TestDateTimeZone.testGetShortName_berlin()
Source: src/test/java/org/joda/time/TestDateTimeZone.java

```java
661 |     public void testGetShortName_berlin() {
662 |         DateTimeZone berlin = DateTimeZone.forID("Europe/Berlin");
663 |         assertEquals("CET", berlin.getShortName(TEST_TIME_WINTER, Locale.ENGLISH));
664 |         assertEquals("CEST", berlin.getShortName(TEST_TIME_SUMMER, Locale.ENGLISH));
665 |         if (JDK6) {
666 |           assertEquals("MEZ", berlin.getShortName(TEST_TIME_WINTER, Locale.GERMAN));
667 |           assertEquals("MESZ", berlin.getShortName(TEST_TIME_SUMMER, Locale.GERMAN));
668 |         } else {
669 |           assertEquals("CET", berlin.getShortName(TEST_TIME_WINTER, Locale.GERMAN));
670 |           assertEquals("CEST", berlin.getShortName(TEST_TIME_SUMMER, Locale.GERMAN));
671 |         }
672 |     }
```
