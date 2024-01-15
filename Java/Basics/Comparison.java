import java.util.Scanner;

public class Comparison {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        if (true) {
            System.out.println("This code is unavoidable!");
        }
        int number = 11;
        if (number > 10) {
            System.out.println("The number was greater than 10");
        }
        
        System.out.println("What was your speed: ");
        double speed = Double.valueOf(sc.nextLine());
        if (speed > 120){
            System.out.println("You were driving too fast! You've been fined $50.");
        }
        number = 5;

        if (number == 0) {
            System.out.println("The number is zero.");
        } else if (number > 0) {
            System.out.println("The number is greater than zero.");
        } else if (number > 2) {
            System.out.println("The number is greater than two.");
        } else {
            System.out.println("The number is less than zero.");
        }
    }
}
