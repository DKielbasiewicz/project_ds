import csv
from Student import Student
class Database:
  __students_file = "students.csv"
  __courses_file = "courses.csv"
  __encoding_style = "utf-8"

  @classmethod
  def save_student(cls, new_student: Student):
    with open(cls.__students_file, mode='a', newline='', encoding=cls.__encoding_style) as file:
      writer = csv.writer(file)
      writer.writerow([new_student.name, new_student.surname, new_student.age, new_student.gender, new_student.id])

  @classmethod
  def load_students(cls):
    students = []
    with open(cls.__students_file, mode='r', encoding=cls.__encoding_style) as file:
      reader = csv.reader(file)
      for row in reader:
        student = Student(row[0], row[1], row[2], row[3], row[4])
        students.append(student)
    return students
  
  @classmethod
  def save_course(cls, new_course):
    with open(cls.__courses_file, mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([new_course.course_id, new_course.course_name, new_course.course_credits, new_course.year, new_course.professor, new_course.students, new_course.grades])
  

  

if __name__ == "__main__":
  student1 = Student("John", "Doe", 22, "M", "123")
  student2 = Student("Jane", "Doe", 22, "F", "124")
  Database.save_student(student1)
  Database.save_student(student2)
  read_students = Database.load_students()
  for student in read_students:
    print(student)



