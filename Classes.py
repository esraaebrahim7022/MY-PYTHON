class Employee:

    def __init__(self,first,last,age,departement ,is_manager,salary):
        self.first = first
        self.last = last
        self.age = age
        self.departement = departement
        self.is_manager = is_manager
        self.salary = salary

    def bonus(self):
        if self.age== 40:
            self.salary +=500
            print("salary icreased to "+ str(self.salary))
        else:
            print("no bonus for you , salary still: "+ str(self.salary))

##############################################
class Student :

    def __init__(self,name,gpa,age,major,rating):
        self.name = name
        self.gpa = gpa
        self.age = age
        self.major = major
        self.rating = rating

    def is_excellent(self):
        if self.rating >= 3.5:
            return True
        else:
            return False