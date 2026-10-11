# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldGetElem()
Resolved declaration: com.google.javascript.jscomp.PeepholeFoldConstantsTest.testFoldGetElem()
Source: test/com/google/javascript/jscomp/PeepholeFoldConstantsTest.java

```java
764 |   public void testFoldGetElem() {
765 |     fold("x = [,10][0]", "x = void 0");
766 |     fold("x = [10, 20][0]", "x = 10");
767 |     fold("x = [10, 20][1]", "x = 20");
768 |     fold("x = [10, 20][0.5]", "",
769 |         PeepholeFoldConstants.INVALID_GETELEM_INDEX_ERROR);
770 |     fold("x = [10, 20][-1]",    "",
771 |         PeepholeFoldConstants.INDEX_OUT_OF_BOUNDS_ERROR);
772 |     fold("x = [10, 20][2]",     "",
773 |         PeepholeFoldConstants.INDEX_OUT_OF_BOUNDS_ERROR);
774 | 
775 |     foldSame("x = [foo(), 0][1]");
776 |     fold("x = [0, foo()][1]", "x = foo()");
777 |     foldSame("x = [0, foo()][0]");
778 |   }
```
