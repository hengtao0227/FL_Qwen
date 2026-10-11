# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath272()
Resolved declaration: org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath272()
Source: src/test/org/apache/commons/math/optimization/linear/SimplexSolverTest.java

```java
34 |     @Test
35 |     public void testMath272() throws OptimizationException {
36 |         LinearObjectiveFunction f = new LinearObjectiveFunction(new double[] { 2, 2, 1 }, 0);
37 |         Collection<LinearConstraint> constraints = new ArrayList<LinearConstraint>();
38 |         constraints.add(new LinearConstraint(new double[] { 1, 1, 0 }, Relationship.GEQ,  1));
39 |         constraints.add(new LinearConstraint(new double[] { 1, 0, 1 }, Relationship.GEQ,  1));
40 |         constraints.add(new LinearConstraint(new double[] { 0, 1, 0 }, Relationship.GEQ,  1));
41 | 
42 |         SimplexSolver solver = new SimplexSolver();
43 |         RealPointValuePair solution = solver.optimize(f, constraints, GoalType.MINIMIZE, true);
44 |         
45 |         assertEquals(0.0, solution.getPoint()[0], .0000001);
46 |         assertEquals(1.0, solution.getPoint()[1], .0000001);
47 |         assertEquals(1.0, solution.getPoint()[2], .0000001);
48 |         assertEquals(3.0, solution.getValue(), .0000001);
49 |       }
```
