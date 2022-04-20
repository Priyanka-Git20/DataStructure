'''
@Author : Priyanka
@Date : 2022-04-18  8:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 8:35:00
@Title :Write a Python program to get a string from a given string where all occurrences of its
       first char have been changed to '$', except the first char itself.
'''


def replace_string():
    """
       Description:
            From the given string all the occurrences of the first character except first character replace with $.
       Parameter:
            none
       Return:
           Returning nothing but printing the replace string.
   """
    str1 = input("Enter the string :")
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    print("String after replacing is :",str1)


replace_string()



