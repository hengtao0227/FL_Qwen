# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.genetics.ListPopulationTest.testIterator()
Resolved declaration: org.apache.commons.math3.genetics.ListPopulationTest.testIterator()
Source: src/test/java/org/apache/commons/math3/genetics/ListPopulationTest.java

```java
167 |     @Test(expected = UnsupportedOperationException.class)
168 |     public void testIterator() {
169 |         final ArrayList<Chromosome> chromosomes = new ArrayList<Chromosome>();
170 |         chromosomes.add(new DummyBinaryChromosome(BinaryChromosome.randomBinaryRepresentation(3)));
171 |         chromosomes.add(new DummyBinaryChromosome(BinaryChromosome.randomBinaryRepresentation(3)));
172 |         chromosomes.add(new DummyBinaryChromosome(BinaryChromosome.randomBinaryRepresentation(3)));
173 | 
174 |         final ListPopulation population = new ListPopulation(10) {
175 |             public Population nextGeneration() {
176 |                 // not important
177 |                 return null;
178 |             }
179 |         };
180 | 
181 |         population.addChromosomes(chromosomes);
182 | 
183 |         final Iterator<Chromosome> iter = population.iterator();
184 |         while (iter.hasNext()) {
185 |             iter.next();
186 |             iter.remove();
187 |         }
188 |     }
```
