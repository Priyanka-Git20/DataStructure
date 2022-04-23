'''
@Author : Priyanka
@Date : 2022-04-23  2:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 2:50:00
@Title :Write a Python program to count number of items in a dictionary value that is a list.
'''


def counting_dictionary_values_that_are_list():
    """
      Description:
          creating a dictionary and count the number of items in dictionary value that are list.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
  """
    # defining the dictionary
    d = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'B': 34,
         'C': 12,
         'D': ["siya", "Piya", "salunkhe", 6, 4,1.56,True]}

    # using the in operator
    count = 0
    for x in d:
        if isinstance(d[x], list):
            count += len(d[x])
    print(count)


if __name__ == '__main__':
    counting_dictionary_values_that_are_list()