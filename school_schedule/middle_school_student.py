from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def transportation_summary(self):
        has_message = "has" if self.gets_transportation else "doesn't have"
        return f"{self.name} {has_message} transportation"
    
    def summary(self):
        student_summary = super().summary()
        gets_transportation_message = self.transportation_summary()
    
        return "\n".join((student_summary, gets_transportation_message))
        
# add MiddleSchoolStudent here
"""We would like to derive a MiddleSchoolStudent child class. MiddleSchoolStudent will have all the attributes 
and behaviors of Student, but it will also:

Track whether the student receives school transportation using the boolean attribute gets_transportation 
(can be set in the constructor, defaults to False)
Update the summary method to include information about the student's transportation status
In the main.py, create an instance of a MiddleSchoolStudent and add it to the student list. 
Make sure its summary gets printed out.
Include tests for the additional functionality
There is one test provided (currently commented out)
Uncomment the test and implement the MiddleSchoolStudent class so that it passes
Implement additional tests for the MiddleSchoolStudent class (review the High School Student class for ideas)
"""