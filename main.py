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
    self.__available_courses = Database.load_course()
    self.__employees = Database.load_professors()
    self.__buildings = []
    self.__students = Database.load_students()
        
    """courses_temp = self.__available_courses
    courses_proper = []
    
    for course_temp in courses_temp:
      
      grades_temp = list(zip(course_temp[-2],course_temp[-1]))
      students_temp = course_temp[-3]
      prof_temp = course_temp[-4]
      print(course_temp)
      students_proper = []
      grades_proper = []
      
      for student in self.__students:
        if student.id in students_temp:
          students_proper.append(student)

          for grade in grades_temp:
            if grade[1] == student.id:
              grades_proper.append((grade[0],student))
              
          
      for prof in self.__employees:
        if prof.id == prof_temp:
          prof_temp = prof
          
      course_proper = Course(course_temp[0],course_temp[1],course_temp[2],course_temp[3], prof_temp, students_proper, [])
      
      for grade_proper in grades_proper:
        course_proper.add_grade(grade_proper[0], grade_proper[1], course_proper)
        
    self.__available_courses = courses_proper"""
          
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

  def add_professor(self, prof_name, prof_surname, prof_age, prof_gender):
    # add prof ID number NOTE essential for the application
    if not self.__employees:
      prof_id = 1
    else:
      prof_id = self.__employees[-1].id+1
    
    ...
  
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
    raise ValueError(" This Course already exist in our database") 
  
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
  
  def __str__(self):
      return f"{self.__name} is great"

    
class UniTrackApp:
  def __init__(self):
    self.__uniTrack = University()

  def help(self):
    list_of_commands = """List of commands:\n
    [1] - Add student
    [2] 
    [3] 
    [4] 
    [5] 
    [6] 
    [7] 
    [8] - Show University statistics
    [9] - Exit the application
    """
    print(list_of_commands)

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
  
  def run_statistics(self):
    what_stat = """What would you like to display?
    [1] Entire University statistics
    [2] Individual course statistics
    """
    while True:
      print(what_stat)
      command_stat = input("Enter command: ")
      
      if command_stat == '1' or command_stat == '2':
        break
      else:
        print("Invalid command")
        
    if command_stat == '1':
      UniversityStatistics.avg_grade_uni(self.__uniTrack)
      return 
    # second case, aka. pick a course and print its stat
    all_courses = self.__uniTrack.available_courses
    print('Which course would you like to evaluate?')
    for id_course,course in enumerate(all_courses):
      print(f'[{id_course+1}] {course.name} ({course.course_id})')
    
    command_course = -1
    while not command_course in range(len(all_courses)):
      command_course = int(input("Enter command: "))-1
      
    UniversityStatistics.avg_grade_course(all_courses[command_course])
    return
    
  def run(self):
    while True:
      self.help()
      command = input("Enter command: ")
      if command == "1":
        print(self.add_student())
      if command == '8':
        self.run_statistics()
        
      if command == "9":
        print("Thank you for using UniTrack!")
        break
      else:
        print("Invalid command")

if __name__ == "__main__":
  app = UniTrackApp()
  app.run()