public class Objects {
    public static class Student { /**The Student class is an inner class of the Objects class. 
        In your main method, which is a static method, you are trying to create an instance of 
        the non-static inner class Student. To fix this, you should declare the Student class as static:
        would not need static if it was the main class
        */

        /**
         * The static modifier indicates that the method in question does not belong to an object 
         * and thus cannot be used to access any variables that belong to objects.Going forward, 
         * our methods will not include the static keyword if they're used to process information 
         * about objects created from a given class. If a method receives as parameters all the 
         * variables whose values ​​it uses, it can have a static modifier.
         */
        private int credits; //this is an instance variable, private means its hidden in the class (encapsulation)
    
        public Student() {
            this.credits = 0;
        }
    
        public void play() { //this is called a method and runs code for the class, has to public
            // so it can be run from outside the class and since it returns nothing its void 
            this.credits = this.credits - 8;
        }
    }

    public static class Person { //this is called a constructor and sets initial values for the object
        private String name;
        private int age;
        private int height;
        private int weight;
    
        public Person(String initialName) {
            this.age = 0; //sets the age to 0 for "this" object, which means for a new object the age is set to 0
            this.name = initialName;
            this.height = 0;
            this.weight = 0;
        }
        
        public Person(String name, int age) { //this is an alternative constructor and allows you to set the name as well as the age
            this.name = name; // having 2 constructors in the class is known as constructor overloading 
            this.age = age; // we cannot have 2 contructors with the same type though so public Person(String name, int weight) would not work
            this.weight = 0; // the first constructor has a lot of repeated code and we can see how to make it better in the people class
            this.height = 0;
        }

        public String toString() { //by calling this method toString it is automatically called when printing the class
            return this.name + ", age " + this.returnAge() /*call internal method this way */ + " years " + this.height + "cms";
        }

        public int returnAge(){
            return this.age;
        }

        public boolean isOfLegalAge(){
            return (this.age >= 18);
        }

        
        public void setHeight(int newHeight) { //these are called setters as they are setting an instance variable
            this.height = newHeight;
        }

        public void setWeight(int newWeight) {
            this.weight = newWeight;
        }

        public double bodyMassIndex() {
            double heigthPerHundred = this.height / 100.0;
            return this.weight / (heigthPerHundred * heigthPerHundred);
        }

    }
   
    
    public static void main(String[] args) {
        Student matt = new Student();
        matt.credits = 5;
        matt.play();

        Person ada = new Person("Ada");
        System.out.println(ada); // to use the printPerson method we call like this
        ada.height = 100;
        System.out.println(ada); // to use the printPerson method we call like this

        
    }
}


