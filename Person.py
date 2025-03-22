class Person:
  def __init__(self, name: str, surname: str, age: int, gender: str):
    self.__name = name
    self.__surname = surname
    self.__age = age
    self._gender = gender

  @property
  def name(self):
    return self.__name
  
  @property
  def surname(self):
    return self.__surname
  
  @property
  def age(self):
    return self.__age
  
  @property
  def gender(self):
    return self._gender
  
  def __str__(self):
    return f"{self.__name} {self.__surname} is {self.__gender} and is {self.__age} years old"