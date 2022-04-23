'''
@Author : Priyanka
@Date : 2022-04-19  3:05:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-019 3:20:00
@Title : Write a Python function that takes two lists and returns True if they have at least one common member.
'''


def check_Common_item():
    """
       Description:
            By using in operator and for loop checking two list have at least one common member.
       Parameter:
            none
       Return:
           Returning nothing but print the result.
   """

    lst1 = [2,5,7,9,10,2,4]
    lst2 = [3,1,0,6,5,8,11]
    result = False
    for x in lst1:
        for y in lst2:
            if x == y:
                result = True


    print(result)

if __name__ == '__main__':
    check_Common_item()
