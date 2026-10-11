# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZoneCutover.test_DateTime_constructor_Moscow_Autumn()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.test_DateTime_constructor_Moscow_Autumn()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
920 |     public void test_DateTime_constructor_Moscow_Autumn() {
921 |         DateTime dt = new DateTime(2007, 10, 28, 2, 30, ZONE_MOSCOW);
922 |         assertEquals("2007-10-28T02:30:00.000+04:00", dt.toString());
923 |     }
```

## org.joda.time.TestDateTimeZoneCutover.test_getOffsetFromLocal_Moscow_Autumn_overlap_mins()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.test_getOffsetFromLocal_Moscow_Autumn_overlap_mins()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
910 |     public void test_getOffsetFromLocal_Moscow_Autumn_overlap_mins() {
911 |         for (int min = 0; min < 60; min++) {
912 |             if (min < 10) {
913 |                 doTest_getOffsetFromLocal(10, 28, 2, min, "2007-10-28T02:0" + min + ":00.000+04:00", ZONE_MOSCOW);
914 |             } else {
915 |                 doTest_getOffsetFromLocal(10, 28, 2, min, "2007-10-28T02:" + min + ":00.000+04:00", ZONE_MOSCOW);
916 |             }
917 |         }
918 |     }
```

## org.joda.time.TestDateTimeZoneCutover.test_getOffsetFromLocal_Moscow_Autumn()
Resolved declaration: org.joda.time.TestDateTimeZoneCutover.test_getOffsetFromLocal_Moscow_Autumn()
Source: src/test/java/org/joda/time/TestDateTimeZoneCutover.java

```java
889 |     public void test_getOffsetFromLocal_Moscow_Autumn() {
890 |         doTest_getOffsetFromLocal(10, 28, 0, 0, "2007-10-28T00:00:00.000+04:00", ZONE_MOSCOW);
891 |         doTest_getOffsetFromLocal(10, 28, 0,30, "2007-10-28T00:30:00.000+04:00", ZONE_MOSCOW);
892 |         doTest_getOffsetFromLocal(10, 28, 1, 0, "2007-10-28T01:00:00.000+04:00", ZONE_MOSCOW);
893 |         doTest_getOffsetFromLocal(10, 28, 1,30, "2007-10-28T01:30:00.000+04:00", ZONE_MOSCOW);
894 |         
895 |         doTest_getOffsetFromLocal(10, 28, 2, 0, "2007-10-28T02:00:00.000+04:00", ZONE_MOSCOW);
896 |         doTest_getOffsetFromLocal(10, 28, 2,30, "2007-10-28T02:30:00.000+04:00", ZONE_MOSCOW);
897 |         doTest_getOffsetFromLocal(10, 28, 2,30,59,999, "2007-10-28T02:30:59.999+04:00", ZONE_MOSCOW);
898 |         doTest_getOffsetFromLocal(10, 28, 2,59,59,998, "2007-10-28T02:59:59.998+04:00", ZONE_MOSCOW);
899 |         doTest_getOffsetFromLocal(10, 28, 2,59,59,999, "2007-10-28T02:59:59.999+04:00", ZONE_MOSCOW);
900 |         
901 |         doTest_getOffsetFromLocal(10, 28, 3, 0, "2007-10-28T03:00:00.000+03:00", ZONE_MOSCOW);
902 |         doTest_getOffsetFromLocal(10, 28, 3,30, "2007-10-28T03:30:00.000+03:00", ZONE_MOSCOW);
903 |         doTest_getOffsetFromLocal(10, 28, 4, 0, "2007-10-28T04:00:00.000+03:00", ZONE_MOSCOW);
904 |         doTest_getOffsetFromLocal(10, 28, 5, 0, "2007-10-28T05:00:00.000+03:00", ZONE_MOSCOW);
905 |         doTest_getOffsetFromLocal(10, 28, 6, 0, "2007-10-28T06:00:00.000+03:00", ZONE_MOSCOW);
906 |         doTest_getOffsetFromLocal(10, 28, 7, 0, "2007-10-28T07:00:00.000+03:00", ZONE_MOSCOW);
907 |         doTest_getOffsetFromLocal(10, 28, 8, 0, "2007-10-28T08:00:00.000+03:00", ZONE_MOSCOW);
908 |     }
```
