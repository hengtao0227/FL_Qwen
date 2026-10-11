# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.linear.ArrayRealVectorTest.testBasicFunctions()
Resolved declaration: org.apache.commons.math.linear.ArrayRealVectorTest.testBasicFunctions()
Source: src/test/java/org/apache/commons/math/linear/ArrayRealVectorTest.java

```java
1080 |     public void testBasicFunctions() {
1081 |         ArrayRealVector v1 = new ArrayRealVector(vec1);
1082 |         ArrayRealVector v2 = new ArrayRealVector(vec2);
1083 |         ArrayRealVector v5 = new ArrayRealVector(vec5);
1084 |         ArrayRealVector v_null = new ArrayRealVector(vec_null);
1085 | 
1086 |         RealVectorTestImpl v2_t = new RealVectorTestImpl(vec2);
1087 | 
1088 |         // emacs calc: [-4, 0, 3, 1, -6, 3] A --> 8.4261497731763586307
1089 |         double d_getNorm = v5.getNorm();
1090 |         assertEquals("compare values  ", 8.4261497731763586307, d_getNorm);
1091 | 
1092 |         // emacs calc: [-4, 0, 3, 1, -6, 3] vN --> 17
1093 |         double d_getL1Norm = v5.getL1Norm();
1094 |         assertEquals("compare values  ", 17.0, d_getL1Norm);
1095 | 
1096 |         // emacs calc: [-4, 0, 3, 1, -6, 3] vn --> 6
1097 |         double d_getLInfNorm = v5.getLInfNorm();
1098 |         assertEquals("compare values  ", 6.0, d_getLInfNorm);
1099 | 
1100 | 
1101 |         //octave =  sqrt(sumsq(v1-v2))
1102 |         double dist = v1.getDistance(v2);
1103 |         assertEquals("compare values  ",v1.subtract(v2).getNorm(), dist );
1104 | 
1105 |         //octave =  sqrt(sumsq(v1-v2))
1106 |         double dist_2 = v1.getDistance(v2_t);
1107 |         assertEquals("compare values  ", v1.subtract(v2).getNorm(),dist_2 );
1108 | 
1109 |         //octave =  sqrt(sumsq(v1-v2))
1110 |         double dist_3 = v1.getDistance((RealVector) v2);
1111 |         assertEquals("compare values  ", v1.subtract(v2).getNorm(),dist_3 );
1112 | 
1113 |         //octave =  ???
1114 |         double d_getL1Distance = v1. getL1Distance(v2);
1115 |         assertEquals("compare values  ",9d, d_getL1Distance );
1116 | 
1117 |         double d_getL1Distance_2 = v1. getL1Distance(v2_t);
1118 |         assertEquals("compare values  ",9d, d_getL1Distance_2 );
1119 | 
1120 |         double d_getL1Distance_3 = v1. getL1Distance((RealVector) v2);
1121 |         assertEquals("compare values  ",9d, d_getL1Distance_3 );
1122 | 
1123 |         //octave =  ???
1124 |         double d_getLInfDistance = v1. getLInfDistance(v2);
1125 |         assertEquals("compare values  ",3d, d_getLInfDistance );
1126 | 
1127 |         double d_getLInfDistance_2 = v1. getLInfDistance(v2_t);
1128 |         assertEquals("compare values  ",3d, d_getLInfDistance_2 );
1129 | 
1130 |         double d_getLInfDistance_3 = v1. getLInfDistance((RealVector) v2);
1131 |         assertEquals("compare values  ",3d, d_getLInfDistance_3 );
1132 | 
1133 |         //octave =  v1 + v2
1134 |         ArrayRealVector v_add = v1.add(v2);
1135 |         double[] result_add = {5d, 7d, 9d};
1136 |         assertClose("compare vect" ,v_add.getData(),result_add,normTolerance);
1137 | 
1138 |         RealVectorTestImpl vt2 = new RealVectorTestImpl(vec2);
1139 |         RealVector v_add_i = v1.add(vt2);
1140 |         double[] result_add_i = {5d, 7d, 9d};
1141 |         assertClose("compare vect" ,v_add_i.getData(),result_add_i,normTolerance);
1142 | 
1143 |         //octave =  v1 - v2
1144 |         ArrayRealVector v_subtract = v1.subtract(v2);
1145 |         double[] result_subtract = {-3d, -3d, -3d};
1146 |         assertClose("compare vect" ,v_subtract.getData(),result_subtract,normTolerance);
1147 | 
1148 |         RealVector v_subtract_i = v1.subtract(vt2);
1149 |         double[] result_subtract_i = {-3d, -3d, -3d};
1150 |         assertClose("compare vect" ,v_subtract_i.getData(),result_subtract_i,normTolerance);
1151 | 
1152 |         // octave v1 .* v2
1153 |         ArrayRealVector  v_ebeMultiply = v1.ebeMultiply(v2);
1154 |         double[] result_ebeMultiply = {4d, 10d, 18d};
1155 |         assertClose("compare vect" ,v_ebeMultiply.getData(),result_ebeMultiply,normTolerance);
1156 | 
1157 |         RealVector  v_ebeMultiply_2 = v1.ebeMultiply(v2_t);
1158 |         double[] result_ebeMultiply_2 = {4d, 10d, 18d};
1159 |         assertClose("compare vect" ,v_ebeMultiply_2.getData(),result_ebeMultiply_2,normTolerance);
1160 | 
1161 |         RealVector  v_ebeMultiply_3 = v1.ebeMultiply((RealVector) v2);
1162 |         double[] result_ebeMultiply_3 = {4d, 10d, 18d};
1163 |         assertClose("compare vect" ,v_ebeMultiply_3.getData(),result_ebeMultiply_3,normTolerance);
1164 | 
1165 |         // octave v1 ./ v2
1166 |         ArrayRealVector  v_ebeDivide = v1.ebeDivide(v2);
1167 |         double[] result_ebeDivide = {0.25d, 0.4d, 0.5d};
1168 |         assertClose("compare vect" ,v_ebeDivide.getData(),result_ebeDivide,normTolerance);
1169 | 
1170 |         RealVector  v_ebeDivide_2 = v1.ebeDivide(v2_t);
1171 |         double[] result_ebeDivide_2 = {0.25d, 0.4d, 0.5d};
1172 |         assertClose("compare vect" ,v_ebeDivide_2.getData(),result_ebeDivide_2,normTolerance);
1173 | 
1174 |         RealVector  v_ebeDivide_3 = v1.ebeDivide((RealVector) v2);
1175 |         double[] result_ebeDivide_3 = {0.25d, 0.4d, 0.5d};
1176 |         assertClose("compare vect" ,v_ebeDivide_3.getData(),result_ebeDivide_3,normTolerance);
1177 | 
1178 |         // octave  dot(v1,v2)
1179 |         double dot =  v1.dotProduct(v2);
1180 |         assertEquals("compare val ",32d, dot);
1181 | 
1182 |         // octave  dot(v1,v2_t)
1183 |         double dot_2 =  v1.dotProduct(v2_t);
1184 |         assertEquals("compare val ",32d, dot_2);
1185 | 
1186 |         RealMatrix m_outerProduct = v1.outerProduct(v2);
1187 |         assertEquals("compare val ",4d, m_outerProduct.getEntry(0,0));
1188 | 
1189 |         RealMatrix m_outerProduct_2 = v1.outerProduct(v2_t);
1190 |         assertEquals("compare val ",4d, m_outerProduct_2.getEntry(0,0));
1191 | 
1192 |         RealMatrix m_outerProduct_3 = v1.outerProduct((RealVector) v2);
1193 |         assertEquals("compare val ",4d, m_outerProduct_3.getEntry(0,0));
1194 | 
1195 |         RealVector v_unitVector = v1.unitVector();
1196 |         RealVector v_unitVector_2 = v1.mapDivide(v1.getNorm());
1197 |         assertClose("compare vect" ,v_unitVector.getData(),v_unitVector_2.getData(),normTolerance);
1198 | 
1199 |         try {
1200 |             v_null.unitVector();
1201 |             fail("Expecting ArithmeticException");
1202 |         } catch (ArithmeticException ex) {
1203 |             // expected behavior
1204 |         } catch (Exception e) {
1205 |             fail("wrong exception caught");
1206 |         }
1207 | 
1208 |         ArrayRealVector v_unitize = (ArrayRealVector)v1.copy();
1209 |         v_unitize.unitize();
1210 |         assertClose("compare vect" ,v_unitVector_2.getData(),v_unitize.getData(),normTolerance);
1211 |         try {
1212 |             v_null.unitize();
1213 |             fail("Expecting ArithmeticException");
1214 |         } catch (ArithmeticException ex) {
1215 |             // expected behavior
1216 |         } catch (Exception e) {
1217 |             fail("wrong exception caught");
1218 |         }
1219 | 
1220 |         ArrayRealVector v_projection = v1.projection(v2);
1221 |         double[] result_projection = {1.662337662337662, 2.0779220779220777, 2.493506493506493};
1222 |         assertClose("compare vect", v_projection.getData(), result_projection, normTolerance);
1223 | 
1224 |         RealVector v_projection_2 = v1.projection(v2_t);
1225 |         double[] result_projection_2 = {1.662337662337662, 2.0779220779220777, 2.493506493506493};
1226 |         assertClose("compare vect", v_projection_2.getData(), result_projection_2, normTolerance);
1227 | 
1228 |         RealVector v_projection_3 = v1.projection(v2.getData());
1229 |         double[] result_projection_3 = {1.662337662337662, 2.0779220779220777, 2.493506493506493};
1230 |         assertClose("compare vect", v_projection_3.getData(), result_projection_3, normTolerance);
1231 | 
1232 |     }
```

