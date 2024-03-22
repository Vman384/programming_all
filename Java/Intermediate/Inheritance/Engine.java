package Inheritance;

public class Engine extends Part { 
/* we use inheritance to stop overlapping code as engine is a special type of part
engine will also get to use all the methods that part has and the attributes as well 
part is the superclass and engine is a subclass
*/
    private String engineType;

    public Engine(String engineType, String identifier, String manufacturer, String description) {
        super(identifier, manufacturer, description); // this calls public Part(String identifier, String manufacturer, String description)
        this.engineType = engineType;
    }
/*
 * If a method or variable has the access modifier private, 
 * it is visible only to the internal methods of that class. Subclasses will not see it,
 * If we want to define some variables or methods that are visible to the subclasses but invisible to everything else, 
 * we can use the access modifier protected to achieve this.
 */
    public String getEngineType() {
        return engineType;
    }

    public void printIdentifier(){
        // System.out.println(identifier); //cannot use identifier like this as it uses private in the sub class
        System.out.println(super.getIdentifier());
    }

    public static void main(String[] args) {
        Engine vw = new Engine("combustion", "hz", "volkswagen", "VW GOLF 1L 86-91");
        vw.printIdentifier();
    }
}
