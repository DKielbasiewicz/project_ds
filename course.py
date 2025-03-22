"""
TODO: write me 


"""
from Student import Student
from Grade import Grade

class Course:
    def __init__(self, course_id: str, course_name: str, course_credits: int,  year: int, professor: None, students: list[Student], grades: list[Grade]):
        self.__course_id = course_id            # str: id code for the course NOTE should be unique?
        self.course_name = course_name          # str: name of the course
        self.course_credits = course_credits    # int: ec of the course
        self.year = year                        # int: year var *TODO specify how to use year var*
        self._professor = professor             # Professor: object Professor assigned to the course
        self.__students = students              # list[Student]: list containing all the students enrolled for the course ***NOTE Only unique values
        self.__final_grades = grades            # list[Grade]: list containing all the final grades  ***NOTE Only unique values
    
    def add_student(self, new_student: Student) -> None:
        if new_student.id in self.__students: # if student is enrolled for the course, i.e. is in __students
            raise Exception('') # TODO change error handling
        
        self.__students.append(new_student) # else, append Student obj to the list 
    
    def grade(self, picked_student: Student): # returns Grade obj
        # get a grade of chosen student
        for grade in self.__final_grades: # go over all grades
            if grade.identify_student == picked_student.id: # TODO optimize the comparison NOTE may not work in current state
                return grade # return student grade
        
        print(f"{picked_student.name} doesn't have any grades yet") # return Nonetype when picked_student has no grade assigned
        return 
    
    def add_grade(self, new_grade: Grade):
        # TODO This part can be optimized, not yet sure how
        # *NOTE* usage of in comparator may seem confusing here, for clarification look in grade.py for check membership
        if new_grade in self.__final_grades:                            # check if the student has a grade
            for final_grade_idx in range(len(self.__final_grades)):     # loop over all index values of final_grade list
                if new_grade in self.__final_grades[final_grade_idx]:   # check for the right grade
                    self.__final_grades[final_grade_idx] = new_grade    # change the grade to the new grade
            return
        self.__final_grades.append(new_grade) # append grade if no grade is present in the list
        
    def __str__(self) -> str: #string representation of Course obj
        return f"{self.course_name} (ID: {self.__course_id}), course taught by {self._professor.name}. \n[credits: {self.course_credits}, year: {self.year}, {len(self.__students)} students enlisted]"
    