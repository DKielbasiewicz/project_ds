from Person import Person

class Professor(Person):
  def __init__(self, name, surname, age, gender):
    super().__init__(name, surname, age, gender)
    self.taught_courses = []

  def __str__(self):
    return f"{super().__str__()} and teaches {len(self.taught_courses)} courses"