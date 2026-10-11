# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_baseStartYear()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_baseStartYear()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
873 |     public void testParseInto_monthOnly_baseStartYear() {
874 |         DateTimeFormatter f = DateTimeFormat.forPattern("M").withLocale(Locale.UK);
875 |         MutableDateTime result = new MutableDateTime(2004, 1, 1, 12, 20, 30, 0, TOKYO);
876 |         assertEquals(1, f.parseInto(result, "5", 0));
877 |         assertEquals(new MutableDateTime(2004, 5, 1, 12, 20, 30, 0, TOKYO), result);
878 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_parseStartYear()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_parseStartYear()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
880 |     public void testParseInto_monthOnly_parseStartYear() {
881 |         DateTimeFormatter f = DateTimeFormat.forPattern("M").withLocale(Locale.UK);
882 |         MutableDateTime result = new MutableDateTime(2004, 2, 1, 12, 20, 30, 0, TOKYO);
883 |         assertEquals(1, f.parseInto(result, "1", 0));
884 |         assertEquals(new MutableDateTime(2004, 1, 1, 12, 20, 30, 0, TOKYO), result);
885 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_baseEndYear()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_baseEndYear()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
887 |     public void testParseInto_monthOnly_baseEndYear() {
888 |         DateTimeFormatter f = DateTimeFormat.forPattern("M").withLocale(Locale.UK);
889 |         MutableDateTime result = new MutableDateTime(2004, 12, 31, 12, 20, 30, 0, TOKYO);
890 |         assertEquals(1, f.parseInto(result, "5", 0));
891 |         assertEquals(new MutableDateTime(2004, 5, 31, 12, 20, 30, 0, TOKYO), result);
892 |    }
```

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
866 |     public void testParseInto_monthOnly() {
867 |         DateTimeFormatter f = DateTimeFormat.forPattern("M").withLocale(Locale.UK);
868 |         MutableDateTime result = new MutableDateTime(2004, 1, 9, 12, 20, 30, 0, LONDON);
869 |         assertEquals(1, f.parseInto(result, "5", 0));
870 |         assertEquals(new MutableDateTime(2004, 5, 9, 12, 20, 30, 0, LONDON), result);
871 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_withDefaultYear_feb29()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_withDefaultYear_feb29()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
908 |     public void testParseInto_monthDay_withDefaultYear_feb29() {
909 |         DateTimeFormatter f = DateTimeFormat.forPattern("M d").withDefaultYear(2012);
910 |         MutableDateTime result = new MutableDateTime(2004, 1, 9, 12, 20, 30, 0, LONDON);
911 |         assertEquals(4, f.parseInto(result, "2 29", 0));
912 |         assertEquals(new MutableDateTime(2004, 2, 29, 12, 20, 30, 0, LONDON), result);
913 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_feb29()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthDay_feb29()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
901 |     public void testParseInto_monthDay_feb29() {
902 |         DateTimeFormatter f = DateTimeFormat.forPattern("M d").withLocale(Locale.UK);
903 |         MutableDateTime result = new MutableDateTime(2004, 1, 9, 12, 20, 30, 0, LONDON);
904 |         assertEquals(4, f.parseInto(result, "2 29", 0));
905 |         assertEquals(new MutableDateTime(2004, 2, 29, 12, 20, 30, 0, LONDON), result);
906 |     }
```

## org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_parseEndYear()
Resolved declaration: org.joda.time.format.TestDateTimeFormatter.testParseInto_monthOnly_parseEndYear()
Source: src/test/java/org/joda/time/format/TestDateTimeFormatter.java

```java
894 |     public void testParseInto_monthOnly_parseEndYear() {
895 |         DateTimeFormatter f = DateTimeFormat.forPattern("M").withLocale(Locale.UK);
896 |         MutableDateTime result = new MutableDateTime(2004, 1, 31, 12, 20, 30, 0,TOKYO);
897 |         assertEquals(2, f.parseInto(result, "12", 0));
898 |         assertEquals(new MutableDateTime(2004, 12, 31, 12, 20, 30, 0, TOKYO), result);
899 |     }
```
