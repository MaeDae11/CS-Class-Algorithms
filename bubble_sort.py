import picasso
import numpy.random as r
# Bubble sort:
#  - for each scan through, going to bubble the highest number to the top
#  - repeatedly scan untill scan through and DONT swap
#  - even if no (is i > i+1 ex: 3 > 4) still keep checking

def bubble_sort(a):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                swapped = True
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


p = picasso.Picasso('bubble_sort')
p.draw_best_fitting_line = True
for i in range(0, 15001, 1000):
    p.start(i)
    a = r.random_integers(0, i, i)
    bubble_sort(a)
    p.end()
    p.export()


# How to find time complexity of an algorithm
#  ex: [3, 2, 1]
# start at the top   --> 1
# outter loop is going to run 4 times

#  1 + n ( 1 + (n-1) (3) )
#  1 + n + 3n(2) - 3n
#  1 - 2n + 3n(2) 
#  n(2)

# space complexity of bubble sort is n