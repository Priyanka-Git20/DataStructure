'''
@Author : Priyanka
@Date : 2022-04-18  3:40:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 3:50:00
@Title : Write a Python script to add a key to a dictionary.
'''


def add_items():
    """
       Description:
            By using the update method add the items in the dictionary.
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """

    thisDict = {0: 10, 1: 20}
    print("Dictionary before adding the items :",thisDict)
    thisDict.update({2:30})
    print("Dictionary after adding the items :",thisDict)

add_items()
