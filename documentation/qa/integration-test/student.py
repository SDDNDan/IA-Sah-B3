from course import Course
class Student:
    def __init__(self,name):
        self.name=name
        self.courses=list()

    def addCourse(self,course):
        self.courses.append(course)

    def getCourseByIndex(self,courseIndex):
        return self.courses[courseIndex]

    def graduateAllCourse(self):
        for course in self.courses:
            course.graduateCourse()
            
    def checkIfCourseIsInList(self,courseName):
        for course in self.courses:
            if course.name==courseName:
                return True
        return False
    