'''
@Author : Priyanka
@Date : 2022-04-18  11:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 11:10:00
@Title : Write a python program to access environment variables.
'''

import os

def access_env_variable():
    """
      Description:
           python program to access environment variables.
      Parameter:
           None
      Return:
          Returning nothing but printing the message.
    """


    print(os.environ)
    print('.....................................')

    print(os.environ['OS'])

    print(os.environ['PATH'])

    print(os.environ['ALLUSERSPROFILE'])

    print(os.environ['APPDATA'])

    print(os.environ['COMMONPROGRAMFILES'])

    print(os.environ['COMMONPROGRAMFILES(X86)'])

    print(os.environ['COMPUTERNAME'])

    print(os.environ['COMSPEC'])

    print(os.environ['DRIVERDATA'])

    print(os.environ['ONEDRIVECONSUMER'])

    print(os.environ['PATHEXT'])

access_env_variable()

