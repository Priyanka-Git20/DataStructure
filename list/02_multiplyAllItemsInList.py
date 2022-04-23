'''
@Author : Priyanka
@Date : 2022-04-19  1:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 1:20:00
@Title : Write a Python program to multiply all the items in a list
'''


def multiply_all_items_in_list():
    """
       Description:
            Iterate the list and multiply all the items in the list.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    lst = [1,2,3,4,5,6,7]
    multiplication = 1
    for i in lst:
        multiplication *= i
    print("Multiplication of all the element in the list is :",multiplication)

if __name__ == '__main__':
    multiply_all_items_in_list()