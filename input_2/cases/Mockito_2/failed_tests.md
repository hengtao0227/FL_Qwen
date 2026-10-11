# Failing test code

Full extracted test bodies; no assertion trimming.

## org.mockito.internal.util.TimerTest.should_throw_friendly_reminder_exception_when_duration_is_negative()
Resolved declaration: org.mockito.internal.util.TimerTest.should_throw_friendly_reminder_exception_when_duration_is_negative()
Source: test/org/mockito/internal/util/TimerTest.java

```java
38 |     @Test
39 |     public void should_throw_friendly_reminder_exception_when_duration_is_negative() {
40 |         try {
41 |             new Timer(-1);
42 |             Assert.fail("It is forbidden to create timer with negative value of timer's duration.");
43 |         } catch (FriendlyReminderException e) {
44 |             Assert.assertTrue(true);
45 |         }
46 |     }
```

## org.mockito.verification.NegativeDurationTest.should_throw_exception_when_duration_is_negative_for_timeout_method()
Resolved declaration: org.mockito.verification.NegativeDurationTest.should_throw_exception_when_duration_is_negative_for_timeout_method()
Source: test/org/mockito/verification/NegativeDurationTest.java

```java
10 |     @Test
11 |     public void should_throw_exception_when_duration_is_negative_for_timeout_method() {
12 |         try {
13 |             Mockito.timeout(-1);
14 |             Assert.fail("It is forbidden to invoke Mockito.timeout() with negative value.");
15 |         } catch (FriendlyReminderException e) {
16 |             Assert.assertTrue(true);
17 |         }
18 |     }
```

## org.mockito.verification.NegativeDurationTest.should_throw_exception_when_duration_is_negative_for_after_method()
Resolved declaration: org.mockito.verification.NegativeDurationTest.should_throw_exception_when_duration_is_negative_for_after_method()
Source: test/org/mockito/verification/NegativeDurationTest.java

```java
20 |     @Test
21 |     public void should_throw_exception_when_duration_is_negative_for_after_method() {
22 |         try {
23 |             Mockito.after(-1);
24 |             Assert.fail("It is forbidden to invoke Mockito.after() with negative value.");
25 |         } catch (FriendlyReminderException e) {
26 |             Assert.assertTrue(true);
27 |         }
28 |     }
```
