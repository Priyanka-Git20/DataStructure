'''
@Author : Priyanka
@Date : 2022-04-18  12:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-018 12:10:00
@Title : check whether a specified value is contained in a group of values or not.
'''


def check_value_present_or_not(thisList,n):
    """
      Description:
           check whether a specified value is contained in a group of values or not.
      Parameter:
           list and number which we want to check it is present in list or not
      Return:
          Returning True if condition satisfy else return False.
    """

    for x in thisList:
        if x == n:
            return True

    return False


print(check_value_present_or_not([1,5,8,3],3))
print(check_value_present_or_not([1, 5, 8, 3],-1))


def check_value():
   thslist = [1,5,8,3]
   print(3 in thslist)
   print(-1 in thslist)

check_value()









