class Course:
    def __init__(self,name):
        self.name=name
        self.graduated=False

    def graduateCourse(self):
        self.graduated=True

    def getGraduateStatus(self):
        return self.graduated    
    
    def getCourseName(self):
        return self.name