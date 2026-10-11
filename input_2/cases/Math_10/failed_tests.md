# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.analysis.differentiation.DerivativeStructureTest.testAtan2SpecialCases()
Resolved declaration: org.apache.commons.math3.analysis.differentiation.DerivativeStructureTest.testAtan2SpecialCases()
Source: src/test/java/org/apache/commons/math3/analysis/differentiation/DerivativeStructureTest.java

```java
810 |     @Test
811 |     public void testAtan2SpecialCases() {
812 | 
813 |         DerivativeStructure pp =
814 |                 DerivativeStructure.atan2(new DerivativeStructure(2, 2, 1, +0.0),
815 |                                           new DerivativeStructure(2, 2, 1, +0.0));
816 |         Assert.assertEquals(0, pp.getValue(), 1.0e-15);
817 |         Assert.assertEquals(+1, FastMath.copySign(1, pp.getValue()), 1.0e-15);
818 | 
819 |         DerivativeStructure pn =
820 |                 DerivativeStructure.atan2(new DerivativeStructure(2, 2, 1, +0.0),
821 |                                           new DerivativeStructure(2, 2, 1, -0.0));
822 |         Assert.assertEquals(FastMath.PI, pn.getValue(), 1.0e-15);
823 | 
824 |         DerivativeStructure np =
825 |                 DerivativeStructure.atan2(new DerivativeStructure(2, 2, 1, -0.0),
826 |                                           new DerivativeStructure(2, 2, 1, +0.0));
827 |         Assert.assertEquals(0, np.getValue(), 1.0e-15);
828 |         Assert.assertEquals(-1, FastMath.copySign(1, np.getValue()), 1.0e-15);
829 | 
830 |         DerivativeStructure nn =
831 |                 DerivativeStructure.atan2(new DerivativeStructure(2, 2, 1, -0.0),
832 |                                           new DerivativeStructure(2, 2, 1, -0.0));
833 |         Assert.assertEquals(-FastMath.PI, nn.getValue(), 1.0e-15);
834 | 
835 |     }
```
