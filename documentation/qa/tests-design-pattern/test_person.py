from unittest import TestCase
import testsdesign

class TestPerson(TestCase):

    # Test Initialize
    SUT = testsdesign.Person("Ceausescu", 20)                 

    def When_PersonExists_AndWeEditHisName_HisName_ShouldUpdate(self):
        
        # ARRANGE ACT ( Nu avem arrange deci acesta va fi la acelasi nivel cu ACT)
        TestPerson.SUT.name = "Test"
        
        # ASSERT
        assert TestPerson.SUT.name == "Test"

     def When_PersonHasValidName_AndWannaGetHisNameReversed_ThenReversedNameShouldGetIt(self):
        
         # ARRANGE 
         TestPerson.SUT.name = "Test"
        
         # ACT
         result = TestPerson.SUT.reversedName()
        
         # ASSERT
         assert TestPerson.SUT.name == "tseT"
     
    
    
     def test_sayHello(self):
        raspuns1 = TestPerson.SUT.sayHello()           #Act
        assert raspuns1 == "Hello, my name is Ceausescu!"  #Assert
        assert raspuns1 != "Dragi tovarasi"                #Assert

    def test_ageplus(self):
        raspuns3 = TestPerson.student.ageplus()
        assert raspuns3 == 21
        assert raspuns3 != 20
