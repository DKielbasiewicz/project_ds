from Person import Person

class Student(Person):
  def __init__(self, name, surname, age, student_id):
    super().__init__(name, surname, age)
    """I created ec, year, filed_courses and passed_courses as private
    variables because they should not be accessed directly and we
    should keept only within the class"""
    self.__ec = 0
    self.__year = 1
    self.__studentid = student_id
    self.current_courses = []
    self.__failed_courses = []
    self.__passed_courses = []

  @property
  #The property works as an attribute, however it is only read-only
  def year(self):
    return self.__year
  
  @property
  def ec(self):
    return self.__ec
  
  @property
  def id(self):
    return self.__studentid
    
  @year.setter
  #The setter works like a method of the object 
  def year(self, new_year):
    self.__year = new_year

  def add_course_grade(self, course_name, grade):
    pass

