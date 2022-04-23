'''
@Author : Priyanka
@Date : 2022-04-18  4:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 4:37:00
@Title :Write a Python program to print all unique values in a dictionary.
'''


def print_unique_values():
    """
       Description:
           printing the all unique values in dictionary.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """
    mydict= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    print("Original list is ",mydict)
    value = set(val for dic in mydict for val in dic.values())
    print(value)


if __name__ == '__main__':
    print_unique_values()