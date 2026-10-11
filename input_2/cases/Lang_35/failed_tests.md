# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.ArrayUtilsAddTest.testLANG571()
Resolved declaration: org.apache.commons.lang3.ArrayUtilsAddTest.testLANG571()
Source: src/test/java/org/apache/commons/lang3/ArrayUtilsAddTest.java

```java
225 |     public void testLANG571(){
226 |         String[] stringArray=null;
227 |         String aString=null;
228 |         try {
229 |             @SuppressWarnings("unused")
230 |             String[] sa = ArrayUtils.add(stringArray, aString);
231 |             fail("Should have caused IllegalArgumentException");
232 |         } catch (IllegalArgumentException iae){
233 |             //expected
234 |         }
235 |         try {
236 |             @SuppressWarnings("unused")
237 |             String[] sa = ArrayUtils.add(stringArray, 0, aString);
238 |             fail("Should have caused IllegalArgumentException");
239 |         } catch (IllegalArgumentException iae){
240 |             //expected
241 |         }
242 |     }
```
