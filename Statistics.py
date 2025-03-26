import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator, FuncFormatter

class UniversityStatistics:
    @staticmethod
    def avg_grade_course(chosen_course, plot_on = True): 
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
    
    @classmethod
    def avg_grade_uni(cls, university): # Shows the overall statistics of all the courses
        all_courses = university.available_courses # list of all the courses
        sum_ = [0] # the first number in the list of averages is the sum of all averages, look at the second line of for loop
        for course in all_courses:
            sum_.append(cls.avg_grade_course(course, False)) 
            sum_[0] += sum_[-1] # This is the sum of all averages
        #ploten machen
        plt.plot([course.course_id for course in all_courses], sum_[1::], 'ro')
        plt.ylabel('Average Grade')
        plt.title("Graph of all courses' grades")
        plt.show()
    
        return sum_[0]/len(sum_[1::]) # returns the average grade of the all averages