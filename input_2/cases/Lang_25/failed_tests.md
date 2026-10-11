# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.text.translate.EntityArraysTest.testISO8859_1_ESCAPE()
Resolved declaration: org.apache.commons.lang3.text.translate.EntityArraysTest.testISO8859_1_ESCAPE()
Source: src/test/java/org/apache/commons/lang3/text/translate/EntityArraysTest.java

```java
47 |     public void testISO8859_1_ESCAPE(){
48 |         Set<String> col0 = new HashSet<String>();
49 |         Set<String> col1 = new HashSet<String>();
50 |         String [][] sa = EntityArrays.ISO8859_1_ESCAPE();
51 |         boolean success = true;
52 |         for(int i =0; i <sa.length; i++){
53 |             boolean add0 = col0.add(sa[i][0]);
54 |             boolean add1 = col1.add(sa[i][1]);
55 |             if (!add0) { 
56 |                 success = false;
57 |                 System.out.println("Already added entry 0: "+i+" "+sa[i][0]+" "+sa[i][1]);
58 |             }
59 |             if (!add1) {
60 |                 success = false;
61 |                 System.out.println("Already added entry 1: "+i+" "+sa[i][0]+" "+sa[i][1]);
62 |             }
63 |         }
64 |         assertTrue("One or more errors detected",success);
65 |     }
```
