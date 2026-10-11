# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldComparison3()
Resolved declaration: com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldComparison3()
Source: test/com/google/javascript/jscomp/PeepholeFoldConstantsTest.java

```java
699 |   public void testFoldComparison3() {
700 |     fold("x = !1 == !0", "x = false");
701 | 
702 |     fold("x = !0 == !0", "x = true");
703 |     fold("x = !1 == !1", "x = true");
704 |     fold("x = !1 == null", "x = false");
705 |     fold("x = !1 == !0", "x = false");
706 |     fold("x = !0 == null", "x = false");
707 | 
708 |     fold("!0 == !0", "true");
709 |     fold("!1 == null", "false");
710 |     fold("!1 == !0", "false");
711 |     fold("!0 == null", "false");
712 | 
713 |     fold("x = !0 === !0", "x = true");
714 |     fold("x = !1 === !1", "x = true");
715 |     fold("x = !1 === null", "x = false");
716 |     fold("x = !1 === !0", "x = false");
717 |     fold("x = !0 === null", "x = false");
718 | 
719 |     fold("!0 === !0", "true");
720 |     fold("!1 === null", "false");
721 |     fold("!1 === !0", "false");
722 |     fold("!0 === null", "false");
723 |   }
```

## com.google.javascript.jscomp.PeepholeFoldConstantsTest.testInvertibleOperators()
Resolved declaration: com.google.javascript.jscomp.PeepholeFoldConstantsTest.testInvertibleOperators()
Source: test/com/google/javascript/jscomp/PeepholeFoldConstantsTest.java

```java
1094 |   public void testInvertibleOperators() {
1095 |     Map<String, String> inverses = ImmutableMap.<String, String>builder()
1096 |         .put("==", "!=")
1097 |         .put("===", "!==")
1098 |         .put("<=", ">")
1099 |         .put("<", ">=")
1100 |         .put(">=", "<")
1101 |         .put(">", "<=")
1102 |         .put("!=", "==")
1103 |         .put("!==", "===")
1104 |         .build();
1105 |     Set<String> comparators = ImmutableSet.of("<=", "<", ">=", ">");
1106 |     Set<String> equalitors = ImmutableSet.of("==", "===");
1107 |     Set<String> uncomparables = ImmutableSet.of("undefined", "void 0");
1108 |     List<String> operators = ImmutableList.copyOf(inverses.values());
1109 |     for (int iOperandA = 0; iOperandA < LITERAL_OPERANDS.size(); iOperandA++) {
1110 |       for (int iOperandB = 0;
1111 |            iOperandB < LITERAL_OPERANDS.size();
1112 |            iOperandB++) {
1113 |         for (int iOp = 0; iOp < operators.size(); iOp++) {
1114 |           String a = LITERAL_OPERANDS.get(iOperandA);
1115 |           String b = LITERAL_OPERANDS.get(iOperandB);
1116 |           String op = operators.get(iOp);
1117 |           String inverse = inverses.get(op);
1118 | 
1119 |           // Test invertability.
1120 |           if (comparators.contains(op) &&
1121 |               (uncomparables.contains(a) || uncomparables.contains(b))) {
1122 |             assertSameResults(join(a, op, b), "false");
1123 |             assertSameResults(join(a, inverse, b), "false");
1124 |           } else if (a.equals(b) && equalitors.contains(op)) {
1125 |             if (a.equals("NaN") || a.equals("Infinity")) {
1126 |               foldSame(join(a, op, b));
1127 |               foldSame(join(a, inverse, b));
1128 |             } else {
1129 |               assertSameResults(join(a, op, b), "true");
1130 |               assertSameResults(join(a, inverse, b), "false");
1131 |             }
1132 |           } else {
1133 |             assertNotSameResults(join(a, op, b), join(a, inverse, b));
1134 |           }
1135 |         }
1136 |       }
1137 |     }
1138 |   }
```

## com.google.javascript.jscomp.PeepholeFoldConstantsTest.testCommutativeOperators()
Resolved declaration: com.google.javascript.jscomp.PeepholeFoldConstantsTest.testCommutativeOperators()
Source: test/com/google/javascript/jscomp/PeepholeFoldConstantsTest.java

```java
1140 |   public void testCommutativeOperators() {
1141 |     List<String> operators =
1142 |         ImmutableList.of(
1143 |             "==",
1144 |             "!=",
1145 |             "===",
1146 |             "!==",
1147 |             "*",
1148 |             "|",
1149 |             "&",
1150 |             "^");
1151 |     for (int iOperandA = 0; iOperandA < LITERAL_OPERANDS.size(); iOperandA++) {
1152 |       for (int iOperandB = iOperandA;
1153 |            iOperandB < LITERAL_OPERANDS.size();
1154 |            iOperandB++) {
1155 |         for (int iOp = 0; iOp < operators.size(); iOp++) {
1156 |           String a = LITERAL_OPERANDS.get(iOperandA);
1157 |           String b = LITERAL_OPERANDS.get(iOperandB);
1158 |           String op = operators.get(iOp);
1159 | 
1160 |           // Test commutativity.
1161 |           // TODO(nicksantos): Eventually, all cases should be collapsed.
1162 |           assertSameResultsOrUncollapsed(join(a, op, b), join(b, op, a));
1163 |         }
1164 |       }
1165 |     }
1166 |   }
```
