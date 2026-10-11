# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.util.reflection.GenericMasterTest.shouldDealWithNestedGenerics()
Resolved declaration: org.mockito.internal.util.reflection.GenericMasterTest.shouldDealWithNestedGenerics()
Source: test/org/mockito/internal/util/reflection/GenericMasterTest.java

```java
36 |     @Test
37 |     public void shouldDealWithNestedGenerics() throws Exception {
38 |         assertEquals(Set.class, m.getGenericType(field("nested")));
39 |         assertEquals(Set.class, m.getGenericType(field("multiNested")));
40 |     }
```

## org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldUseAnnotatedCaptor()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldUseAnnotatedCaptor()
Source: test/org/mockitousage/annotation/CaptorAnnotationBasicTest.java

```java
64 |     @Test
65 |     public void shouldUseAnnotatedCaptor() {
66 |         //when
67 |         createPerson("Wes", "Williams");
68 |         
69 |         //then
70 |         verify(peopleRepository).save(captor.capture());
71 |         assertEquals("Wes", captor.getValue().getName());
72 |         assertEquals("Williams", captor.getValue().getSurname());
73 |     }
```

## org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldUseCaptorInOrdinaryWay()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldUseCaptorInOrdinaryWay()
Source: test/org/mockitousage/annotation/CaptorAnnotationBasicTest.java

```java
50 |     @Test
51 |     public void shouldUseCaptorInOrdinaryWay() {
52 |         //when
53 |         createPerson("Wes", "Williams");
54 |         
55 |         //then
56 |         ArgumentCaptor<Person> captor = ArgumentCaptor.forClass(Person.class);
57 |         verify(peopleRepository).save(captor.capture());
58 |         assertEquals("Wes", captor.getValue().getName());
59 |         assertEquals("Williams", captor.getValue().getSurname());
60 |     }
```

## org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldCaptureGenericList()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldCaptureGenericList()
Source: test/org/mockitousage/annotation/CaptorAnnotationBasicTest.java

```java
91 |     @Test
92 |     public void shouldCaptureGenericList() {
93 |         //given
94 |         List<String> list = new LinkedList<String>();
95 |         mock.listArgMethod(list);
96 |                 
97 |         //when
98 |         verify(mock).listArgMethod(genericListCaptor.capture());
99 |         
100 |         //then
101 |         assertSame(list, genericListCaptor.getValue());
102 |     } 
```

## org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldUseGenericlessAnnotatedCaptor()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationBasicTest.shouldUseGenericlessAnnotatedCaptor()
Source: test/org/mockitousage/annotation/CaptorAnnotationBasicTest.java

```java
77 |     @Test
78 |     public void shouldUseGenericlessAnnotatedCaptor() {
79 |         //when
80 |         createPerson("Wes", "Williams");
81 |         
82 |         //then
83 |         verify(peopleRepository).save((Person) genericLessCaptor.capture());
84 |         assertEquals("Wes", ((Person) genericLessCaptor.getValue()).getName());
85 |         assertEquals("Williams", ((Person) genericLessCaptor.getValue()).getSurname());
86 |     }  
```

## org.mockitousage.annotation.CaptorAnnotationTest.shouldScreamWhenWrongTypeForCaptor()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationTest.shouldScreamWhenWrongTypeForCaptor()
Source: test/org/mockitousage/annotation/CaptorAnnotationTest.java

```java
78 |     @Test
79 |     public void shouldScreamWhenWrongTypeForCaptor() {
80 |         try {
81 |             MockitoAnnotations.initMocks(new WrongType());
82 |             fail();
83 |         } catch (MockitoException e) {}
84 |     }
```

## org.mockitousage.annotation.CaptorAnnotationTest.testNormalUsage()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationTest.testNormalUsage()
Source: test/org/mockitousage/annotation/CaptorAnnotationTest.java

```java
49 |     @Test
50 |     public void testNormalUsage() {
51 | 
52 |         MockitoAnnotations.initMocks(this);
53 | 
54 |         // check if assigned correctly
55 |         assertNotNull(finalCaptor);
56 |         assertNotNull(genericsCaptor);
57 |         assertNotNull(nonGenericCaptorIsAllowed);
58 |         assertNull(notAMock);
59 | 
60 |         // use captors in the field to be sure they are cool
61 |         String argForFinalCaptor = "Hello";
62 |         ArrayList<List<String>> argForGenericsCaptor = new ArrayList<List<String>>();
63 | 
64 |         mockInterface.testMe(argForFinalCaptor, argForGenericsCaptor);
65 | 
66 |         Mockito.verify(mockInterface).testMe(finalCaptor.capture(), genericsCaptor.capture());
67 | 
68 |         assertEquals(argForFinalCaptor, finalCaptor.getValue());
69 |         assertEquals(argForGenericsCaptor, genericsCaptor.getValue());
70 | 
71 |     }
```

## org.mockitousage.annotation.CaptorAnnotationTest.shouldScreamWhenMoreThanOneMockitoAnnotaton()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationTest.shouldScreamWhenMoreThanOneMockitoAnnotaton()
Source: test/org/mockitousage/annotation/CaptorAnnotationTest.java

```java
92 |     @Test
93 |     public void shouldScreamWhenMoreThanOneMockitoAnnotaton() {
94 |         try {
95 |             MockitoAnnotations.initMocks(new ToManyAnnotations());
96 |             fail();
97 |         } catch (MockitoException e) {
98 |             assertContains("missingGenericsField", e.getMessage());
99 |             assertContains("multiple Mockito annotations", e.getMessage());            
100 |         }
101 |     }
```

## org.mockitousage.annotation.CaptorAnnotationTest.shouldScreamWhenInitializingCaptorsForNullClass()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationTest.shouldScreamWhenInitializingCaptorsForNullClass()
Source: test/org/mockitousage/annotation/CaptorAnnotationTest.java

```java
103 |     @Test
104 |     public void shouldScreamWhenInitializingCaptorsForNullClass() throws Exception {
105 |         try {
106 |             MockitoAnnotations.initMocks(null);
107 |             fail();
108 |         } catch (MockitoException e) {
109 |         }
110 |     }
```

## org.mockitousage.annotation.CaptorAnnotationTest.shouldLookForAnnotatedCaptorsInSuperClasses()
Resolved declaration: org.mockitousage.annotation.CaptorAnnotationTest.shouldLookForAnnotatedCaptorsInSuperClasses()
Source: test/org/mockitousage/annotation/CaptorAnnotationTest.java

```java
112 |     @Test
113 |     public void shouldLookForAnnotatedCaptorsInSuperClasses() throws Exception {
114 |         Sub sub = new Sub();
115 |         MockitoAnnotations.initMocks(sub);
116 | 
117 |         assertNotNull(sub.getCaptor());
118 |         assertNotNull(sub.getBaseCaptor());
119 |         assertNotNull(sub.getSuperBaseCaptor());
120 |     }
```
