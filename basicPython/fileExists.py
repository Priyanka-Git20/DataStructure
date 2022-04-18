'''
@Author : Priyanka
@Date : 2022-04-18  2:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 2:15:00
@Title :Write a Python program to check whether a file exists.
'''

from pathlib import Path


def file_existence():
    """
      Description:
           Check whether a file exists or not by using file name or path of that file.
      Parameter:
           None
      Return:
          Returning nothing but printing the message.
    """

    path_to_file = input("Enter the file or a symlink to a file")
    path = Path(path_to_file)

    if path.is_file():
        print('The file {} exists'.format(path_to_file))
    else:
        print('The file {} does not exist'.format(path_to_file))

file_existence()





