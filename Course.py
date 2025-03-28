"""
Course object stores:
            course_id: str | string used to represent individual courses
            course_name: str | name of the course
            course_credits: int | amount of ec assigned to the course
            year: int 
            professor: Professor | Professor obj associated with the course
            students: list[Student] | list of Student objects that are enlisted for the course
            final_grades: list[Grade] | list of Grade objects that are associated with the course and enlisted students

Course class depends on 3 classes, that is: Student class, Professor class and Grade class
"""
from Student import Student
from Professor import Professor
from Grade import Grade

class Course:
    def __init__(self, course_id: str, course_name: str, course_credits: int,  year: int, professor: Professor, students: list[Student], grades: list[Grade]):
        self.__course_id = course_id            # str: id code for the course 
        self.__course_name = course_name          # str: name of the course
        self.__course_credits = course_credits    # int: ec of the course
        self._year = year                        # int: year var
        self._professor = professor             # Professor: object Professor assigned to the course
        self.__students = students              # list[Student]: list containing all the students enrolled for the course ***NOTE Only unique values
        self.__final_grades = grades            # list[Grade]: list containing all the final grades  ***NOTE Only unique values
    
    @property
    def get_grades(self): #getter for list of Grades
        return self.__final_grades
    @property
    def name(self):
        return self.__course_name
    @property
    def course_id(self):
        return self.__course_id
    
    @property
    def professor(self):
        return self._professor
    
    @property
    def course_credits(self):
        return self.__course_credits
    
    @property
    def year(self):
        return self._year
    
    @property
    def all_students(self):
        return self.__students
    
    def add_student(self, new_student: Student) -> None:
        if new_student in self.__students: # if student is enrolled for the course, i.e. is in __students
            raise Exception('Student already enlisted')
        
        self.__students.append(new_student) # else, append Student obj to the list 
    
    def grade(self, picked_student: Student): # returns Grade obj
        # get a grade of chosen student
        for grade in self.__final_grades: # go over all grades
            if grade.identify_student == picked_student.id:
                return grade # return student grade
        
        print(f"{picked_student.name} doesn't have any grades yet") # return Nonetype when picked_student has no grade assigned
        return 
    
    def add_grade(self, new_grade: Grade):
        # *NOTE* usage of in comparator may seem confusing here, for clarification look in grade.py for check membership    
        for id_g, final_grade in enumerate(self.__final_grades):     # loop over all values of final_grade list
            if new_grade in final_grade:   # check for the right grade
                self.__final_grades[id_g] = new_grade    # change the old grade to the new grade
                return
    
        self.__final_grades.append(new_grade) # append grade if no grade is present in the list
    
    def __str__(self) -> str: #string representation of Course obj
        return f"{self.__course_name} (ID: {self.__course_id}), course taught by {self._professor.name}. \n[credits: {self.__course_credits}, year: {self._year}, {len(self.__students)} students enlisted]"
