# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.FoldConstantsTest.testStringJoinAdd()
Resolved declaration: com.google.javascript.jscomp.FoldConstantsTest.testStringJoinAdd()
Source: test/com/google/javascript/jscomp/FoldConstantsTest.java

```java
623 |   public void testStringJoinAdd() {
624 |     fold("x = ['a', 'b', 'c'].join('')", "x = \"abc\"");
625 |     fold("x = [].join(',')", "x = \"\"");
626 |     fold("x = ['a'].join(',')", "x = \"a\"");
627 |     fold("x = ['a', 'b', 'c'].join(',')", "x = \"a,b,c\"");
628 |     fold("x = ['a', foo, 'b', 'c'].join(',')", "x = [\"a\",foo,\"b,c\"].join(\",\")");
629 |     fold("x = [foo, 'a', 'b', 'c'].join(',')", "x = [foo,\"a,b,c\"].join(\",\")");
630 |     fold("x = ['a', 'b', 'c', foo].join(',')", "x = [\"a,b,c\",foo].join(\",\")");
631 | 
632 |     // Works with numbers
633 |     fold("x = ['a=', 5].join('')", "x = \"a=5\"");
634 |     fold("x = ['a', '5'].join(7)", "x = \"a75\"");
635 | 
636 |     // Works on boolean
637 |     fold("x = ['a=', false].join('')", "x = \"a=false\"");
638 |     fold("x = ['a', '5'].join(true)", "x = \"atrue5\"");
639 |     fold("x = ['a', '5'].join(false)", "x = \"afalse5\"");
640 | 
641 |     // Only optimize if it's a size win.
642 |     fold("x = ['a', '5', 'c'].join('a very very very long chain')",
643 |          "x = [\"a\",\"5\",\"c\"].join(\"a very very very long chain\")");
644 |     
645 |     // TODO(user): Its possible to fold this better.
646 |     foldSame("x = ['', foo].join(',')");
647 |     foldSame("x = ['', foo, ''].join(',')");
648 |     
649 |     fold("x = ['', '', foo, ''].join(',')", "x = [',', foo, ''].join(',')");
650 |     fold("x = ['', '', foo, '', ''].join(',')",
651 |          "x = [',', foo, ','].join(',')");
652 |     
653 |     fold("x = ['', '', foo, '', '', bar].join(',')",
654 |          "x = [',', foo, ',', bar].join(',')");
655 |     
656 |     fold("x = [1,2,3].join('abcdef')",
657 |          "x = '1abcdef2abcdef3'");
658 |   }
```
