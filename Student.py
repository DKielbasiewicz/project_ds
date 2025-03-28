from Person import Person
from random import randint

class Student(Person):
  def __init__(self, name, surname, age, gender, given_student_id: int = None):
    super().__init__(name, surname, age, gender)
    """I created ec, year, filed_courses and passed_courses as private
    variables because they should not be accessed directly and 
    should be kept only within the class"""
    self._ec = 0
    self._year = 1
    self.__studentid = self.__random_student_id(given_student_id)
    self.current_courses = []
    self._failed_courses = []
    self._passed_courses = []

  def __str__(self):
    return f"{self.name} {self.surname} is at {self._year} year and has {self._ec} credits"
  
  def __eq__(self, another):
    return self._ec == another.ec
  
  def __lt__(self, another):
    return self._ec < another.ec
  
  def __gt__(self, another):
    return self._ec > another.ec
  
  def __random_student_id(self, given_student_id):
    #it generates random student number within the given range
    if given_student_id == None:
      #if it is a new student added by app, then the default student id is None, but
      #if different then it is already in the database, that is why we pass the saved student number
      from Database import Database
      #loading all students
      all_students = Database.load_students()
      while True:
        #generating the number
        new_generated_id = randint(1000000, 9999999)
        if all_students:
          for student in all_students:
            # if someone has generated number then it redo the loop
            if student.id == new_generated_id:
              continue
            #if nobody has generated number then it returns it as new student id
          return new_generated_id
        else:
          return new_generated_id
    else:
      #if student is already in database then pass his student number
      return given_student_id

  @property
  #The property works as an attribute, however it is only read-only
  def year(self):
    return self._year
  
  @property
  def ec(self):
    return self._ec
  
  @property
  def id(self):
    return self.__studentid
    
  @year.setter
  #The setter works like a method of the object 
  def year(self, new_year):
    self._year = new_year
