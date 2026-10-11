# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.TypeCheckTest.testIssue700()
Resolved declaration: com.google.javascript.jscomp.TypeCheckTest.testIssue700()
Source: test/com/google/javascript/jscomp/TypeCheckTest.java

```java
5776 |   public void testIssue700() throws Exception {
5777 |     testTypes(
5778 |         "/**\n" +
5779 |         " * @param {{text: string}} opt_data\n" +
5780 |         " * @return {string}\n" +
5781 |         " */\n" +
5782 |         "function temp1(opt_data) {\n" +
5783 |         "  return opt_data.text;\n" +
5784 |         "}\n" +
5785 |         "\n" +
5786 |         "/**\n" +
5787 |         " * @param {{activity: (boolean|number|string|null|Object)}} opt_data\n" +
5788 |         " * @return {string}\n" +
5789 |         " */\n" +
5790 |         "function temp2(opt_data) {\n" +
5791 |         "  /** @notypecheck */\n" +
5792 |         "  function __inner() {\n" +
5793 |         "    return temp1(opt_data.activity);\n" +
5794 |         "  }\n" +
5795 |         "  return __inner();\n" +
5796 |         "}\n" +
5797 |         "\n" +
5798 |         "/**\n" +
5799 |         " * @param {{n: number, text: string, b: boolean}} opt_data\n" +
5800 |         " * @return {string}\n" +
5801 |         " */\n" +
5802 |         "function temp3(opt_data) {\n" +
5803 |         "  return 'n: ' + opt_data.n + ', t: ' + opt_data.text + '.';\n" +
5804 |         "}\n" +
5805 |         "\n" +
5806 |         "function callee() {\n" +
5807 |         "  var output = temp3({\n" +
5808 |         "    n: 0,\n" +
5809 |         "    text: 'a string',\n" +
5810 |         "    b: true\n" +
5811 |         "  })\n" +
5812 |         "  alert(output);\n" +
5813 |         "}\n" +
5814 |         "\n" +
5815 |         "callee();");
5816 |   }
```
