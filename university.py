"""
    TODO: write documentation    
    

"""
from Grade import Grade
from Course import Course
from Student import Student 
from Professor import Professor 

class University:
    def __init__(self, name: str, courses: list[Course], employees: list[Professor]):
        self.name = name
        self.available_courses = courses
        self.__employees = employees
        
    def avg_grade_course(self, chosen_course: Course):
        sum_ = 0
        final_grades = chosen_course.get_grades()
        print(final_grades)
        for final_grade in final_grades:
            sum_ += final_grade.grade
        return sum_/len(final_grades)
        
    def avg_grade_uni(self):
        all_courses = self.available_courses
        sum_ = 0
        for course in all_courses:
            sum_ += self.avg_grade_course(course)
        return sum_
        
    def __eq__(self, another_uni) -> bool:
        if self.avg_grade_uni() == another_uni.avg_grade_uni():
            return True
        return False
    
    #def __lt__(self, another_uni)
    
    def __str__(self):
        return f""