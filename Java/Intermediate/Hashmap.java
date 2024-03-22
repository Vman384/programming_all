import java.util.HashMap;

public class Hashmap {
    public static void main(String[] args) {
        HashMap<String, String> postalCodes = new HashMap<>();
        postalCodes.put("00710", "Helsinki");
        postalCodes.put("90014", "Oulu");
        postalCodes.put("33720", "Tampere");
        postalCodes.put("33014", "Tampere");

        System.out.println(postalCodes.get("00710")); // if item does not exist in hash map get returns null

        for (String keys : postalCodes.keySet()){
            System.out.println(keys);
        }

        for (String values: postalCodes.values()) {
            System.out.println(values);
        }

        //Java converts primitive variables to reference-types automatically as they are added to either a HashMap or 
        //an ArrayList. This automatic conversion to a reference-type variable is termed auto-boxing in Java


        /*
         * int = primitive varaible type
         * Integer = reference varaible type
         * double = primitive
         * Double = reference
         * char = primitive
         * Character = reference
         */
    }
}
