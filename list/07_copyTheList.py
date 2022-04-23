'''
@Author : Priyanka
@Date : 2022-04-19  2:25:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 2:35:00
@Title : Write a Python program to clone or copy a list.
'''


def copy_the_list():
    """
       Description:
            Clone the list.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    lst1 = [12,2,45,6,7,87,21,13]
    lst2 = lst1.copy()
    print(lst2)


def clone_the_list():
    lst1 = [12, 2, 45, 6, 7, 87, 21, 13]
    lst2 = []
    for i in lst1:
        lst2.append(i)

    print(lst2)


def clone_the_list1():
    lst1 = [12, 2, 45, 6, 7, 87, 21, 13]
    lst2 = []
    lst2.extend(lst1)
    print(lst2)


if __name__ == '__main__':
    copy_the_list()
    clone_the_list()
    clone_the_list1()


