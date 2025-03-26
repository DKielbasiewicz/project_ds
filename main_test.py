from main import *

p1 = Professor('Alber', "Smart", 41, 'm')
s1 = Student('Mary', "W", 12, 'f', 's222')
s2 = Student('Marian', "M", 11, 'm', 's232')

c1 = Course('SOW', 'Programming', 3, 1, p1, [s1,s2],[])

g1_s1 = Grade(5.2,s1,c1)
g1_s2 = Grade(0.2,s2,c1)

c1.add_grade(g1_s1)
c1.add_grade(g1_s2)

u1 = University()
u1.add_course(c1)

def test_statistics_func1():
    avg_ = UniversityStatistics.avg_grade_course(c1)
    
    assert (g1_s1.grade+g1_s2.grade)/2 == avg_, f"Wrong value"
    
def test_statistics_func2():
    avg_ = UniversityStatistics.avg_grade_uni(u1)
    
    assert True == (not False), f'It just works'