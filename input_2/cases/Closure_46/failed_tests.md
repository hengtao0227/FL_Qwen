# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.rhino.jstype.JSTypeTest.testRecordTypeLeastSuperType2()
Resolved declaration: com.google.javascript.rhino.jstype.JSTypeTest.testRecordTypeLeastSuperType2()
Source: test/com/google/javascript/rhino/jstype/JSTypeTest.java

```java
2714 |   public void testRecordTypeLeastSuperType2() {
2715 |     RecordTypeBuilder builder = new RecordTypeBuilder(registry);
2716 |     builder.addProperty("e", NUMBER_TYPE, null);
2717 |     builder.addProperty("b", STRING_TYPE, null);
2718 |     builder.addProperty("c", STRING_TYPE, null);
2719 |     JSType otherRecordType = builder.build();
2720 | 
2721 |     assertTypeEquals(
2722 |         registry.createUnionType(recordType, otherRecordType),
2723 |         recordType.getLeastSupertype(otherRecordType));
2724 |   }
```

## com.google.javascript.rhino.jstype.JSTypeTest.testRecordTypeLeastSuperType3()
Resolved declaration: com.google.javascript.rhino.jstype.JSTypeTest.testRecordTypeLeastSuperType3()
Source: test/com/google/javascript/rhino/jstype/JSTypeTest.java

```java
2726 |   public void testRecordTypeLeastSuperType3() {
2727 |     RecordTypeBuilder builder = new RecordTypeBuilder(registry);
2728 |     builder.addProperty("d", NUMBER_TYPE, null);
2729 |     builder.addProperty("e", STRING_TYPE, null);
2730 |     builder.addProperty("f", STRING_TYPE, null);
2731 |     JSType otherRecordType = builder.build();
2732 | 
2733 |     assertTypeEquals(
2734 |         registry.createUnionType(recordType, otherRecordType),
2735 |         recordType.getLeastSupertype(otherRecordType));
2736 |   }
```

## com.google.javascript.rhino.jstype.RecordTypeTest.testSupAndInf()
Resolved declaration: com.google.javascript.rhino.jstype.RecordTypeTest.testSupAndInf()
Source: test/com/google/javascript/rhino/jstype/RecordTypeTest.java

```java
76 |   public void testSupAndInf() {
77 |     JSType recordA = new RecordTypeBuilder(registry)
78 |         .addProperty("a", NUMBER_TYPE, null)
79 |         .addProperty("b", NUMBER_TYPE, null)
80 |         .build();
81 |     JSType recordC = new RecordTypeBuilder(registry)
82 |         .addProperty("b", NUMBER_TYPE, null)
83 |         .addProperty("c", NUMBER_TYPE, null)
84 |         .build();
85 |     ProxyObjectType proxyRecordA = new ProxyObjectType(registry, recordA);
86 |     ProxyObjectType proxyRecordC = new ProxyObjectType(registry, recordC);
87 | 
88 |     JSType aInfC = new RecordTypeBuilder(registry)
89 |         .addProperty("a", NUMBER_TYPE, null)
90 |         .addProperty("b", NUMBER_TYPE, null)
91 |         .addProperty("c", NUMBER_TYPE, null)
92 |         .build();
93 | 
94 |     JSType aSupC = registry.createUnionType(recordA, recordC);
95 | 
96 |     Asserts.assertTypeEquals(
97 |         aInfC, recordA.getGreatestSubtype(recordC));
98 |     Asserts.assertTypeEquals(
99 |         aSupC, recordA.getLeastSupertype(recordC));
100 | 
101 |     Asserts.assertTypeEquals(
102 |         aInfC, proxyRecordA.getGreatestSubtype(proxyRecordC));
103 |     Asserts.assertTypeEquals(
104 |         aSupC, proxyRecordA.getLeastSupertype(proxyRecordC));
105 |   }
```
