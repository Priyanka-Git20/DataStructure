'''
@Author : Priyanka
@Date : 2022-04-19  8:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 8:40:00
@Title : Write a Python program to clear a set.
'''


def clear_a_set():
    """
       Description:
            By using the clear method clear the set and all items are remove but remain empty set.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    vowels = {"a","e","i","o","u"}
    print("Set before clear:",vowels)
    vowels.clear()
    print("Set after clear:",vowels)

if __name__ == '__main__':
    clear_a_set()