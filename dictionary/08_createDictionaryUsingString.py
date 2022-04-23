'''
@Author : Priyanka
@Date : 2022-04-23  1:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-23 1:20:00
@Title :Write a Python program to create a dictionary from a string.
'''


def dictionary_from_string():
    """
       Description:
           creating a dictionary from a string.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    str = 'google.com'
    my_dict = {}

    for i in str:
        my_dict[i] = my_dict.get(i, 0) + 1

    print("Dictionary is: ", my_dict)


if __name__ == '__main__':
    dictionary_from_string()