import java.io.*;
import java.lang.instrument.*;
import java.security.ProtectionDomain;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.jar.JarFile;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;

/** Records actual method entries, including methods that exit by throwing. */
public final class MethodEntryAgent {
    private static final Set<String> errors = Collections.newSetFromMap(new ConcurrentHashMap<String, Boolean>());
    public static void premain(String args, Instrumentation instrumentation) throws Exception {
        final String[] paths = args.split("\\|", -1);
        instrumentation.appendToBootstrapClassLoaderSearch(new JarFile(paths[2]));
        CoverageRecorder.hits.size();
        final Set<String> production = new HashSet<String>();
        BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(paths[0]), "UTF-8"));
        String line; while ((line = reader.readLine()) != null) production.add(line);
        reader.close();
        Runtime.getRuntime().addShutdownHook(new Thread(new Runnable() {
            public void run() {
                try {
                    PrintWriter out = new PrintWriter(paths[1], "UTF-8");
                    List<String> sorted = new ArrayList<String>(CoverageRecorder.hits); Collections.sort(sorted);
                    for (String key : sorted) out.println(key); out.close();
                    out = new PrintWriter(paths[1] + ".errors", "UTF-8");
                    for (String error : errors) out.println(error); out.close();
                } catch (Exception e) { e.printStackTrace(); }
            }
        }));
        instrumentation.addTransformer(new ClassFileTransformer() {
            public byte[] transform(ClassLoader loader, String name, Class<?> type,
                                    ProtectionDomain domain, byte[] bytes) {
                if (!production.contains(name)) return null;
                try {
                    ClassNode cls = new ClassNode(Opcodes.ASM5);
                    new ClassReader(bytes).accept(cls, 0);
                    for (Object item : cls.methods) {
                        MethodNode method = (MethodNode)item;
                        if ((method.access & (Opcodes.ACC_ABSTRACT | Opcodes.ACC_NATIVE | Opcodes.ACC_SYNTHETIC | Opcodes.ACC_BRIDGE)) != 0
                                || method.name.equals("<clinit>")) continue;
                        TreeSet<Integer> lines = new TreeSet<Integer>();
                        for (AbstractInsnNode node = method.instructions.getFirst(); node != null; node = node.getNext())
                            if (node instanceof LineNumberNode) lines.add(((LineNumberNode)node).line);
                        StringBuilder numbers = new StringBuilder();
                        for (Integer number : lines) { if (numbers.length() > 0) numbers.append(','); numbers.append(number); }
                        String key = name + "\t" + cls.sourceFile + "\t" + method.name + "\t" + method.desc + "\t" + numbers;
                        InsnList prefix = new InsnList();
                        prefix.add(new LdcInsnNode(key));
                        prefix.add(new MethodInsnNode(Opcodes.INVOKESTATIC, "CoverageRecorder", "hit", "(Ljava/lang/String;)V", false));
                        method.instructions.insert(prefix);
                    }
                    ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_MAXS);
                    cls.accept(writer); return writer.toByteArray();
                } catch (Throwable e) { errors.add(name + ": " + e); return null; }
            }
        });
    }
}
