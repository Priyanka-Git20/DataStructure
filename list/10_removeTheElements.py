'''
@Author : Priyanka
@Date : 2022-04-19  3:25:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 3:40:00
@Title : Write a Python program to print a specified list after removing the 0th, 4th and 5th elements,
'''


def remove_items():
    """
       Description:
            By using pop method remove the items
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    lst =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    lst.pop(0)
    lst.pop(4)
    lst.pop()
    print(lst)


if __name__ == '__main__':
    remove_items()

