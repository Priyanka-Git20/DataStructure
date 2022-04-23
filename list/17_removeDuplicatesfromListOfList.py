'''
@Author : Priyanka
@Date : 2022-04-19  4:45:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 5:00:00
@Title : Write a Python program to remove duplicates from a list of lists.
'''


def remove_duplicate_from_list_of_list():
    """
       Description:
           Remove the duplicate item in the list.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    print("After removing the duplicate items in list,the new list is ", new_lst)


if __name__ == '__main__':
    remove_duplicate_from_list_of_list()