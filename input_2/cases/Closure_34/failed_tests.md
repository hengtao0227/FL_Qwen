# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.CodePrinterTest.testManyAdds()
Resolved declaration: com.google.javascript.jscomp.CodePrinterTest.testManyAdds()
Source: test/com/google/javascript/jscomp/CodePrinterTest.java

```java
1382 |   public void testManyAdds() {
1383 |     int numAdds = 10000;
1384 |     List<String> numbers = Lists.newArrayList("0", "1");
1385 |     Node current = new Node(Token.ADD, Node.newNumber(0), Node.newNumber(1));
1386 |     for (int i = 2; i < numAdds; i++) {
1387 |       current = new Node(Token.ADD, current);
1388 | 
1389 |       // 1000 is printed as 1E3, and screws up our test.
1390 |       int num = i % 1000;
1391 |       numbers.add(String.valueOf(num));
1392 |       current.addChildToBack(Node.newNumber(num));
1393 |     }
1394 | 
1395 |     String expected = Joiner.on("+").join(numbers);
1396 |     String actual = printNode(current).replace("\n", "");
1397 |     assertEquals(expected, actual);
1398 |   }
```
