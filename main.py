"""
General structure of the UniTrack application
"""
from Grade import Grade
from Course import Course
from Student import Student 
from Professor import Professor 
from GeneralWorker import GeneralWorker
from Database import Database
from Statistics import UniversityStatistics
from Building import Building

class University():
  def __init__(self):
    self.__name = "UniTrack University"
    self.__available_courses = Database.load_courses()
    #self.__available_courses = [Course('SOW', 'Prog', 3,1, Professor('Alber', "Smart", 41, 'm',1), [Student('Mary', "W", 12, 'f', 222)],[])]   #NOTE debug 
    #employees is a dictionary
    #"Professors" : list[Professor]
    #"General Workers" : list[GeneralWorker]
    self.__employees = Database.load_employees()
    self.__buildings = []
    self.__students = Database.load_students()
          
  @property
  def available_courses(self):
    return self.__available_courses

  @property
  def get_students(self):
    return self.__students
    
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
    new_professor = Professor(prof_name, prof_surname, prof_age, prof_gender)
    self.__employees["Professors"].append(new_professor)
    Database.save_employee(new_professor)

  def add_general_worker(self, worker_name: str, worker_surname: str, worker_age: int, worker_gender: str, worker_job: str, worker_salary: int):
    new_general_worker = GeneralWorker(worker_name, worker_surname, worker_age, worker_gender, worker_job, worker_salary)
    self.__employees["General Workers"].append(new_general_worker)
    Database.save_employee(new_general_worker)
  
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
      
  def __str__(self):
      return f"{self.__name} is great!"

    
