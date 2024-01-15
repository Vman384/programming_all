import java.util.Scanner;

public class Loops {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        // For saving number of numbers
        int numberOfPositives = 0;
        int numberOfNegatives = 0;

        // For repeatedly asking for numbers
        while (true) {
            System.out.println("Give a number (0 to stop): ");
            // For reading user input
            int numberFromUser = Integer.valueOf(reader.nextLine());

            // For breaking the loop when user writes 0
            if (numberFromUser == 0) {
                break;
            }

            // For increasing numberOfPositives by one
            // when user gives a positive number
            if (numberFromUser > 0) {
                numberOfPositives = numberOfPositives + 1;
            }

            // For increasing numberOfNegatives by one
            // when user gives a negative number
            if (numberFromUser < 0) {
                numberOfNegatives = numberOfNegatives + 1;
            }

            // Also could have used..
            // if (numberFromUser > 0) {
            //     numberOfPositives = numberOfPositives + 1;
            // } else {
            //     numberOfNegatives = numberOfNegatives + 1;
            // }

        }

        // For printing the number of positive numbers
        System.out.println("Positive numbers: " + numberOfPositives);
        // For printing the number of negative numbers
        System.out.println("Negative numbers: " + numberOfNegatives);

        // For printing the percentage of positive numbers from all numbers

        if (numberOfPositives + numberOfNegatives > 0) {
            // Print only if user has given numbers
            // to avoid dividing by zero
            double percentageOfPositives = 100.0 * numberOfPositives / (numberOfPositives + numberOfNegatives);
            System.out.println("Percentage of positive numbers: " + percentageOfPositives + "%");
        }   

        Scanner scanner = new Scanner(System.in);

        // The task is to read an input from the user
        while (true) {

            // The task is to keep count of number ones
            int ones = 0;

            System.out.println("Input a number (0 exits): ");
            // The task is to read a user inputted number
            int number = Integer.valueOf(scanner.nextLine());

            // The task is to exit the loop if the user
            // has inputted zero
            if (number == 0) {
                break;
            }

            // The task is to increase the amount of ones
            // if the user inputs a number one
            if (number == 1) {
                ones = ones + 1;
            }
        }

        // The task is to print out the total of ones
        // This doesn't work because the variable ones has been
        // introduced within the loop
        // define the variable outside the loop to use it
        System.out.println("The total of ones: " + ones);

    }
}
