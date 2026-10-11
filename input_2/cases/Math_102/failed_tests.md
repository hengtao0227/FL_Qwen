# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.stat.inference.ChiSquareFactoryTest.testChiSquareLargeTestStatistic()
Resolved declaration: org.apache.commons.math.stat.inference.ChiSquareTestTest.testChiSquareLargeTestStatistic()
Source: src/test/org/apache/commons/math/stat/inference/ChiSquareTestTest.java

```java
170 |     public void testChiSquareLargeTestStatistic() throws Exception {
171 |         double[] exp = new double[] {
172 |             3389119.5, 649136.6, 285745.4, 25357364.76, 11291189.78, 543628.0, 
173 |             232921.0, 437665.75
174 |         };
175 | 
176 |         long[] obs = new long[] {
177 |             2372383, 584222, 257170, 17750155, 7903832, 489265, 209628, 393899
178 |         };
179 |         org.apache.commons.math.stat.inference.ChiSquareTestImpl csti =
180 |             new org.apache.commons.math.stat.inference.ChiSquareTestImpl(); 
181 |         double cst = csti.chiSquareTest(exp, obs); 
182 |         assertEquals("chi-square p-value", 0.0, cst, 1E-3);
183 |         assertEquals( "chi-square test statistic", 
184 |                 114875.90421929007, testStatistic.chiSquare(exp, obs), 1E-9);
185 |     }
```

## org.apache.commons.math.stat.inference.ChiSquareFactoryTest.testChiSquare()
Resolved declaration: org.apache.commons.math.stat.inference.ChiSquareTestTest.testChiSquare()
Source: src/test/org/apache/commons/math/stat/inference/ChiSquareTestTest.java

```java
46 |     public void testChiSquare() throws Exception {
47 |  
48 |         // Target values computed using R version 1.8.1 
49 |         // Some assembly required ;-)  
50 |         //      Use sum((obs - exp)^2/exp) for the chi-square statistic and
51 |         //      1 - pchisq(sum((obs - exp)^2/exp), length(obs) - 1) for the p-value
52 |         
53 |         long[] observed = {10, 9, 11};
54 |         double[] expected = {10, 10, 10};
55 |         assertEquals("chi-square statistic", 0.2,  testStatistic.chiSquare(expected, observed), 10E-12);
56 |         assertEquals("chi-square p-value", 0.904837418036, testStatistic.chiSquareTest(expected, observed), 1E-10);
57 |         
58 |         long[] observed1 = { 500, 623, 72, 70, 31 };
59 |         double[] expected1 = { 485, 541, 82, 61, 37 };
60 |         assertEquals( "chi-square test statistic", 9.023307936427388, testStatistic.chiSquare(expected1, observed1), 1E-10);
61 |         assertEquals("chi-square p-value", 0.06051952647453607, testStatistic.chiSquareTest(expected1, observed1), 1E-9);
62 |         assertTrue("chi-square test reject", testStatistic.chiSquareTest(expected1, observed1, 0.08));
63 |         assertTrue("chi-square test accept", !testStatistic.chiSquareTest(expected1, observed1, 0.05));
64 | 
65 |         try {
66 |             testStatistic.chiSquareTest(expected1, observed1, 95);
67 |             fail("alpha out of range, IllegalArgumentException expected");
68 |         } catch (IllegalArgumentException ex) {
69 |             // expected
70 |         }  
71 |         
72 |         long[] tooShortObs = { 0 };
73 |         double[] tooShortEx = { 1 };
74 |         try {
75 |             testStatistic.chiSquare(tooShortEx, tooShortObs);
76 |             fail("arguments too short, IllegalArgumentException expected");
77 |         } catch (IllegalArgumentException ex) {
78 |             // expected
79 |         }
80 | 
81 |         // unmatched arrays
82 |         long[] unMatchedObs = { 0, 1, 2, 3 };
83 |         double[] unMatchedEx = { 1, 1, 2 };
84 |         try {
85 |             testStatistic.chiSquare(unMatchedEx, unMatchedObs);
86 |             fail("arrays have different lengths, IllegalArgumentException expected");
87 |         } catch (IllegalArgumentException ex) {
88 |             // expected
89 |         }
90 |         
91 |         // 0 expected count
92 |         expected[0] = 0;
93 |         try {
94 |             testStatistic.chiSquareTest(expected, observed, .01);
95 |             fail("bad expected count, IllegalArgumentException expected");
96 |         } catch (IllegalArgumentException ex) {
97 |             // expected
98 |         } 
99 |         
100 |         // negative observed count
101 |         expected[0] = 1;
102 |         observed[0] = -1;
103 |         try {
104 |             testStatistic.chiSquareTest(expected, observed, .01);
105 |             fail("bad expected count, IllegalArgumentException expected");
106 |         } catch (IllegalArgumentException ex) {
107 |             // expected
108 |         } 
109 |         
110 |     }
```

