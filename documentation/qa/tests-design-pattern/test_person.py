from unittest import TestCase
import testsdesign

class TestPerson(TestCase):

    student = testsdesign.Person("Ceausescu", 20)                 #Arrange

    def test_init(self):
        assert TestPerson.student.name == "Ceausescu"
        assert TestPerson.student.age == 20

    def test_sayHello(self):
        raspuns1 = TestPerson.student.sayHello()           #Act
        assert raspuns1 == "Hello, my name is Ceausescu!"  #Assert
        assert raspuns1 != "Dragi tovarasi"                #Assert

    def test_reversedName(self):
        raspuns2 = TestPerson.student.reversedName()       #Act
        assert raspuns2 == "ucsesuaeC"                     #Assert
        assert raspuns2 != "Ceausescu"                     #Assert

    def test_ageplus(self):
        raspuns3 = TestPerson.student.ageplus()
        assert raspuns3 == 21
        assert raspuns3 != 20
