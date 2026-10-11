# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.lang3.text.ExtendedMessageFormatTest.testEqualsHashcode()
Resolved declaration: org.apache.commons.lang3.text.ExtendedMessageFormatTest.testEqualsHashcode()
Source: src/test/java/org/apache/commons/lang3/text/ExtendedMessageFormatTest.java

```java
270 |     public void testEqualsHashcode() {
271 |         Map<String, ? extends FormatFactory> registry = Collections.singletonMap("testfmt", new LowerCaseFormatFactory());
272 |         Map<String, ? extends FormatFactory> otherRegitry = Collections.singletonMap("testfmt", new UpperCaseFormatFactory());
273 | 
274 |         String pattern = "Pattern: {0,testfmt}";
275 |         ExtendedMessageFormat emf = new ExtendedMessageFormat(pattern, Locale.US, registry);
276 | 
277 |         ExtendedMessageFormat other = null;
278 | 
279 |         // Same object
280 |         assertTrue("same, equals()",   emf.equals(emf));
281 |         assertTrue("same, hashcode()", emf.hashCode() == emf.hashCode());
282 | 
283 |         // Equal Object
284 |         other = new ExtendedMessageFormat(pattern, Locale.US, registry);
285 |         assertTrue("equal, equals()",   emf.equals(other));
286 |         assertTrue("equal, hashcode()", emf.hashCode() == other.hashCode());
287 | 
288 |         // Different Class
289 |         other = new OtherExtendedMessageFormat(pattern, Locale.US, registry);
290 |         assertFalse("class, equals()",  emf.equals(other));
291 |         assertTrue("class, hashcode()", emf.hashCode() == other.hashCode()); // same hashcode
292 |         
293 |         // Different pattern
294 |         other = new ExtendedMessageFormat("X" + pattern, Locale.US, registry);
295 |         assertFalse("pattern, equals()",   emf.equals(other));
296 |         assertFalse("pattern, hashcode()", emf.hashCode() == other.hashCode());
297 | 
298 |         // Different registry
299 |         other = new ExtendedMessageFormat(pattern, Locale.US, otherRegitry);
300 |         assertFalse("registry, equals()",   emf.equals(other));
301 |         assertFalse("registry, hashcode()", emf.hashCode() == other.hashCode());
302 | 
303 |         // Different Locale
304 |         other = new ExtendedMessageFormat(pattern, Locale.FRANCE, registry);
305 |         assertFalse("locale, equals()",  emf.equals(other));
306 |         assertTrue("locale, hashcode()", emf.hashCode() == other.hashCode()); // same hashcode
307 |     }
```
