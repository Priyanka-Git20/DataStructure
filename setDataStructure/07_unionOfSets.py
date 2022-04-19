'''
@Author : Priyanka
@Date : 2022-04-19  8:05:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 8:15:00
@Title :Write a Python program to create a union of sets.
'''


def union_of_sets():
    """
       Description:
            By using the union method create a union of two sets.
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
    set3 = set1|set2
    print("Set after union of sets is ",set3)

if __name__ == '__main__':
    union_of_sets()