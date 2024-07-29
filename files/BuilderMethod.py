from abc import abstractmethod

class Course:

    def __init__(self, name, fee, batches):
        self.name = name
        self.fee = fee
        self.batches = batches

class ComplexCourse(Course):

    def __repr__(self):
        return f"This complex {self.name} has {self.fee} fee and {self.batches} batches"
    
class NormalCourse(Course):

    def __repr__(self):
        return f"This normal {self.name} has {self.fee} fee and {self.batches} batches"
    
math = ComplexCourse('Math', 8000, 2)
print(math)

literature = NormalCourse('Literature', 2000, 5)
print(literature)

