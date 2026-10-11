# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.RandomStringUtilsTest.testLANG807()
Resolved declaration: org.apache.commons.lang3.RandomStringUtilsTest.testLANG807()
Source: src/test/java/org/apache/commons/lang3/RandomStringUtilsTest.java

```java
133 |     public void testLANG807() {
134 |         try {
135 |             RandomStringUtils.random(3,5,5,false,false);
136 |             fail("Expected IllegalArgumentException");
137 |         } catch (IllegalArgumentException ex) { // distinguish from Random#nextInt message
138 |             final String msg = ex.getMessage();
139 |             assertTrue("Message (" + msg + ") must contain 'start'", msg.contains("start"));
140 |             assertTrue("Message (" + msg + ") must contain 'end'", msg.contains("end"));
141 |         }
142 |     }
```
