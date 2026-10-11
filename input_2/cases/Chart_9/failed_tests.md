# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.time.junit.TimeSeriesTests.testBug1864222()
Resolved declaration: org.jfree.data.time.junit.TimeSeriesTests.testBug1864222()
Source: tests/org/jfree/data/time/junit/TimeSeriesTests.java

```java
823 |     public void testBug1864222() {
824 |         TimeSeries s = new TimeSeries("S");
825 |         s.add(new Day(19, 8, 2005), 1);
826 |         s.add(new Day(31, 1, 2006), 1);
827 |         boolean pass = true;
828 |         try {
829 |             s.createCopy(new Day(1, 12, 2005), new Day(18, 1, 2006));
830 |         }
831 |         catch (CloneNotSupportedException e) {
832 |             pass = false;
833 |         }
834 |         assertTrue(pass);
835 |     }
```
