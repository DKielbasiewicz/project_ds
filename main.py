"""
General structure of the UniTrack application
"""
from Grade import Grade
from Course import Course
from Student import Student 
from Professor import Professor 

class University:
    def __init__(self):
        self.name = "UniTrack University"
        self.__available_courses = []
        self.__employees = []
        
    def avg_grade_course(self, chosen_course: Course):
        sum_ = 0
        final_grades = chosen_course.get_grades
        for final_grade in final_grades:
            sum_ += final_grade.grade
        return sum_/len(final_grades)
        
    def avg_grade_uni(self):
        all_courses = self.available_courses
        sum_ = 0
        for course in all_courses:
            sum_ += self.avg_grade_course(course)
            
        return sum_/len(all_courses)
        
    def __eq__(self, another_uni) -> bool:
        if self.avg_grade_uni() == another_uni.avg_grade_uni():
            return True
        return False
    
    #def __lt__(self, another_uni)
    
    def __str__(self):
        return f""

class UniTrackApp:
  def __init__(self):
    self.__uniTrack = University()

  def help(self):
    print("List of commands:")
    print("[1] - Add course")

  def add_course(self, name, ec):
    name = input("Enter name of the course: ")
    ec = input("Number of credits: ")
    pass

  def run(self):
    while True:
      self.help()
      print("\n")
      command = input("Enter command: ")
      if command == "1":
        self.help()
      else:
        print("Invalid command")