import java.io.File;
import java.lang.reflect.Field;
import sun.misc.Unsafe;

/** POSIX public path constants for Closure's in-memory JS filenames.
 * Native WinNTFileSystem is initialized first and retains native disk handling.
 * Used identically in the baseline and instrumented run; no production rewrite.
 */
public final class PosixSourcePathRunner {
    public static void main(String[] args) throws Exception {
        new File(".").getCanonicalPath();
        Field handle = Unsafe.class.getDeclaredField("theUnsafe");
        handle.setAccessible(true);
        Unsafe u = (Unsafe)handle.get(null);
        Field separator = File.class.getDeclaredField("separator");
        u.putObject(u.staticFieldBase(separator), u.staticFieldOffset(separator), "/");
        Field character = File.class.getDeclaredField("separatorChar");
        u.putChar(u.staticFieldBase(character), u.staticFieldOffset(character), '/');
        TriggerRunner.main(args);
    }
}
