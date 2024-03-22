import java.util.ArrayList;
import java.util.Scanner;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Testing{
    public static void main(){
        String input = "one\n" + "two\n"  + 
                "three\n" + "four\n" +
                "five\n" + "one\n"  +
                "six\n"; //we can pass input into the scanner as so

    Scanner reader = new Scanner(input);

    ArrayList<String> read = new ArrayList<>();

    while (true) {
        System.out.println("Enter an input: ");
        String line = reader.nextLine();
        if (read.contains(line)) {
            break;
        }

        read.add(line);
    }

    System.out.println("Thank you!");

    if (read.contains("six")) {
        System.out.println("A value that should not have been added to the group was added to it.");
    }
        }

    public class Calculator {

        private int value;
    
        public Calculator() {
            this.value = 0;
        }
    
        public void add(int number) {
            this.value = this.value + number;
        }
    
        public void subtract(int number) {
            this.value = this.value + number;
        }
    
        public int getValue() {
            return this.value;
        }
    }     
    public class CalculatorTest {

        @Test
        public void calculatorInitialValueZero() {
            Calculator calculator = new Calculator();
            assertEquals(0, calculator.getValue());
        }
    }   
}