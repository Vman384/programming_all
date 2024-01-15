public class Variables {
    public static void main(String[] args) {
        double pi = 3.14;
        // double pi = 3.141592653; cannot redefine a variable 

        String text = "contains text";
        int wholeNumber = 123;
        double floatingPoint = 3.141592653; //can change this to an int type though
        boolean trueOrFalse = true;

        // trueOrFalse = 5; cannot change a variables type as well

        System.out.println("Text variable: " + text);
        System.out.println("Integer variable: " + wholeNumber);
        System.out.println("Floating-point variable: " + floatingPoint);
        System.out.println("Boolean: " + trueOrFalse);

        System.out.println("The value of pi is: " + pi);

        String valueAsString = "42";
        int value = Integer.valueOf(valueAsString); //converts string to an int

        System.out.println(value);

        valueAsString = "42.42";
        double value2 = Double.valueOf(valueAsString); //converts string to float/double
        System.out.println(value2);


        valueAsString = "true1fesdv";
        boolean bool = Boolean.valueOf(valueAsString); //converts string to boolean, string must be true or false, case insensitive, if its not true then becomes false
        System.out.println(bool);

        valueAsString = "true";
        bool = Boolean.valueOf(valueAsString); //converts string to boolean, string must be true or false, case insensitive, if its not true then becomes false
        System.out.println(bool);
    }
}