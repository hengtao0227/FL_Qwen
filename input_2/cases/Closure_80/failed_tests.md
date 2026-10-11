# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.NodeUtilTest.testIsBooleanResult()
Resolved declaration: com.google.javascript.jscomp.NodeUtilTest.testIsBooleanResult()
Source: test/com/google/javascript/jscomp/NodeUtilTest.java

```java
1467 |   public void testIsBooleanResult() {
1468 |     assertFalse(NodeUtil.isBooleanResult(getNode("1")));
1469 |     assertTrue(NodeUtil.isBooleanResult(getNode("true")));
1470 |     assertFalse(NodeUtil.isBooleanResult(getNode("+true")));
1471 |     assertFalse(NodeUtil.isBooleanResult(getNode("+1")));
1472 |     assertFalse(NodeUtil.isBooleanResult(getNode("-1")));
1473 |     assertFalse(NodeUtil.isBooleanResult(getNode("-Infinity")));
1474 |     assertFalse(NodeUtil.isBooleanResult(getNode("Infinity")));
1475 |     assertFalse(NodeUtil.isBooleanResult(getNode("NaN")));
1476 |     assertFalse(NodeUtil.isBooleanResult(getNode("undefined")));
1477 |     assertFalse(NodeUtil.isBooleanResult(getNode("void 0")));
1478 | 
1479 |     assertFalse(NodeUtil.isBooleanResult(getNode("a << b")));
1480 |     assertFalse(NodeUtil.isBooleanResult(getNode("a >> b")));
1481 |     assertFalse(NodeUtil.isBooleanResult(getNode("a >>> b")));
1482 | 
1483 |     assertTrue(NodeUtil.isBooleanResult(getNode("a == b")));
1484 |     assertTrue(NodeUtil.isBooleanResult(getNode("a != b")));
1485 |     assertTrue(NodeUtil.isBooleanResult(getNode("a === b")));
1486 |     assertTrue(NodeUtil.isBooleanResult(getNode("a !== b")));
1487 |     assertTrue(NodeUtil.isBooleanResult(getNode("a < b")));
1488 |     assertTrue(NodeUtil.isBooleanResult(getNode("a > b")));
1489 |     assertTrue(NodeUtil.isBooleanResult(getNode("a <= b")));
1490 |     assertTrue(NodeUtil.isBooleanResult(getNode("a >= b")));
1491 |     assertTrue(NodeUtil.isBooleanResult(getNode("a in b")));
1492 |     assertTrue(NodeUtil.isBooleanResult(getNode("a instanceof b")));
1493 | 
1494 |     assertFalse(NodeUtil.isBooleanResult(getNode("'a'")));
1495 |     assertFalse(NodeUtil.isBooleanResult(getNode("'a'+b")));
1496 |     assertFalse(NodeUtil.isBooleanResult(getNode("a+'b'")));
1497 |     assertFalse(NodeUtil.isBooleanResult(getNode("a+b")));
1498 |     assertFalse(NodeUtil.isBooleanResult(getNode("a()")));
1499 |     assertFalse(NodeUtil.isBooleanResult(getNode("''.a")));
1500 |     assertFalse(NodeUtil.isBooleanResult(getNode("a.b")));
1501 |     assertFalse(NodeUtil.isBooleanResult(getNode("a.b()")));
1502 |     assertFalse(NodeUtil.isBooleanResult(getNode("a().b()")));
1503 |     assertFalse(NodeUtil.isBooleanResult(getNode("new a()")));
1504 |     assertTrue(NodeUtil.isBooleanResult(getNode("delete a")));
1505 | 
1506 |     // Definitely not boolean
1507 |     assertFalse(NodeUtil.isBooleanResult(getNode("([true,false])")));
1508 |     assertFalse(NodeUtil.isBooleanResult(getNode("({a:true})")));
1509 | 
1510 |     // These are boolean but aren't handled yet, "false" here means "unknown".
1511 |     assertTrue(NodeUtil.isBooleanResult(getNode("true && false")));
1512 |     assertTrue(NodeUtil.isBooleanResult(getNode("true || false")));
1513 |     assertTrue(NodeUtil.isBooleanResult(getNode("a ? true : false")));
1514 |     assertTrue(NodeUtil.isBooleanResult(getNode("a,true")));
1515 |     assertTrue(NodeUtil.isBooleanResult(getNode("a=true")));
1516 |     assertFalse(NodeUtil.isBooleanResult(getNode("a=1")));
1517 |   }
```

## com.google.javascript.jscomp.NodeUtilTest.testLocalValue1()
Resolved declaration: com.google.javascript.jscomp.NodeUtilTest.testLocalValue1()
Source: test/com/google/javascript/jscomp/NodeUtilTest.java

