from unittest import TestCase
import testsdesign

class TestPerson(TestCase):

    # Test Initialization
    SUT = testsdesign.Person("Ceausescu", 20)                 

    def test_When_PersonExists_AndWeEditHisName_ShouldUpdate(self):
        
        # ARRANGE ACT ( Nu avem arrange deci acesta va fi la acelasi nivel cu ACT)
        TestPerson.SUT.name = "Test"
        
        # ASSERT
        assert TestPerson.SUT.name == "Test"

    def test_When_PersonExists_AndWeEditHisAge_ShouldUpdate(self):

        # ARRANGE ACT ( Nu avem arrange deci acesta va fi la acelasi nivel cu ACT)
        TestPerson.SUT.age = 25

        # ASSERT
        assert TestPerson.SUT.age == 25

    def test_When_PersonExists_AndWeCall_sayHello_ShoulRespond(self):

        # ARRANGE ACT (arrange facut la #Test initialization)
        result = TestPerson.SUT.sayHello()

        # ASSERT
        assert result == "Hello, my name is Ceausescu!"

    def test_When_PersonHasValidName_AndWannaGetHisNameReversed_ThenReversedNameShouldGetIt(self):

         # ARRANGE
         TestPerson.SUT.name = "Test"
        
         # ACT
         result = TestPerson.SUT.reversedName()
        
         # ASSERT
         assert result == "tseT"
     

    def test_When_PersonHasValidAge_AndWeCall_ageplus_WeShoulGetAgePlusPlus(self):

        # ARRANGE
        TestPerson.SUT.age = 23

        # ACT
        result = TestPerson.SUT.ageplus()

        # ASSERT
        assert result == 24