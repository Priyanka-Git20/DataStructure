'''
@Author : Priyanka
@Date : 2022-04-20  1:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 1:50:00
@Title :Write a Python program to create the colon of a tuple.
'''

from  copy import deepcopy


def clone_of_tuple():
    """
       Description:
            creating a copy of a tuple.
       Parameter:
            none
       Return:
           Returning nothing but printing result.
   """
    fruits = ("apple", "banana", "cherry")
    myFruits = deepcopy(fruits)
    print("The copy of the fruits tuple is ",myFruits)
    

if __name__ == '__main__':
    clone_of_tuple()
