'''
@Author : Priyanka
@Date : 2022-04-19  9:05:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 9:15:00
@Title : Write a Python program to find maximum and the minimum value in a set
'''


def find_max_and_min():
    """
       Description:
            By using the min() and max() method finding the maximum and minimum values in the set.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    set1 = {3,4,7,1,80,34,23,6}
    print("Original set is :",set1)
    print("Maximum value in set is :")
    print(max(set1))
    print("Minimum value in set is :")
    print(min(set1))


if __name__ == '__main__':
    find_max_and_min()