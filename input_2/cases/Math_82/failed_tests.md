# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath288()
Resolved declaration: org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath288()
Source: src/test/java/org/apache/commons/math/optimization/linear/SimplexSolverTest.java

```java
61 |     @Test
62 |     public void testMath288() throws OptimizationException {
63 |         LinearObjectiveFunction f = new LinearObjectiveFunction(new double[] { 7, 3, 0, 0 }, 0 );
64 |         Collection<LinearConstraint> constraints = new ArrayList<LinearConstraint>();
65 |         constraints.add(new LinearConstraint(new double[] { 3, 0, -5, 0 }, Relationship.LEQ, 0.0));
66 |         constraints.add(new LinearConstraint(new double[] { 2, 0, 0, -5 }, Relationship.LEQ, 0.0));
67 |         constraints.add(new LinearConstraint(new double[] { 0, 3, 0, -5 }, Relationship.LEQ, 0.0));
68 |         constraints.add(new LinearConstraint(new double[] { 1, 0, 0, 0 }, Relationship.LEQ, 1.0));
69 |         constraints.add(new LinearConstraint(new double[] { 0, 1, 0, 0 }, Relationship.LEQ, 1.0));
70 | 
71 |         SimplexSolver solver = new SimplexSolver();
72 |         RealPointValuePair solution = solver.optimize(f, constraints, GoalType.MAXIMIZE, true);
73 |         assertEquals(10.0, solution.getValue(), .0000001);
74 |     }
```
