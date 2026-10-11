# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang.time.DateUtilsTest.testTruncateLang59()
Resolved declaration: org.apache.commons.lang.time.DateUtilsTest.testTruncateLang59()
Source: src/test/org/apache/commons/lang/time/DateUtilsTest.java

```java
890 |     public void testTruncateLang59() throws Exception {
891 | 
892 |         // Set TimeZone to Mountain Time
893 |         TimeZone MST_MDT = TimeZone.getTimeZone("MST7MDT");
894 |         TimeZone.setDefault(MST_MDT);
895 |         DateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS z");
896 |         format.setTimeZone(MST_MDT);
897 | 
898 |         Date oct31_01MDT = new Date(1099206000000L); 
899 | 
900 |         Date oct31MDT             = new Date(oct31_01MDT.getTime()       - 3600000L); // - 1 hour
901 |         Date oct31_01_02MDT       = new Date(oct31_01MDT.getTime()       + 120000L);  // + 2 minutes
902 |         Date oct31_01_02_03MDT    = new Date(oct31_01_02MDT.getTime()    + 3000L);    // + 3 seconds
903 |         Date oct31_01_02_03_04MDT = new Date(oct31_01_02_03MDT.getTime() + 4L);       // + 4 milliseconds
904 | 
905 |         assertEquals("Check 00:00:00.000", "2004-10-31 00:00:00.000 MDT", format.format(oct31MDT));
906 |         assertEquals("Check 01:00:00.000", "2004-10-31 01:00:00.000 MDT", format.format(oct31_01MDT));
907 |         assertEquals("Check 01:02:00.000", "2004-10-31 01:02:00.000 MDT", format.format(oct31_01_02MDT));
908 |         assertEquals("Check 01:02:03.000", "2004-10-31 01:02:03.000 MDT", format.format(oct31_01_02_03MDT));
909 |         assertEquals("Check 01:02:03.004", "2004-10-31 01:02:03.004 MDT", format.format(oct31_01_02_03_04MDT));
910 | 
911 |         // ------- Demonstrate Problem -------
912 |         Calendar gval = Calendar.getInstance();
913 |         gval.setTime(new Date(oct31_01MDT.getTime()));
914 |         gval.set(Calendar.MINUTE, gval.get(Calendar.MINUTE)); // set minutes to the same value
915 |         assertEquals("Demonstrate Problem", gval.getTime().getTime(), oct31_01MDT.getTime() + 3600000L);
916 | 
917 |         // ---------- Test Truncate ----------
918 |         assertEquals("Truncate Calendar.MILLISECOND",
919 |                 oct31_01_02_03_04MDT, DateUtils.truncate(oct31_01_02_03_04MDT, Calendar.MILLISECOND));
920 | 
921 |         assertEquals("Truncate Calendar.SECOND",
922 |                    oct31_01_02_03MDT, DateUtils.truncate(oct31_01_02_03_04MDT, Calendar.SECOND));
923 | 
924 |         assertEquals("Truncate Calendar.MINUTE",
925 |                       oct31_01_02MDT, DateUtils.truncate(oct31_01_02_03_04MDT, Calendar.MINUTE));
926 | 
927 |         assertEquals("Truncate Calendar.HOUR_OF_DAY",
928 |                          oct31_01MDT, DateUtils.truncate(oct31_01_02_03_04MDT, Calendar.HOUR_OF_DAY));
929 | 
930 |         assertEquals("Truncate Calendar.HOUR",
931 |                          oct31_01MDT, DateUtils.truncate(oct31_01_02_03_04MDT, Calendar.HOUR));
932 | 
933 |         assertEquals("Truncate Calendar.DATE",
934 |                             oct31MDT, DateUtils.truncate(oct31_01_02_03_04MDT, Calendar.DATE));
935 | 
936 | 
937 |         // ---------- Test Round (down) ----------
938 |         assertEquals("Round Calendar.MILLISECOND",
939 |                 oct31_01_02_03_04MDT, DateUtils.round(oct31_01_02_03_04MDT, Calendar.MILLISECOND));
940 | 
941 |         assertEquals("Round Calendar.SECOND",
942 |                    oct31_01_02_03MDT, DateUtils.round(oct31_01_02_03_04MDT, Calendar.SECOND));
943 | 
944 |         assertEquals("Round Calendar.MINUTE",
945 |                       oct31_01_02MDT, DateUtils.round(oct31_01_02_03_04MDT, Calendar.MINUTE));
946 | 
947 |         assertEquals("Round Calendar.HOUR_OF_DAY",
948 |                          oct31_01MDT, DateUtils.round(oct31_01_02_03_04MDT, Calendar.HOUR_OF_DAY));
949 | 
950 |         assertEquals("Round Calendar.HOUR",
951 |                          oct31_01MDT, DateUtils.round(oct31_01_02_03_04MDT, Calendar.HOUR));
952 | 
953 |         assertEquals("Round Calendar.DATE",
954 |                             oct31MDT, DateUtils.round(oct31_01_02_03_04MDT, Calendar.DATE));
955 | 
956 |         // restore default time zone
957 |         TimeZone.setDefault(defaultZone);
958 |     }
```
