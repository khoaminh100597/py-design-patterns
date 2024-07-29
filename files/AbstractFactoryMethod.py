import random

class Course_AT_GFG():
    """
        GeeksForGeeks portal for courses
    """

    def __init__(self, course_factory=None):
        self.course_factory = course_factory

    def show_course(self):
        """
            Creates and show courses using the abstract factory
        """
        course = self.course_factory
        print(f'We have a course named {course}')
        print(f'Its price is {course.Fee()}')

class DSA:
    
    """Class for Data Structure and Algorithms"""
    def Fee(self):
        return 1000
    
    def __str__(self) -> str:
        return "DSA"
    
class STL:
    
    """Class for Standard Template Library"""
    def Fee(self):
        return 8000
    
    def __str__(self) -> str:
        return "STL"

class SDE:
    
    """Class for Software Development Engineer"""
    def Fee(self):
        return 200
    
    def __str__(self) -> str:
        return "SDE"

def random_course():
    """A random class for choosing the course"""

    return random.choice([DSA, SDE, STL])()

for i in range(5):
    course = Course_AT_GFG(random_course())
    course.show_course()