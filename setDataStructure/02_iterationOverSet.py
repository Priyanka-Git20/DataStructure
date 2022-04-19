'''
@Author : Priyanka
@Date : 2022-04-19  6:55:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 7:05:00
@Title :Write a Python program to iteration over sets.
'''


def iteration_over_set():
    """
       Description:
            Access the items in the set using for loop.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    thisset = {"apple", "banana", "cherry",1,5,9}
    for i in thisset:
        print(i,end=" , ")

if __name__ == '__main__':
    iteration_over_set()