'''
@Author : Priyanka
@Date : 2022-04-19  1:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 1:45:00
@Title : Write a Python program to get the smallest number from a list.
'''


def find_smallest_number():
    """
       Description:
            Finding the smallest item in the listr.
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """
    lst = [25,60,40,34,24,56]
    min1 = lst[0]
    for i in range(0,len(lst)):
        if lst[i] < min1:
            min1 = lst[i]

    print(min1)

if __name__ == '__main__':
    find_smallest_number()
