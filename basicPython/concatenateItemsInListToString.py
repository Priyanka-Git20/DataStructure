'''
@Author : Priyanka
@Date : 2022-04-18  1:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 1:15:00
@Title : Write a program to concatenate all elements in a list into a string.
'''


def concatenate_list(lst):
    """
      Description:
           First taking the empty string and the elements in the list are add to the string.
      Parameter:
           list
      Return:
          Returning the string.
    """

    result = ""
    for element in lst:
        result += str(element)

    return result

print(concatenate_list(["My","name","is""Priyanka"]))
print(concatenate_list(["p","r","i","y","a"]))
print(concatenate_list([1,4,0,8,1,9,9,5]))
