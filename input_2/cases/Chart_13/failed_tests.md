# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.block.junit.BorderArrangementTests.testSizingWithWidthConstraint()
Resolved declaration: org.jfree.chart.block.junit.BorderArrangementTests.testSizingWithWidthConstraint()
Source: tests/org/jfree/chart/block/junit/BorderArrangementTests.java

```java
496 |     public void testSizingWithWidthConstraint() {
497 |         RectangleConstraint constraint = new RectangleConstraint(
498 |             10.0, new Range(10.0, 10.0), LengthConstraintType.FIXED,
499 |             0.0, new Range(0.0, 0.0), LengthConstraintType.NONE
500 |         );
501 |                 
502 |         BlockContainer container = new BlockContainer(new BorderArrangement());
503 |         BufferedImage image = new BufferedImage(
504 |             200, 100, BufferedImage.TYPE_INT_RGB
505 |         );
506 |         Graphics2D g2 = image.createGraphics();
507 |         
508 |         // TBLRC
509 |         // 00001 - center item only
510 |         container.add(new EmptyBlock(5.0, 6.0));
511 |         Size2D size = container.arrange(g2, constraint);
512 |         assertEquals(10.0, size.width, EPSILON);
513 |         assertEquals(6.0, size.height, EPSILON);
514 |         
515 |         container.clear();
516 |         container.add(new EmptyBlock(15.0, 16.0));
517 |         size = container.arrange(g2, constraint);
518 |         assertEquals(10.0, size.width, EPSILON);
519 |         assertEquals(16.0, size.height, EPSILON);
520 | 
521 |         // TBLRC
522 |         // 00010 - right item only
523 |         container.clear();
524 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.RIGHT);
525 |         size = container.arrange(g2, constraint);
526 |         assertEquals(10.0, size.width, EPSILON);
527 |         assertEquals(45.6, size.height, EPSILON);
528 |         
529 |         // TBLRC
530 |         // 00011 - right and center items
531 |         container.clear();
532 |         container.add(new EmptyBlock(7.0, 20.0));
533 |         container.add(new EmptyBlock(8.0, 45.6), RectangleEdge.RIGHT);
534 |         size = container.arrange(g2, constraint);
535 |         assertEquals(10.0, size.width, EPSILON);
536 |         assertEquals(45.6, size.height, EPSILON);
537 |         
538 |         // TBLRC
539 |         // 00100 - left item only
540 |         container.clear();
541 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.LEFT);
542 |         size = container.arrange(g2, constraint);
543 |         assertEquals(10.0, size.width, EPSILON);
544 |         assertEquals(45.6, size.height, EPSILON);
545 |         
546 |         // TBLRC
547 |         // 00101 - left and center items
548 |         container.clear();
549 |         container.add(new EmptyBlock(10.0, 20.0));
550 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.LEFT);
551 |         size = container.arrange(g2, constraint);
552 |         assertEquals(10.0, size.width, EPSILON);
553 |         assertEquals(45.6, size.height, EPSILON);
554 |         
555 |         // TBLRC
556 |         // 00110 - left and right items
557 |         container.clear();
558 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.RIGHT);
559 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.LEFT);
560 |         size = container.arrange(g2, constraint);
561 |         assertEquals(10.0, size.width, EPSILON);
562 |         assertEquals(45.6, size.height, EPSILON);
563 |         
564 |         // TBLRC
565 |         // 00111 - left, right and center items
566 |         container.clear();
567 |         container.add(new EmptyBlock(10.0, 20.0));
568 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.LEFT);
569 |         container.add(new EmptyBlock(5.4, 3.2), RectangleEdge.RIGHT);
570 |         size = container.arrange(g2, constraint);
571 |         assertEquals(10.0, size.width, EPSILON);
572 |         assertEquals(45.6, size.height, EPSILON);
573 |         
574 |         // TBLRC
575 |         // 01000 - bottom item only
576 |         container.clear();
577 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
578 |         size = container.arrange(g2, constraint);
579 |         assertEquals(10.0, size.width, EPSILON);
580 |         assertEquals(45.6, size.height, EPSILON);
581 |         
582 |         // TBLRC
583 |         // 01001 - bottom and center only
584 |         container.clear();
585 |         container.add(new EmptyBlock(10.0, 20.0));
586 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
587 |         size = container.arrange(g2, constraint);
588 |         assertEquals(10.0, size.width, EPSILON);
589 |         assertEquals(65.6, size.height, EPSILON);
590 |         
591 |         // TBLRC
592 |         // 01010 - bottom and right only
593 |         container.clear();
594 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.RIGHT);
595 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
596 |         size = container.arrange(g2, constraint);
597 |         assertEquals(10.0, size.width, EPSILON);
598 |         assertEquals(65.6, size.height, EPSILON);
599 |         
600 |         // TBLRC
601 |         // 01011 - bottom, right and center
602 |         container.clear();
603 |         container.add(new EmptyBlock(21.0, 12.3));
604 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.RIGHT);
605 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
606 |         size = container.arrange(g2, constraint);
607 |         assertEquals(10.0, size.width, EPSILON);
608 |         assertEquals(65.6, size.height, EPSILON);
609 |         
610 |         // TBLRC
611 |         // 01100
612 |         container.clear();
613 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.LEFT);
614 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
615 |         size = container.arrange(g2, constraint);
616 |         assertEquals(10.0, size.width, EPSILON);
617 |         assertEquals(65.6, size.height, EPSILON);
618 |         
619 |         // TBLRC
620 |         // 01101 - bottom, left and center
621 |         container.clear();
622 |         container.add(new EmptyBlock(21.0, 12.3));
623 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.LEFT);
624 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
625 |         size = container.arrange(g2, constraint);
626 |         assertEquals(10.0, size.width, EPSILON);
627 |         assertEquals(65.6, size.height, EPSILON);
628 |         
629 |         // TBLRC
630 |         // 01110 - bottom. left and right
631 |         container.clear();
632 |         container.add(new EmptyBlock(21.0, 12.3), RectangleEdge.RIGHT);
633 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.LEFT);
634 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
635 |         size = container.arrange(g2, constraint);
636 |         assertEquals(10.0, size.width, EPSILON);
637 |         assertEquals(65.6, size.height, EPSILON);
638 |         
639 |         // TBLRC
640 |         // 01111
641 |         container.clear();
642 |         container.add(new EmptyBlock(3.0, 4.0), RectangleEdge.BOTTOM);
643 |         container.add(new EmptyBlock(5.0, 6.0), RectangleEdge.LEFT);
644 |         container.add(new EmptyBlock(7.0, 8.0), RectangleEdge.RIGHT);
645 |         container.add(new EmptyBlock(9.0, 10.0));
646 |         size = container.arrange(g2, constraint);
647 |         assertEquals(10.0, size.width, EPSILON);
648 |         assertEquals(14.0, size.height, EPSILON);
649 |         
650 |         // TBLRC
651 |         // 10000 - top item only
652 |         container.clear();
653 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.TOP);
654 |         size = container.arrange(g2, constraint);
655 |         assertEquals(10.0, size.width, EPSILON);
656 |         assertEquals(45.6, size.height, EPSILON);
657 |         
658 |         // TBLRC
659 |         // 10001 - top and center only
660 |         container.clear();
661 |         container.add(new EmptyBlock(10.0, 20.0));
662 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.TOP);
663 |         size = container.arrange(g2, constraint);
664 |         assertEquals(10.0, size.width, EPSILON);
665 |         assertEquals(65.6, size.height, EPSILON);
666 |                 
667 |         // TBLRC
668 |         // 10010 - right and top only
669 |         container.clear();
670 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.RIGHT);
671 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.TOP);
672 |         size = container.arrange(g2, constraint);
673 |         assertEquals(10.0, size.width, EPSILON);
674 |         assertEquals(65.6, size.height, EPSILON);
675 |         
676 |         // TBLRC
677 |         // 10011 - top, right and center
678 |         container.clear();
679 |         container.add(new EmptyBlock(21.0, 12.3));
680 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.TOP);
681 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.RIGHT);
682 |         size = container.arrange(g2, constraint);
683 |         assertEquals(10.0, size.width, EPSILON);
684 |         assertEquals(65.6, size.height, EPSILON);
685 | 
686 |         // TBLRC
687 |         // 10100 - top and left only
688 |         container.clear();
689 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.LEFT);
690 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.TOP);
691 |         size = container.arrange(g2, constraint);
692 |         assertEquals(10.0, size.width, EPSILON);
693 |         assertEquals(65.6, size.height, EPSILON);
694 |         
695 |         // TBLRC
696 |         // 10101 - top, left and center
697 |         container.clear();
698 |         container.add(new EmptyBlock(21.0, 12.3));
699 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.TOP);
700 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.LEFT);
701 |         size = container.arrange(g2, constraint);
702 |         assertEquals(10.0, size.width, EPSILON);
703 |         assertEquals(65.6, size.height, EPSILON);
704 |         
705 |         // TBLRC
706 |         // 10110 - top, left and right
707 |         container.clear();
708 |         container.add(new EmptyBlock(21.0, 12.3), RectangleEdge.RIGHT);
709 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.TOP);
710 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.LEFT);
711 |         size = container.arrange(g2, constraint);
712 |         assertEquals(10.0, size.width, EPSILON);
713 |         assertEquals(65.6, size.height, EPSILON);
714 |         
715 |         // TBLRC
716 |         // 10111
717 |         container.clear();
718 |         container.add(new EmptyBlock(1.0, 2.0), RectangleEdge.TOP);
719 |         container.add(new EmptyBlock(5.0, 6.0), RectangleEdge.LEFT);
720 |         container.add(new EmptyBlock(7.0, 8.0), RectangleEdge.RIGHT);
721 |         container.add(new EmptyBlock(9.0, 10.0));
722 |         size = container.arrange(g2, constraint);
723 |         assertEquals(10.0, size.width, EPSILON);
724 |         assertEquals(12.0, size.height, EPSILON);
725 | 
726 |         // TBLRC
727 |         // 11000 - top and bottom only
728 |         container.clear();
729 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.TOP);
730 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
731 |         size = container.arrange(g2, constraint);
732 |         assertEquals(10.0, size.width, EPSILON);
733 |         assertEquals(65.6, size.height, EPSILON);
734 |         
735 |         // TBLRC
736 |         // 11001
737 |         container.clear();
738 |         container.add(new EmptyBlock(21.0, 12.3));
739 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.TOP);
740 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
741 |         size = container.arrange(g2, constraint);
742 |         assertEquals(10.0, size.width, EPSILON);
743 |         assertEquals(77.9, size.height, EPSILON);
744 |         
745 |         // TBLRC
746 |         // 11010 - top, bottom and right
747 |         container.clear();
748 |         container.add(new EmptyBlock(21.0, 12.3), RectangleEdge.RIGHT);
749 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.TOP);
750 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
751 |         size = container.arrange(g2, constraint);
752 |         assertEquals(10.0, size.width, EPSILON);
753 |         assertEquals(77.9, size.height, EPSILON);
754 |                 
755 |         // TBLRC
756 |         // 11011
757 |         container.clear();
758 |         container.add(new EmptyBlock(1.0, 2.0), RectangleEdge.TOP);
759 |         container.add(new EmptyBlock(3.0, 4.0), RectangleEdge.BOTTOM);
760 |         container.add(new EmptyBlock(7.0, 8.0), RectangleEdge.RIGHT);
761 |         container.add(new EmptyBlock(9.0, 10.0));
762 |         size = container.arrange(g2, constraint);
763 |         assertEquals(10.0, size.width, EPSILON);
764 |         assertEquals(16.0, size.height, EPSILON);
765 |         
766 |         // TBLRC
767 |         // 11100
768 |         container.clear();
769 |         container.add(new EmptyBlock(21.0, 12.3), RectangleEdge.LEFT);
770 |         container.add(new EmptyBlock(10.0, 20.0), RectangleEdge.TOP);
771 |         container.add(new EmptyBlock(12.3, 45.6), RectangleEdge.BOTTOM);
772 |         size = container.arrange(g2, constraint);
773 |         assertEquals(10.0, size.width, EPSILON);
774 |         assertEquals(77.9, size.height, EPSILON);
775 | 
776 |         // TBLRC
777 |         // 11101
778 |         container.clear();
779 |         container.add(new EmptyBlock(1.0, 2.0), RectangleEdge.TOP);
780 |         container.add(new EmptyBlock(3.0, 4.0), RectangleEdge.BOTTOM);
781 |         container.add(new EmptyBlock(5.0, 6.0), RectangleEdge.LEFT);
782 |         container.add(new EmptyBlock(9.0, 10.0));
783 |         size = container.arrange(g2, constraint);
784 |         assertEquals(10.0, size.width, EPSILON);
785 |         assertEquals(16.0, size.height, EPSILON);
786 |         
787 |         // TBLRC
788 |         // 11110
789 |         container.clear();
790 |         container.add(new EmptyBlock(1.0, 2.0), RectangleEdge.TOP);
791 |         container.add(new EmptyBlock(3.0, 4.0), RectangleEdge.BOTTOM);
792 |         container.add(new EmptyBlock(5.0, 6.0), RectangleEdge.LEFT);
793 |         container.add(new EmptyBlock(7.0, 8.0), RectangleEdge.RIGHT);
794 |         size = container.arrange(g2, constraint);
795 |         assertEquals(10.0, size.width, EPSILON);
796 |         assertEquals(14.0, size.height, EPSILON);
797 |         
798 |         // TBLRC
799 |         // 11111 - all
800 |         container.clear();
801 |         container.add(new EmptyBlock(1.0, 2.0), RectangleEdge.TOP);
802 |         container.add(new EmptyBlock(3.0, 4.0), RectangleEdge.BOTTOM);
803 |         container.add(new EmptyBlock(5.0, 6.0), RectangleEdge.LEFT);
804 |         container.add(new EmptyBlock(7.0, 8.0), RectangleEdge.RIGHT);
805 |         container.add(new EmptyBlock(9.0, 10.0));
806 |         size = container.arrange(g2, constraint);
807 |         assertEquals(10.0, size.width, EPSILON);
808 |         assertEquals(16.0, size.height, EPSILON);
809 | 
810 |         // TBLRC
811 |         // 00000 - no items
812 |         container.clear();
813 |         size = container.arrange(g2, constraint);
814 |         assertEquals(10.0, size.width, EPSILON);
815 |         assertEquals(0.0, size.height, EPSILON);
816 |         
817 |     }
```
