from Person import Person

class Professor(Person):
  def __init__(self, name, surname, age, gender, id_num):
    super().__init__(name, surname, age, gender)
    self.taught_courses = []
    self.__id = id_num
  
  @property
  def id(self):
    return self.__id

  def __str__(self):
    return f"{super().__str__()} and teaches {len(self.taught_courses)} courses"