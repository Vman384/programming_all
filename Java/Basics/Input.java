import java.util.Scanner;

public class Input {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("whats your name");

        String message = scanner.nextLine();
        
        System.out.println("Hi " + message);


    }

    public static void temp(Integer args){
        int x = 1+args;
        System.out.println(x);

    }
}
