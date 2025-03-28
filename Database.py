import csv
from Student import Student
from Professor import Professor
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
  def save_course(cls, new_course):
    with open(cls.__courses_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      
      students_temp = [student.id for student in new_course.students]
      students = ','.join(map(str, students_temp))
      grades_num_temp = [grade.grade for grade in new_course.grades]
      grades_num = ','.join(map(str, grades_num_temp))
      grades_id_temp = [grade.identify_student for grade in new_course.grades]
      grades_id = ','.join(map(str, grades_id_temp))
      
      writer.writerow([new_course.course_id, new_course.course_name, new_course.course_credits, new_course.year, new_course.professor.id, students, grades_num, grades_id])
      
  @classmethod #TODO
  def load_course(cls):
    courses = []
    with open(cls.__courses_file, mode="r", encoding=cls.__encoding_style) as file:
      reader = csv.reader(file)
      
      for row in reader:
        print(row[-2])
        courses.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6], row[7]])
        
    return courses
  
  @classmethod
  #just a structure of the class
  def save_employee(cls, new_employee: Professor):
    with open(cls.__employees_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      writer.writerow([new_employee.name, new_employee.surname, new_employee.age, new_employee.gender, new_employee.id])

  @classmethod
  def save_building(cls, new_building: Building):
    with open(cls.__buildings_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      writer.writerow([new_building.name, new_building.address, new_building.capacity])
  
  @classmethod
  def load_professors(cls):
    professors = []
    with open(cls.__employees_file, mode="r", encoding=cls.__encoding_style) as file:
      reader = csv.reader(file)
      for row in reader:
        prof = Professor(row[0], row[1], row[2], row[3], row[4])
        professors.append(prof)
    return professors