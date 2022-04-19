'''
@Author : Priyanka
@Date : 2022-04-19  7:05:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 7:15:00
@Title :Write a Python program to add member(s) in a set..
'''


def add_members():
    """
       Description:
            Add the elements in the set by using the add() and update() method.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    set1 = {"apple","yellow","red",1,23}
    print("Original set is ",set1)
    set1.add("orange")
    print("Set after adding elements is ",set1)
    lst = ["black","green",12]
    set1.update(lst)
    print("Set after adding the elements of the list is ",set1)


if __name__ == '__main__':
    add_members()

