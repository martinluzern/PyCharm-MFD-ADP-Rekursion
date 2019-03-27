#this programm shows the iterative and recursive version of factorial number
#Martin Vogel - Example Code in Python

def factorial_iterative(n):
    fac = 1
    for i in range(1, n+1, 1):
        fac *= i
    return fac


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)


#main: both calculations...
# n is the number of factorial to be calculated
n = -0
print("Iterative:  " + str(n) + "! = " + str(factorial_iterative(n)))
print("Recursive:  " + str(n) + "! = " + str(factorial_recursive(n)))


