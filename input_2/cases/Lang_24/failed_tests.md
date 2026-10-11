# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.NumberUtilsTest.testIsNumber()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.testIsNumber()
Source: src/test/java/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
1005 |     public void testIsNumber() {
1006 |         String val = "12345";
1007 |         assertTrue("isNumber(String) 1 failed", NumberUtils.isNumber(val));
1008 |         assertTrue("isNumber(String)/createNumber(String) 1 failed", checkCreateNumber(val));
1009 |         val = "1234.5";
1010 |         assertTrue("isNumber(String) 2 failed", NumberUtils.isNumber(val));
1011 |         assertTrue("isNumber(String)/createNumber(String) 2 failed", checkCreateNumber(val));
1012 |         val = ".12345";
1013 |         assertTrue("isNumber(String) 3 failed", NumberUtils.isNumber(val));
1014 |         assertTrue("isNumber(String)/createNumber(String) 3 failed", checkCreateNumber(val));
1015 |         val = "1234E5";
1016 |         assertTrue("isNumber(String) 4 failed", NumberUtils.isNumber(val));
1017 |         assertTrue("isNumber(String)/createNumber(String) 4 failed", checkCreateNumber(val));
1018 |         val = "1234E+5";
1019 |         assertTrue("isNumber(String) 5 failed", NumberUtils.isNumber(val));
1020 |         assertTrue("isNumber(String)/createNumber(String) 5 failed", checkCreateNumber(val));
1021 |         val = "1234E-5";
1022 |         assertTrue("isNumber(String) 6 failed", NumberUtils.isNumber(val));
1023 |         assertTrue("isNumber(String)/createNumber(String) 6 failed", checkCreateNumber(val));
1024 |         val = "123.4E5";
1025 |         assertTrue("isNumber(String) 7 failed", NumberUtils.isNumber(val));
1026 |         assertTrue("isNumber(String)/createNumber(String) 7 failed", checkCreateNumber(val));
1027 |         val = "-1234";
1028 |         assertTrue("isNumber(String) 8 failed", NumberUtils.isNumber(val));
1029 |         assertTrue("isNumber(String)/createNumber(String) 8 failed", checkCreateNumber(val));
1030 |         val = "-1234.5";
1031 |         assertTrue("isNumber(String) 9 failed", NumberUtils.isNumber(val));
1032 |         assertTrue("isNumber(String)/createNumber(String) 9 failed", checkCreateNumber(val));
1033 |         val = "-.12345";
1034 |         assertTrue("isNumber(String) 10 failed", NumberUtils.isNumber(val));
1035 |         assertTrue("isNumber(String)/createNumber(String) 10 failed", checkCreateNumber(val));
1036 |         val = "-1234E5";
1037 |         assertTrue("isNumber(String) 11 failed", NumberUtils.isNumber(val));
1038 |         assertTrue("isNumber(String)/createNumber(String) 11 failed", checkCreateNumber(val));
1039 |         val = "0";
1040 |         assertTrue("isNumber(String) 12 failed", NumberUtils.isNumber(val));
1041 |         assertTrue("isNumber(String)/createNumber(String) 12 failed", checkCreateNumber(val));
1042 |         val = "-0";
1043 |         assertTrue("isNumber(String) 13 failed", NumberUtils.isNumber(val));
1044 |         assertTrue("isNumber(String)/createNumber(String) 13 failed", checkCreateNumber(val));
1045 |         val = "01234";
1046 |         assertTrue("isNumber(String) 14 failed", NumberUtils.isNumber(val));
1047 |         assertTrue("isNumber(String)/createNumber(String) 14 failed", checkCreateNumber(val));
1048 |         val = "-01234";
1049 |         assertTrue("isNumber(String) 15 failed", NumberUtils.isNumber(val));
1050 |         assertTrue("isNumber(String)/createNumber(String) 15 failed", checkCreateNumber(val));
1051 |         val = "0xABC123";
1052 |         assertTrue("isNumber(String) 16 failed", NumberUtils.isNumber(val));
1053 |         assertTrue("isNumber(String)/createNumber(String) 16 failed", checkCreateNumber(val));
1054 |         val = "0x0";
1055 |         assertTrue("isNumber(String) 17 failed", NumberUtils.isNumber(val));
1056 |         assertTrue("isNumber(String)/createNumber(String) 17 failed", checkCreateNumber(val));
1057 |         val = "123.4E21D";
1058 |         assertTrue("isNumber(String) 19 failed", NumberUtils.isNumber(val));
1059 |         assertTrue("isNumber(String)/createNumber(String) 19 failed", checkCreateNumber(val));
1060 |         val = "-221.23F";
1061 |         assertTrue("isNumber(String) 20 failed", NumberUtils.isNumber(val));
1062 |         assertTrue("isNumber(String)/createNumber(String) 20 failed", checkCreateNumber(val));
1063 |         val = "22338L";
1064 |         assertTrue("isNumber(String) 21 failed", NumberUtils.isNumber(val));
1065 |         assertTrue("isNumber(String)/createNumber(String) 21 failed", checkCreateNumber(val));
1066 |         val = null;
1067 |         assertTrue("isNumber(String) 1 Neg failed", !NumberUtils.isNumber(val));
1068 |         assertTrue("isNumber(String)/createNumber(String) 1 Neg failed", !checkCreateNumber(val));
1069 |         val = "";
1070 |         assertTrue("isNumber(String) 2 Neg failed", !NumberUtils.isNumber(val));
1071 |         assertTrue("isNumber(String)/createNumber(String) 2 Neg failed", !checkCreateNumber(val));
1072 |         val = "--2.3";
1073 |         assertTrue("isNumber(String) 3 Neg failed", !NumberUtils.isNumber(val));
1074 |         assertTrue("isNumber(String)/createNumber(String) 3 Neg failed", !checkCreateNumber(val));
1075 |         val = ".12.3";
1076 |         assertTrue("isNumber(String) 4 Neg failed", !NumberUtils.isNumber(val));
1077 |         assertTrue("isNumber(String)/createNumber(String) 4 Neg failed", !checkCreateNumber(val));
1078 |         val = "-123E";
1079 |         assertTrue("isNumber(String) 5 Neg failed", !NumberUtils.isNumber(val));
1080 |         assertTrue("isNumber(String)/createNumber(String) 5 Neg failed", !checkCreateNumber(val));
1081 |         val = "-123E+-212";
1082 |         assertTrue("isNumber(String) 6 Neg failed", !NumberUtils.isNumber(val));
1083 |         assertTrue("isNumber(String)/createNumber(String) 6 Neg failed", !checkCreateNumber(val));
1084 |         val = "-123E2.12";
1085 |         assertTrue("isNumber(String) 7 Neg failed", !NumberUtils.isNumber(val));
1086 |         assertTrue("isNumber(String)/createNumber(String) 7 Neg failed", !checkCreateNumber(val));
1087 |         val = "0xGF";
1088 |         assertTrue("isNumber(String) 8 Neg failed", !NumberUtils.isNumber(val));
1089 |         assertTrue("isNumber(String)/createNumber(String) 8 Neg failed", !checkCreateNumber(val));
1090 |         val = "0xFAE-1";
1091 |         assertTrue("isNumber(String) 9 Neg failed", !NumberUtils.isNumber(val));
1092 |         assertTrue("isNumber(String)/createNumber(String) 9 Neg failed", !checkCreateNumber(val));
1093 |         val = ".";
1094 |         assertTrue("isNumber(String) 10 Neg failed", !NumberUtils.isNumber(val));
1095 |         assertTrue("isNumber(String)/createNumber(String) 10 Neg failed", !checkCreateNumber(val));
1096 |         val = "-0ABC123";
1097 |         assertTrue("isNumber(String) 11 Neg failed", !NumberUtils.isNumber(val));
1098 |         assertTrue("isNumber(String)/createNumber(String) 11 Neg failed", !checkCreateNumber(val));
1099 |         val = "123.4E-D";
1100 |         assertTrue("isNumber(String) 12 Neg failed", !NumberUtils.isNumber(val));
1101 |         assertTrue("isNumber(String)/createNumber(String) 12 Neg failed", !checkCreateNumber(val));
1102 |         val = "123.4ED";
1103 |         assertTrue("isNumber(String) 13 Neg failed", !NumberUtils.isNumber(val));
1104 |         assertTrue("isNumber(String)/createNumber(String) 13 Neg failed", !checkCreateNumber(val));
1105 |         val = "1234E5l";
1106 |         assertTrue("isNumber(String) 14 Neg failed", !NumberUtils.isNumber(val));
1107 |         assertTrue("isNumber(String)/createNumber(String) 14 Neg failed", !checkCreateNumber(val));
1108 |         val = "11a";
1109 |         assertTrue("isNumber(String) 15 Neg failed", !NumberUtils.isNumber(val));
1110 |         assertTrue("isNumber(String)/createNumber(String) 15 Neg failed", !checkCreateNumber(val)); 
1111 |         val = "1a";
1112 |         assertTrue("isNumber(String) 16 Neg failed", !NumberUtils.isNumber(val));
1113 |         assertTrue("isNumber(String)/createNumber(String) 16 Neg failed", !checkCreateNumber(val)); 
1114 |         val = "a";
1115 |         assertTrue("isNumber(String) 17 Neg failed", !NumberUtils.isNumber(val));
1116 |         assertTrue("isNumber(String)/createNumber(String) 17 Neg failed", !checkCreateNumber(val)); 
1117 |         val = "11g";
1118 |         assertTrue("isNumber(String) 18 Neg failed", !NumberUtils.isNumber(val));
1119 |         assertTrue("isNumber(String)/createNumber(String) 18 Neg failed", !checkCreateNumber(val)); 
1120 |         val = "11z";
1121 |         assertTrue("isNumber(String) 19 Neg failed", !NumberUtils.isNumber(val));
1122 |         assertTrue("isNumber(String)/createNumber(String) 19 Neg failed", !checkCreateNumber(val)); 
1123 |         val = "11def";
1124 |         assertTrue("isNumber(String) 20 Neg failed", !NumberUtils.isNumber(val));
1125 |         assertTrue("isNumber(String)/createNumber(String) 20 Neg failed", !checkCreateNumber(val)); 
1126 |         val = "11d11";
1127 |         assertTrue("isNumber(String) 21 Neg failed", !NumberUtils.isNumber(val));
1128 |         assertTrue("isNumber(String)/createNumber(String) 21 Neg failed", !checkCreateNumber(val)); 
1129 |         val = "11 11";
1130 |         assertTrue("isNumber(String) 22 Neg failed", !NumberUtils.isNumber(val));
1131 |         assertTrue("isNumber(String)/createNumber(String) 22 Neg failed", !checkCreateNumber(val));
1132 |         val = " 1111";
1133 |         assertTrue("isNumber(String) 23 Neg failed", !NumberUtils.isNumber(val));
1134 |         assertTrue("isNumber(String)/createNumber(String) 23 Neg failed", !checkCreateNumber(val));
1135 |         val = "1111 ";
1136 |         assertTrue("isNumber(String) 24 Neg failed", !NumberUtils.isNumber(val));
1137 |         assertTrue("isNumber(String)/createNumber(String) 24 Neg failed", !checkCreateNumber(val));
1138 | 
1139 |         // LANG-521
1140 |         val = "2.";
1141 |         assertTrue("isNumber(String) LANG-521 failed", NumberUtils.isNumber(val));
1142 | 
1143 |         // LANG-664
1144 |         val = "1.1L";
1145 |         assertFalse("isNumber(String) LANG-664 failed", NumberUtils.isNumber(val));
1146 |     }
```
