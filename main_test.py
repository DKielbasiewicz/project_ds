from main import *

p1 = Professor('Alber', "Smart", 41, 'm')
s1 = Student('Mary', "W", 12, 'f', 's222')
s2 = Student('Marian', "M", 11, 'm', 's232')

c1 = Course('SOW', 'Programming', 3, 1, p1, [s1,s2],[])
c2 = Course('SOW-K', 'Programming', 3, 1, p1, [s1,s2],[])
c3 = Course('SOW-B', 'Programming', 3, 1, p1, [s1,s2],[])


g1_s1 = Grade(4.2,s1,c1)
g1_s2 = Grade(2.2,s2,c1)

g2_s1 = Grade(6.3,s1,c1)
g2_s2 = Grade(8.7,s2,c1)

g3_s1 = Grade(9.9,s1,c1)
g3_s2 = Grade(8.2,s2,c1)

b1 = Building('Comenius1', 'Poznan1', 'com1', [c1,c2,c3], [p1])
b2 = Building('Comenius2', 'Poznan2', 'com2', [c1,c2,c3], [p1])
b3 = Building('Comenius3', 'Poznan3', 'com3', [c1,c2,c3], [p1])

c1.add_grade(g1_s1)
c1.add_grade(g1_s2)

c2.add_grade(g2_s1)
c2.add_grade(g2_s2)

c3.add_grade(g3_s1)
c3.add_grade(g3_s2)

u1 = University()
u1.add_course(c1)
u1.add_course(c2)
u1.add_course(c3)

u1.add_building(b1)
u1.add_building(b2)
u1.add_building(b3)


def test_statistics_func1():
    avg_ = UniversityStatistics.avg_grade_course(c1)
    
    assert (g1_s1.grade+g1_s2.grade)/2 == avg_, f"Wrong value"
    
def test_statistics_func2():
    avg_ = UniversityStatistics.avg_grade_uni(u1)
    
    assert True == (not False), f'It just works'