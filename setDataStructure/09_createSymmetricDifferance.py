'''
@Author : Priyanka
@Date : 2022-04-19  8:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 8:40:00
@Title : Write a Python program to create a symmetric difference.
'''


def create_set_difference():
    """
       Description:
            By using the symmetric difference method print the remaining items in both the set.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    set1 = {4, 5, "Red", "Orange", "Blue", "Black"}
    set2 = {"Red", 4, "Yellow", "white"}
    print("Original sets are")
    print(set1)
    print(set2)
    x1 = set1.symmetric_difference(set2)
    print("Symmetric differance of set1-set2 :",x1)
    x2 = set2.symmetric_difference(set1)
    print("Symmetric differance of set2-set1 :", x2)

if __name__ == '__main__':
    create_set_difference()