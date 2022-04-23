'''
@Author : Priyanka
@Date : 2022-04-19  4:45:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 5:00:00
@Title : Write a Python program to append a list to the second list.
'''


def append_the_list():
    """
       Description:
            Append the list1 in to the list2.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    lst1 = [12,23,4,5,65,12,8,35]
    lst2 = ["Red","Yellow","Orange"]
    for i in lst1:
        lst2.append(i)
    print(lst2)

def append_list():
    lst1 = [12, 23, 4, 5, 65, 12, 8, 35]
    lst2 = ["Red", "Yellow", "Orange"]
    lst2.extend(lst1)
    print(lst2)

def append():
    lst1 = [12, 23, 4, 5, 65, 12, 8, 35]
    lst2 = ["Red", "Yellow", "Orange"]
    new_lst = lst2 + lst1
    print(new_lst)

if __name__ == '__main__':
    append_the_list()
    append_list()
    append()

