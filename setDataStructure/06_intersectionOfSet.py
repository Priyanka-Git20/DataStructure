'''
@Author : Priyanka
@Date : 2022-04-19  7:55:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 8:00:00
@Title :Write a Python program to create an intersection of sets.
'''


def intersection_of_sets():
    """
       Description:
            By using the intersection method create a intersection of two sets.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    set1 = {4,5,"Red","Orange","Blue","Black"}
    set2 = {"Red",4,"Yellow","white"}
    print("Original sets are")
    print(set1)
    print(set2)
    set3 = set1.intersection(set2)
    print("Set after intersection is ",set3)

if __name__ == '__main__':
    intersection_of_sets()