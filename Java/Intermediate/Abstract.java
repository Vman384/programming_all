import java.util.Scanner;

public class Abstract {
     /* An abstract class is used when we want to take advantage of inheritance  
     but don't necessarily have a full implementation for the super class yet or it doesnt make sense to 
     have an instance of that class
     */
    public abstract class Operation { //The abstract class Operation works as a basis for implementing different actions

        private String name;

        public Operation(String name) {
            this.name = name;
        }

        public String getName() {
            return this.name;
        }

        public abstract void execute(Scanner scanner);
    }

    /*
     * The greatest difference between interfaces and abstract classes is that
     *  abstract classes can contain object variables and constructors in addition to methods
     */

    public class PlusOperation extends Operation {

        public PlusOperation() {
            super("PlusOperation");
        }
    
        @Override
        public void execute(Scanner scanner) {
            System.out.print("First number: ");
            int first = Integer.valueOf(scanner.nextLine());
            System.out.print("Second number: ");
            int second = Integer.valueOf(scanner.nextLine());
    
            System.out.println("The sum of the numbers is " + (first + second));
        }
    }


}
