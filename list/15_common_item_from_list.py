'''
@Author : Priyanka
@Date : 2022-04-19  5:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 5:15:00
@Title : Write a Python program to find common items from two lists..
'''


def common_items_in_list():
    """
       Description:
           By using intersection method finding the common items between two list.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    lst1 = [12,23,3,4,6,2,1,3,4]
    lst2 = [1,2,4,5,6,8,13,34,56,7]
    common = list(set(lst1).intersection(set(lst2)))
    print("Common items in the list are " ,common)

if __name__ == '__main__':
     common_items_in_list()