'''
@Author : Priyanka
@Date : 2022-04-20  4:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 4:10:00
@Title :Write a Python program to check whether an element exists within a tuple.
'''


def check_element_exists_in_tuple():
    """
       Description:
            By using in operator check element is present in tuple or not.
       Parameter:
            none
       Return:
           Returning nothing but printing message.
   """

    vowels = ("a","e","i","o","u")
    print("i" in vowels)
    print("s"in vowels)

if __name__ == '__main__':
    check_element_exists_in_tuple()
