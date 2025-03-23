from Person import Person

class Student(Person):
  def __init__(self, name, surname, age, gender,  student_id):
    super().__init__(name, surname, age, gender)
    """I created ec, year, filed_courses and passed_courses as private
    variables because they should not be accessed directly and we
    should keept only within the class"""
    self._ec = 0
    self._year = 1
    self.__studentid = student_id
    self.current_courses = []
    self._failed_courses = []
    self._passed_courses = []

  def __str__(self):
    return f"{self.name} {self.surname} is at {self._year} year and has {self._ec} credits"

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

  def add_course_grade(self, course_name, grade):
    pass

