# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZoneCutover.testWithSecondOfMinuteInDstChange()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testWithSecondOfMinuteInDstChange()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1097 |     public void testWithSecondOfMinuteInDstChange() {
1098 |         DateTime dateTime = new DateTime("2010-10-31T02:30:10.123+02:00", ZONE_PARIS);
1099 |         assertEquals("2010-10-31T02:30:10.123+02:00", dateTime.toString());
1100 |         DateTime test = dateTime.withSecondOfMinute(0);
1101 |         assertEquals("2010-10-31T02:30:00.123+02:00", test.toString());
1102 |     }
```

## org.joda.time.TestDateTimeZoneCutover.testWithMinuteOfHourInDstChange()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testWithMinuteOfHourInDstChange()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1090 |     public void testWithMinuteOfHourInDstChange() {
1091 |         DateTime dateTime = new DateTime("2010-10-31T02:30:10.123+02:00", ZONE_PARIS);
1092 |         assertEquals("2010-10-31T02:30:10.123+02:00", dateTime.toString());
1093 |         DateTime test = dateTime.withMinuteOfHour(0);
1094 |         assertEquals("2010-10-31T02:00:10.123+02:00", test.toString());
1095 |     }
```

## org.joda.time.TestDateTimeZoneCutover.testWithMinuteOfHourInDstChange_mockZone()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testWithMinuteOfHourInDstChange_mockZone()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1063 |     public void testWithMinuteOfHourInDstChange_mockZone() {
1064 |         DateTime cutover = new DateTime(2010, 10, 31, 1, 15, DateTimeZone.forOffsetHoursMinutes(0, 30));
1065 |         assertEquals("2010-10-31T01:15:00.000+00:30", cutover.toString());
1066 |         DateTimeZone halfHourZone = new MockZone(cutover.getMillis(), 3600000, -1800);
1067 |         DateTime pre = new DateTime(2010, 10, 31, 1, 0, halfHourZone);
1068 |         assertEquals("2010-10-31T01:00:00.000+01:00", pre.toString());
1069 |         DateTime post = new DateTime(2010, 10, 31, 1, 59, halfHourZone);
1070 |         assertEquals("2010-10-31T01:59:00.000+00:30", post.toString());
1071 |         
1072 |         DateTime testPre1 = pre.withMinuteOfHour(30);
1073 |         assertEquals("2010-10-31T01:30:00.000+01:00", testPre1.toString());  // retain offset
1074 |         DateTime testPre2 = pre.withMinuteOfHour(50);
1075 |         assertEquals("2010-10-31T01:50:00.000+00:30", testPre2.toString());
1076 |         
1077 |         DateTime testPost1 = post.withMinuteOfHour(30);
1078 |         assertEquals("2010-10-31T01:30:00.000+00:30", testPost1.toString());  // retain offset
1079 |         DateTime testPost2 = post.withMinuteOfHour(10);
1080 |         assertEquals("2010-10-31T01:10:00.000+01:00", testPost2.toString());
1081 |     }
```

## org.joda.time.TestDateTimeZoneCutover.testBug2182444_usCentral()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testBug2182444_usCentral()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1153 |     public void testBug2182444_usCentral() {
1154 |         Chronology chronUSCentral = GregorianChronology.getInstance(DateTimeZone.forID("US/Central"));
1155 |         Chronology chronUTC = GregorianChronology.getInstance(DateTimeZone.UTC);
1156 |         DateTime usCentralStandardInUTC = new DateTime(2008, 11, 2, 7, 0, 0, 0, chronUTC);
1157 |         DateTime usCentralDaylightInUTC = new DateTime(2008, 11, 2, 6, 0, 0, 0, chronUTC);
1158 |         assertTrue("Should be standard time", chronUSCentral.getZone().isStandardOffset(usCentralStandardInUTC.getMillis()));
1159 |         assertFalse("Should be daylight time", chronUSCentral.getZone().isStandardOffset(usCentralDaylightInUTC.getMillis()));
1160 |         
1161 |         DateTime usCentralStandardInUSCentral = usCentralStandardInUTC.toDateTime(chronUSCentral);
1162 |         DateTime usCentralDaylightInUSCentral = usCentralDaylightInUTC.toDateTime(chronUSCentral);
1163 |         assertEquals(1, usCentralStandardInUSCentral.getHourOfDay());
1164 |         assertEquals(usCentralStandardInUSCentral.getHourOfDay(), usCentralDaylightInUSCentral.getHourOfDay());
1165 |         assertTrue(usCentralStandardInUSCentral.getMillis() != usCentralDaylightInUSCentral.getMillis());
1166 |         assertEquals(usCentralStandardInUSCentral, usCentralStandardInUSCentral.withHourOfDay(1));
1167 |         assertEquals(usCentralStandardInUSCentral.getMillis() + 3, usCentralStandardInUSCentral.withMillisOfSecond(3).getMillis());
1168 |         assertEquals(usCentralDaylightInUSCentral, usCentralDaylightInUSCentral.withHourOfDay(1));
1169 |         assertEquals(usCentralDaylightInUSCentral.getMillis() + 3, usCentralDaylightInUSCentral.withMillisOfSecond(3).getMillis());
1170 |     }
```

