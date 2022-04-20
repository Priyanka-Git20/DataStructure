''
@Author : Priyanka
@Date : 2022-04-18  2:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 12:15:00
@Title :Write a Python program to check whether a file exists.
'''


import os


def file_existence():
    """
      Description:
           Check whether a file exists or not by using exists function in the os module.
      Parameter:
           None
      Return:
          Returning nothing but printing the message.
    """

    file_exists = os.path.exists("/String/03_replaceString.py")
    print(file_exists)

if __name__ == '__main__':

    file_existence()

