# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockitousage.annotation.SpyAnnotationTest.should_spy_inner_class()
Resolved declaration: org.mockitousage.annotation.SpyAnnotationTest.should_spy_inner_class()
Source: test/org/mockitousage/annotation/SpyAnnotationTest.java

```java
123 |     @Test
124 |     public void should_spy_inner_class() throws Exception {
125 |     	 
126 |      class WithMockAndSpy {
127 |     		@Spy private InnerStrength strength;
128 |     		@Mock private List<String> list;
129 | 
130 |             abstract class InnerStrength {
131 |             	private final String name;
132 | 
133 |             	InnerStrength() {
134 |             		// Make sure that @Mock fields are always injected before @Spy fields.
135 |             		assertNotNull(list);
136 |             		// Make sure constructor is indeed called.
137 |             		this.name = "inner";
138 |             	}
139 |             	
140 |             	abstract String strength();
141 |             	
142 |             	String fullStrength() {
143 |             		return name + " " + strength();
144 |             	}
145 |             }
146 |     	}
147 | 		WithMockAndSpy outer = new WithMockAndSpy();
148 |         MockitoAnnotations.initMocks(outer);
149 |         when(outer.strength.strength()).thenReturn("strength");
150 |         assertEquals("inner strength", outer.strength.fullStrength());
151 |     }
```

## org.mockitousage.annotation.SpyAnnotationTest.should_report_when_constructor_is_explosive()
Resolved declaration: org.mockitousage.annotation.SpyAnnotationTest.should_report_when_constructor_is_explosive()
Source: test/org/mockitousage/annotation/SpyAnnotationTest.java

```java
92 |     @Test
93 |     public void should_report_when_constructor_is_explosive() throws Exception {
94 | 		class FailingSpy {
95 | 	        @Spy
96 |             ThrowingConstructor throwingConstructor;
97 | 		}
98 | 
99 |         try {
100 |             MockitoAnnotations.initMocks(new FailingSpy());
101 |             fail();
102 |         } catch (MockitoException e) {
103 |             Assertions.assertThat(e.getMessage()).contains("Unable to create mock instance");
104 |         }
105 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_spy_abstract_classes()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_spy_abstract_classes()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
43 |     @Test
44 |     public void can_spy_abstract_classes() {
45 |         AbstractMessage mock = spy(AbstractMessage.class);
46 |         assertEquals("hey!", mock.getMessage());
47 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.exception_message_when_constructor_not_found()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.exception_message_when_constructor_not_found()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
59 |     @Test
60 |     public void exception_message_when_constructor_not_found() {
61 |         try {
62 |             //when
63 |             spy(HasConstructor.class);
64 |             //then
65 |             fail();
66 |         } catch (MockitoException e) {
67 |             assertEquals("Unable to create mock instance of type 'HasConstructor'", e.getMessage());
68 |             assertContains("0-arg constructor", e.getCause().getMessage());
69 |         }
70 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_create_mock_with_constructor()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_create_mock_with_constructor()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
30 |     @Test
31 |     public void can_create_mock_with_constructor() {
32 |         Message mock = mock(Message.class, withSettings().useConstructor().defaultAnswer(CALLS_REAL_METHODS));
33 |         //the message is a part of state of the mocked type that gets initialized in constructor
34 |         assertEquals("hey!", mock.getMessage());
35 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_mock_inner_classes()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_mock_inner_classes()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
49 |     @Test
50 |     public void can_mock_inner_classes() {
51 |         InnerClass mock = mock(InnerClass.class, withSettings().useConstructor().outerInstance(this).defaultAnswer(CALLS_REAL_METHODS));
52 |         assertEquals("hey!", mock.getMessage());
53 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.mocking_inner_classes_with_wrong_outer_instance()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.mocking_inner_classes_with_wrong_outer_instance()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
72 |     @Test
73 |     public void mocking_inner_classes_with_wrong_outer_instance() {
74 |         try {
75 |             //when
76 |             mock(InnerClass.class, withSettings().useConstructor().outerInstance("foo").defaultAnswer(CALLS_REAL_METHODS));
77 |             //then
78 |             fail();
79 |         } catch (MockitoException e) {
80 |             assertEquals("Unable to create mock instance of type 'InnerClass'", e.getMessage());
81 |             assertContains("Please ensure that the outer instance has correct type and that the target class has 0-arg constructor.", e.getCause().getMessage());
82 |         }
83 |     }
```

## org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_mock_abstract_classes()
Resolved declaration: org.mockitousage.constructor.CreatingMocksWithConstructorTest.can_mock_abstract_classes()
Source: test/org/mockitousage/constructor/CreatingMocksWithConstructorTest.java

```java
37 |     @Test
38 |     public void can_mock_abstract_classes() {
39 |         AbstractMessage mock = mock(AbstractMessage.class, withSettings().useConstructor().defaultAnswer(CALLS_REAL_METHODS));
40 |         assertEquals("hey!", mock.getMessage());
41 |     }
```
