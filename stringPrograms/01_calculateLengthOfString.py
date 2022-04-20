'''
@Author : Priyanka
@Date : 2022-04-18  7:55:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 8:05:00
@Title : Write a Python program to calculate the length of a string.
'''


def calculate_length():
    """
       Description:
            By using len() function calculate the length of the string
       Parameter:
            none
       Return:
           Returning nothing but print the length of the string.
   """

    txt = input("Enter the string : ")
    print("length of the string is ",len(txt))

calculate_length()
