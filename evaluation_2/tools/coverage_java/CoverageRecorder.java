import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

/** Bootstrap-visible recorder also works with deliberately isolated classloaders. */
public final class CoverageRecorder {
    public static final Set<String> hits = Collections.newSetFromMap(new ConcurrentHashMap<String, Boolean>());
    public static void hit(String key) { if (!hits.contains(key)) hits.add(key); }
}