## org.apache.commons.math.stat.inference.ChiSquareTestTest.testChiSquareLargeTestStatistic()
Resolved declaration: org.apache.commons.math.stat.inference.ChiSquareTestTest.testChiSquareLargeTestStatistic()
Source: src/test/org/apache/commons/math/stat/inference/ChiSquareTestTest.java

```java
170 |     public void testChiSquareLargeTestStatistic() throws Exception {
171 |         double[] exp = new double[] {
172 |             3389119.5, 649136.6, 285745.4, 25357364.76, 11291189.78, 543628.0, 
173 |             232921.0, 437665.75
174 |         };
175 | 
176 |         long[] obs = new long[] {
177 |             2372383, 584222, 257170, 17750155, 7903832, 489265, 209628, 393899
178 |         };
179 |         org.apache.commons.math.stat.inference.ChiSquareTestImpl csti =
180 |             new org.apache.commons.math.stat.inference.ChiSquareTestImpl(); 
181 |         double cst = csti.chiSquareTest(exp, obs); 
182 |         assertEquals("chi-square p-value", 0.0, cst, 1E-3);
183 |         assertEquals( "chi-square test statistic", 
184 |                 114875.90421929007, testStatistic.chiSquare(exp, obs), 1E-9);
185 |     }
```

## org.apache.commons.math.stat.inference.ChiSquareTestTest.testChiSquare()
Resolved declaration: org.apache.commons.math.stat.inference.ChiSquareTestTest.testChiSquare()
Source: src/test/org/apache/commons/math/stat/inference/ChiSquareTestTest.java

```java
46 |     public void testChiSquare() throws Exception {
47 |  
48 |         // Target values computed using R version 1.8.1 
49 |         // Some assembly required ;-)  
50 |         //      Use sum((obs - exp)^2/exp) for the chi-square statistic and
51 |         //      1 - pchisq(sum((obs - exp)^2/exp), length(obs) - 1) for the p-value
52 |         
53 |         long[] observed = {10, 9, 11};
54 |         double[] expected = {10, 10, 10};
55 |         assertEquals("chi-square statistic", 0.2,  testStatistic.chiSquare(expected, observed), 10E-12);
56 |         assertEquals("chi-square p-value", 0.904837418036, testStatistic.chiSquareTest(expected, observed), 1E-10);
57 |         
58 |         long[] observed1 = { 500, 623, 72, 70, 31 };
59 |         double[] expected1 = { 485, 541, 82, 61, 37 };
60 |         assertEquals( "chi-square test statistic", 9.023307936427388, testStatistic.chiSquare(expected1, observed1), 1E-10);
61 |         assertEquals("chi-square p-value", 0.06051952647453607, testStatistic.chiSquareTest(expected1, observed1), 1E-9);
62 |         assertTrue("chi-square test reject", testStatistic.chiSquareTest(expected1, observed1, 0.08));
63 |         assertTrue("chi-square test accept", !testStatistic.chiSquareTest(expected1, observed1, 0.05));
64 | 
65 |         try {
66 |             testStatistic.chiSquareTest(expected1, observed1, 95);
67 |             fail("alpha out of range, IllegalArgumentException expected");
68 |         } catch (IllegalArgumentException ex) {
69 |             // expected
70 |         }  
71 |         
72 |         long[] tooShortObs = { 0 };
73 |         double[] tooShortEx = { 1 };
74 |         try {
75 |             testStatistic.chiSquare(tooShortEx, tooShortObs);
76 |             fail("arguments too short, IllegalArgumentException expected");
77 |         } catch (IllegalArgumentException ex) {
78 |             // expected
79 |         }
80 | 
81 |         // unmatched arrays
82 |         long[] unMatchedObs = { 0, 1, 2, 3 };
83 |         double[] unMatchedEx = { 1, 1, 2 };
84 |         try {
85 |             testStatistic.chiSquare(unMatchedEx, unMatchedObs);
86 |             fail("arrays have different lengths, IllegalArgumentException expected");
87 |         } catch (IllegalArgumentException ex) {
88 |             // expected
89 |         }
90 |         
91 |         // 0 expected count
92 |         expected[0] = 0;
93 |         try {
94 |             testStatistic.chiSquareTest(expected, observed, .01);
95 |             fail("bad expected count, IllegalArgumentException expected");
96 |         } catch (IllegalArgumentException ex) {
97 |             // expected
98 |         } 
99 |         
100 |         // negative observed count
101 |         expected[0] = 1;
102 |         observed[0] = -1;
103 |         try {
104 |             testStatistic.chiSquareTest(expected, observed, .01);
105 |             fail("bad expected count, IllegalArgumentException expected");
106 |         } catch (IllegalArgumentException ex) {
107 |             // expected
108 |         } 
109 |         
110 |     }
```

