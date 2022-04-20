'''
@Author : Priyanka
@Date : 2022-04-18  10:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 10:45:00
@Title :Write a Python program to reverse a string
'''


def reverse_the_string():
    """
       Description:
            Taking the string from the user and then reverse the string by using the negative indexing.
       Parameter:
            none
       Return:
           Returning nothing but printing the string.
   """
    string = input("Enter the string")
    print("original string is :",string)
    string = string[::-1]
    print("Reverse string is",string)

if __name__ == '__main__':
    reverse_the_string()