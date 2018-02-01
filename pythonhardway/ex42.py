## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Is-a
class Dog(Animal):

    def __init__(self, name):
        ## Has-a
        self.name = name

## Is-a
class Cat(Animal):

    def __init__(self, name):
        ## Has-a
        self.name = name

## Is-a
class Person(object):

    def __init__(self, name):
        ## Has-a
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## Is-a
        super(Employee, self).__init__(name)
        ## Has-a
        self.salary = salary

## Is-a
class Fish(object):
    pass

## Is-a
class Salmon(Fish):
    pass

## Is-a
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
