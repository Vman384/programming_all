import java.util.ArrayList;
import java.util.HashMap;

public class Equals {
    public static void main(String[] args) {
        Book bookObject = new Book("Book object", 2000, "...");
        Book anotherBookObject = bookObject;

        if (bookObject.equals(anotherBookObject)) { //this is just checking the reference of bookObject
            System.out.println("The books are the same");
        } else {
            System.out.println("The books aren't the same");
        }

        // we now create an object with the same content that's nonetheless its own object
        anotherBookObject = new Book("Book object", 2000, "...");

        if (bookObject.equals(anotherBookObject)) { //this doesnt work as we dont have a custom implementation for the 
            //equals method inside our class
            System.out.println("The books are the same");
        } else {
            System.out.println("The books aren't the same");
        }

        HashMap<Book, String> borrowers = new HashMap<>();

        bookObject = new Book("Book Object", 2000, "...");
        borrowers.put(bookObject, "Pekka");
        borrowers.put(new Book("Test Driven Development", 1999, "..."), "Arto");
        // hash maps hash based on the memory reference of the object and not the object value itself thats why checking 
        // the same object below returns null but
        System.out.println(borrowers.get(bookObject));
        System.out.println(borrowers.get(new Book("Book Object", 2000, "...")));
        System.out.println(borrowers.get(new Book("Test Driven Development", 1999, "...")));

        HashMap<String, ArrayList<String>> phoneNumbers = new HashMap<>();

        // let's initially attatch an empty list to the name Pekka
        phoneNumbers.put("Pekka", new ArrayList<>());

        // and add a phone number to the list at Pekka
        phoneNumbers.get("Pekka").add("040-12348765");
        // and let's add another phone number
        phoneNumbers.get("Pekka").add("09-111333");

        System.out.println("Pekka's numbers: " + phoneNumbers.get("Pekka"));
    }
        
  
    
}