## org.apache.commons.math.linear.SparseRealVectorTest.testBasicFunctions()
Resolved declaration: org.apache.commons.math.linear.SparseRealVectorTest.testBasicFunctions()
Source: src/test/java/org/apache/commons/math/linear/SparseRealVectorTest.java

```java
950 |     public void testBasicFunctions() {
951 |         OpenMapRealVector v1 = new OpenMapRealVector(vec1);
952 |         OpenMapRealVector v2 = new OpenMapRealVector(vec2);
953 |         OpenMapRealVector v5 = new OpenMapRealVector(vec5);
954 |         OpenMapRealVector v_null = new OpenMapRealVector(vec_null);
955 | 
956 |         SparseRealVectorTestImpl v2_t = new SparseRealVectorTestImpl(vec2);
957 | 
958 |         // emacs calc: [-4, 0, 3, 1, -6, 3] A --> 8.4261497731763586307
959 |         double d_getNorm = v5.getNorm();
960 |         assertEquals("compare values  ", 8.4261497731763586307, d_getNorm);
961 | 
962 |         // emacs calc: [-4, 0, 3, 1, -6, 3] vN --> 17
963 |         double d_getL1Norm = v5.getL1Norm();
964 |         assertEquals("compare values  ", 17.0, d_getL1Norm);
965 | 
966 |         // emacs calc: [-4, 0, 3, 1, -6, 3] vn --> 6
967 |         double d_getLInfNorm = v5.getLInfNorm();
968 |         assertEquals("compare values  ", 6.0, d_getLInfNorm);
969 | 
970 |         //octave =  sqrt(sumsq(v1-v2))
971 |         double dist = v1.getDistance(v2);
972 |         assertEquals("compare values  ",v1.subtract(v2).getNorm(), dist );
973 | 
974 |         //octave =  sqrt(sumsq(v1-v2))
975 |         double dist_2 = v1.getDistance(v2_t);
976 |         assertEquals("compare values  ", v1.subtract(v2).getNorm(),dist_2 );
977 | 
978 |         //octave =  ???
979 |         double d_getL1Distance = v1. getL1Distance(v2);
980 |         assertEquals("compare values  ",9d, d_getL1Distance );
981 | 
982 |         double d_getL1Distance_2 = v1. getL1Distance(v2_t);
983 |         assertEquals("compare values  ",9d, d_getL1Distance_2 );
984 | 
985 |         //octave =  ???
986 |         double d_getLInfDistance = v1. getLInfDistance(v2);
987 |         assertEquals("compare values  ",3d, d_getLInfDistance );
988 | 
989 |         double d_getLInfDistance_2 = v1. getLInfDistance(v2_t);
990 |         assertEquals("compare values  ",3d, d_getLInfDistance_2 );
991 | 
992 |         //octave =  v1 + v2
993 |         OpenMapRealVector v_add = v1.add(v2);
994 |         double[] result_add = {5d, 7d, 9d};
995 |         assertClose("compare vect" ,v_add.getData(),result_add,normTolerance);
996 | 
997 |         SparseRealVectorTestImpl vt2 = new SparseRealVectorTestImpl(vec2);
998 |         RealVector v_add_i = v1.add(vt2);
999 |         double[] result_add_i = {5d, 7d, 9d};
1000 |         assertClose("compare vect" ,v_add_i.getData(),result_add_i,normTolerance);
1001 | 
1002 |         //octave =  v1 - v2
1003 |         OpenMapRealVector v_subtract = v1.subtract(v2);
1004 |         double[] result_subtract = {-3d, -3d, -3d};
1005 |         assertClose("compare vect" ,v_subtract.getData(),result_subtract,normTolerance);
1006 | 
1007 |         RealVector v_subtract_i = v1.subtract(vt2);
1008 |         double[] result_subtract_i = {-3d, -3d, -3d};
1009 |         assertClose("compare vect" ,v_subtract_i.getData(),result_subtract_i,normTolerance);
1010 | 
1011 |         // octave v1 .* v2
1012 |         RealVector  v_ebeMultiply = v1.ebeMultiply(v2);
1013 |         double[] result_ebeMultiply = {4d, 10d, 18d};
1014 |         assertClose("compare vect" ,v_ebeMultiply.getData(),result_ebeMultiply,normTolerance);
1015 | 
1016 |         RealVector  v_ebeMultiply_2 = v1.ebeMultiply(v2_t);
1017 |         double[] result_ebeMultiply_2 = {4d, 10d, 18d};
1018 |         assertClose("compare vect" ,v_ebeMultiply_2.getData(),result_ebeMultiply_2,normTolerance);
1019 | 
1020 |         // octave v1 ./ v2
1021 |         RealVector  v_ebeDivide = v1.ebeDivide(v2);
1022 |         double[] result_ebeDivide = {0.25d, 0.4d, 0.5d};
1023 |         assertClose("compare vect" ,v_ebeDivide.getData(),result_ebeDivide,normTolerance);
1024 | 
1025 |         RealVector  v_ebeDivide_2 = v1.ebeDivide(v2_t);
1026 |         double[] result_ebeDivide_2 = {0.25d, 0.4d, 0.5d};
1027 |         assertClose("compare vect" ,v_ebeDivide_2.getData(),result_ebeDivide_2,normTolerance);
1028 | 
1029 |         // octave  dot(v1,v2)
1030 |         double dot =  v1.dotProduct(v2);
1031 |         assertEquals("compare val ",32d, dot);
1032 | 
1033 |         // octave  dot(v1,v2_t)
1034 |         double dot_2 =  v1.dotProduct(v2_t);
1035 |         assertEquals("compare val ",32d, dot_2);
1036 | 
1037 |         RealMatrix m_outerProduct = v1.outerProduct(v2);
1038 |         assertEquals("compare val ",4d, m_outerProduct.getEntry(0,0));
1039 | 
1040 |         RealMatrix m_outerProduct_2 = v1.outerProduct(v2_t);
1041 |         assertEquals("compare val ",4d, m_outerProduct_2.getEntry(0,0));
1042 | 
1043 |         RealVector v_unitVector = v1.unitVector();
1044 |         RealVector v_unitVector_2 = v1.mapDivide(v1.getNorm());
1045 |         assertClose("compare vect" ,v_unitVector.getData(),v_unitVector_2.getData(),normTolerance);
1046 | 
1047 |         try {
1048 |             v_null.unitVector();
1049 |             fail("Expecting ArithmeticException");
1050 |         } catch (ArithmeticException ex) {
1051 |             // expected behavior
1052 |         } catch (Exception e) {
1053 |             fail("wrong exception caught");
1054 |         }
1055 | 
1056 |         OpenMapRealVector v_unitize = v1.copy();
1057 |         v_unitize.unitize();
1058 |         assertClose("compare vect" ,v_unitVector_2.getData(),v_unitize.getData(),normTolerance);
1059 |         try {
1060 |             v_null.unitize();
1061 |             fail("Expecting ArithmeticException");
1062 |         } catch (ArithmeticException ex) {
1063 |             // expected behavior
1064 |         } catch (Exception e) {
1065 |             fail("wrong exception caught");
1066 |         }
1067 | 
1068 |         RealVector v_projection = v1.projection(v2);
1069 |         double[] result_projection = {1.662337662337662, 2.0779220779220777, 2.493506493506493};
1070 |         assertClose("compare vect", v_projection.getData(), result_projection, normTolerance);
1071 | 
1072 |         RealVector v_projection_2 = v1.projection(v2_t);
1073 |         double[] result_projection_2 = {1.662337662337662, 2.0779220779220777, 2.493506493506493};
1074 |         assertClose("compare vect", v_projection_2.getData(), result_projection_2, normTolerance);
1075 | 
1076 |     }
```