## org.apache.commons.math.stat.inference.TestUtilsTest.testChiSquareLargeTestStatistic()
Resolved declaration: org.apache.commons.math.stat.inference.TestUtilsTest.testChiSquareLargeTestStatistic()
Source: src/test/org/apache/commons/math/stat/inference/TestUtilsTest.java

```java
168 |     public void testChiSquareLargeTestStatistic() throws Exception {
169 |         double[] exp = new double[] {
170 |                 3389119.5, 649136.6, 285745.4, 25357364.76, 11291189.78, 543628.0, 
171 |                 232921.0, 437665.75
172 |         };
173 | 
174 |         long[] obs = new long[] {
175 |                 2372383, 584222, 257170, 17750155, 7903832, 489265, 209628, 393899
176 |         };
177 |         org.apache.commons.math.stat.inference.ChiSquareTestImpl csti =
178 |             new org.apache.commons.math.stat.inference.ChiSquareTestImpl(); 
179 |         double cst = csti.chiSquareTest(exp, obs); 
180 |         assertEquals("chi-square p-value", 0.0, cst, 1E-3);
181 |         assertEquals( "chi-square test statistic", 
182 |                 114875.90421929007, TestUtils.chiSquare(exp, obs), 1E-9);
183 |     }
```

## org.apache.commons.math.stat.inference.TestUtilsTest.testChiSquare()
Resolved declaration: org.apache.commons.math.stat.inference.TestUtilsTest.testChiSquare()
Source: src/test/org/apache/commons/math/stat/inference/TestUtilsTest.java

```java
44 |     public void testChiSquare() throws Exception {
45 |         
46 |         // Target values computed using R version 1.8.1 
47 |         // Some assembly required ;-)  
48 |         //      Use sum((obs - exp)^2/exp) for the chi-square statistic and
49 |         //      1 - pchisq(sum((obs - exp)^2/exp), length(obs) - 1) for the p-value
50 |         
51 |         long[] observed = {10, 9, 11};
52 |         double[] expected = {10, 10, 10};
53 |         assertEquals("chi-square statistic", 0.2,  TestUtils.chiSquare(expected, observed), 10E-12);
54 |         assertEquals("chi-square p-value", 0.904837418036, TestUtils.chiSquareTest(expected, observed), 1E-10);
55 |         
56 |         long[] observed1 = { 500, 623, 72, 70, 31 };
57 |         double[] expected1 = { 485, 541, 82, 61, 37 };
58 |         assertEquals( "chi-square test statistic", 9.023307936427388, TestUtils.chiSquare(expected1, observed1), 1E-10);
59 |         assertEquals("chi-square p-value", 0.06051952647453607, TestUtils.chiSquareTest(expected1, observed1), 1E-9);
60 |         assertTrue("chi-square test reject", TestUtils.chiSquareTest(expected1, observed1, 0.07));
61 |         assertTrue("chi-square test accept", !TestUtils.chiSquareTest(expected1, observed1, 0.05));
62 | 
63 |         try {
64 |             TestUtils.chiSquareTest(expected1, observed1, 95);
65 |             fail("alpha out of range, IllegalArgumentException expected");
66 |         } catch (IllegalArgumentException ex) {
67 |             // expected
68 |         }  
69 |         
70 |         long[] tooShortObs = { 0 };
71 |         double[] tooShortEx = { 1 };
72 |         try {
73 |             TestUtils.chiSquare(tooShortEx, tooShortObs);
74 |             fail("arguments too short, IllegalArgumentException expected");
75 |         } catch (IllegalArgumentException ex) {
76 |             // expected
77 |         }
78 | 
79 |         // unmatched arrays
80 |         long[] unMatchedObs = { 0, 1, 2, 3 };
81 |         double[] unMatchedEx = { 1, 1, 2 };
82 |         try {
83 |             TestUtils.chiSquare(unMatchedEx, unMatchedObs);
84 |             fail("arrays have different lengths, IllegalArgumentException expected");
85 |         } catch (IllegalArgumentException ex) {
86 |             // expected
87 |         }
88 |         
89 |         // 0 expected count
90 |         expected[0] = 0;
91 |         try {
92 |             TestUtils.chiSquareTest(expected, observed, .01);
93 |             fail("bad expected count, IllegalArgumentException expected");
94 |         } catch (IllegalArgumentException ex) {
95 |             // expected
96 |         } 
97 |         
98 |         // negative observed count
99 |         expected[0] = 1;
100 |         observed[0] = -1;
101 |         try {
102 |             TestUtils.chiSquareTest(expected, observed, .01);
103 |             fail("bad expected count, IllegalArgumentException expected");
104 |         } catch (IllegalArgumentException ex) {
105 |             // expected
106 |         } 
107 |         
108 |     }
```
