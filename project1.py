# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Import time, random, plotting, stats, and numpy.
import time
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy
"""
Math 560
Project 1
Fall 2020

Partner 1:
Partner 2:
Date:
"""
"""
Function:Selection Sort

"""
def SelectionSort(listToSort):
    length1 = len(listToSort)
    for i in range(0, length1-1):
        for j in range(i+1, length1):
            if listToSort[j] < listToSort[i]:
                # swap
                x = listToSort[j]
                listToSort[j] = listToSort[i]
                listToSort[i] = x
    return listToSort




"""
InsertionSort
"""
def InsertionSort(listToSort):
    length2 = len(listToSort)
    for j in range(1, length2):
        # Divide the list into sorted and unsorted parts
        num = listToSort[j]     # First unsorted number
        i = j - 1
        while i >= 0 and listToSort[i] > num:
            # Compared with sorted number which are before it
            listToSort[i+1] = listToSort[i]
            i -= 1
        listToSort[i+1] = num       # insert it in the right place
    return listToSort



"""
BubbleSort
Sort an array by iterating through it and swap the consecutive elements which\
are out of order.
This function takes one input
   listToSort: list to be sorted
output: input list in an ascending order
"""
def BubbleSort(listToSort):
    n=len(listToSort)
    # for each iteration, it makes sure the largest element in the unsorted \
    # part goes the the end
    for i in range(n):
        # in j th iteration, the j th largest element is placed correctly
        # so only need to compare n-k elements
        # since we can compare 2 elements at once, so only need to compare\
        # n-k-1 times to compare n-k consecutive elements
        for j in range(0,n-i-1):
            # if listToSort[j]>listToSort[j+1], the array is out of order
            if listToSort[j]>listToSort[j+1]:
                # swap listToSort[j] and listToSort[j+1]
                temp = listToSort[j]
                listToSort[j] = listToSort[j+1]
                listToSort[j+1] = temp
    return listToSort
"""
MergeSort
"""
def MergeSort(listToSort):
    return listToSort

"""
QuickSort
Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""

"""
Function: partition(arr,left,right)
This function choose a pivot and then partition the list based on the pivot.
If the element is smaller than the pivot, it goes to the left of the pivot.
If the element is larger than the pivot, it goes to the right of the pivot.
It takes 3 inputs:
  arr: list to be sorted
  left: left boundary of the list to be sorted
  right: right boundary of the list to be sorted
output:
  a: the index of the pivot in the sorted list
"""
def partition(arr,left,right):
    a=left
    b=right-1
    # set pivot to be the first element of the list
    pivot= arr[left]
    # while a and b are not equal, keep scanning the list
    while a!=b:
        # when arr[b] is larger than pivot and a is smaller than b, b moves \
        # one step to left
        while arr[b]> pivot and a<b :
            b-=1
        # when arr[a] is smaller than pivot and a is smaller than b, a moves \
        # one step to right
        while arr[a]< pivot and a<b :
            a+=1
        # when a and b stuck
        # if arr[a] == arr[b] == pivot and a is smaller than b
        #   a moves one step to the left
        if arr[a]==pivot and arr[a] == arr[b] and a<b:
            a+=1
        # else:
        #   swap arr[a] and arr[b]
        else:
            temp = arr[a]
            arr[a]=arr[b]
            arr[b]=temp
    return a


"""
Function: QuickSort(listToSort, i=0, j=None)
This function sorts the input array in an ascending order with partitioning \
the array recursively until it can't be split into 2 parts. 
It takes 3 input:
  listToSort: list to be sorted
  i: left boundary of the list to be sorted
  j: right boundary of the list to be sorted
output: the input list in an ascending order
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    # if i==j , there is no need to do the partition
    if i == j :
        return
    # partition the array and get the index of the pivot
    index=partition(listToSort,i,j)
    # split the list into 2 parts: list[i , index], list [index+1 ,j],
    # then sorts this two parts respectively.
    if index>i:
        QuickSort(listToSort, i, index)
    if index<j:
        QuickSort(listToSort, index+1, j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *






# Press the green button in the gutter to run the script.

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing InsertionSort Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    """print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()"""
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
