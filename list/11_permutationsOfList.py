'''
@Author : Priyanka
@Date : 2022-04-19  3:45:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 4:00:00
@Title : Write a Python program to generate all permutations of a list in Python.
'''

import itertools


def permutations_of_list():
    """
       Description:
           From intertools module permutation()method is used to generage all permutations of a list.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    lst = [1,2,3,4]
    print(list(itertools.permutations(lst)))


if __name__ == '__main__':
    permutations_of_list()
