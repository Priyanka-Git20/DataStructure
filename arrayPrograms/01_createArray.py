'''
@Author : Priyanka
@Date : 2022-04-20  11:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 11:30:00
@Title : Write a Python program to create an array of 5 integers and display the array items.Access individual element through indexes.
'''

import array as arr

def create_array():
    """
      Description:
          Creating an array and printing the element by using for loop and also by accessing index.
      Parameter:
           None
      Return:
          Returning nothing but printing the result.
    """

    a = arr.array('i', [1,2, 4, 6, 8])
    for i in a:
        print(i)

    print("Access the element through index")
    print("First element is",a[0])
    print("Second element is",a[1])
    print("Third element is",a[2])
    print("Fourth element is",a[3])
    print("Fifth element is",a[4])

if __name__ == '__main__':
    create_array()
