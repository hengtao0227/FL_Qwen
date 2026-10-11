# Failing test code

Full extracted test bodies; no assertion trimming.

## org.apache.commons.math3.dfp.DfpTest.testMultiply()
Resolved declaration: org.apache.commons.math3.dfp.DfpTest.testMultiply()
Source: src/test/java/org/apache/commons/math3/dfp/DfpTest.java

```java
755 |     @Test
756 |     public void testMultiply()
757 |     {
758 |         test(field.newDfp("1").multiply(field.newDfp("1")),      // Basic tests   1*1 = 1
759 |              field.newDfp("1"),
760 |              0, "Multiply #1");
761 | 
762 |         test(field.newDfp("1").multiply(1),             // Basic tests   1*1 = 1
763 |              field.newDfp("1"),
764 |              0, "Multiply #2");
765 | 
766 |         test(field.newDfp("-1").multiply(field.newDfp("1")),     // Basic tests   -1*1 = -1
767 |              field.newDfp("-1"),
768 |              0, "Multiply #3");
769 | 
770 |         test(field.newDfp("-1").multiply(1),            // Basic tests   -1*1 = -1
771 |              field.newDfp("-1"),
772 |              0, "Multiply #4");
773 | 
774 |         // basic tests with integers
775 |         test(field.newDfp("2").multiply(field.newDfp("3")),
776 |              field.newDfp("6"),
777 |              0, "Multiply #5");
778 | 
779 |         test(field.newDfp("2").multiply(3),
780 |              field.newDfp("6"),
781 |              0, "Multiply #6");
782 | 
783 |         test(field.newDfp("-2").multiply(field.newDfp("3")),
784 |              field.newDfp("-6"),
785 |              0, "Multiply #7");
786 | 
787 |         test(field.newDfp("-2").multiply(3),
788 |              field.newDfp("-6"),
789 |              0, "Multiply #8");
790 | 
791 |         test(field.newDfp("2").multiply(field.newDfp("-3")),
792 |              field.newDfp("-6"),
793 |              0, "Multiply #9");
794 | 
795 |         test(field.newDfp("-2").multiply(field.newDfp("-3")),
796 |              field.newDfp("6"),
797 |              0, "Multiply #10");
798 | 
799 |         //multiply by zero
800 | 
801 |         test(field.newDfp("-2").multiply(field.newDfp("0")),
802 |              field.newDfp("-0"),
803 |              0, "Multiply #11");
804 | 
805 |         test(field.newDfp("-2").multiply(0),
806 |              field.newDfp("-0"),
807 |              0, "Multiply #12");
808 | 
809 |         test(field.newDfp("2").multiply(field.newDfp("0")),
810 |              field.newDfp("0"),
811 |              0, "Multiply #13");
812 | 
813 |         test(field.newDfp("2").multiply(0),
814 |              field.newDfp("0"),
815 |              0, "Multiply #14");
816 | 
817 |         test(field.newDfp("2").multiply(pinf),
818 |              pinf,
819 |              0, "Multiply #15");
820 | 
821 |         test(field.newDfp("2").multiply(ninf),
822 |              ninf,
823 |              0, "Multiply #16");
824 | 
825 |         test(field.newDfp("-2").multiply(pinf),
826 |              ninf,
827 |              0, "Multiply #17");
828 | 
829 |         test(field.newDfp("-2").multiply(ninf),
830 |              pinf,
831 |              0, "Multiply #18");
832 | 
833 |         test(ninf.multiply(field.newDfp("-2")),
834 |              pinf,
835 |              0, "Multiply #18.1");
836 | 
837 |         test(field.newDfp("5e131071").multiply(2),
838 |              pinf,
839 |              DfpField.FLAG_OVERFLOW, "Multiply #19");
840 | 
841 |         test(field.newDfp("5e131071").multiply(field.newDfp("1.999999999999999")),
842 |              field.newDfp("9.9999999999999950000e131071"),
843 |              0, "Multiply #20");
844 | 
845 |         test(field.newDfp("-5e131071").multiply(2),
846 |              ninf,
847 |              DfpField.FLAG_OVERFLOW, "Multiply #22");
848 | 
849 |         test(field.newDfp("-5e131071").multiply(field.newDfp("1.999999999999999")),
850 |              field.newDfp("-9.9999999999999950000e131071"),
851 |              0, "Multiply #23");
852 | 
853 |         test(field.newDfp("1e-65539").multiply(field.newDfp("1e-65539")),
854 |              field.newDfp("1e-131078"),
855 |              DfpField.FLAG_UNDERFLOW, "Multiply #24");
856 | 
857 |         test(field.newDfp("1").multiply(nan),
858 |              nan,
859 |              0, "Multiply #25");
860 | 
861 |         test(nan.multiply(field.newDfp("1")),
862 |              nan,
863 |              0, "Multiply #26");
864 | 
865 |         test(nan.multiply(pinf),
866 |              nan,
867 |              0, "Multiply #27");
868 | 
869 |         test(pinf.multiply(nan),
870 |              nan,
871 |              0, "Multiply #27");
872 | 
873 |         test(pinf.multiply(field.newDfp("0")),
874 |              nan,
875 |              DfpField.FLAG_INVALID, "Multiply #28");
876 | 
877 |         test(field.newDfp("0").multiply(pinf),
878 |              nan,
879 |              DfpField.FLAG_INVALID, "Multiply #29");
880 | 
881 |         test(pinf.multiply(pinf),
882 |              pinf,
883 |              0, "Multiply #30");
884 | 
885 |         test(ninf.multiply(pinf),
886 |              ninf,
887 |              0, "Multiply #31");
888 | 
889 |         test(pinf.multiply(ninf),
890 |              ninf,
891 |              0, "Multiply #32");
892 | 
893 |         test(ninf.multiply(ninf),
894 |              pinf,
895 |              0, "Multiply #33");
896 | 
897 |         test(pinf.multiply(1),
898 |              pinf,
899 |              0, "Multiply #34");
900 | 
901 |         test(pinf.multiply(0),
902 |              nan,
903 |              DfpField.FLAG_INVALID, "Multiply #35");
904 | 
905 |         test(nan.multiply(1),
906 |              nan,
907 |              0, "Multiply #36");
908 | 
909 |         test(field.newDfp("1").multiply(10000),
910 |              field.newDfp("10000"),
911 |              0, "Multiply #37");
912 | 
913 |         test(field.newDfp("2").multiply(1000000),
914 |              field.newDfp("2000000"),
915 |              0, "Multiply #38");
916 | 
917 |         test(field.newDfp("1").multiply(-1),
918 |              field.newDfp("-1"),
919 |              0, "Multiply #39");
920 |     }
```
