# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.category.junit.DefaultCategoryDatasetTests.testBug1835955()
Resolved declaration: org.jfree.data.category.junit.DefaultCategoryDatasetTests.testBug1835955()
Source: tests/org/jfree/data/category/junit/DefaultCategoryDatasetTests.java

```java
345 |     public void testBug1835955() {
346 |     	DefaultCategoryDataset d = new DefaultCategoryDataset();
347 |     	d.addValue(1.0, "R1", "C1");
348 |     	d.addValue(2.0, "R2", "C2");
349 |     	d.removeColumn("C2");
350 |     	d.addValue(3.0, "R2", "C2");
351 |     	assertEquals(3.0, d.getValue("R2", "C2").doubleValue(), EPSILON);
352 |     }
```

## org.jfree.data.junit.DefaultKeyedValues2DTests.testRemoveColumnByKey()
Resolved declaration: org.jfree.data.junit.DefaultKeyedValues2DTests.testRemoveColumnByKey()
Source: tests/org/jfree/data/junit/DefaultKeyedValues2DTests.java

```java
349 |     public void testRemoveColumnByKey() {
350 |     	DefaultKeyedValues2D d = new DefaultKeyedValues2D();
351 |     	d.addValue(new Double(1.0), "R1", "C1");
352 |     	d.addValue(new Double(2.0), "R2", "C2");
353 |     	d.removeColumn("C2");
354 |     	d.addValue(new Double(3.0), "R2", "C2");
355 |     	assertEquals(3.0, d.getValue("R2", "C2").doubleValue(), EPSILON);
356 |     	
357 |     	// check for unknown column
358 |     	boolean pass = false;
359 |     	try {
360 |     		d.removeColumn("XXX");
361 |     	}
362 |     	catch (UnknownKeyException e) {
363 |     		pass = true;
364 |     	}
365 |     	assertTrue(pass);
366 |     }
```

## org.jfree.data.junit.DefaultKeyedValuesTests.testRemoveValue()
Resolved declaration: org.jfree.data.junit.DefaultKeyedValuesTests.testRemoveValue()
Source: tests/org/jfree/data/junit/DefaultKeyedValuesTests.java

```java
355 |     public void testRemoveValue() {
356 |         DefaultKeyedValues data = new DefaultKeyedValues();
357 |         data.addValue("A", new Double(1.0));
358 |         data.addValue("B", null);
359 |         data.addValue("C", new Double(3.0));
360 |         data.addValue("D", new Double(2.0));
361 |         assertEquals(1, data.getIndex("B"));
362 |         data.removeValue("B");
363 |         assertEquals(-1, data.getIndex("B"));
364 |         
365 |         boolean pass = false;
366 |         try {
367 |             data.removeValue("XXX");
368 |         }
369 |         catch (UnknownKeyException e) {
370 |             pass = true;   
371 |         }
372 |         assertTrue(pass);
373 |     }
```

## org.jfree.data.junit.DefaultKeyedValuesTests.testGetIndex2()
Resolved declaration: org.jfree.data.junit.DefaultKeyedValuesTests.testGetIndex2()
Source: tests/org/jfree/data/junit/DefaultKeyedValuesTests.java

```java
238 |     public void testGetIndex2() {
239 |     	DefaultKeyedValues v = new DefaultKeyedValues();
240 |     	assertEquals(-1, v.getIndex("K1"));
241 |     	v.addValue("K1", 1.0);
242 |     	assertEquals(0, v.getIndex("K1"));
243 |     	v.removeValue("K1");
244 |     	assertEquals(-1, v.getIndex("K1"));
245 |     }
```
