'''
@Author : Priyanka
@Date : 2022-04-18  4:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 4:25:00
@Title :write a program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
'''


def generate_dictionary():
    """
       Description:
            Generate and print the dictionary.
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """

    n = int(input("Enter the length of the dictionary"))
    dictionary = {}

    for i in range(1,n+1):
        dictionary[i] = i*i

    print(dictionary)

generate_dictionary()