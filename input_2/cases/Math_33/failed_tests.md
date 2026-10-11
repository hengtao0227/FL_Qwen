# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.optimization.linear.SimplexSolverTest.testMath781()
Resolved declaration: org.apache.commons.math3.optimization.linear.SimplexSolverTest.testMath781()
Source: src/test/java/org/apache/commons/math3/optimization/linear/SimplexSolverTest.java

```java
32 |     @Test
33 |     public void testMath781() {
34 |         LinearObjectiveFunction f = new LinearObjectiveFunction(new double[] { 2, 6, 7 }, 0);
35 | 
36 |         ArrayList<LinearConstraint> constraints = new ArrayList<LinearConstraint>();
37 |         constraints.add(new LinearConstraint(new double[] { 1, 2, 1 }, Relationship.LEQ, 2));
38 |         constraints.add(new LinearConstraint(new double[] { -1, 1, 1 }, Relationship.LEQ, -1));
39 |         constraints.add(new LinearConstraint(new double[] { 2, -3, 1 }, Relationship.LEQ, -1));
40 | 
41 |         double epsilon = 1e-6;
42 |         SimplexSolver solver = new SimplexSolver();
43 |         PointValuePair solution = solver.optimize(f, constraints, GoalType.MAXIMIZE, false);
44 | 
45 |         Assert.assertTrue(Precision.compareTo(solution.getPoint()[0], 0.0d, epsilon) > 0);
46 |         Assert.assertTrue(Precision.compareTo(solution.getPoint()[1], 0.0d, epsilon) > 0);
47 |         Assert.assertTrue(Precision.compareTo(solution.getPoint()[2], 0.0d, epsilon) < 0);
48 |         Assert.assertEquals(2.0d, solution.getValue(), epsilon);
49 |     }
```
