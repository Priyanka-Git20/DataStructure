'''
@Author : Priyanka
@Date : 2022-04-20  11:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 11:45:00
@Title : Write a Python program to reverse the order of the items in the array.
'''

import array as arr


def reverse_the_array():
    """
      Description:
           Reversing the array by slicing and also by reversed()method.
      Parameter:
           None
      Return:
          Returning nothing but printing the result.
    """

    a = arr.array('i', [1,2, 4, 6, 8,9,12])
    print("Original array is",a)
    res = a[::-1]          #reversing an array by slicing
    print("Array after reversing the element is",res)
    res = list(reversed(a))
    print("Array after reversing the element is",res)


if __name__ == '__main__':
    reverse_the_array()