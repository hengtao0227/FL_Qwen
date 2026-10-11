# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.ConvertToDottedPropertiesTest.testQuotedProps()
Resolved declaration: com.google.javascript.jscomp.ConvertToDottedPropertiesTest.testQuotedProps()
Source: test/com/google/javascript/jscomp/ConvertToDottedPropertiesTest.java

```java
68 |   public void testQuotedProps() {
69 |     testSame("({'':0})");
70 |     testSame("({'1.0':0})");
71 |     testSame("({'\u1d17A':0})");
72 |     testSame("({'a\u0004b':0})");
73 |   }
```

## com.google.javascript.jscomp.ConvertToDottedPropertiesTest.testDoNotConvert()
Resolved declaration: com.google.javascript.jscomp.ConvertToDottedPropertiesTest.testDoNotConvert()
Source: test/com/google/javascript/jscomp/ConvertToDottedPropertiesTest.java

```java
41 |   public void testDoNotConvert() {
42 |     testSame("a[0]");
43 |     testSame("a['']");
44 |     testSame("a[' ']");
45 |     testSame("a[',']");
46 |     testSame("a[';']");
47 |     testSame("a[':']");
48 |     testSame("a['.']");
49 |     testSame("a['0']");
50 |     testSame("a['p ']");
51 |     testSame("a['p' + '']");
52 |     testSame("a[p]");
53 |     testSame("a[P]");
54 |     testSame("a[$]");
55 |     testSame("a[p()]");
56 |     testSame("a['default']");
57 |     // Ignorable control characters are ok in Java identifiers, but not in JS.
58 |     testSame("a['A\u0004']");
59 |     // upper case lower half of o from phonetic extensions set.
60 |     // valid in Safari, not in Firefox, IE.
61 |     test("a['\u1d17A']", "a['\u1d17A']");
62 |     // Latin capital N with tilde - nice if we handled it, but for now let's
63 |     // only allow simple Latin (aka ASCII) to be converted.
64 |     test("a['\u00d1StuffAfter']", "a['\u00d1StuffAfter']");
65 |   }
```
