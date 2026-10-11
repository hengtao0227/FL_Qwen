# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeReplaceKnownMethodsTest.testStringJoinAdd()
Resolved declaration: com.google.javascript.jscomp.PeepholeReplaceKnownMethodsTest.testStringJoinAdd()
Source: test/com/google/javascript/jscomp/PeepholeReplaceKnownMethodsTest.java

```java
82 |   public void testStringJoinAdd() {
83 |     fold("x = ['a', 'b', 'c'].join('')", "x = \"abc\"");
84 |     fold("x = [].join(',')", "x = \"\"");
85 |     fold("x = ['a'].join(',')", "x = \"a\"");
86 |     fold("x = ['a', 'b', 'c'].join(',')", "x = \"a,b,c\"");
87 |     fold("x = ['a', foo, 'b', 'c'].join(',')",
88 |         "x = [\"a\",foo,\"b,c\"].join()");
89 |     fold("x = [foo, 'a', 'b', 'c'].join(',')",
90 |         "x = [foo,\"a,b,c\"].join()");
91 |     fold("x = ['a', 'b', 'c', foo].join(',')",
92 |         "x = [\"a,b,c\",foo].join()");
93 | 
94 |     // Works with numbers
95 |     fold("x = ['a=', 5].join('')", "x = \"a=5\"");
96 |     fold("x = ['a', '5'].join(7)", "x = \"a75\"");
97 | 
98 |     // Works on boolean
99 |     fold("x = ['a=', false].join('')", "x = \"a=false\"");
100 |     fold("x = ['a', '5'].join(true)", "x = \"atrue5\"");
101 |     fold("x = ['a', '5'].join(false)", "x = \"afalse5\"");
102 | 
103 |     // Only optimize if it's a size win.
104 |     fold("x = ['a', '5', 'c'].join('a very very very long chain')",
105 |          "x = [\"a\",\"5\",\"c\"].join(\"a very very very long chain\")");
106 | 
107 |     // TODO(user): Its possible to fold this better.
108 |     foldSame("x = ['', foo].join('-')");
109 |     foldSame("x = ['', foo, ''].join()");
110 | 
111 |     fold("x = ['', '', foo, ''].join(',')",
112 |          "x = [',', foo, ''].join()");
113 |     fold("x = ['', '', foo, '', ''].join(',')",
114 |          "x = [',', foo, ','].join()");
115 | 
116 |     fold("x = ['', '', foo, '', '', bar].join(',')",
117 |          "x = [',', foo, ',', bar].join()");
118 | 
119 |     fold("x = [1,2,3].join('abcdef')",
120 |          "x = '1abcdef2abcdef3'");
121 | 
122 |     fold("x = [1,2].join()", "x = '1,2'");
123 |     fold("x = [null,undefined,''].join(',')", "x = ',,'");
124 |     fold("x = [null,undefined,0].join(',')", "x = ',,0'");
125 |     // This can be folded but we don't currently.
126 |     foldSame("x = [[1,2],[3,4]].join()"); // would like: "x = '1,2,3,4'"
127 |   }
```

## com.google.javascript.jscomp.PeepholeReplaceKnownMethodsTest.testNoStringJoin()
Resolved declaration: com.google.javascript.jscomp.PeepholeReplaceKnownMethodsTest.testNoStringJoin()
Source: test/com/google/javascript/jscomp/PeepholeReplaceKnownMethodsTest.java

```java
77 |   public void testNoStringJoin() {
78 |     foldSame("x = [].join(',',2)");
79 |     foldSame("x = [].join(f)");
80 |   }
```
