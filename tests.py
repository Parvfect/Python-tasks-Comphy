
import task2 as t2
import task4 as t4
import task5 as t5
import task6 as t6
import task7 as t7
"""
Really can only test 2, 4, 5, 6 and 7
"""


def task2():
    """ Projectile Motion """
    t,l,h = t2.projectile(20, 20, 20)
    T, L, H = t2.projectile(0,0,0)
    assert (round(t,2), round(l,2), round(h,2)) == (2.83, 53.25, 22.38)
    assert (T,L,H) == (0.0, 0.0, 0.0)

    print("Tests for Task 2 passed")

def task4():
    """ Random number generator """
    master.task4()

def task5():
    """ Random Walk """
    master.task5()

def task6():
    """ Walk from sides of square """
    master.task6()

def task7():
    """ Efficiency of Carnot Cycle """
    master.task7()




task2()