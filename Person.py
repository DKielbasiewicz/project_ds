class Person:
  def __init__(self, name, surname, age):
    self.__name = name
    self.__surname = surname
    self.__age = age

  @property
  def name(self):
    return self.__name
  
  @property
  def surname(self):
    return self.__surname
  
  @property
  def age(self):
    return self.__age