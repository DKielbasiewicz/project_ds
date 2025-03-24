"""
General structure of the UniTrack application
"""
from Grade import Grade
from Course import Course
from Student import Student 
from Professor import Professor 

import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator, FuncFormatter
class UniversityStatistics:
  def avg_grade_course(self, chosen_course: Course, plot_on = True):
    sum_,min_,max_ = 0,10,0
    final_grades = chosen_course.get_grades
    for final_grade in final_grades:
        grade_temp = final_grade.grade # made a temp var to avoid calling .grade over and over again
        # sum and maxima
        sum_ += grade_temp
        if grade_temp > max_: max_ = grade_temp
        elif grade_temp < min_: min_ = grade_temp
    #average of all grades
    avg_ = sum_/len(final_grades)
    # if plot then do plot
    if plot_on:
      plt.bar([f'Lowest Grade: {min_}', f'Average Grade: {avg_}', f'Highest Grade: {max_}'],[min_, avg_, max_])
      plt.ylabel('Grade')
      plt.title(chosen_course)
      plt.show()
    # return average
    return avg_
        
  def avg_grade_uni(self):
    all_courses = self.available_courses
    sum_ = [0] # the first number in the list of averages is the sum of all averages, look at the second line of for loop
    for course in all_courses:
        sum_.append(self.avg_grade_course(course, False)) 
        sum_[0] += sum_[-1] # This is the sum of all averages
    #ploten machen
    plt.plot([course.course_id for course in all_courses], sum_[1::], 'ro') 
    plt.ylabel('Average Grade')
    plt.title("Graph of all courses' grades")
    plt.show()
    
    return sum_[0]/len(sum_[1::])

class University(UniversityStatistics):
  def __init__(self):
    self.name = "UniTrack University"
    self.__available_courses = []
    self.__employees = []  
      
  @property
  def available_courses(self):
    return self.__available_courses
  
  def add_course(self, new_course: Course):
    if not new_course in self.__available_courses:
      self.__available_courses.append(new_course)
      return
    raise ValueError(" How to handle adding the same course? ") # <--- !!!
    

  # NOTE Thou shalt decide the fate of all Comparison Operators
  #def __eq__(self, another_uni) -> bool:
  #    if self.avg_grade_uni() == another_uni.avg_grade_uni():
  #        return True
  #    return False
  #def __lt__(self, another_uni)
  
  def __str__(self):
      return f""

class UniTrackApp:
  def __init__(self):
    self.__uniTrack = University()

  def help(self):
    print("List of commands:")
    print("[1] - Add course")

  def add_course(self, name, ec):
    name = input("Enter name of the course: ")
    ec = input("Number of credits: ")
    pass

  def run(self):
    while True:
      self.help()
      print("\n")
      command = input("Enter command: ")
      if command == "1":
        self.help()
      else:
        print("Invalid command")