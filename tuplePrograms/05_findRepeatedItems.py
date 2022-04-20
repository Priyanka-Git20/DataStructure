'''
@Author : Priyanka
@Date : 2022-04-20  1:55:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 2:10:00
@Title :Write a Python program to find the repeated items of a tuple.
'''


def find_repeated_items():
    """
       Description:
            By using count method finding repeated items.
       Parameter:
            none
       Return:
           Returning nothing but printing result.
   """
    mytuple = (12,3,5,7,12,9,45,6,8,12)
    count = mytuple.count(12)
    print("Number of time 12 repeated in tuple is",count)


if __name__ == '__main__':
    find_repeated_items()
