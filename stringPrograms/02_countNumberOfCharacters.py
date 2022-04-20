'''
@Author : Priyanka
@Date : 2022-04-18  8:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 8:20:00
@Title : Write a Python program to count the number of characters (character frequency) in a string.
'''


def count_character_in_string(str1):
    """
       Description:
            Count the number of characters in string using for loop and store in the dictionary.
       Parameter:
            none
       Return:
           Returning nothing but printing the result.
   """

    dir = {}

    for i in str1:
        if i in dir:
            dir[i] += 1
        else:
            dir[i] = 1

    print("Count of all characters in the string is",dir)

if __name__ == '__main__':

    count_character_in_string("All is well")
