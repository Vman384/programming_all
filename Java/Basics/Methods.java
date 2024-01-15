import java.util.ArrayList;

public class Methods {
    public static void main(String[] args) {
        // a method is just another name for a function
        // void can be replaced with the return type for the function
        // the stuff in () is the arguments
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < 10; i++){
            list.add(i);
        }
        double avg = average(list);
        System.out.println(avg);

    }

    public static double average(ArrayList<Integer> numbers) {
        if (numbers.size() == 0) {
            return -1.0;
        }

        int sum = 0;
        for (int number: numbers) {
            sum = sum + number;
        }

        return 1.0 * sum / numbers.size();
        }
}