## org.joda.time.TestDateTimeZoneCutover.testWithMillisOfSecondInDstChange_Paris_summer()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testWithMillisOfSecondInDstChange_Paris_summer()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1104 |     public void testWithMillisOfSecondInDstChange_Paris_summer() {
1105 |         DateTime dateTime = new DateTime("2010-10-31T02:30:10.123+02:00", ZONE_PARIS);
1106 |         assertEquals("2010-10-31T02:30:10.123+02:00", dateTime.toString());
1107 |         DateTime test = dateTime.withMillisOfSecond(0);
1108 |         assertEquals("2010-10-31T02:30:10.000+02:00", test.toString());
1109 |     }
```

## org.joda.time.TestDateTimeZoneCutover.testWithHourOfDayInDstChange()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testWithHourOfDayInDstChange()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1083 |     public void testWithHourOfDayInDstChange() {
1084 |         DateTime dateTime = new DateTime("2010-10-31T02:30:10.123+02:00", ZONE_PARIS);
1085 |         assertEquals("2010-10-31T02:30:10.123+02:00", dateTime.toString());
1086 |         DateTime test = dateTime.withHourOfDay(2);
1087 |         assertEquals("2010-10-31T02:30:10.123+02:00", test.toString());
1088 |     }
```

## org.joda.time.TestDateTimeZoneCutover.testWithMillisOfSecondInDstChange_NewYork_winter()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testWithMillisOfSecondInDstChange_NewYork_winter()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1125 |     public void testWithMillisOfSecondInDstChange_NewYork_winter() {
1126 |         DateTime dateTime = new DateTime("2007-11-04T01:30:00.123-05:00", ZONE_NEW_YORK);
1127 |         assertEquals("2007-11-04T01:30:00.123-05:00", dateTime.toString());
1128 |         DateTime test = dateTime.withMillisOfSecond(0);
1129 |         assertEquals("2007-11-04T01:30:00.000-05:00", test.toString());
1130 |     }
```

## org.joda.time.TestDateTimeZoneCutover.testBug2182444_ausNSW()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.testBug2182444_ausNSW()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
1172 |     public void testBug2182444_ausNSW() {
1173 |         Chronology chronAusNSW = GregorianChronology.getInstance(DateTimeZone.forID("Australia/NSW"));
1174 |         Chronology chronUTC = GregorianChronology.getInstance(DateTimeZone.UTC);
1175 |         DateTime australiaNSWStandardInUTC = new DateTime(2008, 4, 5, 16, 0, 0, 0, chronUTC);
1176 |         DateTime australiaNSWDaylightInUTC = new DateTime(2008, 4, 5, 15, 0, 0, 0, chronUTC);
1177 |         assertTrue("Should be standard time", chronAusNSW.getZone().isStandardOffset(australiaNSWStandardInUTC.getMillis()));
1178 |         assertFalse("Should be daylight time", chronAusNSW.getZone().isStandardOffset(australiaNSWDaylightInUTC.getMillis()));
1179 |         
1180 |         DateTime australiaNSWStandardInAustraliaNSW = australiaNSWStandardInUTC.toDateTime(chronAusNSW);
1181 |         DateTime australiaNSWDaylightInAusraliaNSW = australiaNSWDaylightInUTC.toDateTime(chronAusNSW);
1182 |         assertEquals(2, australiaNSWStandardInAustraliaNSW.getHourOfDay());
1183 |         assertEquals(australiaNSWStandardInAustraliaNSW.getHourOfDay(), australiaNSWDaylightInAusraliaNSW.getHourOfDay());
1184 |         assertTrue(australiaNSWStandardInAustraliaNSW.getMillis() != australiaNSWDaylightInAusraliaNSW.getMillis());
1185 |         assertEquals(australiaNSWStandardInAustraliaNSW, australiaNSWStandardInAustraliaNSW.withHourOfDay(2));
1186 |         assertEquals(australiaNSWStandardInAustraliaNSW.getMillis() + 3, australiaNSWStandardInAustraliaNSW.withMillisOfSecond(3).getMillis());
1187 |         assertEquals(australiaNSWDaylightInAusraliaNSW, australiaNSWDaylightInAusraliaNSW.withHourOfDay(2));
1188 |         assertEquals(australiaNSWDaylightInAusraliaNSW.getMillis() + 3, australiaNSWDaylightInAusraliaNSW.withMillisOfSecond(3).getMillis());
1189 |     }
```