```java
1073 |   public void testLocalValue1() throws Exception {
1074 |     // Names are not known to be local.
1075 |     assertFalse(testLocalValue("x"));
1076 |     assertFalse(testLocalValue("x()"));
1077 |     assertFalse(testLocalValue("this"));
1078 |     assertFalse(testLocalValue("arguments"));
1079 | 
1080 |     // We can't know if new objects are local unless we know
1081 |     // that they don't alias themselves.
1082 |     assertFalse(testLocalValue("new x()"));
1083 | 
1084 |     // property references are assume to be non-local
1085 |     assertFalse(testLocalValue("(new x()).y"));
1086 |     assertFalse(testLocalValue("(new x())['y']"));
1087 | 
1088 |     // Primitive values are local
1089 |     assertTrue(testLocalValue("null"));
1090 |     assertTrue(testLocalValue("undefined"));
1091 |     assertTrue(testLocalValue("Infinity"));
1092 |     assertTrue(testLocalValue("NaN"));
1093 |     assertTrue(testLocalValue("1"));
1094 |     assertTrue(testLocalValue("'a'"));
1095 |     assertTrue(testLocalValue("true"));
1096 |     assertTrue(testLocalValue("false"));
1097 |     assertTrue(testLocalValue("[]"));
1098 |     assertTrue(testLocalValue("{}"));
1099 | 
1100 |     // The contents of arrays and objects don't matter
1101 |     assertTrue(testLocalValue("[x]"));
1102 |     assertTrue(testLocalValue("{'a':x}"));
1103 | 
1104 |     // Pre-increment results in primitive number
1105 |     assertTrue(testLocalValue("++x"));
1106 |     assertTrue(testLocalValue("--x"));
1107 | 
1108 |     // Post-increment, the previous value matters.
1109 |     assertFalse(testLocalValue("x++"));
1110 |     assertFalse(testLocalValue("x--"));
1111 | 
1112 |     // The left side of an only assign matters if it is an alias or mutable.
1113 |     assertTrue(testLocalValue("x=1"));
1114 |     assertFalse(testLocalValue("x=[]"));
1115 |     assertFalse(testLocalValue("x=y"));
1116 |     // The right hand side of assignment opts don't matter, as they force
1117 |     // a local result.
1118 |     assertTrue(testLocalValue("x+=y"));
1119 |     assertTrue(testLocalValue("x*=y"));
1120 |     // Comparisons always result in locals, as they force a local boolean
1121 |     // result.
1122 |     assertTrue(testLocalValue("x==y"));
1123 |     assertTrue(testLocalValue("x!=y"));
1124 |     assertTrue(testLocalValue("x>y"));
1125 |     // Only the right side of a comma matters
1126 |     assertTrue(testLocalValue("(1,2)"));
1127 |     assertTrue(testLocalValue("(x,1)"));
1128 |     assertFalse(testLocalValue("(x,y)"));
1129 | 
1130 |     // Both the operands of OR matter
1131 |     assertTrue(testLocalValue("1||2"));
1132 |     assertFalse(testLocalValue("x||1"));
1133 |     assertFalse(testLocalValue("x||y"));
1134 |     assertFalse(testLocalValue("1||y"));
1135 | 
1136 |     // Both the operands of AND matter
1137 |     assertTrue(testLocalValue("1&&2"));
1138 |     assertFalse(testLocalValue("x&&1"));
1139 |     assertFalse(testLocalValue("x&&y"));
1140 |     assertFalse(testLocalValue("1&&y"));
1141 | 
1142 |     // Only the results of HOOK matter
1143 |     assertTrue(testLocalValue("x?1:2"));
1144 |     assertFalse(testLocalValue("x?x:2"));
1145 |     assertFalse(testLocalValue("x?1:x"));
1146 |     assertFalse(testLocalValue("x?x:y"));
1147 | 
1148 |     // Results of ops are local values
1149 |     assertTrue(testLocalValue("!y"));
1150 |     assertTrue(testLocalValue("~y"));
1151 |     assertTrue(testLocalValue("y + 1"));
1152 |     assertTrue(testLocalValue("y + z"));
1153 |     assertTrue(testLocalValue("y * z"));
1154 | 
1155 |     assertTrue(testLocalValue("'a' in x"));
1156 |     assertTrue(testLocalValue("typeof x"));
1157 |     assertTrue(testLocalValue("x instanceof y"));
1158 | 
1159 |     assertTrue(testLocalValue("void x"));
1160 |     assertTrue(testLocalValue("void 0"));
1161 | 
1162 |     assertFalse(testLocalValue("{}.x"));
1163 | 
1164 |     assertTrue(testLocalValue("{}.toString()"));
1165 |     assertTrue(testLocalValue("o.toString()"));
1166 | 
1167 |     assertFalse(testLocalValue("o.valueOf()"));
1168 | 
1169 |     assertTrue(testLocalValue("delete a.b"));
1170 |   }
```
