import java.io.*;
import org.junit.runner.*;
import org.junit.runner.notification.Failure;

/** Runs exactly one requested JUnit test method, retaining genuine failures. */
public final class TriggerRunner {
    private static String clean(String value) {
        return value == null ? "" : value.replace("\t", " ").replace("\r", " ").replace("\n", " ");
    }
    public static void main(String[] args) throws Exception {
        String[] test = args[0].split("::", 2);
        Class<?> clsToRun = Class.forName(test[0]);
        if (junit.framework.TestCase.class.isAssignableFrom(clsToRun)) {
            junit.framework.TestCase tc;
            try { tc = (junit.framework.TestCase)clsToRun.getConstructor(String.class).newInstance(test[1]); }
            catch (NoSuchMethodException e) { tc = (junit.framework.TestCase)clsToRun.newInstance(); tc.setName(test[1]); }
            junit.framework.TestResult result = new junit.framework.TestResult();
            tc.run(result);
            PrintWriter out = new PrintWriter(args[1], "UTF-8");
            out.println("counts\t"+result.runCount()+"\t"+(result.failureCount()+result.errorCount())+"\t0");
            java.util.List<junit.framework.TestFailure> failures = new java.util.ArrayList<junit.framework.TestFailure>();
            java.util.Enumeration<junit.framework.TestFailure> en = result.failures(); while(en.hasMoreElements()) failures.add(en.nextElement());
            en = result.errors(); while(en.hasMoreElements()) failures.add(en.nextElement());
            for (junit.framework.TestFailure failure : failures) {
                Throwable error = failure.thrownException();
                out.println("failure\t"+test[0]+"\t"+test[1]+"\t"+error.getClass().getName()+"\t"+clean(error.getMessage()));
                error.printStackTrace(System.out);
            }
            out.close();
            if(result.runCount()!=1 || failures.size()!=1) System.exit(2);
            System.exit(0);
            return;
        }
        Result result = new JUnitCore().run(Request.method(clsToRun, test[1]));
        PrintWriter out = new PrintWriter(args[1], "UTF-8");
        out.println("counts\t" + result.getRunCount() + "\t" + result.getFailureCount() + "\t" + result.getIgnoreCount());
        for (Failure failure : result.getFailures()) {
            String display = failure.getDescription().getDisplayName();
            int bracket = display.lastIndexOf('(');
            String cls = bracket >= 0 && display.endsWith(")") ? display.substring(bracket+1, display.length()-1) : display;
            String method = bracket >= 0 ? display.substring(0, bracket) : "";
            out.println("failure\t" + clean(cls) + "\t"
                + clean(method) + "\t"
                + failure.getException().getClass().getName() + "\t" + clean(failure.getMessage()));
            failure.getException().printStackTrace(System.out);
            try {
                Object stack = failure.getException().getClass().getMethod("getUnfilteredStackTrace").invoke(failure.getException());
                for (StackTraceElement frame : (StackTraceElement[])stack) System.out.println("\tat " + frame);
            } catch (ReflectiveOperationException ignored) { }
        }
        out.close();
        if (result.getRunCount() != 1 || result.getFailureCount() != 1) System.exit(2);
        System.exit(0);
    }
}
