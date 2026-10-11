# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath286()
Resolved declaration: org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath286()
Source: src/test/java/org/apache/commons/math/optimization/linear/SimplexSolverTest.java

```java
51 |     @Test
52 |     public void testMath286() throws OptimizationException {
53 |       LinearObjectiveFunction f = new LinearObjectiveFunction(new double[] { 0.2, 0.3 }, 0 );
54 |       Collection<LinearConstraint> constraints = new ArrayList<LinearConstraint>();
55 |       constraints.add(new LinearConstraint(new double[] { 1, 1 }, Relationship.EQ, 23.0));
56 | 
57 |       RealPointValuePair solution = new SimplexSolver().optimize(f, constraints, GoalType.MAXIMIZE, true);
58 |       assertEquals(6.9, solution.getValue(), .0000001);
59 |     }
```
