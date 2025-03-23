"""
Grade object stores:
            grade: float
            student: Student obj
            course: Course obj
    
    *NOTE* Only grade attribute can be manipulated
    
    TODO:
    Relationships:
        ...
"""

class Grade:
    def __init__(self, grade: float, student: Student, course: Course):
        self._grade = grade        # float: value of the grade received
        self._student = student    # Student: student object assigned to the grade
        self.course = course       # Course: course object assigned to the grade
    
    @property
    def grade(self) -> float: # returns grade
        return self._grade
    
    @grade.setter
    def grade(self, new_grade: float) -> None: # changes grade
        # check if new_grade takes on correct value
        if not (0 <= new_grade <= 10):
            raise ValueError('Grade has to be no smaller then 0 and no greater then 10') #incorrect grade value
        
        self._grade = new_grade
    
    @property
    def identify_student(self) -> str: # returns student_id from the Student obj
        return self._student.id
    
    def __eq__(self, other_grade): #custom == operator, checks if the numeric value of the Grade object is matching
        if self.grade == other_grade.grade:
            return True
        return False
    
    def __contains__(self, other_grade): # in membership operator adjusted for student_id comparison
        if self.identify_student == other_grade.identify_student: #compare student_id number in order to check if the grades belong to the same student
            return True
        return False
    
    def __str__(self) -> str: #string representation of Grade obj
        return f"{self._student.name} received {self._grade} in {self.course.name}" 
        


