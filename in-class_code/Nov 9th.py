from BabsonPerson import BabsonPerson
from Person import Person

class Student(BabsonPerson):
    pass
class Person(object):
    def __init__(self,name):
        BabsonPerson.__init__(self,name)
        self.year = ClassYear

    def getClass(self):
        return self.year

    def speak(self,utterance):
        return BabsonPerson.speak()
        
class Grad(Student):
    
    def speak(self, utterance):
        return BabsonPerson.speak(self, "How do you do, fellow kids " + utternace)

s1 = UG
s2 = UG
s3 = UG('Gianca Devina', 2019)
s4 = Grad('Matt Damon')

studentLIst = [s1, s2, s3, s4]

print(s1)

print(s1.getClass())

for studnet in studentList:
    print(student.speak('Today is cold.'))

print(isStudent(s1))

#p1 = Person('Taylor Swift')
# print(isStudent(p1))

if __name__ = '__main__':
    main()