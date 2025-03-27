import csv
from Student import Student
from Professor import Professor
from Building import Building
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
      writer.writerow([new_course.course_id, new_course.course_name, new_course.course_credits, new_course.year, new_course.professor, new_course.students, new_course.grades])

  @classmethod
  #just a structure of the class
  def save_employee(cls, new_employee: Professor):
    with open(cls.__employees_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      writer.writerow([new_employee.name, new_employee.surname, new_employee.age, new_employee.gender, new_employee.taught_courses])

  @classmethod
  def save_building(cls, new_building: Building):
    with open(cls.__buildings_file, mode="a", newline="", encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      writer.writerow([new_building.name, new_building.address, new_building.capacity])