'''
@Author : Priyanka
@Date : 2022-04-19  8:45:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 9:00:00
@Title : Write a Python program to use of frozensets.
'''


def frozen_sets():
    """
       Description:
            Frozensets are use to convert the set into the immutable frozenset and also in the dictionary create a set using key.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    vowels = ("a","e","i","o","u")
    fset = frozenset(vowels)
    print("The frozen set is :",fset)

    thisdict = {"brand": "Ford", "model": "Mustang","year": 1964 }
    fset1 = frozenset(thisdict)
    print("The frozen set is :",fset1)

if __name__ == '__main__':
    frozen_sets()
