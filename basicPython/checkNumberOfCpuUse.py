'''
@Author : Priyanka
@Date : 2022-04-18  2:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 2:30:00
@Title : Write a Python program to find out the number of CPUs using.
'''

import os

def number_of_CPUs_use():
    """
      Description:
           By using the cpu_count method from the os module count the number of CPUs used in the sytem.
      Parameter:
           None
      Return:
          Returning nothing but printing the message.
    """
    numberOfCpu = os.cpu_count()
    print("Number of CPUs used in the system is",numberOfCpu)

number_of_CPUs_use()