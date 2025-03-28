"""
General structure of the UniTrack application
"""
from Grade import Grade
from Course import Course
from Student import Student 
from Professor import Professor 
from Database import Database
from Statistics import UniversityStatistics
from Building import Building

class University():
  def __init__(self):
    self.__name = "UniTrack University"
    self.__available_courses = []
    self.__employees = []  
    self.__buildings = []
    self.__students = Database.load_students()
      
  @property
  def available_courses(self):
    return self.__available_courses

  @property
  def employees(self):
    return self.__employees
  
  @property
  def name(self):
    return self.__name
  
  @property
  def buildings(self):
    return self.__buildings

  def add_student(self, student_name: str, student_surname: str, student_age: int, student_gender: str,):
    # making Student object of the given variables
    new_student = Student(student_name, student_surname, student_age, student_gender)
    # adding student to __students list
    self.__students.append(new_student)
    # saving student information to database file "students.csv"
    Database.save_student(new_student)
  
  def add_course(self, new_course: Course):
    if not new_course in self.__available_courses:
      self.__available_courses.append(new_course)
      return
    raise ValueError(" How to handle adding the same course? ") # <--- !!!
  
  def add_building(self, new_building: Building):
    if not new_building in self.__buildings:
      self.__buildings.append(new_building)
      return
    raise ValueError(" Two buildings at the same address won't work. ")
    
  def add_employee(self, new_employee: Professor): #adds an employee, i.e. an Professor obj to the self.__employees list
    if not new_employee in self.__employees: # check if the obj is already in the list
      self.__employee.append(new_employee) # if not append
      return 
    
    raise ValueError("This person is already employed!") # else raise errno
    
  # NOTE Thou shalt decide the fate of all Comparison Operators
  #def __eq__(self, another_uni) -> bool:
  #    if self.avg_grade_uni() == another_uni.avg_grade_uni():
  #        return True
  #    return False
  #def __lt__(self, another_uni)
  
  def __str__(self):
      return f"{self.__name} is great, not sure what to include here, open for ideas" # <----- TODO

    
class UniTrackApp:
  def __init__(self):
    self.__uniTrack = University()

  def help(self):
    print("List of commands:")
    print("[1] - Add student")
    print("[9] - Exit the application")
    print("")

  def add_student(self):
    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    while True:
      try:
        age = int(input("Enter student age: "))
        break
      except Exception:
         print("Invalid age: Age has to be a natural number")
    while True:
      gender = input("Enter student gender (M/F): ")
      try:
        # we try to add student if it fails then it's gender string problem
        # we give feedback and redo the loop
        self.__uniTrack.add_student(name, surname, age, gender)
        break
      except NameError as invalid_gender:
        print(invalid_gender)
    return "Student added successfully to the University\n"
        
  def run(self):
    while True:
      self.help()
      command = input("Enter command: ")
      if command == "1":
        print(self.add_student())
      if command == "9":
        print("Thank you for using UniTrack!")
        break
      else:
        print("Invalid command")

if __name__ == "__main__":
  app = UniTrackApp()
  app.run()