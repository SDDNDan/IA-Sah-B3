
'''
"AssembleActivateAssert/ArrangeActAssert"
a pattern for arranging and formatting code in UnitTest methods:
Each method should group these functional sections, separated by blank lines:
1.Arrange all necessary preconditions and inputs.
2.Act on the object or method under test.
3.Assert that the expected results have occurred.


Pattern:

def test_functionName():
    #ARRANGE
    a = assemble()
    #ACT
    var = a.functionName()
    #ASSERT
    assert var == expected_result
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        return "Hello, my name is " + self.name + "!"

    def reversedName(self):
        return self.name[::-1]

    def ageplus(self):
        return self.age + 1
