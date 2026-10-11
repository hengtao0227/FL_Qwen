# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.rhino.jstype.RecordTypeTest.testRecursiveRecord()
Resolved declaration: com.google.javascript.rhino.jstype.RecordTypeTest.testRecursiveRecord()
Source: test/com/google/javascript/rhino/jstype/RecordTypeTest.java

```java
46 |   public void testRecursiveRecord() {
47 |     ProxyObjectType loop = new ProxyObjectType(registry, NUMBER_TYPE);
48 |     JSType record = new RecordTypeBuilder(registry)
49 |         .addProperty("loop", loop, null)
50 |         .addProperty("number", NUMBER_TYPE, null)
51 |         .addProperty("string", STRING_TYPE, null)
52 |         .build();
53 |     assertEquals("{loop: number, number: number, string: string}",
54 |         record.toString());
55 | 
56 |     loop.setReferencedType(record);
57 |     assertEquals("{loop: {...}, number: number, string: string}",
58 |         record.toString());
59 |     assertEquals("{loop: ?, number: number, string: string}",
60 |         record.toAnnotationString());
61 | 
62 |     Asserts.assertEquivalenceOperations(record, loop);
63 |   }
```

## com.google.javascript.rhino.jstype.RecordTypeTest.testLongToString()
Resolved declaration: com.google.javascript.rhino.jstype.RecordTypeTest.testLongToString()
Source: test/com/google/javascript/rhino/jstype/RecordTypeTest.java

```java
65 |   public void testLongToString() {
66 |     JSType record = new RecordTypeBuilder(registry)
67 |         .addProperty("a1", NUMBER_TYPE, null)
68 |         .addProperty("a2", NUMBER_TYPE, null)
69 |         .addProperty("a3", NUMBER_TYPE, null)
70 |         .addProperty("a4", NUMBER_TYPE, null)
71 |         .addProperty("a5", NUMBER_TYPE, null)
72 |         .addProperty("a6", NUMBER_TYPE, null)
73 |         .build();
74 |     assertEquals("{a1: number, a2: number, a3: number, a4: number, ...}",
75 |         record.toString());
76 |     assertEquals(
77 |         "{a1: number, a2: number, a3: number, a4: number," +
78 |         " a5: number, a6: number}",
79 |         record.toAnnotationString());
80 |   }
```
