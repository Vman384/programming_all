import java.util.ArrayList;
import java.util.Scanner;

public class UserInterface {
    private GradeRegister gradeRegister;
    private Scanner scanner;

    public UserInterface(Scanner scanner){
        this.scanner = scanner;
        this.gradeRegister = new GradeRegister();
    }
    public void ReadInput(){
        System.out.println("Enter the grade: ");
        while(true){
            Integer grade = Integer.valueOf(scanner.nextLine());
            if(grade >=0 & grade<=100){
                gradeRegister.addGrade(grade);
            }
            if(grade == -1){
                System.out.println("The average is: " + gradeRegister.averagePassing(0));
                System.out.println("The average pass rate is: " + gradeRegister.averagePassing(50));   
                System.out.println("The pass percentage is: " + gradeRegister.passPercent(50));
                ArrayList dist = gradeRegister.gradeDistribution();   
                System.out.println("0: " + dist.get(0));
                System.out.println("1: " + dist.get(1));
                System.out.println("2: " + dist.get(2));
                System.out.println("3: " + dist.get(3));
                System.out.println("4: " + dist.get(4));
                System.out.println("5: " + dist.get(5));

                break;
            }
        }

        
    }

    public String outString(){
        return "test";
    };

    public static void main(String[] args) {
        // String input = "5\n " + "50\n" + "80\n" + "70\n" + "65\n" + "-1";
        Scanner scanner = new Scanner(System.in);
        UserInterface userInterface = new UserInterface(scanner);
        userInterface.ReadInput();
    }
}
