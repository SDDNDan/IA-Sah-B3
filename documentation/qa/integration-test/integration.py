import unittest
from student import Student 
from course import Course
class IntegrationTesting(unittest.TestCase):
    def setUp(self):
        self.student=Student("John")
        self.course1=Course("ML")
        self.course2=Course("TW")
        self.course3=Course("IA")

    def testAddingCourse(self):
        self.student.addCourse(self.course1)
        self.student.addCourse(self.course2)
        self.student.addCourse(self.course3)
        
        self.assertEqual(self.student.checkIfCourseIsInList("ML"),True,"Error in adding courses")

    def testGraduatingCourses(self):
        self.student.graduateAllCourse()
        expected=True
        for course in self.student.courses:
            if  course.getGraduateStatus==False:
                check=False
        self.assertEqual(expected,True,"Error in graduating all courses")
if __name__ == '__main__':
    unittest.main()
    
