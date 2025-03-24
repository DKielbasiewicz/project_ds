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
  """
  NOTE I've decided to put this class here, as putting it into separate file created some unwanted issues.
  Although I'm not 100% sure, I believe that keeping this function next to the University Class is the best choice. If you have some thoughts, please share them   <--- TODO DELETE ME
  
  Class made to separate the statistical methods and plots from the main, University Class
  
  All available methods: (NOTE I plan on adding more)
    avg_grade_course()
          >calculates the avg grade for a specific course
          >finds the min and max grade in the course
          >creates a plot for the grades
          
    avg_grade_uni()
          >calculates the avg grade for all courses
          >creates a plot for the data 
  """
  
  def avg_grade_course(self, chosen_course: Course, plot_on = True): 
    """
    Args:
        chosen_course (Course): Course obj
        plot_on (bool, optional): This boolean decides whether to plot the course or no | this method is used in avg_grade_uni function, we don't want to see the plot for each course there. <- Defaults to True

    Returns:
        average grade: float
    """
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
        
  def avg_grade_uni(self): # Shows the overall statistics of all the courses
    all_courses = self.available_courses # list of all the courses
    sum_ = [0] # the first number in the list of averages is the sum of all averages, look at the second line of for loop
    for course in all_courses:
        sum_.append(self.avg_grade_course(course, False)) 
        sum_[0] += sum_[-1] # This is the sum of all averages
    #ploten machen
    plt.plot([course.course_id for course in all_courses], sum_[1::], 'ro')
    plt.ylabel('Average Grade')
    plt.title("Graph of all courses' grades")
    plt.show()
    
    return sum_[0]/len(sum_[1::]) # returns the average grade of the all averages
class University(UniversityStatistics):
  def __init__(self):
    self.__name = "UniTrack University"
    self.__available_courses = []
    self.__employees = []  
      
  @property
  def available_courses(self):
    return self.__available_courses

  @property
  def employees(self):
    return self.__employees
  
  @property
  def name(self):
    return self.__name
  
  def add_course(self, new_course: Course):
    if not new_course in self.__available_courses:
      self.__available_courses.append(new_course)
      return
    raise ValueError(" How to handle adding the same course? ") # <--- !!!
    
  def add_employee(self, new_employee: Professor): #adds an employee, i.e. an Professor obj to the self.__employees list
    if not new_employee in self.__employees: # check if the obj is already in the list
      self.__employee.append(new_employee) # if not append
      return 
    
    raise ValueError("This person is already employed!") # else raise errno
    
  # NOTE Thou shalt decide the fate of all Comparison Operators
  #def __eq__(self, another_uni) -> bool:
  #    if self.avg_grade_uni() == another_uni.avg_grade_uni():
  #        return True
  #    return False
  #def __lt__(self, another_uni)
  
  def __str__(self):
      return f"{self.__name} is great, not sure what to include here, open for ideas" # <----- TODO

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