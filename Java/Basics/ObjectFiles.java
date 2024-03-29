import java.util.ArrayList;


public class ObjectFiles {
    public class AmusementParkRide {
        private String name;
        private int minimumHeight;
        private int visitors;
        private ArrayList<Person> riding;

        public AmusementParkRide(String name, int minimumHeight) {
            this.name = name;
            this.minimumHeight = minimumHeight;
            this.visitors = 0;
            this.riding = new ArrayList<>();
        }

        public void removeEveryoneOnRide() {
            this.riding.clear();
        }

        public boolean isAllowedOn(Person person) {
            if (person.getHeight() < this.minimumHeight) {
                return false;
            }

            this.visitors++;
            this.riding.add(person);
            return true;
        }

        public String toString() {

            String printOutput = this.name + ", minimum height requirement: " + this.minimumHeight +
                ", visitors: " + this.visitors + "\n";
    
            if (riding.isEmpty()) {
                return printOutput + "no one is on the ride.";
            }
    
            // we form a string from the people on the list
            String peopleOnRide = "";
    
            for (Person person: riding) {
                peopleOnRide = peopleOnRide + person.getName() + "\n";
            }
    
            return printOutput + "\n" +
                "on the ride:\n" + peopleOnRide;
        }

        public double averageHeightOfPeopleOnRide() {
            if (riding.isEmpty()) {
                return -1;
            }
    
            int sumOfHeights = 0;
            for (Person per: riding) {
                sumOfHeights += per.getHeight();
            }
    
            return 1.0 * sumOfHeights / riding.size();
        }

        public Person getTallest() {
            // return a null reference if there's no one on the ride
            if (this.riding.isEmpty()) {
                return null;
            }
        
            // create an object reference for the object to be returned
            // its first value is the first object on the list
            Person returnObject = this.riding.get(0);
        
            // go through the list
            for (Person prs: this.riding) {
                // compare each object on the list
                // to the returnObject -- we compare heights
                // since we're searching for the tallest,
        
                if (returnObject.getHeight() < prs.getHeight()) {
                    // if we find a taller person in the comparison,
                    // we assign it as the value of the returnObject
                    returnObject = prs;
                }
            }
        
            // finally, the object reference describing the
            // return object is returned
            return returnObject;
        }
    
    }
}
