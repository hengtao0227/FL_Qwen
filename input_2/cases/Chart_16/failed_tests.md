# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetCategoryIndex()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetCategoryIndex()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
410 |     public void testGetCategoryIndex() {
411 |     	// check an empty dataset
412 |     	DefaultIntervalCategoryDataset empty 
413 |     	        = new DefaultIntervalCategoryDataset(new double[0][0], 
414 |     	        		new double[0][0]);
415 |     	assertEquals(-1, empty.getCategoryIndex("ABC"));
416 |     }
```

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testSetCategoryKeys()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testSetCategoryKeys()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
432 |     public void testSetCategoryKeys() {
433 |     	// check an empty dataset
434 |     	DefaultIntervalCategoryDataset empty 
435 |     	        = new DefaultIntervalCategoryDataset(new double[0][0], 
436 |     	        		new double[0][0]);
437 |     	boolean pass = true;
438 |     	try {
439 |     		empty.setCategoryKeys(new String[0]);
440 |     	}
441 |     	catch (RuntimeException e) {
442 |     		pass = false;
443 |     	}
444 |     	assertTrue(pass);
445 |     }
```

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetSeriesIndex()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetSeriesIndex()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
370 |     public void testGetSeriesIndex() {
371 |     	// check an empty dataset
372 |     	DefaultIntervalCategoryDataset empty 
373 |     	        = new DefaultIntervalCategoryDataset(new double[0][0], 
374 |     	        		new double[0][0]);
375 |     	assertEquals(-1, empty.getSeriesIndex("ABC"));
376 |     }
```

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetRowCount()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetRowCount()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
485 |     public void testGetRowCount() {
486 |     	// check an empty dataset
487 |     	DefaultIntervalCategoryDataset empty 
488 |     	        = new DefaultIntervalCategoryDataset(new double[0][0], 
489 |     	        		new double[0][0]);
490 |         assertEquals(0, empty.getColumnCount());
491 |     }
```

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetRowIndex()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetRowIndex()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
381 |     public void testGetRowIndex() {
382 |     	// check an empty dataset
383 |     	DefaultIntervalCategoryDataset empty 
384 |     	        = new DefaultIntervalCategoryDataset(new double[0][0], 
385 |     	        		new double[0][0]);
386 |     	assertEquals(-1, empty.getRowIndex("ABC"));
387 |     }
```

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetColumnCount()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetColumnCount()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
474 |     public void testGetColumnCount() {
475 |     	// check an empty dataset
476 |     	DefaultIntervalCategoryDataset empty 
477 |     	        = new DefaultIntervalCategoryDataset(new double[0][0], 
478 |     	        		new double[0][0]);
479 |         assertEquals(0, empty.getColumnCount());
480 |     }
```

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetColumnIndex()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testGetColumnIndex()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
421 |     public void testGetColumnIndex() {
422 |     	// check an empty dataset
423 |     	DefaultIntervalCategoryDataset empty 
424 |     	        = new DefaultIntervalCategoryDataset(new double[0][0], 
425 |     	        		new double[0][0]);
426 |     	assertEquals(-1, empty.getColumnIndex("ABC"));
427 |     }
```

## org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testCloning2()
Resolved declaration: org.jfree.data.category.junit.DefaultIntervalCategoryDatasetTests.testCloning2()
Source: tests/org/jfree/data/category/junit/DefaultIntervalCategoryDatasetTests.java

```java
259 |     public void testCloning2() {
260 |     	DefaultIntervalCategoryDataset d1 
261 |                 = new DefaultIntervalCategoryDataset(new double[0][0], 
262 |         		    new double[0][0]);
263 |         DefaultIntervalCategoryDataset d2 = null;
264 |         try {
265 |             d2 = (DefaultIntervalCategoryDataset) d1.clone();
266 |         }
267 |         catch (CloneNotSupportedException e) {
268 |             e.printStackTrace();
269 |         }
270 |         assertTrue(d1 != d2);
271 |         assertTrue(d1.getClass() == d2.getClass());
272 |         assertTrue(d1.equals(d2));	
273 |     }
```
