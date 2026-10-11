# Failing test code

Full extracted test bodies; no assertion trimming.

## org.joda.time.TestDateTimeZone.testForID_String_old()
Resolved declaration: org.joda.time.TestDateTimeZone.testForID_String_old()
Source: src/test/java/org/joda/time/TestDateTimeZone.java

```java
243 |     public void testForID_String_old() {
244 |         Map<String, String> map = new LinkedHashMap<String, String>();
245 |         map.put("GMT", "UTC");
246 |         map.put("WET", "WET");
247 |         map.put("CET", "CET");
248 |         map.put("MET", "CET");
249 |         map.put("ECT", "CET");
250 |         map.put("EET", "EET");
251 |         map.put("MIT", "Pacific/Apia");
252 |         map.put("HST", "Pacific/Honolulu");
253 |         map.put("AST", "America/Anchorage");
254 |         map.put("PST", "America/Los_Angeles");
255 |         map.put("MST", "America/Denver");
256 |         map.put("PNT", "America/Phoenix");
257 |         map.put("CST", "America/Chicago");
258 |         map.put("EST", "America/New_York");
259 |         map.put("IET", "America/Indiana/Indianapolis");
260 |         map.put("PRT", "America/Puerto_Rico");
261 |         map.put("CNT", "America/St_Johns");
262 |         map.put("AGT", "America/Argentina/Buenos_Aires");
263 |         map.put("BET", "America/Sao_Paulo");
264 |         map.put("ART", "Africa/Cairo");
265 |         map.put("CAT", "Africa/Harare");
266 |         map.put("EAT", "Africa/Addis_Ababa");
267 |         map.put("NET", "Asia/Yerevan");
268 |         map.put("PLT", "Asia/Karachi");
269 |         map.put("IST", "Asia/Kolkata");
270 |         map.put("BST", "Asia/Dhaka");
271 |         map.put("VST", "Asia/Ho_Chi_Minh");
272 |         map.put("CTT", "Asia/Shanghai");
273 |         map.put("JST", "Asia/Tokyo");
274 |         map.put("ACT", "Australia/Darwin");
275 |         map.put("AET", "Australia/Sydney");
276 |         map.put("SST", "Pacific/Guadalcanal");
277 |         map.put("NST", "Pacific/Auckland");
278 |         for (String key : map.keySet()) {
279 |             String value = map.get(key);
280 |             TimeZone juZone = TimeZone.getTimeZone(key);
281 |             DateTimeZone zone = DateTimeZone.forTimeZone(juZone);
282 |             assertEquals(value, zone.getID());
283 | //            System.out.println(juZone);
284 | //            System.out.println(juZone.getDisplayName());
285 | //            System.out.println(zone);
286 | //            System.out.println("------");
287 |         }
288 |     }
```
