'''
@Author : Priyanka
@Date : 2022-04-20  1:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 1:25:00
@Title :Write a Python program to create a tuple.
'''

def create_tuple():
    """
       Description:
            creating a tuple and printing the tuple.
       Parameter:
            none
       Return:
           Returning string.
   """
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print("Tuple is ",thistuple)
    thistuple1 = (1,2,3,4,5,6,7)
    print("The tuple is",thistuple1)

if __name__ == '__main__':
    create_tuple()