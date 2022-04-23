'''
@Author : Priyanka
@Date : 2022-04-19  12:40:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 1:00:00
@Title : Write a Python program to sum all the items in a list
'''


def sum_all_items_in_list():
    """
       Description:
            Iterate the list and add all the items in the list.
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """

    lst = [12,14,15,34,56,78]
    sum = 0
    for i in lst:
        sum += i
    print("Addition of the all element in the list is ",sum)


if __name__ == '__main__':
    sum_all_items_in_list()