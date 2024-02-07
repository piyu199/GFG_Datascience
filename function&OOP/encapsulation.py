class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grades=[]

    def add_grades(self,grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades)/len(self.grades)
    

s1=Student("Prajesh",25)
s1.add_grades(10)
s1.add_grades(50)
s1.add_grades(40)
s1.add_grades(60)
s1.add_grades(80)
print(s1.average_grade())
