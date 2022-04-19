'''
@Author : Priyanka
@Date : 2022-04-19  7:40:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 7:50:00
@Title :Write a Python program to remove an item from a set if it is present in the set.
'''


def check_remove_item_present_or_not():
    """
       Description:
            After removing an item from a set check  it is present in the set or not by using in operator.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    thisset = {'green', 'yellow', 1, 'orange', 12, 'black', 'apple', 23, 'red'}
    thisset.remove("orange")
    print("orange"in thisset)

if __name__ == '__main__':
    check_remove_item_present_or_not()