class UniTrackApp:
  def __init__(self):
    self.__uniTrack = University()

  def help(self):
    list_of_commands = """List of commands:\n
    [1] - Add Student to the database
    [2] - Add Professor
    [3] - Add General Worker
    [4] - Add Course
    [5] - Enlist students to course
    [6] 
    [7] - Add Grades 
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
  
  def add_professor(self):
    name = input("Enter professor name: ")
    surname = input("Enter professor surname: ")
    while True:
      try:
        age = int(input("Enter professor age: "))
        break
      except Exception:
        print("Invalid age: Age has to be a natural number")
    while True:
      gender = input("Enter professor gender (M/F): ")
      try:
        # we try to add professor if it fails then it's gender string problem
        # we give feedback and redo the loop
        self.__uniTrack.add_professor(name, surname, age, gender)
        break
      except NameError as invalid_gender:
        print(invalid_gender)
    return "Professor added successfully to the University\n"
  
  def add_general_worker(self):
    name = input("Enter worker name: ")
    surname = input("Enter worker surname: ")
    while True:
      try:
        age = int(input("Enter worker age: "))
        break
      except Exception:
        print("Invalid age: Age has to be a natural number")
    from Person import Person
    while True:
      gender = input("Enter worker gender (M/F): ")
      try:
        # we try to add professor if it fails then it's gender string problem
        # we give feedback and redo the loop
        Person(name, surname, age, gender)
      except NameError as invalid_gender:
        print(invalid_gender)
      else:
        break
    while True:
      job = input("Enter worker job title: ")
      try:
        if job.lower() == "professor":
          raise NameError
      except NameError:
        print("This person cannot be a professor")
      else:
        break
    while True:
      try:
        salary = int(input("Enter worker salary (positive integer): "))
        if salary < 0:
          raise Exception
        break
      except Exception:
        print("Worker salary has to be positive integer")
    self.__uniTrack.add_general_worker(name, surname, age, gender, job, salary)
    return "Employee added succesfully to the University"

  def add_course(self):
    professors = self.__uniTrack.employees["Professors"]
    if len(professors) == 0:
      print("There are no professors in our database!\nFirst add professor to the university")
      return 
    
    print("Adding new course")
    
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    
    while True:
      try:
        course_credits = int(input("Enter course credits: "))
        if course_credits < 1:
          raise ValueError
        break
      except ValueError:
        print("Invalid input, EC's must be greater then zero")
    
    while True:
      try:
        course_year = int(input("Enter intended year of the course: "))
        if course_year < 1:
          raise ValueError
        break
      except ValueError:
        print("Invalid input, year has to be greater then 0")
        
    print("Select a professor for this course:")
    for id_prof, prof in enumerate(professors):
        print(f"[{id_prof + 1}] {prof.name} {prof.surname}")
    
    selected_prof = False
    while not selected_prof:
      try:
        chosen_prof = int(input("Enter professor number from the list: "))-1
        if chosen_prof not in range(len(professors)):
          raise ValueError
        selected_prof = professors[chosen_prof]
        
      except ValueError:
        print("Invalid input, pick a professor from the list")
    
    new_course = Course(course_id,course_name,course_credits,course_year,selected_prof,[],[])
    
    try:
        self.__uniTrack.add_course(new_course)
        print(f"Course '{course_name}' added successfully.")
        print("Now you may enlist students to the course")
    except Exception as e:
        print(e)

  def add_students_to_course(self):
    students = self.__uniTrack.get_students
    courses = self.__uniTrack.available_courses
    if len(students) == 0:
      return "There are no students in our database\nAdd students to the database"
    if len(courses) == 0:
      return "There are no courses in our database\nAdd courses to the database"
    
    print("Pick a course:")
    for id_course, course in enumerate(courses):
      print(f"[{id_course+1}] {course.course_id}")
    
    while True:
      try:
        picked_course_id = int(input("Enter command: "))-1
        if picked_course_id not in range(len(courses)):
          raise ValueError
        break
      except ValueError:
        print("Invalid input, pick a course from the list")
        
    picked_course = courses[picked_course_id]
    
    print("Pick students from the list (enter individual reference numbers)")
    for id_student, student in enumerate(students):
      print(f"[{id_student+1}] {student.name} {student.id}")
    
    picked_students = []
    while True:
      pick = input("To quit enter q\nTo add more students, enter the number: ")
      if pick == 'q':
        break
      try:
        pick = int(pick)-1
        if pick not in range(len(students)):
          raise ValueError
        picked_students.append(students[pick])
      except ValueError:
        print()

    successful_enlistments = 0
    for chosen_one in picked_students:
      try:
        picked_course.add_student(chosen_one)
        successful_enlistments += 1
      except Exception as e:
        print(e)
        
    return f"Successfully added {successful_enlistments} students!"

  def add_grade(self):
    print("Pick to what course you want to add the grade")
    all_courses = self.__uniTrack.available_courses
    if len(all_courses) == 0:
      print('There are no courses in our database')
      return
    for id_course, course in enumerate(all_courses):
      print(f"[{id_course+1}] {course.name}")
    
    command_course = -1
    while command_course not in range(len(all_courses)):
      command_course = input("Enter command: ")
      if not command_course.isdigit():
        print("Please select one of the courses")
        command_course = -1
      else:
        command_course = int(command_course)-1
    
    picked_course = all_courses[command_course]
    students_from_course = picked_course.all_students
    
    if len(students_from_course) == 0:
      print("There are no students enlisted for the course\nFirst add students to the course")
      return 
    
    while True:
      print("Pick a student to assign a grade\nPress q to quite")
      for id_students, student in enumerate(students_from_course):
        print(f"[{id_students+1}] {student.name} student id:{student.id}")
      
      command_student = input("Enter command: ")
      if not command_student.isdigit():
        if command_student == 'q':
          return
        
        print('Invalid input')
        continue
      
      else: 
        command_student = int(command_student)-1
        
      if command_student in range(len(students_from_course)):
        new_grade_val = input("Please enter a grade: ")
        try:
          new_grade_val = float(new_grade_val)
          
        except ValueError:
          print("Invalid grade")
          continue
      new_grade = Grade(new_grade_val, students_from_course[command_student].id, picked_course.course_id)
      self.__uniTrack.available_courses[command_course].add_grade(new_grade)

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
    while command_course not in range(len(all_courses)):
      command_course = input("Enter command: ")
      if not command_course.isdigit():
        print("Please select one of the courses")
        command_course = -1
      else:
        command_course = int(command_course)-1
      
    UniversityStatistics.avg_grade_course(all_courses[command_course])
    return
    
  def run(self):
    while True:
      self.help()
      command = input("Enter command: ")
      if command == "1":
        print(self.add_student())
      if command == "2":
        print(self.add_professor())
      if command == "3":
        print(self.add_general_worker())
      if command == '4':
        self.add_course()
      if command == '5':
        print(self.add_students_to_course())
      if command == '7':
        self.add_grade()
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