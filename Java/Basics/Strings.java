public class Strings {
    public static void main(String[] args) {
        String text = "course";
        String anotherText = "horse";

        if (text.equals(anotherText)) {
            System.out.println("The two texts are equal!");
        } else {
            System.out.println("The two texts are not equal!");
        }

        System.out.println("Make sure the text is not 'cake'"); 
        if (!(text.equals("cake"))) {  // true if the condition text.equals("cake") is false
            System.out.println("it wasn't!");
        } else {
            System.out.println("it was!");
        }

        text = "first second third fourth";
        String[] pieces = text.split(" "); //this splits the string based on the regex
        System.out.println(pieces[0]);
        System.out.println(pieces[1]);
        System.out.println(pieces[2]);
        System.out.println(pieces[3]);

        System.out.println();

        for (int i = 0; i < pieces.length; i++) {
            System.out.println(pieces[i]);
        }
    }   
}
