# example program on summing up numbers recursively
# Martin Vogel, hslu Informatik

# Iterative Implementierung
def isum(n):
    summe = 0
    i = 0
    while i <= n:
        summe += i
        i += 1
    return summe


# Rekursive Implementierung
def rsum(n):
    if n > 0:
        summe = rsum(n-1) + n
    else:
        summe = 0
    return summe


# main program for both approaches
print("summing up interatively: ", isum(10))
print("summing up recursively: ", rsum(10))
