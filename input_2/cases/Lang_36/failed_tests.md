# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.testCreateNumber()
Source: src/test/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
176 |     public void testCreateNumber() {
177 |         // a lot of things can go wrong
178 |         assertEquals("createNumber(String) 1 failed", new Float("1234.5"), NumberUtils.createNumber("1234.5"));
179 |         assertEquals("createNumber(String) 2 failed", new Integer("12345"), NumberUtils.createNumber("12345"));
180 |         assertEquals("createNumber(String) 3 failed", new Double("1234.5"), NumberUtils.createNumber("1234.5D"));
181 |         assertEquals("createNumber(String) 3 failed", new Double("1234.5"), NumberUtils.createNumber("1234.5d"));
182 |         assertEquals("createNumber(String) 4 failed", new Float("1234.5"), NumberUtils.createNumber("1234.5F"));
183 |         assertEquals("createNumber(String) 4 failed", new Float("1234.5"), NumberUtils.createNumber("1234.5f"));
184 |         assertEquals("createNumber(String) 5 failed", new Long(Integer.MAX_VALUE + 1L), NumberUtils.createNumber(""
185 |             + (Integer.MAX_VALUE + 1L)));
186 |         assertEquals("createNumber(String) 6 failed", new Long(12345), NumberUtils.createNumber("12345L"));
187 |         assertEquals("createNumber(String) 6 failed", new Long(12345), NumberUtils.createNumber("12345l"));
188 |         assertEquals("createNumber(String) 7 failed", new Float("-1234.5"), NumberUtils.createNumber("-1234.5"));
189 |         assertEquals("createNumber(String) 8 failed", new Integer("-12345"), NumberUtils.createNumber("-12345"));
190 |         assertTrue("createNumber(String) 9 failed", 0xFADE == NumberUtils.createNumber("0xFADE").intValue());
191 |         assertTrue("createNumber(String) 10 failed", -0xFADE == NumberUtils.createNumber("-0xFADE").intValue());
192 |         assertEquals("createNumber(String) 11 failed", new Double("1.1E200"), NumberUtils.createNumber("1.1E200"));
193 |         assertEquals("createNumber(String) 12 failed", new Float("1.1E20"), NumberUtils.createNumber("1.1E20"));
194 |         assertEquals("createNumber(String) 13 failed", new Double("-1.1E200"), NumberUtils.createNumber("-1.1E200"));
195 |         assertEquals("createNumber(String) 14 failed", new Double("1.1E-200"), NumberUtils.createNumber("1.1E-200"));
196 |         assertEquals("createNumber(null) failed", null, NumberUtils.createNumber(null));
197 |         assertEquals("createNumber(String) failed", new BigInteger("12345678901234567890"), NumberUtils
198 |                 .createNumber("12345678901234567890L"));
199 | 
200 |         // jdk 1.2 doesn't support this. unsure about jdk 1.2.2
201 |         if (SystemUtils.isJavaVersionAtLeast(1.3f)) {
202 |             assertEquals("createNumber(String) 15 failed", new BigDecimal("1.1E-700"), NumberUtils
203 |                     .createNumber("1.1E-700F"));
204 |         }
205 |         assertEquals("createNumber(String) 16 failed", new Long("10" + Integer.MAX_VALUE), NumberUtils
206 |                 .createNumber("10" + Integer.MAX_VALUE + "L"));
207 |         assertEquals("createNumber(String) 17 failed", new Long("10" + Integer.MAX_VALUE), NumberUtils
208 |                 .createNumber("10" + Integer.MAX_VALUE));
209 |         assertEquals("createNumber(String) 18 failed", new BigInteger("10" + Long.MAX_VALUE), NumberUtils
210 |                 .createNumber("10" + Long.MAX_VALUE));
211 | 
212 |         // LANG-521
213 |         assertEquals("createNumber(String) LANG-521 failed", new Float("2."), NumberUtils.createNumber("2."));
214 |     }
```

## org.apache.commons.lang3.math.NumberUtilsTest.testIsNumber()
Resolved declaration: org.apache.commons.lang3.math.NumberUtilsTest.testIsNumber()
Source: src/test/org/apache/commons/lang3/math/NumberUtilsTest.java

```java
1002 |     public void testIsNumber() {
1003 |         String val = "12345";
1004 |         assertTrue("isNumber(String) 1 failed", NumberUtils.isNumber(val));
1005 |         assertTrue("isNumber(String)/createNumber(String) 1 failed", checkCreateNumber(val));
1006 |         val = "1234.5";
1007 |         assertTrue("isNumber(String) 2 failed", NumberUtils.isNumber(val));
1008 |         assertTrue("isNumber(String)/createNumber(String) 2 failed", checkCreateNumber(val));
1009 |         val = ".12345";
1010 |         assertTrue("isNumber(String) 3 failed", NumberUtils.isNumber(val));
1011 |         assertTrue("isNumber(String)/createNumber(String) 3 failed", checkCreateNumber(val));
1012 |         val = "1234E5";
1013 |         assertTrue("isNumber(String) 4 failed", NumberUtils.isNumber(val));
1014 |         assertTrue("isNumber(String)/createNumber(String) 4 failed", checkCreateNumber(val));
1015 |         val = "1234E+5";
1016 |         assertTrue("isNumber(String) 5 failed", NumberUtils.isNumber(val));
1017 |         assertTrue("isNumber(String)/createNumber(String) 5 failed", checkCreateNumber(val));
1018 |         val = "1234E-5";
1019 |         assertTrue("isNumber(String) 6 failed", NumberUtils.isNumber(val));
1020 |         assertTrue("isNumber(String)/createNumber(String) 6 failed", checkCreateNumber(val));
1021 |         val = "123.4E5";
1022 |         assertTrue("isNumber(String) 7 failed", NumberUtils.isNumber(val));
1023 |         assertTrue("isNumber(String)/createNumber(String) 7 failed", checkCreateNumber(val));
1024 |         val = "-1234";
1025 |         assertTrue("isNumber(String) 8 failed", NumberUtils.isNumber(val));
1026 |         assertTrue("isNumber(String)/createNumber(String) 8 failed", checkCreateNumber(val));
1027 |         val = "-1234.5";
1028 |         assertTrue("isNumber(String) 9 failed", NumberUtils.isNumber(val));
1029 |         assertTrue("isNumber(String)/createNumber(String) 9 failed", checkCreateNumber(val));
1030 |         val = "-.12345";
1031 |         assertTrue("isNumber(String) 10 failed", NumberUtils.isNumber(val));
1032 |         assertTrue("isNumber(String)/createNumber(String) 10 failed", checkCreateNumber(val));
1033 |         val = "-1234E5";
1034 |         assertTrue("isNumber(String) 11 failed", NumberUtils.isNumber(val));
1035 |         assertTrue("isNumber(String)/createNumber(String) 11 failed", checkCreateNumber(val));
1036 |         val = "0";
1037 |         assertTrue("isNumber(String) 12 failed", NumberUtils.isNumber(val));
1038 |         assertTrue("isNumber(String)/createNumber(String) 12 failed", checkCreateNumber(val));
1039 |         val = "-0";
1040 |         assertTrue("isNumber(String) 13 failed", NumberUtils.isNumber(val));
1041 |         assertTrue("isNumber(String)/createNumber(String) 13 failed", checkCreateNumber(val));
1042 |         val = "01234";
1043 |         assertTrue("isNumber(String) 14 failed", NumberUtils.isNumber(val));
1044 |         assertTrue("isNumber(String)/createNumber(String) 14 failed", checkCreateNumber(val));
1045 |         val = "-01234";
1046 |         assertTrue("isNumber(String) 15 failed", NumberUtils.isNumber(val));
1047 |         assertTrue("isNumber(String)/createNumber(String) 15 failed", checkCreateNumber(val));
1048 |         val = "0xABC123";
1049 |         assertTrue("isNumber(String) 16 failed", NumberUtils.isNumber(val));
1050 |         assertTrue("isNumber(String)/createNumber(String) 16 failed", checkCreateNumber(val));
1051 |         val = "0x0";
1052 |         assertTrue("isNumber(String) 17 failed", NumberUtils.isNumber(val));
1053 |         assertTrue("isNumber(String)/createNumber(String) 17 failed", checkCreateNumber(val));
1054 |         val = "123.4E21D";
1055 |         assertTrue("isNumber(String) 19 failed", NumberUtils.isNumber(val));
1056 |         assertTrue("isNumber(String)/createNumber(String) 19 failed", checkCreateNumber(val));
1057 |         val = "-221.23F";
1058 |         assertTrue("isNumber(String) 20 failed", NumberUtils.isNumber(val));
1059 |         assertTrue("isNumber(String)/createNumber(String) 20 failed", checkCreateNumber(val));
1060 |         val = "22338L";
1061 |         assertTrue("isNumber(String) 21 failed", NumberUtils.isNumber(val));
1062 |         assertTrue("isNumber(String)/createNumber(String) 21 failed", checkCreateNumber(val));
1063 |         val = null;
1064 |         assertTrue("isNumber(String) 1 Neg failed", !NumberUtils.isNumber(val));
1065 |         assertTrue("isNumber(String)/createNumber(String) 1 Neg failed", !checkCreateNumber(val));
1066 |         val = "";
1067 |         assertTrue("isNumber(String) 2 Neg failed", !NumberUtils.isNumber(val));
1068 |         assertTrue("isNumber(String)/createNumber(String) 2 Neg failed", !checkCreateNumber(val));
1069 |         val = "--2.3";
1070 |         assertTrue("isNumber(String) 3 Neg failed", !NumberUtils.isNumber(val));
1071 |         assertTrue("isNumber(String)/createNumber(String) 3 Neg failed", !checkCreateNumber(val));
1072 |         val = ".12.3";
1073 |         assertTrue("isNumber(String) 4 Neg failed", !NumberUtils.isNumber(val));
1074 |         assertTrue("isNumber(String)/createNumber(String) 4 Neg failed", !checkCreateNumber(val));
1075 |         val = "-123E";
1076 |         assertTrue("isNumber(String) 5 Neg failed", !NumberUtils.isNumber(val));
1077 |         assertTrue("isNumber(String)/createNumber(String) 5 Neg failed", !checkCreateNumber(val));
1078 |         val = "-123E+-212";
1079 |         assertTrue("isNumber(String) 6 Neg failed", !NumberUtils.isNumber(val));
1080 |         assertTrue("isNumber(String)/createNumber(String) 6 Neg failed", !checkCreateNumber(val));
1081 |         val = "-123E2.12";
1082 |         assertTrue("isNumber(String) 7 Neg failed", !NumberUtils.isNumber(val));
1083 |         assertTrue("isNumber(String)/createNumber(String) 7 Neg failed", !checkCreateNumber(val));
1084 |         val = "0xGF";
1085 |         assertTrue("isNumber(String) 8 Neg failed", !NumberUtils.isNumber(val));
1086 |         assertTrue("isNumber(String)/createNumber(String) 8 Neg failed", !checkCreateNumber(val));
1087 |         val = "0xFAE-1";
1088 |         assertTrue("isNumber(String) 9 Neg failed", !NumberUtils.isNumber(val));
1089 |         assertTrue("isNumber(String)/createNumber(String) 9 Neg failed", !checkCreateNumber(val));
1090 |         val = ".";
1091 |         assertTrue("isNumber(String) 10 Neg failed", !NumberUtils.isNumber(val));
1092 |         assertTrue("isNumber(String)/createNumber(String) 10 Neg failed", !checkCreateNumber(val));
1093 |         val = "-0ABC123";
1094 |         assertTrue("isNumber(String) 11 Neg failed", !NumberUtils.isNumber(val));
1095 |         assertTrue("isNumber(String)/createNumber(String) 11 Neg failed", !checkCreateNumber(val));
1096 |         val = "123.4E-D";
1097 |         assertTrue("isNumber(String) 12 Neg failed", !NumberUtils.isNumber(val));
1098 |         assertTrue("isNumber(String)/createNumber(String) 12 Neg failed", !checkCreateNumber(val));
1099 |         val = "123.4ED";
1100 |         assertTrue("isNumber(String) 13 Neg failed", !NumberUtils.isNumber(val));
1101 |         assertTrue("isNumber(String)/createNumber(String) 13 Neg failed", !checkCreateNumber(val));
1102 |         val = "1234E5l";
1103 |         assertTrue("isNumber(String) 14 Neg failed", !NumberUtils.isNumber(val));
1104 |         assertTrue("isNumber(String)/createNumber(String) 14 Neg failed", !checkCreateNumber(val));
1105 |         val = "11a";
1106 |         assertTrue("isNumber(String) 15 Neg failed", !NumberUtils.isNumber(val));
1107 |         assertTrue("isNumber(String)/createNumber(String) 15 Neg failed", !checkCreateNumber(val)); 
1108 |         val = "1a";
1109 |         assertTrue("isNumber(String) 16 Neg failed", !NumberUtils.isNumber(val));
1110 |         assertTrue("isNumber(String)/createNumber(String) 16 Neg failed", !checkCreateNumber(val)); 
1111 |         val = "a";
1112 |         assertTrue("isNumber(String) 17 Neg failed", !NumberUtils.isNumber(val));
1113 |         assertTrue("isNumber(String)/createNumber(String) 17 Neg failed", !checkCreateNumber(val)); 
1114 |         val = "11g";
1115 |         assertTrue("isNumber(String) 18 Neg failed", !NumberUtils.isNumber(val));
1116 |         assertTrue("isNumber(String)/createNumber(String) 18 Neg failed", !checkCreateNumber(val)); 
1117 |         val = "11z";
1118 |         assertTrue("isNumber(String) 19 Neg failed", !NumberUtils.isNumber(val));
1119 |         assertTrue("isNumber(String)/createNumber(String) 19 Neg failed", !checkCreateNumber(val)); 
1120 |         val = "11def";
1121 |         assertTrue("isNumber(String) 20 Neg failed", !NumberUtils.isNumber(val));
1122 |         assertTrue("isNumber(String)/createNumber(String) 20 Neg failed", !checkCreateNumber(val)); 
1123 |         val = "11d11";
1124 |         assertTrue("isNumber(String) 21 Neg failed", !NumberUtils.isNumber(val));
1125 |         assertTrue("isNumber(String)/createNumber(String) 21 Neg failed", !checkCreateNumber(val)); 
1126 |         val = "11 11";
1127 |         assertTrue("isNumber(String) 22 Neg failed", !NumberUtils.isNumber(val));
1128 |         assertTrue("isNumber(String)/createNumber(String) 22 Neg failed", !checkCreateNumber(val));
1129 |         val = " 1111";
1130 |         assertTrue("isNumber(String) 23 Neg failed", !NumberUtils.isNumber(val));
1131 |         assertTrue("isNumber(String)/createNumber(String) 23 Neg failed", !checkCreateNumber(val));
1132 |         val = "1111 ";
1133 |         assertTrue("isNumber(String) 24 Neg failed", !NumberUtils.isNumber(val));
1134 |         assertTrue("isNumber(String)/createNumber(String) 24 Neg failed", !checkCreateNumber(val));
1135 | 
1136 |         // LANG-521
1137 |         val = "2.";
1138 |         assertTrue("isNumber(String) LANG-521 failed", NumberUtils.isNumber(val));
1139 |     }
```
