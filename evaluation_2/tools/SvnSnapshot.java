import java.io.*;
import java.util.*;
import java.util.zip.*;
import org.tmatesoft.svn.core.*;
import org.tmatesoft.svn.core.io.*;
import org.tmatesoft.svn.core.internal.io.fs.FSRepositoryFactory;

/** Exports the exact fixed SVN tree into the same snapshot ZIP shape as Git archives. */
public class SvnSnapshot {
    static SVNRepository repository;
    static ZipOutputStream zip;
    static long revision;
    static void visit(String path, String prefix) throws Exception {
        Collection<SVNDirEntry> entries = new ArrayList<SVNDirEntry>();
        repository.getDir(path, revision, null, entries);
        for (SVNDirEntry entry : entries) {
            String child = path + "/" + entry.getName();
            String name = prefix + entry.getName();
            if (entry.getKind() == SVNNodeKind.DIR) visit(child, name + "/");
            else {
                ZipEntry out = new ZipEntry("snapshot/" + name); out.setTime(0);
                zip.putNextEntry(out);
                repository.getFile(child, revision, null, zip);
                zip.closeEntry();
            }
        }
    }
    public static void main(String[] args) throws Exception {
        FSRepositoryFactory.setup();
        repository = SVNRepositoryFactory.create(SVNURL.fromFile(new File(args[0])));
        revision = Long.parseLong(args[1]);
        zip = new ZipOutputStream(new BufferedOutputStream(new FileOutputStream(args[2])));
        try { visit("trunk", ""); } finally { zip.close(); repository.closeSession(); }
    }
}
