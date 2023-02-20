class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

#if the child doesn't have to add any properties or methods
# just add the pass keyword
class Employee(Person):
    pass

x = Employee("J", "Smith")
x.printname()

#if child class has it's own __init__() method
#then it overrides the parent's constructor
#to call parent's constructor explicitly call it
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

#instead of using the parent class name
#super() can be used
#when using super() self shouldn't be passed as a parameter
class Professor(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
    #super() can be used to call any parent method
    def printname(self):
        print("From child class")
        super().printname()

y = Student("K", "Nate")
y.printname()

z = Professor("D", "Ram")
z.printname()