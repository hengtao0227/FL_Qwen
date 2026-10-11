# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath713NegativeVariable()
Resolved declaration: org.apache.commons.math.optimization.linear.SimplexSolverTest.testMath713NegativeVariable()
Source: src/test/java/org/apache/commons/math/optimization/linear/SimplexSolverTest.java

```java
32 |     @Test
33 |     public void testMath713NegativeVariable() {
34 |         LinearObjectiveFunction f = new LinearObjectiveFunction(new double[] {1.0, 1.0}, 0.0d);
35 |         ArrayList<LinearConstraint> constraints = new ArrayList<LinearConstraint>();
36 |         constraints.add(new LinearConstraint(new double[] {1, 0}, Relationship.EQ, 1));
37 | 
38 |         double epsilon = 1e-6;
39 |         SimplexSolver solver = new SimplexSolver();
40 |         RealPointValuePair solution = solver.optimize(f, constraints, GoalType.MINIMIZE, true);
41 | 
42 |         Assert.assertTrue(Precision.compareTo(solution.getPoint()[0], 0.0d, epsilon) >= 0);
43 |         Assert.assertTrue(Precision.compareTo(solution.getPoint()[1], 0.0d, epsilon) >= 0);
44 |     }
```
