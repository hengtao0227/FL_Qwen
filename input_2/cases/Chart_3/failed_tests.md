# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.time.junit.TimeSeriesTests.testCreateCopy3()
Resolved declaration: org.jfree.data.time.junit.TimeSeriesTests.testCreateCopy3()
Source: tests/org/jfree/data/time/junit/TimeSeriesTests.java

```java
597 |     public void testCreateCopy3() throws CloneNotSupportedException {
598 |         TimeSeries s1 = new TimeSeries("S1");
599 |         s1.add(new Year(2009), 100.0);
600 |         s1.add(new Year(2010), 101.0);
601 |         s1.add(new Year(2011), 102.0);
602 |         assertEquals(100.0, s1.getMinY(), EPSILON);
603 |         assertEquals(102.0, s1.getMaxY(), EPSILON);
604 | 
605 |         TimeSeries s2 = s1.createCopy(0, 1);
606 |         assertEquals(100.0, s2.getMinY(), EPSILON);
607 |         assertEquals(101.0, s2.getMaxY(), EPSILON);
608 | 
609 |         TimeSeries s3 = s1.createCopy(1, 2);
610 |         assertEquals(101.0, s3.getMinY(), EPSILON);
611 |         assertEquals(102.0, s3.getMaxY(), EPSILON);
612 |     }
```
