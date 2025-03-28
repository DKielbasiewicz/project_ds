import csv
from Student import Student
from Professor import Professor
from GeneralWorker import GeneralWorker
from Building import Building
from Course import Course
class Database:
  __students_file = "students.csv"
  __courses_file = "courses.csv"
  __employees_file = "employees.csv"
  __buildings_file = "buildings.csv"
  __encoding_style = "utf-8"

  @classmethod
  # it works
  def save_student(cls, new_student: Student):
    with open(cls.__students_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      writer.writerow([new_student.name, new_student.surname, new_student.age, new_student.gender, new_student.id])

  @classmethod
  # it works
  def load_students(cls):
    students = []
    with open(cls.__students_file, mode="r", encoding=cls.__encoding_style) as file:
      reader = csv.reader(file)
      for row in reader:
        student = Student(row[0], row[1], row[2], row[3], row[4])
        students.append(student)
    return students
  
  @classmethod
  # dose not work still need to make changes
  def save_course(cls, new_course: Course):
    with open(cls.__courses_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      professor_info = [new_course.professor.name, new_course.professor.surname, new_course.professor.age, new_course.professor.gender, new_course.professor.id]
      students_info = []
      for student in new_course.all_students:
        student_info = [student.name, student.surname, student.age, student.gender, student.id]
        students_info.append(student_info)
      grades_info = []
      for grade in new_course.get_grades:
        grade_info = [grade.grade, grade.identify_student, grade.course_id]
        grades_info.append(grade_info)
      
      writer.writerow([new_course.course_id, new_course.name, new_course.course_credits, new_course.year, professor_info, students_info, grades_info])
      
  @classmethod #TODO
  def load_courses(cls):
    from Grade import Grade
    import ast
    courses = []
    with open(cls.__courses_file, mode="r", encoding=cls.__encoding_style) as file:
      reader = csv.reader(file)
      for row in reader:
        temp_prof_info = ast.literal_eval(row[4])
        professor_info = Professor(temp_prof_info[0], temp_prof_info[1], temp_prof_info[2], temp_prof_info[3], temp_prof_info[4])
        #It evaluates string to list without executing the string in brackets like 'eval' does
        all_students_info = ast.literal_eval(row[5])
        all_grades_info = ast.literal_eval(row[6])
        for student in all_students_info:
          student = Student(student[0], student[1], student[2], student[3], student[4])
        for grade in all_grades_info:
          grade = Grade(grade[0], grade[1], grade[2])
        course = Course(row[0], row[1], row[2], row[3], professor_info, all_students_info, all_grades_info)
        courses.append(course)
    return courses
  
  @classmethod
  #just a structure of the class
  def save_employee(cls, new_employee: Professor | GeneralWorker):
    with open(cls.__employees_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      if new_employee.role == "Professor":
        writer.writerow([new_employee.name, new_employee.surname, new_employee.age, new_employee.gender, new_employee.id, new_employee.role])
      else:
        writer.writerow([new_employee.name, new_employee.surname, new_employee.age, new_employee.gender, new_employee.job, new_employee.salary, new_employee.id, new_employee.role])

  @classmethod
  def load_employees(cls):
    professors = []
    general_workers = []
    with open(cls.__employees_file, mode="r", encoding=cls.__encoding_style) as file:
      reader = csv.reader(file)
      for row in reader:
        if row[-1] == "Professor":
          professor = Professor(row[0], row[1], row[2], row[3], row[4])
          professors.append(professor)
        elif row[-1] == "General Worker":
          general_worker = GeneralWorker(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
          general_workers.append(general_worker)
    employees = {"Professors" : professors, "General Workers" : general_workers}
    return employees
  
  @classmethod
  def save_building(cls, new_building: Building):
    with open(cls.__buildings_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      writer.writerow([new_building.name, new_building.address, new_building.capacity])