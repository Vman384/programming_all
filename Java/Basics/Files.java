import java.util.ArrayList;
import java.util.Scanner;
import java.nio.file.Paths;

public class Files {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(Paths.get("file.txt"))) {
            ArrayList<String> lines = new ArrayList<>();
            // we read the file until all lines have been read
            while (scanner.hasNextLine()) {
                // we read one line
                String row = scanner.nextLine();
                // if the line is blank we do nothing
                if (row.isEmpty()) {
                    continue;
                }

                // we print the line that we read
                System.out.println(row);
                lines.add(row);
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
