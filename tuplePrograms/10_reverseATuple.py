'''
@Author : Priyanka
@Date : 2022-04-20  4:45:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 4:55:00
@Title :Write a Python program to reverse a tuple.
'''


def reversed_a_tuple():
    """
       Description:
            By using negative index reversed a tuple and print it.
       Parameter:
            none
       Return:
           Returning nothing but printing the result.
   """

    mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    print("The original tuple is",mytuple)
    reversedTuple = mytuple[::-1]
    print("The reversed tuple is ",reversedTuple)

if __name__ == '__main__':
    reversed_a_tuple()
