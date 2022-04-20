'''
@Author : Priyanka
@Date : 2022-04-18  9:17:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 9:25:00
@Title :Write a Python script that takes input from the user and displays that input back in upper and lower cases
'''


def case_change():
    """
       Description:
            Take the input from the user and thn by using upper and lower function convert it and print it.
       Parameter:
            none
       Return:
           Returning nothing.
   """

    txt = input("Enter the string")
    print("String in upper case is",txt.upper())
    print("String in lower case is", txt.lower())

if __name__ == '__main__':
    case_change()