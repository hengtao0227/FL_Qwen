# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.linear.SimplexSolverTest.testSingleVariableAndConstraint()
Resolved declaration: org.apache.commons.math.optimization.linear.SimplexSolverTest.testSingleVariableAndConstraint()
Source: src/test/org/apache/commons/math/optimization/linear/SimplexSolverTest.java

```java
67 |     @Test
68 |     public void testSingleVariableAndConstraint() throws OptimizationException {
69 |         LinearObjectiveFunction f = new LinearObjectiveFunction(new double[] { 3 }, 0);
70 |         Collection<LinearConstraint> constraints = new ArrayList<LinearConstraint>();
71 |         constraints.add(new LinearConstraint(new double[] { 1 }, Relationship.LEQ, 10));
72 | 
73 |         SimplexSolver solver = new SimplexSolver();
74 |         RealPointValuePair solution = solver.optimize(f, constraints, GoalType.MAXIMIZE, false);
75 |         assertEquals(10.0, solution.getPoint()[0], 0.0);
76 |         assertEquals(30.0, solution.getValue(), 0.0);
77 |     }
```
