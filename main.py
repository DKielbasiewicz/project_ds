"""
General structure of the UniTrack application
"""
from Grade import Grade
from Course import Course
from Student import Student 
from Professor import Professor 
from Statistics import UniversityStatistics

class University(UniversityStatistics):
  def __init__(self):
    self.__name = "UniTrack University"
    self.__available_courses = []
    self.__employees = []  
      
  @property
  def available_courses(self):
    return self.__available_courses

  @property
  def employees(self):
    return self.__employees
  
  @property
  def name(self):
    return self.__name
  
  def add_course(self, new_course: Course):
    if not new_course in self.__available_courses:
      self.__available_courses.append(new_course)
      return
    raise ValueError(" How to handle adding the same course? ") # <--- !!!
    
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