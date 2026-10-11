# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FunctionInjectorTest.testInline19b()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline19b()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
944 |   public void testInline19b() {
945 |     helperInlineReferenceToFunction(
946 |         "var x = 1; var y = 2;" +
947 |         "function foo(a,b){y = a; x = b;}; " +
948 |         "function bar() { foo(x,y); }",
949 |         "var x = 1; var y = 2;" +
950 |         "function foo(a,b){y = a; x = b;}; " +
951 |         "function bar() {" +
952 |            "{var b$$inline_1=y;" +
953 |             "y = x;" +
954 |             "x = b$$inline_1;}" +
955 |         "}",
956 |         "foo", INLINE_BLOCK);
957 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInlineIntoLoop()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInlineIntoLoop()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
959 |   public void testInlineIntoLoop() {
960 |     helperInlineReferenceToFunction(
961 |         "function foo(a){var b;return a;}; " +
962 |         "for(;1;){ foo(1); }",
963 |         "function foo(a){var b;return a;}; " +
964 |         "for(;1;){ {" +
965 |             "var b$$inline_1=void 0;1}}",
966 |         "foo", INLINE_BLOCK);
967 | 
968 |     helperInlineReferenceToFunction(
969 |         "function foo(a){var b;return a;}; " +
970 |         "do{ foo(1); } while(1)",
971 |         "function foo(a){var b;return a;}; " +
972 |         "do{ {" +
973 |             "var b$$inline_1=void 0;1}}while(1)",
974 |         "foo", INLINE_BLOCK);
975 | 
976 |     helperInlineReferenceToFunction(
977 |         "function foo(a){for(var b in c)return a;}; " +
978 |         "for(;1;){ foo(1); }",
979 |         "function foo(a){var b;for(b in c)return a;}; " +
980 |         "for(;1;){ {JSCompiler_inline_label_foo_2:{" +
981 |             "var b$$inline_1=void 0;for(b$$inline_1 in c){" +
982 |               "1;break JSCompiler_inline_label_foo_2" +
983 |             "}}}}",
984 |         "foo", INLINE_BLOCK);
985 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInline13()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline13()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
864 |   public void testInline13() {
865 |     // Parameter has side-effects.
866 |     helperInlineReferenceToFunction(
867 |         "function foo(a){return a;}; " +
868 |         "function x() { foo(x++); }",
869 |         "function foo(a){return a;}; " +
870 |         "function x() {{var a$$inline_0=x++;" +
871 |             "a$$inline_0}}",
872 |         "foo", INLINE_BLOCK);
873 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInline14()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline14()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
875 |   public void testInline14() {
876 |     // Parameter has side-effects.
877 |     helperInlineReferenceToFunction(
878 |         "function foo(a){return a+a;}; foo(x++);",
879 |         "function foo(a){return a+a;}; " +
880 |             "{var a$$inline_0=x++;" +
881 |             " a$$inline_0+" +
882 |             "a$$inline_0;}",
883 |         "foo", INLINE_BLOCK);
884 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInline15()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline15()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
886 |   public void testInline15() {
887 |     // Parameter has mutable, references more than once.
888 |     helperInlineReferenceToFunction(
889 |         "function foo(a){return a+a;}; foo(new Date());",
890 |         "function foo(a){return a+a;}; " +
891 |             "{var a$$inline_0=new Date();" +
892 |             " a$$inline_0+" +
893 |             "a$$inline_0;}",
894 |         "foo", INLINE_BLOCK);
895 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInline16()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline16()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
897 |   public void testInline16() {
898 |     // Parameter is large, references more than once.
899 |     helperInlineReferenceToFunction(
900 |         "function foo(a){return a+a;}; foo(function(){});",
901 |         "function foo(a){return a+a;}; " +
902 |             "{var a$$inline_0=function(){};" +
903 |             " a$$inline_0+" +
904 |             "a$$inline_0;}",
905 |         "foo", INLINE_BLOCK);
906 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInline17()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline17()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
908 |   public void testInline17() {
909 |     // Parameter has side-effects.
910 |     helperInlineReferenceToFunction(
911 |         "function foo(a){return true;}; foo(goo());",
912 |         "function foo(a){return true;};" +
913 |             "{var a$$inline_0=goo();true}",
914 |         "foo", INLINE_BLOCK);
915 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInline18()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline18()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
917 |   public void testInline18() {
918 |     // This doesn't bring names into the global name space.
919 |     helperInlineReferenceToFunction(
920 |         "function foo(a){var b;return a;}; " +
921 |             "function x() { foo(goo()); }",
922 |             "function foo(a){var b;return a;}; " +
923 |             "function x() {{var a$$inline_0=goo();" +
924 |                 "var b$$inline_1;a$$inline_0}}",
925 |         "foo", INLINE_BLOCK);
926 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInline19()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInline19()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
928 |   public void testInline19() {
929 |     // Properly alias.
930 |     helperInlineReferenceToFunction(
931 |         "var x = 1; var y = 2;" +
932 |         "function foo(a,b){x = b; y = a;}; " +
933 |         "function bar() { foo(x,y); }",
934 |         "var x = 1; var y = 2;" +
935 |         "function foo(a,b){x = b; y = a;}; " +
936 |         "function bar() {" +
937 |            "{var a$$inline_0=x;" +
938 |             "x = y;" +
939 |             "y = a$$inline_0;}" +
940 |         "}",
941 |         "foo", INLINE_BLOCK);
942 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testBug1897706()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testBug1897706()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
1314 |   public void testBug1897706() {
1315 |     helperInlineReferenceToFunction(
1316 |         "function foo(a){}; foo(x())",
1317 |         "function foo(a){}; {var a$$inline_0=x()}",
1318 |         "foo", INLINE_BLOCK);
1319 | 
1320 |     helperInlineReferenceToFunction(
1321 |         "function foo(a){bar()}; foo(x())",
1322 |         "function foo(a){bar()}; {var a$$inline_0=x();bar()}",
1323 |         "foo", INLINE_BLOCK);
1324 | 
1325 |     helperInlineReferenceToFunction(
1326 |         "function foo(a,b){bar()}; foo(x(),y())",
1327 |         "function foo(a,b){bar()};" +
1328 |         "{var a$$inline_0=x();var b$$inline_1=y();bar()}",
1329 |         "foo", INLINE_BLOCK);
1330 |   }
```

## com.google.javascript.jscomp.FunctionInjectorTest.testInlineFunctionWithInnerFunction5()
Resolved declaration: com.google.javascript.jscomp.FunctionInjectorTest.testInlineFunctionWithInnerFunction5()
Source: test/com/google/javascript/jscomp/FunctionInjectorTest.java

```java
1023 |   public void testInlineFunctionWithInnerFunction5() {
1024 |     // Call with inner function statement.
1025 |     helperInlineReferenceToFunction(
1026 |         "function foo(){function x() {var a; return true;} return x}; foo();",
1027 |         "function foo(){function x(){var a;return true}return x};" +
1028 |             "{var x$$inline_0 = function(){" +
1029 |             "var a$$inline_1;return true};x$$inline_0}",
1030 |         "foo", INLINE_BLOCK);
1031 |   }
```

## com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateWithParameters3()
Resolved declaration: com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateWithParameters3()
Source: test/com/google/javascript/jscomp/FunctionToBlockMutatorTest.java

```java
110 |   public void testMutateWithParameters3() {
111 |     // Parameter has side-effects.
112 |     helperMutate(
113 |         "function foo(a){return a;}; " +
114 |         "function x() { foo(x++); }",
115 |         "{var a$$inline_0 = x++; a$$inline_0}",
116 |         "foo", null);
117 |   }
```

## com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateCallInLoopVars1()
Resolved declaration: com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateCallInLoopVars1()
Source: test/com/google/javascript/jscomp/FunctionToBlockMutatorTest.java

```java
148 |   public void testMutateCallInLoopVars1() {
149 |     // baseline: outside a loop, the constant remains constant.
150 |     boolean callInLoop = false;
151 |     helperMutate(
152 |         "function foo(a){var B = bar(); a;}; foo(1);",
153 |         "{var B$$inline_1=bar(); 1;}",
154 |         "foo", null, false, callInLoop);
155 |     // ... in a loop, the constant-ness is removed.
156 |     // TODO(johnlenz): update this test to look for the const annotation.
157 |     callInLoop = true;
158 |     helperMutate(
159 |         "function foo(a){var B = bar(); a;}; foo(1);",
160 |         "{var B$$inline_1 = bar(); 1;}",
161 |         "foo", null, false, callInLoop);
162 |   }
```

## com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateInitializeUninitializedVars1()
Resolved declaration: com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateInitializeUninitializedVars1()
Source: test/com/google/javascript/jscomp/FunctionToBlockMutatorTest.java

```java
128 |   public void testMutateInitializeUninitializedVars1() {
129 |     helperMutate(
130 |         "function foo(a){var b;return a;}; foo(1);",
131 |         "{var b$$inline_1=void 0;1}",
132 |         "foo", null, false, true);
133 |   }
```

## com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateInitializeUninitializedVars2()
Resolved declaration: com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateInitializeUninitializedVars2()
Source: test/com/google/javascript/jscomp/FunctionToBlockMutatorTest.java

```java
135 |   public void testMutateInitializeUninitializedVars2() {
136 |     helperMutate(
137 |         "function foo(a){for(var b in c)return a;}; foo(1);",
138 |         "{JSCompiler_inline_label_foo_2:" +
139 |           "{" +
140 |             "for(var b$$inline_1 in c){" +
141 |                 "1;break JSCompiler_inline_label_foo_2" +
142 |              "}" +
143 |           "}" +
144 |         "}",
145 |         "foo", null);
146 |   }
```

## com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateFunctionDefinition()
Resolved declaration: com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutateFunctionDefinition()
Source: test/com/google/javascript/jscomp/FunctionToBlockMutatorTest.java

```java
164 |   public void testMutateFunctionDefinition() {
165 |      // function declarations are rewritten as function
166 |      // expressions
167 |      helperMutate(
168 |         "function foo(a){function g(){}}; foo(1);",
169 |         "{var g$$inline_1=function(){};}",
170 |         "foo", null);
171 |   }
```

## com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutate8()
Resolved declaration: com.google.javascript.jscomp.FunctionToBlockMutatorTest.testMutate8()
Source: test/com/google/javascript/jscomp/FunctionToBlockMutatorTest.java

```java
119 |   public void testMutate8() {
120 |     // Parameter has side-effects.
121 |     helperMutate(
122 |         "function foo(a){return a+a;}; foo(x++);",
123 |         "{var a$$inline_0 = x++;" +
124 |             "a$$inline_0 + a$$inline_0;}",
125 |         "foo", null);
126 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testLoopWithFunctionWithFunction()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testLoopWithFunctionWithFunction()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2199 |   public void testLoopWithFunctionWithFunction() {
2200 |     assumeMinimumCapture = true;
2201 |     test("function _testLocalVariableInLoop_() {\n" +
2202 |         "  var result = 0;\n" +
2203 |         "  function foo() {\n" +
2204 |         "    var arr = [1, 2, 3, 4, 5];\n" +
2205 |         "    for (var i = 0, l = arr.length; i < l; i++) {\n" +
2206 |         "      var j = arr[i];\n" +
2207 |         // don't inline this function, because the correct behavior depends
2208 |         // captured values.
2209 |         "      (function() {\n" +
2210 |         "        var k = j;\n" +
2211 |         "        setTimeout(function() { result += k; }, 5 * i);\n" +
2212 |         "      })();\n" +
2213 |         "    }\n" +
2214 |         "  }\n" +
2215 |         "  foo();\n" +
2216 |         "}",
2217 |         "function _testLocalVariableInLoop_(){\n" +
2218 |         "  var result=0;\n" +
2219 |         "  {" +
2220 |         "  var arr$$inline_0=[1,2,3,4,5];\n" +
2221 |         "  var i$$inline_1=0;\n" +
2222 |         "  var l$$inline_2=arr$$inline_0.length;\n" +
2223 |         "  for(;i$$inline_1<l$$inline_2;i$$inline_1++){\n" +
2224 |         "    var j$$inline_3=arr$$inline_0[i$$inline_1];\n" +
2225 |         "    (function(){\n" +
2226 |         "       var k$$inline_4=j$$inline_3;\n" +
2227 |         "       setTimeout(function(){result+=k$$inline_4},5*i$$inline_1)\n" +
2228 |         "     })()\n" +
2229 |         "  }\n" +
2230 |         "  }\n" +
2231 |         "}");
2232 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables16()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables16()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
842 |   public void testShadowVariables16() {
843 |     assumeMinimumCapture = false;
844 |     // Inline functions defined as a child of the CALL node.
845 |     test("var a=3;" +
846 |          "function foo(){return a}" +
847 |          "(function(){var a=5;(function(){foo()})()})()",
848 |          "var a=3;" +
849 |          "{var a$$inline_0=5;{a}}"
850 |          );
851 | 
852 |     assumeMinimumCapture = true;
853 |     // Inline functions defined as a child of the CALL node.
854 |     test("var a=3;" +
855 |          "function foo(){return a}" +
856 |          "(function(){var a=5;(function(){foo()})()})()",
857 |          "var a=3;" +
858 |          "{var a$$inline_1=5;{a}}"
859 |          );
860 | 
861 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables18()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables18()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
873 |   public void testShadowVariables18() {
874 |     test("var a=0;" +
875 |         "function bar(){return a+a}" +
876 |         "function foo(){var a=3;return bar()}" +
877 |         "function _goo(){var a=2;var x=foo();}",
878 | 
879 |         "var a=0;" +
880 |         "function _goo(){var a$$2=2;var x;" +
881 |         "{var a$$inline_0=3;x=a+a}}");
882 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testCostBasedInlining11()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testCostBasedInlining11()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
994 |   public void testCostBasedInlining11() {
995 |     // With block inlining
996 |     test("function f(a){return a + a;}" +
997 |          "var a = f(f(1))",
998 |          "var a;" +
999 |          "{var a$$inline_0=1+1;" +
1000 |          "a=a$$inline_0+a$$inline_0}");
1001 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testMixedModeInliningCosting3()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testMixedModeInliningCosting3()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
527 |   public void testMixedModeInliningCosting3() {
528 |     // Do inline here because the function definition can be eliminated.
529 |     test(
530 |         "function foo(a,b){return a+b+a+b+4+5+6+7+8+9+1+2+3+10}" +
531 |         "foo(1,2);" +
532 |         "foo(2,3,x())",
533 | 
534 |         "1+2+1+2+4+5+6+7+8+9+1+2+3+10;" +
535 |         "{var JSCompiler_inline_anon_param_2=x();" +
536 |         "2+3+2+3+4+5+6+7+8+9+1+2+3+10}");
537 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineNeverMutateConstants()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineNeverMutateConstants()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
616 |   public void testInlineNeverMutateConstants() {
617 |     test("function f(x){return x=1}f(undefined)",
618 |          "{var x$$inline_0=undefined;" +
619 |          "x$$inline_0=1}");
620 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineWithThis7()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineWithThis7()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1892 |   public void testInlineWithThis7() {
1893 |     assumeStrictThis = true;
1894 |     // In strict mode, "this" is never coerced so we can use the provided value.
1895 |     test("function f(a){a=1;this} f.call();",
1896 |          "{var a$$inline_0=void 0; a$$inline_0=1; void 0;}");
1897 |     test("function f(a){a=1;this} f.call(x, x);",
1898 |          "{var a$$inline_0=x; a$$inline_0=1; x;}");
1899 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testAnonymous1()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testAnonymous1()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2167 |   public void testAnonymous1() {
2168 |     assumeMinimumCapture = false;
2169 |     test("(function(){var a=10;(function(){var b=a;a++;alert(b)})()})();",
2170 |          "{var a$$inline_0=10;" +
2171 |          "{var b$$inline_1=a$$inline_0;" +
2172 |          "a$$inline_0++;alert(b$$inline_1)}}");
2173 | 
2174 |     assumeMinimumCapture = true;
2175 |     test("(function(){var a=10;(function(){var b=a;a++;alert(b)})()})();",
2176 |         "{var a$$inline_2=10;" +
2177 |         "{var b$$inline_0=a$$inline_2;" +
2178 |         "a$$inline_2++;alert(b$$inline_0)}}");
2179 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testAnonymous3()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testAnonymous3()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2185 |   public void testAnonymous3() {
2186 |     // Introducing a new value into is tricky
2187 |     assumeMinimumCapture = false;
2188 |     testSame("(function(){var a=10;(function(){arguments;})()})();");
2189 | 
2190 |     assumeMinimumCapture = true;
2191 |     test("(function(){var a=10;(function(){arguments;})()})();",
2192 |          "{var a$$inline_0=10;(function(){arguments;})();}");
2193 | 
2194 |     test("(function(){(function(){arguments;})()})();",
2195 |         "{(function(){arguments;})()}");
2196 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables1()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables1()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
676 |   public void testShadowVariables1() {
677 |     // The Normalize pass now guarantees that that globals are never shadowed
678 |     // by locals.
679 | 
680 |     // "foo" is inlined here as its parameter "a" doesn't conflict.
681 |     // "bar" is assigned a new name.
682 |     test("var a=0;" +
683 |          "function foo(a){return 3+a}" +
684 |          "function bar(){var a=foo(4)}" +
685 |          "bar();",
686 | 
687 |          "var a=0;" +
688 |          "{var a$$inline_0=3+4}");
689 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables3()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables3()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
704 |   public void testShadowVariables3() {
705 |     // "foo" is inlined into exported "_bar", aliasing foo's "a".
706 |     test("var a=0;" +
707 |         "function foo(){var a=2;return 3+a}" +
708 |         "function _bar(){a=foo()}",
709 | 
710 |         "var a=0;" +
711 |         "function _bar(){{var a$$inline_0=2;" +
712 |         "a=3+a$$inline_0}}");
713 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables6()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables6()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
736 |   public void testShadowVariables6() {
737 |     test("var a=0;" +
738 |         "function foo(){var a=4;return 3+a}" +
739 |         "function _bar(a){a=foo(4)}",
740 | 
741 |         "var a=0;function _bar(a$$2){{" +
742 |         "var a$$inline_0=4;" +
743 |         "a$$2=3+a$$inline_0}}");
744 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables7()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testShadowVariables7()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
746 |   public void testShadowVariables7() {
747 |     assumeMinimumCapture = false;
748 |     test("var a=3;" +
749 |          "function foo(){return a}" +
750 |          "(function(){var a=5;(function(){foo()})()})()",
751 |          "var a=3;" +
752 |          "{var a$$inline_0=5;{a}}"
753 |          );
754 | 
755 |     assumeMinimumCapture = true;
756 |     test("var a=3;" +
757 |          "function foo(){return a}" +
758 |          "(function(){var a=5;(function(){foo()})()})()",
759 |          "var a=3;" +
760 |          "{var a$$inline_1=5;{a}}"
761 |          );
762 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testFunctionExpressionCallInlining11b()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testFunctionExpressionCallInlining11b()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1676 |   public void testFunctionExpressionCallInlining11b() {
1677 |     assumeMinimumCapture = false;
1678 |     // Can't inline functions that return inner functions and have local names.
1679 |     testSame("((function(){var a; return function(){foo()}})())();");
1680 | 
1681 |     assumeMinimumCapture = true;
1682 |     test(
1683 |         "((function(){var a; return function(){foo()}})())();",
1684 | 
1685 |         "{var JSCompiler_inline_result$$0;" +
1686 |         "var a$$inline_1;" +
1687 |         "JSCompiler_inline_result$$0=function(){foo()};}" +
1688 |         "JSCompiler_inline_result$$0()");
1689 | 
1690 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testComplexInlineNoResultNoParamCall3()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testComplexInlineNoResultNoParamCall3()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1206 |   public void testComplexInlineNoResultNoParamCall3() {
1207 |     // We now allow vars in the global space.
1208 |     //   Don't inline into vars into global scope.
1209 |     //   testSame("function f(){a();b();var z=1+1}f()");
1210 | 
1211 |     // But do inline into functions
1212 |     test("function f(){a();b();var z=1+1}function _foo(){f()}",
1213 |          "function _foo(){{a();b();var z$$inline_0=1+1}}");
1214 | 
1215 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testCostBasedInlining9()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testCostBasedInlining9()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
973 |   public void testCostBasedInlining9() {
974 |     // Here both direct and block inlining is used.  The call to f as a
975 |     // parameter is inlined directly, which the call to f with f as a parameter
976 |     // is inlined using block inlining.
977 |     test("function f(a){return 1 + a + a;}" +
978 |          "var a = f(f(1));",
979 |          "var a;" +
980 |          "{var a$$inline_0=1+1+1;" +
981 |          "a=1+a$$inline_0+a$$inline_0}");
982 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testMethodWithFunctionWithFunction()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testMethodWithFunctionWithFunction()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2234 |   public void testMethodWithFunctionWithFunction() {
2235 |     assumeMinimumCapture = true;
2236 |     test("function _testLocalVariable_() {\n" +
2237 |         "  var result = 0;\n" +
2238 |         "  function foo() {\n" +
2239 |         "      var j = [i];\n" +
2240 |         "      (function(j) {\n" +
2241 |         "        setTimeout(function() { result += j; }, 5 * i);\n" +
2242 |         "      })(j);\n" +
2243 |         "      j = null;" +
2244 |         "  }\n" +
2245 |         "  foo();\n" +
2246 |         "}",
2247 |         "function _testLocalVariable_(){\n" +
2248 |         "  var result=0;\n" +
2249 |         "  {\n" +
2250 |         "  var j$$inline_2=[i];\n" +
2251 |         "  {\n" +
2252 |         "  var j$$inline_0=j$$inline_2;\n" +  // this temp is needed.
2253 |         "  setTimeout(function(){result+=j$$inline_0},5*i);\n" +
2254 |         "  }\n" +
2255 |         "  j$$inline_2=null\n" + // because this value can be modified later.
2256 |         "  }\n" +
2257 |         "}");
2258 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testFunctionExpressionYCombinator()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testFunctionExpressionYCombinator()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1902 |   public void testFunctionExpressionYCombinator() {
1903 |     assumeMinimumCapture = false;
1904 |     testSame(
1905 |         "var factorial = ((function(M) {\n" +
1906 |         "      return ((function(f) {\n" +
1907 |         "                 return M(function(arg) {\n" +
1908 |         "                            return (f(f))(arg);\n" +
1909 |         "                            })\n" +
1910 |         "               })\n" +
1911 |         "              (function(f) {\n" +
1912 |         "                 return M(function(arg) {\n" +
1913 |         "                            return (f(f))(arg);\n" +
1914 |         "                           })\n" +
1915 |         "                 }));\n" +
1916 |         "     })\n" +
1917 |         "    (function(f) {\n" +
1918 |         "       return function(n) {\n" +
1919 |         "        if (n === 0)\n" +
1920 |         "          return 1;\n" +
1921 |         "        else\n" +
1922 |         "          return n * f(n - 1);\n" +
1923 |         "       };\n" +
1924 |         "     }));\n" +
1925 |         "\n" +
1926 |         "factorial(5)\n");
1927 | 
1928 |     assumeMinimumCapture = true;
1929 |     test(
1930 |         "var factorial = ((function(M) {\n" +
1931 |         "      return ((function(f) {\n" +
1932 |         "                 return M(function(arg) {\n" +
1933 |         "                            return (f(f))(arg);\n" +
1934 |         "                            })\n" +
1935 |         "               })\n" +
1936 |         "              (function(f) {\n" +
1937 |         "                 return M(function(arg) {\n" +
1938 |         "                            return (f(f))(arg);\n" +
1939 |         "                           })\n" +
1940 |         "                 }));\n" +
1941 |         "     })\n" +
1942 |         "    (function(f) {\n" +
1943 |         "       return function(n) {\n" +
1944 |         "        if (n === 0)\n" +
1945 |         "          return 1;\n" +
1946 |         "        else\n" +
1947 |         "          return n * f(n - 1);\n" +
1948 |         "       };\n" +
1949 |         "     }));\n" +
1950 |         "\n" +
1951 |         "factorial(5)\n",
1952 |         "var factorial;\n" +
1953 |         "{\n" +
1954 |         "var M$$inline_4 = function(f$$2) {\n" +
1955 |         "  return function(n){if(n===0)return 1;else return n*f$$2(n-1)}\n" +
1956 |         "};\n" +
1957 |         "{\n" +
1958 |         "var f$$inline_0=function(f$$inline_7){\n" +
1959 |         "  return M$$inline_4(\n" +
1960 |         "    function(arg$$inline_8){\n" +
1961 |         "      return f$$inline_7(f$$inline_7)(arg$$inline_8)\n" +
1962 |         "     })\n" +
1963 |         "};\n" +
1964 |         "factorial=M$$inline_4(\n" +
1965 |         "  function(arg$$inline_1){\n" +
1966 |         "    return f$$inline_0(f$$inline_0)(arg$$inline_1)\n" +
1967 |         "});\n" +
1968 |         "}\n" +
1969 |         "}" +
1970 |         "factorial(5)");
1971 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testComplexInlineVars7()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testComplexInlineVars7()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1318 |   public void testComplexInlineVars7() {
1319 |     test("function f(x,y){if (x) return y(); else return true;}" +
1320 |          "var b=1;var z=f(1,b)",
1321 |          "var b=1;var z;" +
1322 |          "{JSCompiler_inline_label_f_2:{if(1){z=b();" +
1323 |          "break JSCompiler_inline_label_f_2" +
1324 |          "}else{" +
1325 |          "z=true;break JSCompiler_inline_label_f_2}z=void 0}}");
1326 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testComplexFunctionWithFunctionDefinition2a()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testComplexFunctionWithFunctionDefinition2a()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1516 |   public void testComplexFunctionWithFunctionDefinition2a() {
1517 |     assumeMinimumCapture = false;
1518 | 
1519 |     // Don't inline if local names might be captured.
1520 |     testSame("(function(){" +
1521 |         "var f = function(a){call(function(){return a})};f()})()");
1522 | 
1523 |     assumeMinimumCapture = true;
1524 | 
1525 |     test("(function(){" +
1526 |          "var f = function(a){call(function(){return a})};f()})()",
1527 |          "{{var a$$inline_0=void 0;call(function(){return a$$inline_0})}}");
1528 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testComplexInline7()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testComplexInline7()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1268 |   public void testComplexInline7() {
1269 |     test("function f(x,y){if (x) return y(); else return true;}" +
1270 |          "var b=1;z=f(1,b)",
1271 |          "var b=1;{JSCompiler_inline_label_f_2:{if(1){z=b();" +
1272 |          "break JSCompiler_inline_label_f_2}else{z=true;" +
1273 |          "break JSCompiler_inline_label_f_2}z=void 0}}");
1274 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testFunctionExpressionOmega()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testFunctionExpressionOmega()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1756 |   public void testFunctionExpressionOmega() {
1757 |     // ... with unused recursive name.
1758 |     test("(function (f){f(f)})(function(f){f(f)})",
1759 |          "{var f$$inline_0=function(f$$1){f$$1(f$$1)};" +
1760 |           "{{f$$inline_0(f$$inline_0)}}}");
1761 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions15b()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions15b()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
233 |   public void testInlineFunctions15b() {
234 |     assumeMinimumCapture = false;
235 | 
236 |     // closure factories: don't inline closure with locals into global scope.
237 |     test("function foo(){var x;return function(a){return a+1}}" +
238 |          "var b=function(){return c};" +
239 |          "var d=b()+foo()",
240 | 
241 |          "function foo(){var x;return function(a){return a+1}}" +
242 |          "var d=c+foo()");
243 | 
244 |     assumeMinimumCapture = true;
245 | 
246 |     test("function foo(){var x;return function(a){return a+1}}" +
247 |          "var b=function(){return c};" +
248 |          "var d=b()+foo()",
249 | 
250 |          "var JSCompiler_temp_const$$0 = c;\n" +
251 |          "{\n" +
252 |          "var JSCompiler_inline_result$$1;\n" +
253 |          "var x$$inline_2;\n" +
254 |          "JSCompiler_inline_result$$1 = " +
255 |          "    function(a$$inline_3){ return a$$inline_3+1 };\n" +
256 |          "}" +
257 |          "var d=JSCompiler_temp_const$$0 + JSCompiler_inline_result$$1");
258 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions15d()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions15d()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
282 |   public void testInlineFunctions15d() {
283 |     assumeMinimumCapture = false;
284 | 
285 |     // closure factories: don't inline functions with vars.
286 |     test("function foo(){var x; return function(a){return a+1}}" +
287 |          "var b=function(){return c};" +
288 |          "function _x(){ var d=b()+foo() }",
289 | 
290 |          "function foo(){var x; return function(a){return a+1}}" +
291 |          "function _x(){ var d=c+foo() }");
292 | 
293 |     assumeMinimumCapture = true;
294 | 
295 |     // closure factories: don't inline functions with vars.
296 |     test("function foo(){var x; return function(a){return a+1}}" +
297 |          "var b=function(){return c};" +
298 |          "function _x(){ var d=b()+foo() }",
299 | 
300 |          "function _x() { \n" +
301 |          "  var JSCompiler_temp_const$$0 = c;\n" +
302 |          "  {\n" +
303 |          "  var JSCompiler_inline_result$$1;\n" +
304 |          "  var x$$inline_2;\n" +
305 |          "  JSCompiler_inline_result$$1 = " +
306 |          "      function(a$$inline_3) {return a$$inline_3+1};\n" +
307 |          "  }\n" +
308 |          "  var d = JSCompiler_temp_const$$0+JSCompiler_inline_result$$1\n" +
309 |          "}");
310 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions16a()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions16a()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
312 |   public void testInlineFunctions16a() {
313 |     assumeMinimumCapture = false;
314 | 
315 |     testSame("function foo(b){return window.bar(function(){c(b)})}" +
316 |          "var d=foo(e)");
317 | 
318 |     assumeMinimumCapture = true;
319 | 
320 |     test(
321 |         "function foo(b){return window.bar(function(){c(b)})}" +
322 |         "var d=foo(e)",
323 |         "var d;{var b$$inline_0=e;" +
324 |         "d=window.bar(function(){c(b$$inline_0)})}");
325 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testBug4944818()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testBug4944818()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2076 |   public void testBug4944818() {
2077 |     test(
2078 |         "var getDomServices_ = function(self) {\n" +
2079 |         "  if (!self.domServices_) {\n" +
2080 |         "    self.domServices_ = goog$component$DomServices.get(" +
2081 |         "        self.appContext_);\n" +
2082 |         "  }\n" +
2083 |         "\n" +
2084 |         "  return self.domServices_;\n" +
2085 |         "};\n" +
2086 |         "\n" +
2087 |         "var getOwnerWin_ = function(self) {\n" +
2088 |         "  return getDomServices_(self).getDomHelper().getWindow();\n" +
2089 |         "};\n" +
2090 |         "\n" +
2091 |         "HangoutStarter.prototype.launchHangout = function() {\n" +
2092 |         "  var self = a.b;\n" +
2093 |         "  var myUrl = new goog.Uri(getOwnerWin_(self).location.href);\n" +
2094 |         "};",
2095 |         "HangoutStarter.prototype.launchHangout = function() { " +
2096 |         "  var self$$2 = a.b;" +
2097 |         "  var JSCompiler_temp_const$$0 = goog.Uri;" +
2098 |         "  {" +
2099 |         "  var JSCompiler_inline_result$$1;" +
2100 |         "  var self$$inline_2 = self$$2;" +
2101 |         "  if (!self$$inline_2.domServices_) {" +
2102 |         "    self$$inline_2.domServices_ = goog$component$DomServices.get(" +
2103 |         "        self$$inline_2.appContext_);" +
2104 |         "  }" +
2105 |         "  JSCompiler_inline_result$$1=self$$inline_2.domServices_;" +
2106 |         "  }" +
2107 |         "  var myUrl = new JSCompiler_temp_const$$0(" +
2108 |         "      JSCompiler_inline_result$$1.getDomHelper()." +
2109 |         "          getWindow().location.href)" +
2110 |         "}");
2111 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testComplexSample()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testComplexSample()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1391 |   public void testComplexSample() {
1392 |     String result = "" +
1393 |       "{{" +
1394 |       "var styleSheet$$inline_2=null;" +
1395 |       "if(goog$userAgent$IE)" +
1396 |         "styleSheet$$inline_2=0;" +
1397 |       "else " +
1398 |         "var head$$inline_3=0;" +
1399 |       "{" +
1400 |         "var element$$inline_4=" +
1401 |             "styleSheet$$inline_2;" +
1402 |         "var stylesString$$inline_5=a;" +
1403 |         "if(goog$userAgent$IE)" +
1404 |           "element$$inline_4.cssText=" +
1405 |               "stylesString$$inline_5;" +
1406 |         "else " +
1407 |         "{" +
1408 |           "var propToSet$$inline_6=" +
1409 |               "\"innerText\";" +
1410 |           "element$$inline_4[" +
1411 |               "propToSet$$inline_6]=" +
1412 |                   "stylesString$$inline_5" +
1413 |         "}" +
1414 |       "}" +
1415 |       "styleSheet$$inline_2" +
1416 |       "}}";
1417 | 
1418 |     test("var foo = function(stylesString, opt_element) { " +
1419 |         "var styleSheet = null;" +
1420 |         "if (goog$userAgent$IE)" +
1421 |           "styleSheet = 0;" +
1422 |         "else " +
1423 |           "var head = 0;" +
1424 |         "" +
1425 |         "goo$zoo(styleSheet, stylesString);" +
1426 |         "return styleSheet;" +
1427 |      " };\n " +
1428 | 
1429 |      "var goo$zoo = function(element, stylesString) {" +
1430 |         "if (goog$userAgent$IE)" +
1431 |           "element.cssText = stylesString;" +
1432 |         "else {" +
1433 |           "var propToSet = 'innerText';" +
1434 |           "element[propToSet] = stylesString;" +
1435 |         "}" +
1436 |       "};" +
1437 |       "(function(){foo(a,b);})();",
1438 |      result);
1439 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified1()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified1()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
547 |   public void testNoInlineIfParametersModified1() {
548 |     // Assignment
549 |     test("function f(x){return x=1}f(undefined)",
550 |          "{var x$$inline_0=undefined;" +
551 |          "x$$inline_0=1}");
552 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified2()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified2()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
554 |   public void testNoInlineIfParametersModified2() {
555 |     test("function f(x){return (x)=1;}f(2)",
556 |          "{var x$$inline_0=2;" +
557 |          "x$$inline_0=1}");
558 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified3()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified3()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
560 |   public void testNoInlineIfParametersModified3() {
561 |     // Assignment variant.
562 |     test("function f(x){return x*=2}f(2)",
563 |          "{var x$$inline_0=2;" +
564 |          "x$$inline_0*=2}");
565 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified4()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified4()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
567 |   public void testNoInlineIfParametersModified4() {
568 |     // Assignment in if.
569 |     test("function f(x){return x?(x=2):0}f(2)",
570 |          "{var x$$inline_0=2;" +
571 |          "x$$inline_0?(" +
572 |          "x$$inline_0=2):0}");
573 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified5()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified5()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
575 |   public void testNoInlineIfParametersModified5() {
576 |     // Assignment in if, multiple params
577 |     test("function f(x,y){return x?(y=2):0}f(2,undefined)",
578 |          "{var y$$inline_1=undefined;2?(" +
579 |          "y$$inline_1=2):0}");
580 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified6()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified6()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
582 |   public void testNoInlineIfParametersModified6() {
583 |     test("function f(x,y){return x?(y=2):0}f(2)",
584 |          "{var y$$inline_1=void 0;2?(" +
585 |          "y$$inline_1=2):0}");
586 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified7()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testNoInlineIfParametersModified7()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
588 |   public void testNoInlineIfParametersModified7() {
589 |     // Increment
590 |     test("function f(a){return++a<++a}f(1)",
591 |          "{var a$$inline_0=1;" +
592 |          "++a$$inline_0<" +
593 |          "++a$$inline_0}");
594 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testIssue423()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testIssue423()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
2113 |   public void testIssue423() {
2114 |     assumeMinimumCapture = false;
2115 |     test(
2116 |         "(function($) {\n" +
2117 |         "  $.fn.multicheck = function(options) {\n" +
2118 |         "    initialize.call(this, options);\n" +
2119 |         "  };\n" +
2120 |         "\n" +
2121 |         "  function initialize(options) {\n" +
2122 |         "    options.checkboxes = $(this).siblings(':checkbox');\n" +
2123 |         "    preload_check_all.call(this);\n" +
2124 |         "  }\n" +
2125 |         "\n" +
2126 |         "  function preload_check_all() {\n" +
2127 |         "    $(this).data('checkboxes');\n" +
2128 |         "  }\n" +
2129 |         "})(jQuery)",
2130 |         "(function($){" +
2131 |         "  $.fn.multicheck=function(options$$1){" +
2132 |         "    {" +
2133 |         "     options$$1.checkboxes=$(this).siblings(\":checkbox\");" +
2134 |         "     {" +
2135 |         "       $(this).data(\"checkboxes\")" +
2136 |         "     }" +
2137 |         "    }" +
2138 |         "  }" +
2139 |         "})(jQuery)");
2140 | 
2141 |     assumeMinimumCapture = true;
2142 |     test(
2143 |         "(function($) {\n" +
2144 |         "  $.fn.multicheck = function(options) {\n" +
2145 |         "    initialize.call(this, options);\n" +
2146 |         "  };\n" +
2147 |         "\n" +
2148 |         "  function initialize(options) {\n" +
2149 |         "    options.checkboxes = $(this).siblings(':checkbox');\n" +
2150 |         "    preload_check_all.call(this);\n" +
2151 |         "  }\n" +
2152 |         "\n" +
2153 |         "  function preload_check_all() {\n" +
2154 |         "    $(this).data('checkboxes');\n" +
2155 |         "  }\n" +
2156 |         "})(jQuery)",
2157 |         "{var $$$inline_0=jQuery;\n" +
2158 |         "$$$inline_0.fn.multicheck=function(options$$inline_4){\n" +
2159 |         "  {options$$inline_4.checkboxes=" +
2160 |             "$$$inline_0(this).siblings(\":checkbox\");\n" +
2161 |         "  {$$$inline_0(this).data(\"checkboxes\")}" +
2162 |         "  }\n" +
2163 |         "}\n" +
2164 |         "}");
2165 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testComplexFunctionWithFunctionDefinition2()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testComplexFunctionWithFunctionDefinition2()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1503 |   public void testComplexFunctionWithFunctionDefinition2() {
1504 |     assumeMinimumCapture = false;
1505 | 
1506 |     // Don't inline if local names might be captured.
1507 |     testSame("function f(a){call(function(){return})}f()");
1508 | 
1509 |     assumeMinimumCapture = true;
1510 | 
1511 |     test("(function(){" +
1512 |          "var f = function(a){call(function(){return a})};f()})()",
1513 |          "{{var a$$inline_0=void 0;call(function(){return a$$inline_0})}}");
1514 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testComplexFunctionWithFunctionDefinition3()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testComplexFunctionWithFunctionDefinition3()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1530 |   public void testComplexFunctionWithFunctionDefinition3() {
1531 |     assumeMinimumCapture = false;
1532 | 
1533 |     // Don't inline if local names might need to be captured.
1534 |     testSame("function f(){var a; call(function(){return a})}f()");
1535 | 
1536 |     assumeMinimumCapture = true;
1537 | 
1538 |     test("function f(){var a; call(function(){return a})}f()",
1539 |          "{var a$$inline_0;call(function(){return a$$inline_0})}");
1540 | 
1541 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testDecomposeFunctionExpressionInCall()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testDecomposeFunctionExpressionInCall()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
1552 |   public void testDecomposeFunctionExpressionInCall() {
1553 |     test(
1554 |         "(function(map){descriptions_=map})(\n" +
1555 |            "function(){\n" +
1556 |               "var ret={};\n" +
1557 |               "ret[ONE]='a';\n" +
1558 |               "ret[TWO]='b';\n" +
1559 |               "return ret\n" +
1560 |            "}()\n" +
1561 |         ");",
1562 |         "{" +
1563 |         "var JSCompiler_inline_result$$0;" +
1564 |         "var ret$$inline_1={};\n" +
1565 |         "ret$$inline_1[ONE]='a';\n" +
1566 |         "ret$$inline_1[TWO]='b';\n" +
1567 |         "JSCompiler_inline_result$$0 = ret$$inline_1;\n" +
1568 |         "}" +
1569 |         "{" +
1570 |         "descriptions_=JSCompiler_inline_result$$0;" +
1571 |         "}"
1572 |         );
1573 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineNeverOverrideNewValues()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineNeverOverrideNewValues()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
622 |   public void testInlineNeverOverrideNewValues() {
623 |     test("function f(a){return++a<++a}f(1)",
624 |         "{var a$$inline_0=1;" +
625 |         "++a$$inline_0<++a$$inline_0}");
626 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs1()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs1()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
652 |   public void testInlineBlockMutableArgs1() {
653 |     test("function foo(x){x+x}foo([])",
654 |          "{var x$$inline_0=[];" +
655 |          "x$$inline_0+x$$inline_0}");
656 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs2()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs2()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
658 |   public void testInlineBlockMutableArgs2() {
659 |     test("function foo(x){x+x}foo(new Date)",
660 |          "{var x$$inline_0=new Date;" +
661 |          "x$$inline_0+x$$inline_0}");
662 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs3()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs3()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
664 |   public void testInlineBlockMutableArgs3() {
665 |     test("function foo(x){x+x}foo(true&&new Date)",
666 |          "{var x$$inline_0=true&&new Date;" +
667 |          "x$$inline_0+x$$inline_0}");
668 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs4()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineBlockMutableArgs4()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
670 |   public void testInlineBlockMutableArgs4() {
671 |     test("function foo(x){x+x}foo({})",
672 |          "{var x$$inline_0={};" +
673 |          "x$$inline_0+x$$inline_0}");
674 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions10()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions10()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
182 |   public void testInlineFunctions10() {
183 |     test("function INC(x){return x++}" +
184 |          "var y=INC(i);y=INC(i)",
185 |          "var y;" +
186 |          "{var x$$inline_0=i;" +
187 |          "y=x$$inline_0++}" +
188 |          "{var x$$inline_2=i;" +
189 |          "y=x$$inline_2++}");
190 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions13()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions13()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
208 |   public void testInlineFunctions13() {
209 |     // inline as block if the input parameter has side-effects.
210 |     test("function f(x){return x}" +
211 |          "var y=f(i++)",
212 |          "var y;{var x$$inline_0=i++;y=x$$inline_0}");
213 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions22()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions22()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
373 |   public void testInlineFunctions22() {
374 |     // Another tricky case ... test nested compiler inlines
375 |     test("function plex(a){if(a) return 0;else return 1;}" +
376 |          "function foo(a, b){return bar(a+b)}" +
377 |          "function bar(d){return plex(d)}" +
378 |          "var d=foo(1,2)",
379 | 
380 |          "var d;{JSCompiler_inline_label_plex_1:{" +
381 |          "if(1+2){" +
382 |          "d=0;break JSCompiler_inline_label_plex_1}" +
383 |          "else{" +
384 |          "d=1;break JSCompiler_inline_label_plex_1}d=void 0}}");
385 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions23()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions23()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
387 |   public void testInlineFunctions23() {
388 |     // Test both orderings again
389 |     test("function complex(a){if(a) return 0;else return 1;}" +
390 |          "function bar(d){return complex(d)}" +
391 |          "function foo(a, b){return bar(a+b)}" +
392 |          "var d=foo(1,2)",
393 | 
394 |          "var d;{JSCompiler_inline_label_complex_1:{" +
395 |          "if(1+2){" +
396 |          "d=0;break JSCompiler_inline_label_complex_1" +
397 |          "}else{" +
398 |          "d=1;break JSCompiler_inline_label_complex_1" +
399 |          "}d=void 0}}");
400 |   }
```

## com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions9()
Resolved declaration: com.google.javascript.jscomp.InlineFunctionsTest.testInlineFunctions9()
Source: test/com/google/javascript/jscomp/InlineFunctionsTest.java

```java
174 |   public void testInlineFunctions9() {
175 |     // don't inline if the input parameter is modified.
176 |     test("function INC(x){return x++}" +
177 |          "var y=INC(i)",
178 |          "var y;{var x$$inline_0=i;" +
179 |          "y=x$$inline_0++}");
180 |   }
```

## com.google.javascript.jscomp.MakeDeclaredNamesUniqueTest.testMakeLocalNamesUniqueWithContext5()
Resolved declaration: com.google.javascript.jscomp.MakeDeclaredNamesUniqueTest.testMakeLocalNamesUniqueWithContext5()
Source: test/com/google/javascript/jscomp/MakeDeclaredNamesUniqueTest.java

```java
208 |   public void testMakeLocalNamesUniqueWithContext5() {
209 |     // Set the test type
210 |     this.useDefaultRenamer = true;
211 | 
212 |     testWithInversion(
213 |         "function f(){var f; f = 1}",
214 |         "function f(){var f$$1; f$$1 = 1}");
215 |     testWithInversion(
216 |         "function f(f){f = 1}",
217 |         "function f(f$$1){f$$1 = 1}");
218 |     testWithInversion(
219 |         "function f(f){var f; f = 1}",
220 |         "function f(f$$1){var f$$1; f$$1 = 1}");
221 | 
222 |     test(
223 |         "var fn = function f(){var f; f = 1}",
224 |         "var fn = function f(){var f$$1; f$$1 = 1}");
225 |     test(
226 |         "var fn = function f(f){f = 1}",
227 |         "var fn = function f(f$$1){f$$1 = 1}");
228 |     test(
229 |         "var fn = function f(f){var f; f = 1}",
230 |         "var fn = function f(f$$1){var f$$1; f$$1 = 1}");
231 |   }
```
