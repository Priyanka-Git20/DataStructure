'''
@Author : Priyanka
@Date : 2022-04-18  9:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 9:40:00
@Title :Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
'''


def sort_the_string():
    """
       Description:
            By using split() function split the string into substring,the to avoide repetation coverted into set then sort function to sort the list .
       Parameter:
            none
       Return:
           Returning nothing but printing the result.
   """
    txt = input("Enter the comma separated sequence of words")
    x = txt.split(",")
    y= (set(x))  #To avoid repetation
    z = sorted(y)  #To sort alphanuerically
    print(z)

sort_the_string()