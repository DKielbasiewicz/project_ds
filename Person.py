class Person:
  def __init__(self, name: str, surname: str, age: int, gender: str):
    self.__name = name
    self.__surname = surname
    self.__age = age
    self._gender = self.__validate_gender(gender)

  def __str__(self):
    return f"{self.__name} {self.__surname} is {self._gender} and is {self.__age} years old"
  
  def __validate_gender(self, gender: str):
    # it cheks if the string meet given conditions below.
    # if not then it raise an Error.
    if gender.lower() == "f" or gender.lower() == "female":
      return "female"
    if gender.lower() == "m" or gender.lower() == "male":
      return "male"
    raise NameError("Invalid gender: The Person has to be either Male (M) or Female (F)")

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