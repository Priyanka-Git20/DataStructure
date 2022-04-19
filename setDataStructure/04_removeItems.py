'''
@Author : Priyanka
@Date : 2022-04-19  7:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 7:25:00
@Title :Write a Python program to remove item(s) from set.
'''


def remove_items():
    """
       Description:
            Remove the item in the set by using the remove(),discard(),pop() methods.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    thisset = {'green', 'yellow', 1, 'orange', 12, 'black', 'apple', 23, 'red'}
    thisset.remove(1)
    print("Set after removing 1 is ",thisset)
    thisset.discard("orange")
    print("Set after removing orange is ",thisset)
    thisset.pop()
    print("Set after removing the item is ",thisset)

if __name__ == '__main__':

    remove_items()