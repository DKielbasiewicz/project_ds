"""
Grade object stores:
            grade: float
            student: Student id
            course: Course id
    
    *NOTE* Only grade attribute can be manipulated
"""

class Grade:
    def __init__(self, grade: float, student_id, course_id):
        self.__grade = grade        # float: value of the grade received
        self.__student = student_id    # Student: student object assigned to the grade
        self.__course_id = course_id      # Course: course object assigned to the grade
    
    @property
    def grade(self) -> float: # returns grade
        return self.__grade
    
    @grade.setter
    def grade(self, new_grade: float) -> None: # changes grade
        # check if new_grade takes on correct value
        if not (0 <= new_grade <= 10):
            raise ValueError('Grade has to be no smaller then 0 and no greater then 10') #incorrect grade value
        
        self.__grade = new_grade

    @property
    def course_id(self):
        return self.__course_id
    
    @property
    def identify_student(self) -> str: # returns student_id
        return self.__student
    
    def __eq__(self, other_grade): 
        if self.grade == other_grade.grade:
            return True
        return False
    
    def __lt__(self, other_grade): 
        if self.grade < other_grade.grade:
            return True
        return False
    
    def __gt__(self, other_grade): 
        if self.grade > other_grade.grade:
            return True
        return False
    
    def __contains__(self, other_grade): # in membership operator adjusted for student_id comparison
        if self.identify_student == other_grade.identify_student: #compare student_id number in order to check if the grades belong to the same student
            return True
        return False
    
    def __str__(self) -> str: #string representation of Grade obj
        return f"{self.__student} received {self.__grade} in {self.__course_id}" 