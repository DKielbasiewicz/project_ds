"""
UniversityStatistics is an utility class. 
It's methods are used to graph University data. 
NOTE Uses matplotlib.

    avg_grade_course(chosen_course, plot_on: bool = True)
        this method makes a 3 bar graph with minimal grade, average grade and maximal grade associated with chosen_course Course object
        NOTE graph can be disabled by setting plot_on to False
        
        returns average grade 
    
    avg_grade_uni(cls, university, plot_on: bool = True)
        this method puts all the average grades from all of the Course objects
        *Gets average grade from avg_grade_course
        NOTE graph can be disabled by setting plot_on to False
        
        returns average grade off all courses  
    
    
"""
import matplotlib.pyplot as plt

class UniversityStatistics:
    #NOTE class attributes for maximum and minimum grade
    max_grade = 10  # maximum grade
    min_grade = 0   # minimum grade
    
    def __init__(self):
        raise Exception("UniversityStatistics cannot be represented by a variable")
    
    @staticmethod
    def avg_grade_course(chosen_course, plot_on: bool = True): 
        """
        Args:
            chosen_course (Course): Course obj
            plot_on (bool, optional): This boolean decides whether to plot the course or no | this method is used in avg_grade_uni function, we don't want to see the plot for each course there. <- Defaults to True

        Returns:
            average grade: float
        """
        sum_, min_, max_ = 0, UniversityStatistics.max_grade, UniversityStatistics.min_grade
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
            plt.ylim(0, 10)
            plt.title(chosen_course)
            plt.show()
        # return average
        return avg_
    
    @classmethod
    def avg_grade_uni(cls, university, plot_on: bool = True): # Shows the overall statistics of all the courses
        all_courses = university.available_courses # list of all the courses
        sum_ = [0] # the first number in the list of averages is the sum of all averages, look at the second line of for loop
        for course in all_courses:
            sum_.append(cls.avg_grade_course(course, False)) 
            sum_[0] += sum_[-1] # This is the sum of all averages
        #ploten machen
        if plot_on:
            plt.plot([course.course_id for course in all_courses], sum_[1::], 'ro')
            plt.ylabel('Average Grade')
            plt.ylim(0, 10)
            plt.title("Graph of all courses' grades")
            plt.show()
            
        try:
            avg_ = sum_[0]/len(sum_[1::])
        except ZeroDivisionError:
            print("There are no courses in our database")
            return
        
        return avg_ # returns the average grade of the all averages