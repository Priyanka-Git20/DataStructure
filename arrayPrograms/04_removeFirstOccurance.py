'''
@Author : Priyanka
@Date : 2022-04-20  12:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 01:00:00
@Title : Write a Python program to remove the first occurance of a specified element from an array.
'''

import array as arr


def remove_first_occurance():
    """
      Description:
           Removing the first occurance from the list.
      Parameter:
           None
      Return:
          Returning nothing but printing the result.
    """
    a = arr.array('i', [1, 2, 4, 6,1,8])
    print("Array is: ", a)
    a.remove(1)
    print("array is: ", a)


if __name__ == '__main__':

    remove_first_occurance()