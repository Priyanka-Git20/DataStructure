'''
@Author : Priyanka
@Date : 2022-04-18  8:40:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 8:55:00
@Title :Write a Python program to add 'ing' at the end of a given string (length should be atleast 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
        given string is less than 3, leave it unchanged.
'''


def add_string():
    """
       Description:
            By using len function calculate the length and then check if length is greater than 2 then check the string is
            ends with ing if it is true then add ly at last else add ing at last.
       Parameter:
            none
       Return:
           Returning string.
   """
    str1 =input("Enter the string")
    length = len(str1)

    if length > 2 :
        if str1.endswith("ing"):
            str1 += "ly"
        else:
            str1 += "ing"

    return str1

def add_string2():
    str1 = input("Enter the string")
    length = len(str1)

    if length > 2:
        if str1[-3] == "i"and str1[-2] == "n" and str1[-1] == "g":
            str1 += "ly"
        else:
            str1 += "ing"

    print(str1)


if __name__ == '__main__':
   add_string2()
   print(add_string())
