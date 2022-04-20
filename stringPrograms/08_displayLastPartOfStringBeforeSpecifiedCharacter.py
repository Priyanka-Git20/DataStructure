'''
@Author : Priyanka
@Date : 2022-04-18  9:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 10:00:00
@Title :Write a Python program to get the last part of a string before a specified character..
'''


def display_last_part_of_string():
    """
       Description:
            By using split() function split the string into substring,the to avoide repetation coverted into set then sort function to sort the list .
       Parameter:
            none
       Return:
           Returning nothing but printing the result.
   """

    txt = "www.googole.com"
    print(txt.rsplit(".",1))

    text = "https://mail.google.com/chat/u/0/#chat/space/AAAAN0aKX1U"
    print(text.rsplit("/",2))

if __name__ == '__main__':
    display_last_part_of_string()