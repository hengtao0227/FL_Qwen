# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.genetics.ElitisticListPopulationTest.testChromosomeListConstructorTooLow()
Resolved declaration: org.apache.commons.math3.genetics.ElitisticListPopulationTest.testChromosomeListConstructorTooLow()
Source: src/test/java/org/apache/commons/math3/genetics/ElitisticListPopulationTest.java

```java
78 |     @Test(expected = OutOfRangeException.class)
79 |     public void testChromosomeListConstructorTooLow() {
80 |         final List<Chromosome> chromosomes = Collections.emptyList();
81 |         final double rate = -0.25;
82 |         new ElitisticListPopulation(chromosomes, 100, rate);
83 |     }
```

## org.apache.commons.math3.genetics.ElitisticListPopulationTest.testConstructorTooHigh()
Resolved declaration: org.apache.commons.math3.genetics.ElitisticListPopulationTest.testConstructorTooHigh()
Source: src/test/java/org/apache/commons/math3/genetics/ElitisticListPopulationTest.java

```java
72 |     @Test(expected = OutOfRangeException.class)
73 |     public void testConstructorTooHigh() {
74 |         final double rate = 1.25;
75 |         new ElitisticListPopulation(100, rate);
76 |     }
```

## org.apache.commons.math3.genetics.ElitisticListPopulationTest.testConstructorTooLow()
Resolved declaration: org.apache.commons.math3.genetics.ElitisticListPopulationTest.testConstructorTooLow()
Source: src/test/java/org/apache/commons/math3/genetics/ElitisticListPopulationTest.java

```java
66 |     @Test(expected = OutOfRangeException.class)
67 |     public void testConstructorTooLow() {
68 |         final double rate = -0.25;
69 |         new ElitisticListPopulation(100, rate);
70 |     }
```

## org.apache.commons.math3.genetics.ElitisticListPopulationTest.testChromosomeListConstructorTooHigh()
Resolved declaration: org.apache.commons.math3.genetics.ElitisticListPopulationTest.testChromosomeListConstructorTooHigh()
Source: src/test/java/org/apache/commons/math3/genetics/ElitisticListPopulationTest.java

```java
85 |     @Test(expected = OutOfRangeException.class)
86 |     public void testChromosomeListConstructorTooHigh() {
87 |         final List<Chromosome> chromosomes = Collections.emptyList();
88 |         final double rate = 1.25;
89 |         new ElitisticListPopulation(chromosomes, 100, rate);
90 |     }
```
