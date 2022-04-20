'''
@Author : Priyanka
@Date : 2022-04-18  10:25:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 10:30:00
@Title :Write a python program to count the occurance of the substring in a string.
'''


def count_of_substring():
    """
       Description:
            Taking the string from user and print it then count the occurance of substring in the string by count()function.
       Parameter:
            none
       Return:
           Returning nothing but printing the result.
   """
    txt = input("Enter the string")
    print("The string is :",txt)
    count = txt.count(input("Enter the subString"))
    print("The accurance of susbstring is :",count)

if __name__ == '__main__':
    count_of_substring()