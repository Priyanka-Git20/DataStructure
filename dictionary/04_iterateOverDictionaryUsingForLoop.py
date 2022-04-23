'''
@Author : Priyanka
@Date : 2022-04-20  10:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-20  10:50:00
@Title :Write a Python program to iterate over dictionaries using for loops.
'''


def iterate_over_dictionary():
    """
       Description:
            Iterating the dictionary using for loop.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
    for key,value in thisdict.items():
        print(key,value)

if __name__ == '__main__':
    iterate_over_dictionary()

