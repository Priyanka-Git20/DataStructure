'''
@Author : Priyanka
@Date : 2022-04-18  4:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 4:37:00
@Title :Write a Python program to remove a key from a dictionary.
'''


def remove_key():
    """
       Description:
           By using the del keyword removes the item with the specified key name.
       Parameter:
            none
       Return:
           Returning nothing but print the message.
   """
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)

    if "model" in thisdict:
        del thisdict["model"]

    print(thisdict)

remove_key()

