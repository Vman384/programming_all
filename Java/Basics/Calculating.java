public class Calculating {
    public static void main(String[] args) {
        int a = 10;
        int b = 25;
        int c = a+b;
        System.out.println(a+b);
        System.out.println(c);
        System.out.println("Four: " + (2 + 2));
        System.out.println("But! Twenty-two: " + 2 + 2);

        int first = 3;
        int second = 2;
        double result = first / second; //division of 2 ints always results in an int
        System.out.println(result);

        first = 3;
        second = 2;

        double result1 = (double) first / second; //we can fix it by doing these methods     
        System.out.println(result1); // prints 1.5

        double result2 = first / (double) second;
        System.out.println(result2); // prints 1.5

        double result3 = (double) (first / second);
        System.out.println(result3); // prints 1.0
    }   
}
