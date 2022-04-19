'''
@Author : Priyanka
@Date : 2022-04-19  6:40:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 6:50:00
@Title :Write a Python program to create a set.
'''


def create_set():
    """
       Description:
            Create a set and display it.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    set1 = {"abc", 34, True, 40, "male"}
    print("set1 = ",set1)
    print("Type of set1 is ",type(set1))

if __name__ == '__main__':
    create_set()