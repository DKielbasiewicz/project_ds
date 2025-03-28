from Person import Person
from random import randint

class Professor(Person):
  def __init__(self, name: str, surname: str, age: int, gender: str, given_professor_id: int = None):
    super().__init__(name, surname, age, gender)
    self.taught_courses = []
    self.__professor_id = self.__random_professor_id(given_professor_id)
    self.__role = "Professor"

  def __str__(self):
    return f"{super().__str__()} and teaches {len(self.taught_courses)} courses"
  
  def __random_professor_id(self, given_professor_id):
    #it generates random professor number within the given range
    if given_professor_id == None:
      #if it is a new professor added by app, then the default professor id is None, but
      #if different then it is already in the database, that is why we pass the saved professor number
      from Database import Database
      #loading all employees
      all_employees = Database.load_students()
      while True:
        #generating the number
        new_generated_id = randint(1000, 9999)
        if all_employees:
          for employee in all_employees:
            # if someone has generated number then it redo the loop
            if employee.id == new_generated_id:
              continue
            #if nobody has generated number then it returns it as new student id
          return new_generated_id
        else:
          return new_generated_id
    else:
      #if professor is already in database then pass his professor number
      return given_professor_id
  
  @property
  def id(self):
    return self.__professor_id
  
  @property
  def role(self):
    return self.__role