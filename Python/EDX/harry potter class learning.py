import random
#classes are used to make ibjects 

class Hat:
    #example of class variable (a variable that is only accessible in the class)
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    #a function that is used inside the class that doesnt have access to the object but is inside the class
    @classmethod
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))


Hat.sort('Harry')


class Student:
    #initialize variables and anything before the code
    def __init__(self, name, house):
        #these are also called attributes
        self.name = name
        self.house = house
    #used to return strings in from the class
    def __str__(self):
        return f"{self.name} from {self.house}"
    #a function that is used inside the class that doesnt have access to the object but is inside the class could be outside class and would not make a difference
    @classmethod
    def get(cls):
        name = input('Enter name: ')
        house = input('Enter house: ')
        return cls(name, house)
    #a function that does not need an object to be called
    @staticmethod
    def help():
        return 'this class is for a student and takes inputs of the house and the name of the student'
    # protpery is getter and gets some attributes
    @property
    def name(self):
        return self._name
    #setter sets some attribute
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing name')
        self._name=name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid House')
        self._house = house

#static method is something that is called in the class but does not have anything to do with the object, it could also just be a function outside the class
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing Name')
        self.name=name

#inheritance is being able to use the attributes of another class i.e inherite the attributes from another class
class Professor(Wizard):
    def __init__(self,name,subject): # lets us use the init from the wizard class, stops repeating code
        super().__init(name)
        self.subject=subject

class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts
    def __str__(self):
        return f'{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'
    #operator overloading and allows us to add objects together in a class
    def __add__(self, other):
        galleons=self.galleons+other.galleons
        sickles = self.sickles+other.sickles
        knuts = self.knuts+other.knuts
        return Vault(galleons,sickles,knuts)
potter = Vault(100,50,25)
print(potter)
weasly = Vault(25,50,100)
print(weasly)
total=potter+weasly
print(total)
def main():
    print(Student.help())
    student = Student.get()
    print(student)





if __name__ == "__main__":
    main()
