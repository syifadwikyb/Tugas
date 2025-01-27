//package Liskov2;

class WritableFile {
    public void write(String content) {
        System.out.println("Writing: " + content);
    }

    public void read() {
        System.out.println("Reading file...");
    }
}

class ReadOnlyFile {
    public void read() {
        System.out.println("Reading file...");
    }
}

public class solution2 {
    public static void main(String[] args) {
        WritableFile writableFile = new WritableFile();
        writableFile.write("This is a writable file");
        writableFile.read();

        ReadOnlyFile readOnlyFile = new ReadOnlyFile();
        readOnlyFile.read();
        // Tidak ada metode write() di ReadOnlyFile, jadi tidak ada pelanggaran LSP
    }
}
