'''
@Author : Priyanka
@Date : 2022-04-19  4:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 4:30:00
@Title : Write a Python program to get the difference between the two lists.
'''


def differance_between_two_list():
    """
       Description:
            Finding the differance between two list.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 2, 4, 6, 7, 8]
    diff_list1_list2 = list(set(list1)-set(list2))
    diff_list2_list1 = list(set(list2)-set(list1))
    total_diff = diff_list2_list1 + diff_list1_list2
    print("Total differance is ",total_diff)


def differance():
    """
       Description:
           Using the symmetric difference method and find total difference.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 2, 4, 6, 7, 8]
    diff = list(set(list1).symmetric_difference(list2))
    print(diff)


if __name__ == '__main__':
    differance_between_two_list()
    differance()
