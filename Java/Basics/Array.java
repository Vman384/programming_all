public class Array {
    public static void main(String[] args) {
        int[] numbers = new int[3]; //array to hold 3 integers
        String[] strings = new String[5]; // array to hold 5 strings
        numbers[0] = 2;
        numbers[2] = 5;
        System.out.println(numbers.length); //to find length of array 

        System.out.println(numbers[0]);
        System.out.println(numbers[2]);

        String[] months = new String[12];
        double[] approximations = new double[100];

        months[0] = "January";
        approximations[0] = 3.14;
        int[] numbers2 = {100, 1, 42}; //another way to create an array with elements already in it 
    }
}
