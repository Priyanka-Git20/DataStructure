'''
@Author : Priyanka
@Date : 2022-04-19  2:05:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 2:15:00
@Title : Write a Python program to remove duplicates from a list..
'''


def remove_duplicate():
    """
       Description:
            Remove the duplicate item in the list.
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """
    lst = [2,4,6,8,10,2,4,2,25]
    new_lst = list(set(lst))
    print("After removing the duplicate items in list,the new list is ",new_lst)


def remove_duplicate1():
    new_lst = []
    lst = [2,4,6,8,10,2,4,2,25]
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    print("After removing the duplicate items in list,the new list is ",new_lst)


if __name__ == '__main__':
    remove_duplicate()
    remove_duplicate1()