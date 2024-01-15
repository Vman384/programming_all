public class Person { //this is called a constructor and sets initial values for the object
    private String name;
    private int age;
    private int height;
    private int weight;

    public Person(String name) {
        this(name, 0);
    }
    
    public Person(String name, int age) { //this is an alternative constructor and allows you to set the name as well as the age
        this.name = name; // having 2 constructors in the class is known as constructor overloading 
        this.age = age; // we cannot have 2 contructors with the same type though so public Person(String name, int weight) would not work
        this.weight = 0; // the first constructor has a lot of repeated code and we can make it better by having it call this contructor
        this.height = 0;
    }



    public void growOlder() {
        this.age = this.age + 1;
        //can also do 
        // this.growOlder(1)
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public int getHeight() {
        return this.height;
    }
    
    public void growOlder(int years) { //methods can also be overloaded like constructors 
        this.age = this.age + years;
    }

    public void setHeight(int newHeight) {
        this.height = newHeight;
    }

    public void setWeight(int newWeight) {
        this.weight = newWeight;
    }

    public double bodyMassIndex() {
        double heightPerHundred = this.height / 100.0;
        return this.weight / (heightPerHundred * heightPerHundred);
    }

    @Override
    public String toString() {
        return this.name + ", age " + this.age + " years";
    }

}   

