# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.data.time.junit.TimeSeriesTests.testBug1832432()
Resolved declaration: org.jfree.data.time.junit.TimeSeriesTests.testBug1832432()
Source: tests/org/jfree/data/time/junit/TimeSeriesTests.java

```java
615 |     public void testBug1832432() {
616 |         TimeSeries s1 = new TimeSeries("Series");
617 |         TimeSeries s2 = null;
618 |         try {
619 |             s2 = (TimeSeries) s1.clone();
620 |         }
621 |         catch (CloneNotSupportedException e) {
622 |             e.printStackTrace();
623 |         }
624 |         assertTrue(s1 != s2);
625 |         assertTrue(s1.getClass() == s2.getClass());
626 |         assertTrue(s1.equals(s2));
627 | 
628 |         // test independence
629 |         s1.add(new Day(1, 1, 2007), 100.0);
630 |         assertFalse(s1.equals(s2));    	
631 |     }
```
