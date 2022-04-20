'''
@Author : Priyanka
@Date : 2022-04-18  10:55:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 11:00:00
@Title : Write a Python program to lowercase first n characters in a string.
'''


def lowercase_characters():
    """
       Description:
            By using the lower() function and the slicing concept lowercase the first n characters in a string and print.
       Parameter:
            none
       Return:
           Returning nothing but printing the string.
   """

    n = int(input("Enter the number of characters you want in the lowercase format"))
    str1 = "BRIDGELABZ.COM"
    print(str1[0:n].lower() + str1[n:])

if __name__ == '__main__':
    lowercase_characters()
