from BabsonPerson import BabsonPerson
from Person import Person


class Professor(BabsonPerson):
    
    def __init__(self, name, course):
        BabsonPerson.__init(self,name)
        self.course = course

    def speak(self, utterance):
        newUtterance = 'In course ' + self.course + ' we say '
            return BabsonPerson.speak(self, NeUtterance + utterance)

    def lecture (self, topic):
        return self.speak('it is obvious that ' + topic)

def main():
    faculty = Professor('Zhi Li', 'MIS 3640')
    print(faculty.speak('Python is cool!'))
    print(faculty.lecture('Python is easy.'))
    