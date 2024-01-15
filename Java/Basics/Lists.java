import java.util.ArrayList;
import java.util.Scanner;

public class Lists {

    public static void main(String[] args) {
        // the part in <> is the type of variables 
        /**
         * The reason for this has to do with how the ArrayList is implemented. 
         * Variables in Java can be divided into two categories: value type (primitive) and reference 
         * type (reference type) variables. Value-type variables such as int or double hold their actual values.
         *  Reference-type variables such as ArrayList, in contrast, contain a reference to the location that
         *  contains the value(s) relating to that variable.
         */
        ArrayList<String> wordList = new ArrayList<>();
        ArrayList<Integer> integers = new ArrayList<>();
        int integer = 1;
        integers.add(integer);

        ArrayList<Double> doubles = new ArrayList<>();
        double d = 4.2;
        doubles.add(d);

        // add two values to the word list
        wordList.add("First");
        wordList.add("Second");

        // retrieve the value from position 0 of the word list, and print it
        System.out.println(wordList.get(0));
        System.out.println("Number of values on the list: " + wordList.size());

        wordList.add("Simon");
        wordList.add("Samuel");
        wordList.add("Ann");
        wordList.add("Anna"); // add element at the end of the list 
        wordList.remove(1); //removes elemnet by index
        wordList.remove("Simon"); //can also pass a value to be removed, does not work for integer lists  
        integers.remove(Integer.valueOf(1)); // to remove an integer element do this 

        int index = 0;
        // Repeat for as long as the value of the variable `index`
        // is smaller than the size of the wordList list
        while (index < wordList.size()) {
            System.out.println(wordList.get(index));
            index = index + 1;
        }
        for(index = 0; index < wordList.size(); index++){
            System.out.println(wordList.get(index));

        }

        boolean found = wordList.contains("Ann"); //contains just checks if an element exists
        if (found) { //can replace found with wordList.contains("Ann") dont need to define variable 
            System.out.println("Ann was found");
        }
        integers.add(1);
        integers.add(2); 
        integers.add(3); 

        
        printSmallerThan(integers,2);

    }
    public static void ListExcersise(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> words = new ArrayList<>();
        while(true){
            String message = sc.nextLine();
            if (message.equals("")){
                break;
            }
            else{
                words.add(message);
            }
        }
        System.out.println(words.getLast());
    }
        
    public static void printSmallerThan(ArrayList<Integer> numbers, int threshold) {
        for (int number: numbers) {
            if (number < threshold) {
                System.out.println(number);
            }
        }   
    }
}

