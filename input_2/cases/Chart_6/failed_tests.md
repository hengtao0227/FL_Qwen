# Failing test code

Full extracted test bodies; no assertion trimming.

## org.jfree.chart.util.junit.ShapeListTests.testSerialization()
Resolved declaration: org.jfree.chart.util.junit.ShapeListTests.testSerialization()
Source: tests/org/jfree/chart/util/junit/ShapeListTests.java

```java
128 |     public void testSerialization() {
129 | 
130 |         ShapeList l1 = new ShapeList();
131 |         l1.setShape(0, new Rectangle(1, 2, 3, 4));
132 |         l1.setShape(1, new Line2D.Double(1.0, 2.0, 3.0, 4.0));
133 |         l1.setShape(2, null);
134 | 
135 |         ShapeList l2 = null;
136 | 
137 |         try {
138 |             ByteArrayOutputStream buffer = new ByteArrayOutputStream();
139 |             ObjectOutput out = new ObjectOutputStream(buffer);
140 |             out.writeObject(l1);
141 |             out.close();
142 | 
143 |             ObjectInput in = new ObjectInputStream(new ByteArrayInputStream(
144 |             		buffer.toByteArray()));
145 |             l2 = (ShapeList) in.readObject();
146 |             in.close();
147 |         }
148 |         catch (Exception e) {
149 |             e.printStackTrace();
150 |         }
151 |         assertEquals(l1, l2);
152 | 
153 |     }
```

## org.jfree.chart.util.junit.ShapeListTests.testEquals()
Resolved declaration: org.jfree.chart.util.junit.ShapeListTests.testEquals()
Source: tests/org/jfree/chart/util/junit/ShapeListTests.java

```java
84 |     public void testEquals() {
85 |         ShapeList l1 = new ShapeList();
86 |         l1.setShape(0, new Rectangle(1, 2, 3, 4));
87 |         l1.setShape(1, new Line2D.Double(1.0, 2.0, 3.0, 4.0));
88 |         l1.setShape(2, null);
89 | 
90 |         ShapeList l2 = new ShapeList();
91 |         l2.setShape(0, new Rectangle(1, 2, 3, 4));
92 |         l2.setShape(1, new Line2D.Double(1.0, 2.0, 3.0, 4.0));
93 |         l2.setShape(2, null);
94 | 
95 |         assertTrue(l1.equals(l2));
96 |         assertTrue(l2.equals(l2));
97 |     }
```
