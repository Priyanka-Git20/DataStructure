'''
@Author : Priyanka
@Date : 2022-04-18  11:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 11:20:00
@Title :Print the calendar of the given month and year .
'''

import calendar


def print_calendar():
    """
      Description:
          Print the calendar of the given month and year.
      Parameter:
           none
      Return:
          Returning nothing but printing the calendar of given month and year.
  """

    yy = int(input("Enter the year"))
    mm = int(input("Enter the month"))

    print(calendar.month(yy,mm))

print_calendar()





