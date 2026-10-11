# Failing test code

Full extracted test bodies; no assertion trimming.

## com.google.javascript.jscomp.IntegrationTest.testSingletonGetter1()
Resolved declaration: com.google.javascript.jscomp.IntegrationTest.testSingletonGetter1()
Source: test/com/google/javascript/jscomp/IntegrationTest.java

```java
1937 |   public void testSingletonGetter1() {
1938 |     CompilerOptions options = createCompilerOptions();
1939 |     CompilationLevel.ADVANCED_OPTIMIZATIONS
1940 |         .setOptionsForCompilationLevel(options);
1941 |     options.setCodingConvention(new ClosureCodingConvention());
1942 |     test(options,
1943 |         "/** @const */\n" +
1944 |         "var goog = goog || {};\n" +
1945 |         "goog.addSingletonGetter = function(ctor) {\n" +
1946 |         "  ctor.getInstance = function() {\n" +
1947 |         "    return ctor.instance_ || (ctor.instance_ = new ctor());\n" +
1948 |         "  };\n" +
1949 |         "};" +
1950 |         "function Foo() {}\n" +
1951 |         "goog.addSingletonGetter(Foo);" +
1952 |         "Foo.prototype.bar = 1;" +
1953 |         "function Bar() {}\n" +
1954 |         "goog.addSingletonGetter(Bar);" +
1955 |         "Bar.prototype.bar = 1;",
1956 |         "");
1957 |   }
```
