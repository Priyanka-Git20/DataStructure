'''
@Author : Priyanka
@Date : 2022-04-20  4:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 4:30:00
@Title :Write a Python program to remove an item from a tuple..
'''


def remove_element_from_tuple():
    """
       Description:
            First convert the tuple into list and remove the item by using remove method and then convert the list into tuple.
       Parameter:
            none
       Return:
           Returning nothing but printing message.
   """
    thistuple = ("apple", "banana", 25, "cherry", 12, 3.89, False)
    print("The original tuple is ",thistuple)
    lst = list(thistuple)
    lst.remove("cherry")
    print("List = ",lst)
    thistuple = tuple(lst)
    print("After removing element the tuple is ",thistuple)

if __name__ == '__main__':
    remove_element_from_tuple()
