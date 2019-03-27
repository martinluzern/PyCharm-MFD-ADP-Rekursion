#binary search recursively

import random

def listenGenerator():
    n = 9
    upperlimit = 15
    sliste = []

    for i in range(0, n, 1):
        zahl = random.randrange(0, upperlimit + 1, 1)
        while zahl in sliste:
            zahl = random.randrange(0, upperlimit + 1, 1)
        sliste.append(zahl)
    sliste = sorted(sliste)
    print(sliste)
    return sliste


def binaryRecursiv(left, right, liste, element):
    '''searches in liste the element, left, right are limit indexes low and high
    returns the position - if not found -1'''
    mid = left + (right - left)//2
    if left <= right:
        if element == liste[mid]:
            found = True
            return mid
        elif element < liste[mid]:
            return binaryRecursiv(left, mid-1, liste, element)
        else:
            return binaryRecursiv(mid+1, right, liste, element)
    else:
        return -1


#hier main program
sliste = [11, 18, 21, 25, 29, 34, 36, 48, 54, 55, 73, 81, 99]
suchZahl = 34
first = 0
last = len(sliste)-1

position = binaryRecursiv(first, last, sliste, suchZahl)

if position != -1:
    print(suchZahl, "gefunden an Position:", position)
else:
    print(suchZahl, "nicht gefunden in Liste")





#hier main Programm
# suchliste = listenGenerator()
# suchElement = 5
# first = 0
# last = len(suchliste)-1
#
# position = binaryRecursiv(first, last, suchliste, suchElement)
#
#
#
# if position != -1:
#     print(suchElement, "gefunden an Position:", position)
# else:
#     print(suchElement, "nicht gefunden in Liste")
#
#
#
